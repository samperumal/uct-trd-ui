import flaskr
from flask_socketio import SocketIO, emit
from flaskr import store

if __name__ == '__main__':
    app = flaskr.create_app()
    socketio = SocketIO(app)

    def update():
        socketio.emit('state', store.Store().GetState())

    @socketio.on('connect')
    def test_connect():
        socketio.emit('my response', {'data': 'Connected'})
        update()

    flaskr.updateState = update
    #store.Store().onUpdate = update

    socketio.run(app)