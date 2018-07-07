#!/usr/bin/python3
#encoding: utf-8
from random import choice
from funcoes import format_file

''' 
Abrir um txt de nomes 
sortear um nome
percorrer a lista de lambda que tem os metodo upper lower e title
'''

pessoas = format_file('nomes', 'r')
pessoa = choice(pessoas)

estilos= [
    lambda nome: nome.title(),
    lambda nome: nome.upper(),
    lambda nome: nome.lower(),
    lambda nome: nome.replace('a', '@')
]

for item in estilos:
    print (item(pessoa), end='')

exit()


var = lambda x,y: x + y
print(var(10,5))

lamb = lambda a,b,c : ((b ** 2) - (4))



