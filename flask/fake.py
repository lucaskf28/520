from faker import Faker
from conn import mongo_connect

fake = Faker('pt-BR')

db = mongo_connect()

for x in range(1000):
    data = {
        "_id": x,
        "nome": fake.name(),
        "email": fake.email(),
        "cpf": fake.cpf(),
        "nascimento": fake.date_of_birth().strftime('%d-%m-%Y')
    }
    db.usuario.insert(data)