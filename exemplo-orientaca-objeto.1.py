#!/usr/bin/python3
#encoding: utf-8
from classes import Dog
from time import sleep

dog1 = Dog('bilu',2,'pitbull')
dog2 = Dog('rex',1,'poodle')
dog1.andar()
dog1.dormir()
while True:
    print(dog1.nome)
    if dog1.energia  > 0 and dog1.fome > 0:
        dog1.andar()
    if dog1.energia == 0:
        dog1.dormir()
        sleep(1)
    if dog1.fome == 0:
        dog1.comer()
        sleep(1)
    sleep(2)