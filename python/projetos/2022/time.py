#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Código
import os

os.system('clear')

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' Convertendo tempo '))
print('{:-^40}'.format(''))
print()

calculatime = float(input('Qual a quantidade de minutos a ser convertido? '))

hora = calculatime / 60
print('{} horas'.format(hora))

segundos = calculatime * 60
print('{} segundos'.format(segundos))

milisegundos = calculatime * 60 * 1000
print('{} milisegundos'.format(milisegundos))




# Biblioteca

# print('{}'.format(''))
# variável = int(input(''))
# variável = float(input(''))


# 1 hora = 60 minutos
# 1 minuto = 60 segundos
# 1 segundo = 1000 milisegundos
