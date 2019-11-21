from flask_socketio import SocketIO, emit
from flaskr import store, actions, create_app, updateState, pydim_wrapper

if __name__ == '__main__':
    app = create_app()
    socketio = SocketIO(app)

    def update():
        socketio.emit('state', store.Store().GetState())

    @socketio.on('connect')
    def connect():
        update()

    @socketio.on('run-action')
    def run_action(action):
        actions.run_action(action)
    
    pydim_wrapper.subscribe(update)
    
    socketio.run(app)