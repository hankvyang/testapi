import os
import json

import sae
import web

urls = (
        '/', 'Index',
        '/login','Login'
)

user_name = 'runyang'
password = 'password'
login_cookie = 'cookie'


def is_authenticated(name, password):
    if(name==user_name and password==password):
        return True
    return False    

def is_cookie_present(cookie):
    return True if login_cookie == cookie else False

class Index:
    def GET(self):
        c = web.cookies().get('login_cookie')
        if not is_cookie_present(c):
            return 'you are not logged in'
        todos = [{'id':1,'price':2,'due':'2014/7/30'},{'id':2,'price':2,'due':'2014/7/30'},{'id':3,'price':2,'due':'2014/7/20'},{'id':4,'price':2,'due':'2014/7/31'}]
        web.header('Content-Type', 'application/json')
        return json.dumps(todos)

class Login:
    def POST(self):
        i = web.input()
        if(is_authenticated(i.name, i.password)):
        {
            web.setcookie('login_cookie','cookie')
            return 'ok'
        }
        return 'something goes wrong'


app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
