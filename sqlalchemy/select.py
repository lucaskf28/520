from sqlalchemy import select
from core import user_table

#slct = select([user_table])
#slct = select([user_table.c.nome, user_table.c.idade])
slct = select([user_table]).where(user_table.c.nome.like("teste"))

print(list(slct.execute()))
#registros [x for x in slct.execute() ]
#for registro in slct.execute():
#    print(registro)