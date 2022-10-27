from indication import app
from indication.middleware.check_token import Middleware

app.wsgi_app = Middleware(app.wsgi_app)
if __name__ == "__main__":
    app.run(debug=True)