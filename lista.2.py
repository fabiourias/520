#!/usr/bin/python3
#encoding: utf-8
'''
List de frutas, cada fruta e um dic que tem tipo, preco e qtde.
'''

from pprint import pprint
frutas =  [
    {'nome':'banana', 'preco':2.5,'qtde':20},
    {'nome':'laranja', 'preco':3, 'qtde':50},
    {'nome':'atemoia', 'preco':8.5, 'qtde':4},
    {'nome':'caju', 'preco':5.5, 'qtde':6}
]

frutas1 = []
for fruta in frutas:
    fruta['preco'] -= fruta['preco'] * 0.1
    frutas1.append(fruta)
pprint(frutas1)




