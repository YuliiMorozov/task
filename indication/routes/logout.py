import imp
from indication import app
from flask_login import login_required, logout_user
from flask import redirect, url_for


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))