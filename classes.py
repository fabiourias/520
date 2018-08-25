#!/usr/bin/python3
#encoding: utf-8

class Dog():
    ''' tentando abstrair um cachorro'''

    def __init__(self,nome,idade,raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.energia = 5
        self.fome = 5

    def andar(self):
        self.energia -= 1
        self.fome -= 1
        print('''
    andando......
    energia:{}
    fome:{}'''.format(self.energia, self.fome))

    def comer(self):
        self.fome = 5
        self.energia = 5
        print('comendo.....'.format(self.fome, self.energia))
        sleep(2)
        print(self.fome, self.energia)
    def dormir(self):    
        self.energia = 5
        print('ZzzZzzzZZZ!!!!!')

    
        
class Carro():
    ''' tentando abstrair um carro'''
    
    def __init__(self,modelo,marca,ano,cor='none',placa='none'):
        # Caracteristicas
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.placa = placa
        self.velocidade = 0
        self.tanque = 60
        self.combustivel = 'gasolina'
    #Comportamentos

    def acelerar(self):
        self.velocidade += 10
        print ('VrummMMMM')
        self.tanque -= 1
        
    def frear(self):
        self.velocidade = 0
        print('freando....')
        
    
    def abastecer(self,litros):
        self.tanque += litros
        print ('Abastecendo.....')

    def __str__(self):
        return 'Marca: {} Modelo: {} ano: {}\
        '.format(self.marca, self.modelo, self.ano)


# Classe Pai, Filho e super().O super() mantem o __init__ da classe Pai e troca apens o que vc quiser.

class Carro_eletrico(Carro):
    def __init__(self,ano,modelo,marca):
        super().__init__(ano,modelo,marca)
        self.combustivel ='energia'


        