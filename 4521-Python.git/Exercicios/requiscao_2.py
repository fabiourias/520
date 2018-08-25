#!/usr/bin/python3
#encoding: utf-8

import requests, json
headers = {'content-type': 'application/json'}

data = json.dumps({
    "nome":'joao',
    "sobrenome":"hummel"
})
try:
    requisicao = requests.delete('http://httpbin.org/delete',data=data, headers=headers) 
    conteudo = requisicao.json() 
except Exception as e:
    print ('Erro: {}'.format(e))

print(conteudo)