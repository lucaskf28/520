#!/usr/bin/python3
nome = input("digite o nome do arquivo: ")
shebang = '#!/usr/bin/python3\n'
with open(nome+'.py', 'r') as arquivo:
    linha1 = arquivo.readline()
    if linha1 == "#!/usr/bin/python3":
        print("ja tem xibeng")
    else:
        try:
            with open(nome+'.py', 'x') as arquivo:
                arquivo.write(shebang)
        except FileExistsError:
            print("arquivo ja existe")

