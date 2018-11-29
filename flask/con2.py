from psycopg2 import connect

try:
    con = connect("host=localhost user=lucas password=123456 dbname=fundamentals")
    cur = con.cursor()
    cur.execute("select * from usuario")
    #print(cur.fetchone())
    print(cur.fetchall())
    #cur.execute("insert into usuario (nome, email, cpf, nascimento) \
    #                values ('{}','{}','{}','{}')".format('alonome', 'alo@nome.com', '987.456.887-44', '18/09/1992'))
    #con.commit()
except Exception as e:
    con.rollback()
    print(e)
    
finally:
    try:
        cur.close()
        con.close()
    except Exception:
        print('Cursor nao definido!')
