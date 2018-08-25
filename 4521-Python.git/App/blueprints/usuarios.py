
from flask import Flask, Blueprint, jsonify, make_response, Response, request, redirect
from bson.json_util import dumps
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['flask-app']
except Exception as e:
    print("Error: {}".format(e))
    exit()

app = Flask(__name__)
usuario = Blueprint('usuario', __name__)

def hits():
    status = make_response
    return status   

@usuario.route('/usuarios', methods=['POST'])
def cadastrar_usuarios():
    user = request.get_json()
    if user['nome'] and user['email']:
        db.user.insert_one(
            {
                "nome":user['nome'],
                "email":user['email'],
                "mensagens":user['mensagem']
            }
        )
        mensagem = dumps({'mensagem':"usuario {} cadastrado com Sucesso!".format(user['nome'])})
        status = 201
    else:
        mensagem = dumps({'mensagem': 'Informacoes Invalidas'})
        status = 400
    return Response(mensagem, status=status, content_type="application/json")
    
    #return jsonify({'status': 'running...'})

@usuario.route('/usuarios', methods=['PATCH'])
def atualizar_usuario():
    user = request.get_json()
    update = db.user.update_one(
        {"email":user['email']},
        {"$set":user}
    )
    if update.modified_count:
        mensagem = {"mensagem":"usuario {} atualizando".format(user['nome'])}
        status = 200
    elif update.matched_count:
        mensagem = {"mensagem":"usuario {} nao atualizado".format(user['nome'])}
        status = 400
    else:
        mensagem = { "mensagem": "usuario não cadastrado"}
        status = 404
    return Response(dumps(mensagem), status=status, content_type="application/json")


@usuario.route('/usuarios', methods=['DELETE'])
def deletar_usuario():
    user = request.get_json()
    remove = db.user.delete_one(
        {"email":user["email"]}     
    )
    if remove.deleted_count:
        mensagem = { "mensagem":"usuario {} removido com sucesso!".format(user['email'])}
        status = 200
    else:
        mensagem = { "mensagem":"usuario nao encontrado"}
        status = 404
    return Response(dumps(mensagem), status=status, content_type="application/json")
@usuario.route('/usuarios', methods=['GET'])
def usuarios():
    users = db.user.find()
    return Response(dumps(users), status=777, content_type="application/json")
hits()
