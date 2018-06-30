#!/usr/bin/python3
#encoding: utf-8

aluno = input("Digite o nome do Aluno: ")

nota1 = int(input("Digite a nota 1: " ))
nota2 = int(input("Digite a nota 2: " ))
nota3 = int(input("Digite a nota 3: " ))
nota4 = int(input("Digite a nota 4: " ))

media  = ((nota1 + nota2 + nota3 + nota4) / 4)
if media >= 7:
    result = ('voce foi aprovado!')    

else:
    result = ('voce foi reprovado!')

print ("{0} , Sua media no ano foi : {1}\n {2}".format(aluno.title(), media, result))    

'''
linguagem = input("Digite uma linguagem de programacao:")
linguagem = linguagem.lower().strip()
if linguagem == 'python':
    print ('voce escolheu certo!')
elif linguagem == 'java':
    print ('ta valendo')
else:
    print ('voce errou!')

'''