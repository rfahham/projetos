#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('lista.txt', 'w') 

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' Lista de Alunos '))
print('{:-^40}'.format(''))
print()

texto = """ 
João da Silva 
José Lima 
Maria das Dores
ALexandre
Jorge
""" 

print(texto)
arq.write(texto)
arq.close()
