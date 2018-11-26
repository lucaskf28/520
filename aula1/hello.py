#!/usr/bin/python3
# print('hello world')
# nome = input("Qual a extensao favorita do inri cristo: ")
# if nome == "py":
#    print("aceertou")
# else:
#    print("erouuuu")
# nome = 'Lucas'
# sobrenome = 'bonitao'
# print(nome, sobrenome, 3*'\n')
#
#!/usr/bin/python3

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
media = int(nota1) + int(nota2)
media = media / 2
if media >= 7:
    print('Aprovado')
elif media <= 3:
    print('Reprovado')
else:
    print('Recuperacao')
