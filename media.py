#!/usr/bin/python3
#encoding: utf-8

aluno = input("Digite o nome do Aluno: ")

nota1 = int(input("Digite a nota 1: " ))
nota2 = int(input("Digite a nota 2: " ))
nota3 = int(input("Digite a nota 3: " ))
nota4 = int(input("Digite a nota 4: " ))

media  = ((nota1 + nota2 + nota3 + nota4) / 4)
print ("{0} , Sua media no ano e : {1}".format(aluno.title(), media))    