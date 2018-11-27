#!/usr/bin/python3
#arquivo = open('teste.txt', 'r')
# print(arquivo.readlines())
# print('oi')
# arquivo.close()
#conteudo = 5*['novo\n']


#try:
with open('teste.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
with open('teste.txt', 'w') as arquivo:
    #conteudo = arquivo.readlines()
    #conteudo = arquivo.write('amlk\n')
    cont = 1
    for x in conteudo:
        arquivo.write(str(cont)+'-'+x)
        cont += 1
#except FileExistsError:
#    print('arquivo ja existe')
# print(conteudo)
