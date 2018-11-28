class Pai:
    a = "Classe pai"

class Mae:
    b = "Classe mae"

class Filho(Pai, Mae):
    c = 'classe filho'

obj = Filho()

print(obj.a,obj.c)