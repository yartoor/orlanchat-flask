from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.event
def enter(message):
    try:
        channel_ids = message.get('channel_ids', None)
        if channel_ids is not None and channel_ids:
            for channel_id in channel_ids:
                join_room(channel_id)
            message['message']= "Joined to channel_ids: %s" %(channel_ids)

        else:
            message['message'] = "Provided empty list of channel_ids"

    except:
        message['message'] = "Error occured in request processing"

    finally:

        emit('response',
            {
                  'data': message
            })

@socketio.event
def channel_message(message):
    try:
        channel_id = message.get('channel_id', None)

        if channel_id is not None and channel_id and channel_id in rooms():
            emit('response',
            {
                'data': message
            }, to=channel_id)

    except:
        message['message'] = "Error occured in request processing"
        emit('response',
            {
                'data': message
            })

@socketio.event
def leave(message):
    try:
        channel_ids = message.get('channel_ids', None)
        if channel_ids is not None and channel_ids:
            for channel_id in channel_ids:
                leave_room(channel_id)
            message['message']= "Leaved from channels_id: %s" %(channel_ids)

        else:
            message['message'] = "Provided empty list of channel_ids"

    except:
        message['message'] = "Error occured in request processing"

    finally:

        emit('response',
            {
                  'data': message
            })




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug = True)
