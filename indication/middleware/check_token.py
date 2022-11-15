from base64 import decode
from werkzeug.wrappers import Request, Response
import jwt

class Middleware():

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        request = Request(environ)
        url = request.base_url
        token = request.headers.get('Authorization') 

        if url.find("api/") == -1 or url.split("api/")[1] == "registration" or url.split("api/")[1] == "1" or url.split("api/")[1] == "login":
            return self.app(environ, start_response)
        else:
            try:
                jwt.decode(token.split()[1], "my_secret", algorithms=["HS256"])             
            except:
                res = Response('Authorization failed', mimetype='text/plain', status=401)
                return res(environ, start_response)
            return self.app(environ, start_response)