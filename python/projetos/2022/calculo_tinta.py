#!/usr/bin/env python 
# -*- coding: utf-8 -*-
print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' Calculando Tinta '))
print('{:-^40}'.format(''))
print()

largura = float(input('Digite a largura: '))
altura= float(input('Digite a altura: '))
print()

area = largura * altura

print('Sua parede tem a dimensão de {} x {} e sua área total é de {} m2.'.format(largura, altura, area))

tinta = area /2

print('Para pintar sua parede, você precisará de {}l de tinta.'.format(tinta))

print()

