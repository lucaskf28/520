#!/usr/bin/python3
def teste(*args):
#def teste(x,*args):
    print(args)

teste(1,2,3,4,5,6)

def teste2(**kwargs):
    print(kwargs)

teste2(a=2,b=2,c=3)