#!/usr/bin/python3
#encoding: utf-8

try:
    nome = input('Digite um nome de arquivo:')
    if nome == 'Privado':
        raise FileNotFoundError
    else:
        with open(nome, 'r') as arq:
            conteudo = arq.readlines()
            print(conteudo)
    
except TypeError as e:
    print('Erro, arquivo nao existe: {}'.format(e))

exit()

# Testa a entrada da linguagem digitada
try:
    lang = input('qual melhor linguage?')
    if lang == 'python':
        print('Voce acerto! : {}'.format(lang))
except TypeError as e:
    print('Entrada invalida {}'.format(e))
'''
Blocao else (raise) cria uma excessao com descricao mais friendly quando
       o usuário digita errado.
'''
    else:
        raise TypeError
except TypeError as e:
    print('Entrada invalida {}'.format(e))
finally:
    print('Sempre executa')        