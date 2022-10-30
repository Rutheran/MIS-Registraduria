from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi  
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa


controladorCandidato = ControladorCandidato()
controladorPartido = ControladorPartido()
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


'''Candidatos'''

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
    
@app.route("/candidatos/<string:id>/partidos/<string:id_partido>", methods=['PUT'])
def asignarPartidoACandidato(id, id_partido):
    json= controladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)


'''Mesas'''

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

@app.route("/mesa/<string:id>/partidos/<string:id_partido>", methods=['PUT'])
def asignarPartidoAMesa(id, id_partido):
    json= controladorMesa.asignarPartido(id,id_partido)
    return jsonify(json)


'''Partido'''


@app.route("/partido", methods=['GET'])
def getPartido():
    json = controladorPartido.index()
    return jsonify(json)


@app.route("/partido", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = controladorPartido.create(data)
    return jsonify(json)


@app.route("/partido/<string:id>", methods=['GET'])
def getOnePartido(id):
    json = controladorPartido.show(id)
    return jsonify(json)


@app.route("/partido/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = controladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partido/<string:id>", methods=['DELETE'])
def eliminarPartidonto(id):
    json = controladorPartido.delete(id)
    return jsonify(json)


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

