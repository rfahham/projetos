#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Código

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' Aluguel de Carro '))
print('{:-^40}'.format(''))
print()

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kms rodados? '))
valor = float(input('Valor do KM rodado? '))
pago = (dias * valor) + (km + 0.15)
print()
print('O total a pagar é de R$ {}'.format(pago))
print()

# Biblioteca

# print('{}'.format())
# variável = int(input(''))
# variável = float(input(''))