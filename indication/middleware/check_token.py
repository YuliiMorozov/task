from werkzeug.wrappers import Request, Response
import jwt

class Middleware():

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        token = request.headers.get('Authorization')
        try:
            jwt.decode(token, "my_secret", algorithms=["HS256"])
            return self.app(environ, start_response)
        except:
            res = Response('Authorization failed', mimetype='text/plain', status=401)
            return res(environ, start_response)


        

        