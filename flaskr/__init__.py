import os
import pydim

from flask import Flask, g, jsonify

updateState = None

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def updateGenericInt(key):
        # Curry function to remember key against which to store updated value
        def update(value):
            from . import db
            from . import store

            s = store.Store()
            s.UpdateValue(key, value)
            
            from flask_socketio import emit
            from . import actions
            available_actions = actions.available_actions(s.GetValue("state"))
            if updateState != None: updateState({
                "services": s.GetValues(),
                "available_actions": available_actions
            })

        return update

    # Register listeners before first request - only runs when first actual request hits server
    # https://networklore.com/start-task-with-flask/
    @app.before_first_request
    def activate_job():
        if not pydim.dis_get_dns_node():
            print("No Dim DNS node found. Please set the environment variable DIM_DNS_NODE")
            sys.exit(1)

        # Register listeners
        pydim.dic_info_service("ztt_dimfed_server_trd-fee_00_2_0_STATE", updateGenericInt("state"))

    @app.route('/test/<state>')
    def test(state):
        if state is None:
            import random
            state = random.randrange(0, 100)
        updateGenericInt("state")(state)
        return str(state)

    from . import db
    db.init_app(app)

    from . import root
    app.register_blueprint(root.bp)

    return app

