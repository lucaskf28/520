#!/usr/bin/python3
convidados = []

while True:
    try:
        nome = input("Digite o nome do convidado:")
        if nome.lower().strip() == 'sair':
            raise ValueError
        else:
            convidados.append(nome.lower().strip())
    except ValueError:
        break
for convidado in convidados:
    print("""
        Convite
        Nome: {:>20}
        Endereco: {:>30}
        """.format(convidado, 'blabla'))
