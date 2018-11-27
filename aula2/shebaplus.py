#!/usr/bin/python3
import os, sys, stat
nome = input("digite o nome do arquivo: ")
shebang = '#!/usr/bin/python3\n'
try:
    with open(nome+'.py', 'x') as arquivo:
        arquivo.write(shebang)
        os.chmod(nome+'.py',stat.S_IRWXU)
except FileExistsError:
    with open(nome+'.py', 'r') as arquivo:
        linha1 = arquivo.readline()
        if linha1 != shebang:
            conteudo = arquivo.readlines()
            conteudo.insert(0,shebang)
    try:
        with open(nome+'.py', 'w') as arquivo:
            arquivo.writelines(conteudo)
    except NameError:
        print("ja tem xibeng")