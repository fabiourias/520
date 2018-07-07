#!/usr/bin/python3
#encoding: utf-8

def boas_vindas(nome='Daniel', idade=24):
    nome = input('Digite o seu nome:')
    idade = int(input('Digite sua idade:'))
    dic = {'nome': nome, 'idade': idade}
    return dic

def boas_vindas02(*args):
    for x in args:
        print('Seja bem vindo:  {}!'.format(x))
   
def boas_vindas03(**kwargs):
    ''' funcao de boas vindas! '''
    for x,y in kwargs.items(): #.values .keys .items
        print (x,y, sep=':') 

def calculo_total(**produto):
    ''' funcao calculo soma o total de cada item! '''
    a = produto['qtde']
    b = produto['valor']
    c = produto['nome']
    result = 'Produto: {}, Total: {}'.format(c, a * b)
    return result

def boas_vindas04():
    print ('Seja bem vindo!')

def ola(nome):
    print('Ola {}!'.format(nome))
    boas_vindas04()

#ola('Daniel')

#for nome in nomes:
 #   boas_vindas(nome)

def gravar_log(log):
    with open('python.log', 'a') as arq:
        arq.write(log)


def soma(x ,y):
    return (x + y)

def open_file(nome):
    try:
        with open(nome, 'r') as arquivo:
            return arquivo.readlines()
    except Exception as e:
        return 'Falha ao ler o arquivo informado: {}'.format(e)

def format_file(nome, modo, conteudo=None):
    if modo.lower() == 'r':
        try:            
            with open(nome, modo) as arquivo:
                return arquivo.readlines()
        except Exception as e:
            result = 'Falha ao ler o arquivo informado: {}'.format(e)
            gravar_log(result)
            return result
    elif modo == 'a':
        try:
            with open(nome, modo) as arquivo:
                arquivo.write(conteudo + '\n')
                return True
        except Exception as e:
            return 'Falha ao escrever no arquivo: {} !'.format(e)

