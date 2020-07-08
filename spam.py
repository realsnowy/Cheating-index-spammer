#! python2

import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://tf2cheat.125mb.com/?contact=new'

names = json.loads(open('names.json').read())
messages = json.loads(open('messages.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    steamid = '76561198179913894'
    email = name.lower() + name_extra + '@gmail.com'
    message = random.choice(messages)
    reason = 'report'

    requests.post(url, allow_redirects=False, data ={
        'first': steamid,
        'mail': email,
        'message_text': message,
        'reason': reason
    })

    print 'Sending email [%s] with message [%s]' % (email, message)
