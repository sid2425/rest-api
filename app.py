from database.db import initialize_db
from flask import Flask, request, Response
from database.models import AddressBookHolding
from flask.globals import request
app = Flask(__name__)


DB_URI = 'mongodb+srv://sid2425:N0YOWdpNhjhOxalK@siddartha.9s2er.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app.config["MONGODB_HOST"] = DB_URI
initialize_db(app)


@app.route('/list')
def getData():
    address = AddressBookHolding.objects().to_json()
    return Response(address, mimetype="application/json", status=200)


@app.route('/list/<id>')
def getDataById(id):
    address = AddressBookHolding.objects.get(id=id).to_json()
    return Response(address, mimetype="application/json", status=200)


@app.route('/list', methods=['POST'])
def addAddress():
    body = request.get_json()
    address = AddressBookHolding(**body).save()
    id = address.id
    return {'id': str(id)}, 200


@app.route('/list/<id>', methods=['PUT'])
def updateAddress(id):
    body = request.get_json()
    AddressBookHolding.objects.get(id=id).update(**body)
    return '', 200


@app.route('/list/<id>', methods=['DELETE'])
def deleteAddress(id):
    AddressBookHolding.objects.get(id=id).delete()
    return '', 200


if __name__ == "__main__":
    app.run(debug=True)
