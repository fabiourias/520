#!/usr/bin/python3
#encoding: utf-8


nomes = ['daniel', 'joao', 'kelly']

#list comprehension
print ([nome.title() for nome in nomes])
exit()

#if ternario
#print ('True' if nome =='daniel' else 'false')

'''
print('daniel','prata', sep='.', end='#?\n'),
exit()

nomes =  [' daniel  ', 'joao', 'maria', 'ana']

for nome in nomes:
    if nome == 'maria':
        print ('achei!')
        break
#este else é do for e nao do if!
else:
    print ('Nao achei!')

nomes =  [' daniel  ', 'joao', 'maria', 'ana']
print (nomes)
nome = input ("Digite o nome: ")
nomes.insert(2,nome)
print(nomes)


nome = 'daniel prata da silva'
print (nome.replace('a',"@"))
nomes =  [' daniel  ', 'joao', 'maria', 'ana']
nome = nomes[0].strip()
'''