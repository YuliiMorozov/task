from indication import app
from indication.api.controllers.indications import get_indications

@app.route("/api/payment/<int:flat_id>", methods=["GET"])
def indications(flat_id):
    return get_indications(flat_id)