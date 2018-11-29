from faker import Faker
from psycopg2 import connect

fake = Faker('pt-BR')

con = connect("host=localhost user=lucas password=123456 dbname=fundamentals")
cur = con.cursor()

for x in range(1000):
    cur.execute("insert into usuario (nome, email, cpf, nascimento) \
                    values ('{}','{}','{}','{}')".format(fake.name(), fake.email(), fake.cpf(), fake.date_of_birth().strftime('%d-%m-%Y')))

con.commit()