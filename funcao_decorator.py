#!/usr/bin/python3
#encoding: utf-8
from datetime import datetime
from funcoes import format_file
print(dog1.__doc__)

while True:
    nome_arq = input('Digite o nome do arquivo ou "s" para Sair :')
    if nome_arq == 's':
        break
    mod = input('Modo de Abertura: ')
    if mod == 'r':
        a = format_file(nome_arq, mod)
        print(a)
    elif mod == 'a':
        conteudo = input('Digite o conteudo: ')
        format_file(nome_arq, mod, conteudo)


exit()

def  decorator(func):
    ''' decorator -> interna -> funcao decorada'''
    def interna(x,y):
        print (x, y)
    return interna

decorator ('fabio','urias')
exit()
def externa(idioma):
    dic = {'pt' : 'ola', 'pi': 'Ahoy', 'en': 'Hello'}

    def interna(nome):
        print ('{} {}'.format(dic[idioma], nome))
    return interna


func = externa('pi')
func('Pedro')
func('Daniel')
func('joao')

