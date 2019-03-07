# -*- coding=utf-8 -*-
import requests
import itchat
import random

#登录微信
itchat.auto_login(hotReload=True)

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : 'e2088abe87004b92a298607f1c05ddb9',
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = msg['Text']
    reply = get_response(msg['Text'])
    print("message:%s" % msg['Text'])
    return reply or defaultReply

itchat.auto_login(enableCmdQR=True)
itchat.run()