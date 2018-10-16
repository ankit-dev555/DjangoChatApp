from channels import Group

import json
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
@channel_session_user_from_http
def ws_connect(message,room):


    Group('users-'+str(room)).add(message.reply_channel)
    message.channel_session['room'] = room
    Group('users-'+str(room)).send({
        'text': json.dumps({
            'msg': message.user.username+" is online",

        })
    })

@channel_session_user
def ws_receive(message,room):
    room=message.channel_session['room']
    m=json.loads(message.content['text'])
    #Group('users-'+str(room)).add(message.reply_channel)
    Group('users-' + str(room)).send({
        'text': json.dumps({
            'msg': message.user.username+":"+m['msg'],

        })
    })

@channel_session_user_from_http
def ws_connect_video(message,room1):
    print(room1)

    Group('users' + str(room1)).add(message.reply_channel)
    Group('users' + str(room1)).send({"accept": True})
@channel_session_user
def ws_receive_video(message,room1):

    m1=json.loads(message.content['text'])
    #Group('users').add(message.reply_channel)
    Group('users' + str(room1)).send({'text':json.dumps(m1)})



@channel_session_user
def ws_disconnect(message,room):
    Group('users-' + str(room)).send({
        'text': json.dumps({
            'msg': message.user.username + " is offline",

        })
    })

    Group('users-' + str(room)).discard(message.reply_channel)

@channel_session_user
def ws_disconnect_video(message,room1):
    Group('users' + str(room1)).send({
        'text': json.dumps({
            'msg': message.user.username + " is offline",

        })
    })

    Group('users' + str(room1)).discard(message.reply_channel)

