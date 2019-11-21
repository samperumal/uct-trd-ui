import flaskr
from flask_socketio import SocketIO, emit
from flaskr import store

if __name__ == '__main__':
    app = flaskr.create_app()
    socketio = SocketIO(app)

    @socketio.on('connect')
    def test_connect():
        socketio.emit('my response', {'data': 'Connected'})

    def update(cache):
        socketio.emit('state', cache)

    flaskr.updateState = update
    #store.Store().onUpdate = update

    socketio.run(app)