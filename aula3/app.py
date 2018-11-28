#!/usr/bin/python3
from conta import Conta, Poupanca

c1 = Conta("442", 950)
c2 = Poupanca("998", 1390)

print(c1)
print(dir(c2))
c2.saldo = 2680
print(c2)