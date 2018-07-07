#!/usr/bin/python3
#encoding: utf-8

x = 10

def escopo():
    global x
    #x = 15
    print(x)

print(x)
escopo()
print (x)
