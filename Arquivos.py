


#!/usr/bin/python3
#encoding: utf-8

from datetime import datetime
datetime.now()






'''
ler 20 numeros inteiros e armaze-os num vetor.
Armazene os numros pares no vetor para e o impar no vetor impares
imprime os tres vetores


par = []
impar = []
numeros = []
for x in range(20):
    num = int(input('Digite um numero:'))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(par)
print(impar)
print(numeros)

'''


'''
# inserir nomes ate o fim do looping - digitar sair(sair)
with open ('nomes.txt', 'w') as arquivo:
    while True:
        nome = input('Digite um nome: ')
        if nome.strip().lower() == 'sair':
            break
        arquivo.write(nome + '\n')

#Ja grva o arquivo com o caonteudo em cada linha(se o conteudo tiver /n no fim de cada elemento)

nomes = ['joao\n', 'falvio\n', 'fabio\n']
a = nomes.writelines()
print (str(a))
exit()

#abrindo e lendo aqruivo todo - jogando na variavel
with open('frutas.txt', 'r') as arquivo:
   conteudo = arquivo.readlines() 

#abrir um novo arquivo e adiconar um indice no final da linha.
with open('frutas2.txt', 'w') as arquivo:
    indice = 1
    for linha in conteudo:
        linha = linha.replace('\n', ' - {}\n'.format(indice))
        arquivo.write(linha)
        indice += 1


#print(arquivo.readline().replace('\n','')) ( imprimi a linha e tira o enter)
#arquivo.seek(0) - volta para a linha zero no byte 0.

arquivo = open('frutas.txt', 'r')
print(arquivo.read())
arquivo.close()
'''