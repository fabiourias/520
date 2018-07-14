#!/usr/bin/python3
#encoding: utf-8

from classes import  Carro_eletrico
from datetime import datetime
from time import sleep

carro2 = Carro_eletrico('Prius', 'Toyota', 2018)

while True:
    if carro2.tanque > 0 and carro2.velocidade < 120:
        carro2.acelerar()
        sleep(0.5)
    elif carro2.velocidade >= 120:
        carro2.frear()
        sleep(3)
    elif carro2.tanque == 0:
        litros = int(input('Quanto de carga vai abastecer?'))
        if litros == 0:
            break
        carro2.abastecer(litros)
        sleep(5)

    