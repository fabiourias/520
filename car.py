#!/usr/bin/python3
#encoding: utf-8

from classes import Carro, Carro_eletrico
from datetime import datetime
from time import sleep


carro1 = Carro('i320','BMW', 2017)

print(carro1.modelo)

while True:
    if carro1.tanque > 0 and carro1.velocidade < 120:
        carro1.acelerar()
        sleep(0.5)
    elif carro1.velocidade >= 120:
        carro1.frear()
        sleep(3)
    elif carro1.tanque == 0:
        litros = int(input('Quantos litros para abastacer?'))
        if litros == 0:
            break
        carro1.abastecer(litros)
        sleep(5)

    