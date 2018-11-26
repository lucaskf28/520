#!/usr/bin/python3
#isinstance(num, int)
num = int(input("Digite o numero: "))
#if num % 2 == 0:
#    print('Par')
#else:
#    print('Impar')

pares = []
for x in range(num):
    if x % 2 != 0:
        continue
    else:
        pares.append(x)
    print('item adicionado')
print(pares)
