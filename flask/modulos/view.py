from flask import Blueprint, render_template, request, redirect
from conn import psy_connect

view = Blueprint('view', __name__, url_prefix='/view')
cur = psy_connect('lucas', '123456', 'fundamentals')
#cur = psy_connect()

@view.route('/')
def modelo_view():
#    letras = [chr(x) for x in range(97,123)]
#    return render_template('index.html', letras=letras)
    cur.execute("select * from usuario;")
    return render_template('pg.html', usuarios=cur.fetchall())

@view.route('/<string:nome>')
def render_user(nome):    
    cur.execute("select * from usuario where nome like '%{}%';".format(nome.title()))
    return render_template('pg.html', usuarios=cur.fetchall())

@view.route('/login')
def render_login():
    return render_template('login.html')

@view.route('/login', methods=['POST'])
def auth_login():
    auth = request.form
    if auth['login'].strip().lower() == 'teste' and auth['senha'].strip().lower() == '123':
        retorno = {"auth": True}
    else:
        retorno = {"auth": False}
    #return redirect('/')
    return render_template('login.html', auth=retorno)