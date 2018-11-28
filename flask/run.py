#!/usr/bin/python3
from flask import Flask, jsonify, redirect, request, Response, make_response
import requests
import json
from modulos.usuarios import usuario
from modulos.view import view

app = Flask(__name__)
app.register_blueprint(usuario)
app.register_blueprint(view)

@app.route('/', methods=['GET'])
def index():
    headers = {"Content-Type":"application/json"}
    mensagem = dict({"mensagem": "api rest"})
    #return jsonify(mensagem)
    #return make_response(json.dumps(mensagem),301,headers)
    return Response(json.dumps(mensagem),301,content_type="application/json")
    #return 'hello world'

#@app.route('/cep')
#def buscar_end():
#    re = requests.get("https://viacep.com.br/ws/08270630/json/")
#    return jsonify(re.json())

@app.route('/', methods=['POST'])
def metodo_post():
    #return 'teste'
    print(request.form)
    return redirect('/')

@app.route('/rota/<string:dinamico>')
def rota_dinamico(dinamico):
    return dinamico

@app.route('/cep/<string:cep>')
def buscar_comparametro(cep):
    re = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    return jsonify(re.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)