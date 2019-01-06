from flask import Flask
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_cors import CORS

app  = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

@socketio.on('msg')
def test(message):
    print(message)
    emit('msg', message, broadcast=True)

@app.route('/')
def main():
    print("root directory")
    return 'root'

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    socketio.run(app)