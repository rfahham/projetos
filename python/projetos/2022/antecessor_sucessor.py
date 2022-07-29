#!/usr/bin/env python 
# -*- coding: utf-8 -*-

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' Cálculando o número sucessor e o antecessor '))
print('{:-^40}'.format(''))
print()

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}' . format(n, (n-1),(n+1)))
print()