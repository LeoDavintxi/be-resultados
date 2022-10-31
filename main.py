from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorRegistro_Voto import ControladorRegistro_Voto
miControladorMesa=ControladorMesa()
miControladorPartido=ControladorPartido()
miControladorCandidato=ControladorCandidato()
miControladorRegistro_Votacion=ControladorRegistro_Voto()
###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###################################################################################
@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
###################################################################################
@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)
###################################################################################
@app.route("/candidatos",methods=['GET'])
def getcandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json=miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)
###################################################################################
@app.route("/registro_votaciones",methods=['GET'])
def getRegistro_Votaciones():
    json=miControladorRegistro_Votacion.index()
    return jsonify(json)
@app.route("/registro_votaciones/<string:id>",methods=['GET'])
def getRegistro_Votacion(id):
    json=miControladorRegistro_Votacion.show(id)
    return jsonify(json)
@app.route("/registro_votaciones/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def crearRegistro_Votacion(id_mesa,id_candidato):
    data = request.get_json()
    json=miControladorRegistro_Votacion.create(data,id_mesa,id_candidato)
    return jsonify(json)
@app.route("/registro_votaciones/<string:id_registro_votacion>/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['PUT'])
def modificarRegistro_Votacion(id_registro_votacion,id_mesa,id_candidato):
    data = request.get_json()
    json=miControladorRegistro_Votacion.update(id_registro_votacion,data,id_mesa,id_candidato)
    return jsonify(json)
@app.route("/registro_votaciones/<string:id_registro_votacion>",methods=['DELETE'])
def eliminarRegistro_Votacion(id_registro_votacion):
    json=miControladorRegistro_Votacion.delete(id_registro_votacion)
    return jsonify(json)
@app.route("/registro_votaciones/candidato/<string:id_candidato>",methods=['GET'])
def registro_votacionesEnCandidato(id_candidato):
    json=miControladorRegistro_Votacion.listarVotosEnCandidato(id_candidato)
    return jsonify(json)
@app.route("/registro_votaciones/votos_mayores",methods=['GET'])
def getVotosMayores():
    json=miControladorRegistro_Votacion.votosMasAltosPorCandidato()
    return jsonify(json)
@app.route("/registro_votaciones/promedio_votos/candidato/<string:id_candidato>",methods=['GET'])
def getPromedioVotosEnCandidato(id_candidato):
    json=miControladorRegistro_Votacion.promedioVotosEnCandidato(id_candidato)
    return jsonify(json)
###################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

