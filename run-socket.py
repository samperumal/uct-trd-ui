import flaskr
from flask_socketio import SocketIO, emit

if __name__ == '__main__':
    app = flaskr.create_app()
    socketio = SocketIO(app)

    @socketio.on('connect')
    def test_connect():
        print("Client connected")
        emit('my response', {'data': 'Connected'})

    def update(cache):
        print("Emitting")
        socketio.emit('state', cache)

    flaskr.updateState = update

    socketio.run(app)