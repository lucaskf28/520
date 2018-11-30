from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atlz = update(user_table).where(user_table.c.nome == 'lucas')

atlz = atlz.values(nome='lucas souza')
result = con.execute(atlz)

print(result.rowcount)