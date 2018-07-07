#!/usr/bin/python3
#encoding: utf-8

lista = list(range(1000))
lista = [x+1 for x in range(100) if x%2 ==0]
print (lista)




exit()

try:
    num = int(input("Digite um numero inteiro: "))
    num2 = int(input("Digite um numero inteiro: "))
    div = num /num2
    print(num)
except ValueError as e:
    print('Nao e um numero inteiro {}'.format(e))
except ZeroDivisionError as e:
    print('Numero nao divisivel por 0 {}'.format(e))
except KeyboardInterrupt as e:
    print('Saida inesperada : {}'.format(e))
except Exception as e:
    print('erro desconhecido {}'.format(e))        