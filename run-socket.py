from flask_socketio import SocketIO, emit
from flaskr import store, actions, create_app, updateState, pydim_wrapper
import sys

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
        stdout = actions.run_action(action)
        socketio.emit('cmd-output', { 'stdout': stdout })
    
    pydim_wrapper.subscribe(update)

    host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
    port = sys.argv[2] if len(sys.argv) > 2 else 5001
    
    socketio.run(app, host = host, port = port)