#!/usr/bin/python3
x = 0
soma = 0
nota = []
try:
    qt_notas = int(input("quantas notas vc quer calcular a media: "))
except ValueError as e:
    print('valor invalido')
    exit()
for x in range(qt_notas):
    try:
        nota = float(input('Digite a {} nota: '.format(x+1)))
    except ValueError as e:
        print('Nota invalida')
        exit()
    if nota > 10:
        print('Digite uma nota de 0 a 10')
        qt_notas -= 1
        continue
    soma += nota
media = soma/qt_notas
if media >= 7:
    result = 'Aprovado'
elif media <= 3:
    result = 'Reprovado'
else:
    result = 'Recuperacao'
print('Resultado: {} \nMedia: {}'.format(result, media))
