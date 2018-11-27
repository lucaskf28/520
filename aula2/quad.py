#!/usr/bin/python3
# quad = lambda x: x*x

# for k in range(10):
#     print(quad(k+1))

# for i in range(10):
#     print((lambda x: x*x)(i+1))

quadrado = [(lambda x: x*x)(y+1) for y in range(10)]
print(quadrado)
