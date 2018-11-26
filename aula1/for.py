#!/usr/bin/python3
# 97 to  123
lista = []
for letra in range(0,123):
    lista.append(chr(letra))
#print(lista)

letras = [chr(x).upper() for x in range(97,123) if chr(x) != 'a']
print(letras)