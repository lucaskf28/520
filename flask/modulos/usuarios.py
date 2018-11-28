from flask import Blueprint, jsonify

usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

users = [
    {'nome': 'lucas', 'idade': 28},
    {'nome': 'lucas2', 'idade': 29},
    {'nome': 'lucas3', 'idade': 30},
]

@usuario.route('/')
def get_usuarios():
    return jsonify(users)

@usuario.route('/')
def get_users():
    return jsonify(users)

@usuario.route('/<int:user>')
def get_user(user):
    return jsonify(users[user-1])