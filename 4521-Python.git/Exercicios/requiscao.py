#!/usr/bin/python3
#encoding: utf-8

import requests, json
headers = {'content-type': 'application/json'}

data = json.dumps({
    "nome":'Ana2',
    "email":"AnaUr2@asda.com"
})
try:
    requisicao = requests.delete('http://localhost:5000/usuarios/10', headers=headers ) 
    conteudo = requisicao.json() 
except Exception as e:
    print ('Erro: {}'.format(e))

print(conteudo)