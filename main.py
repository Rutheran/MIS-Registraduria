from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi  
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa


controladorCandidato = ControladorCandidato()
controladorMesa = ControladorMesa()

app = Flask(__name__)
cors = CORS(app)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = controladorCandidato.index()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = controladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = controladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = controladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = controladorCandidato.delete(id)
    return jsonify(json)


###############################################################


@app.route("/mesa",methods=['GET'])
def getMesas():
    json = controladorMesa.index()
    return jsonify(json)


@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=controladorMesa.create(data)
    return jsonify(json)


@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=controladorMesa.show(id)
    return jsonify(json)


@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=controladorMesa.update(id,data)
    return jsonify(json)


@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=controladorMesa.delete(id)
    return jsonify(json)


###################
if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

