#!/usr/bin/python3
class Conta():
    '''
    tentanndo abstrair uma conta corrente
    '''
    def __init__(self,n_cont, saldo=0):
        self.conta = n_cont
        self.saldo = saldo
        #print('metodo construtor')

    def metodo(self):
        print('metodo interno')

    def sacar(self, valor:int) -> bool:
        '''metodo para sacar uma grana da conta'''
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False
            #print("Saldo atual apos saque eh de {}".format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def transferir(self, valor, conta):
        try:
            if not self.sacar(valor):
                raise ValueError("Falha na transferencia")
            try:
                conta.depositar(valor)
            except AttributeError:
                print("Objeto destino nao possui metodo depositar")
                self.depositar(valor)
        except Exception as e:
            print('Erro: {}'.format(e))
        
    def __str__(self):
        return 'conta: {} saldo: {}'.format(self.conta, self.saldo)

c1 = Conta('123', 1000)
c2 = Conta('456', 2500)

c1.sacar(300)
c1.depositar(500)

c1.transferir(350,c1)

print("conta: {}, Saldo:{}".format(c1.conta, c1.saldo))
print("conta: {}, Saldo:{}".format(c2.conta, c2.saldo))