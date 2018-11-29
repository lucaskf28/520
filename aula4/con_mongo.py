from pymongo import MongoClient
from bson import ObjectId

try:
    client = MongoClient()
    db = client['projeto']
except Exception as e:
    print(e)
    exit()

user = {'_id':4, "nome":"maluco doido"}
db.usuario.insert(user)
busca = db.usuario.find()
#print(list(busca))

busca = [x for x in busca]
print(busca)