from flask_socketio import SocketIO, emit
from flaskr import store, actions, create_app, updateState

if __name__ == '__main__':
    app = create_app()
    socketio = SocketIO(app)

    def update():
        socketio.emit('state', store.Store().GetState())

    @socketio.on('connect')
    def test_connect():
        update()

    @socketio.on('run-action')
    def run_action(action):
        actions.run_action(action)
        update()

    updateState = update
    
    socketio.run(app)