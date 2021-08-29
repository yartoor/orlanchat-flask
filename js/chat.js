var socket = io();

channels_data = {
	'channel_ids': ['uuid1', 'uuid2', 'uuid3'],
	'user_id': 'uuid4'
}

channel_data = {
	'channel_id': 'uuid1',
	'user_id': 'uuid4',
	'fio': 'Artur Sabirov',
	'message': 'Artur sabirov message',
	'date': 'дд.мм.гггг / чч:мм'
}


socket.on('enter',function(){
    socket.emit('enter', channels_data)
});
document.querySelector('#join').onclick = function(event) {
    socket.emit('enter', channels_data)
};


socket.on('leave',function(){
    socket.emit('leave', channels_data)
});
document.querySelector('#leave').onclick = function(event) {
    socket.emit('leave', channels_data)
};


document.querySelector('#chat-message-submit').onclick = function(event){

    var message = document.querySelector('#chat-message-input').value;
    channel_data['message']=message;
    socket.emit("channel_message", channel_data)
}
socket.on('response', function(msg, cb) {

    document.querySelector('#chat-log').value += (msg.data.message + '\n');
                if (cb)
                    cb();
            });

