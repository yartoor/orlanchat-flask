from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")


@socketio.event
def join(message):
    join_room(message['room'])
    emit('my_response',
    {
        'data': message['nickname'] +' joined to chat ' + message['room']
    })

@socketio.event
def my_room_event(message):
    emit('my_response',
         {'data': message['data'], 'nickname': message['nickname']},
         to=message['room'])

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)