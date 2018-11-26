#!/usr/bin/python3
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
media = float(nota1) + float(nota2)
media /= 2
if media >= 7:
    result = 'Aprovado'
elif media <= 3:
    result = 'Reprovado'
else:
    result = 'Recuperacao'
print('Resultado: {} \nMedia: {}'.format(result, media))