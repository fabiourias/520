#!/usr/bin/python3
#encoding: utf-8

lista = [
    lambda x,y: x + y,
    lambda x,y: x - y,
    lambda x,y: x * y,
    lambda x,y: x ** y,
    lambda x,y: x ** 0.5 + y ** 0.5,
]
for item in lista:
    print (item(64,25))

exit()


var = lambda x,y: x + y
print(var(10,5))

lamb = lambda a,b,c : ((b ** 2) - (4))



