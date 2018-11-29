from flask import Blueprint, jsonify
from conn import mongo_connect

db = mongo_connect()
usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario.route('/')
def get_users():
    data = db.usuario.find()
#    aux = []
#    for x in data:
#        del x['_id']
#        aux.append(x)
#    return jsonify(aux)
    return jsonify(list(data))

@usuario.route('/<string:user>')
def get_user(user):    
    if user.isnumeric():
        #try:
        return jsonify(db.usuario.find_one({"_id":int(user)}))
        #except Exception:
        #    return None
    #elif len(user) == 14:
    elif len(user.split('.')) == 3:
        return jsonify(db.usuario.find_one({"cpf":user}))
    else:
        return jsonify(list(db.usuario.find({"nome":user})))
