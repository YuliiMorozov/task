from flask import render_template
from indication import app

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")