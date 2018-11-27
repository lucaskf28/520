#!/usr/bin/python3
def ler(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.readlines()
    return conteudo

def contar(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.readlines()
        cont_linhas = conteudo.__len__()
    return cont_linhas

def escrever(texto):
    with open('teste.txt', 'a') as arquivo:
        arquivo.write(texto+'\n')
    return 'escreveu'

print(ler('teste.txt'))
print(contar('teste.txt'))
print(escrever('aehoo'))