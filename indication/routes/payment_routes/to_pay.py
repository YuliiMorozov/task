from indication import app
from flask_login import login_required
from indication.controllers import to_pay


@app.route('/payment/<float:sum>')
@login_required
def item_buy(sum):
    return to_pay()