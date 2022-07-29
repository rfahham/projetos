#!/usr/local/bin/python
# -*- coding: utf-8 -*-

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' História '))
print('{:-^40}'.format(''))
print()


print ('''
Quem descobriu o Brasil?

Selecione a resposta correta:

(a) Rui Barbosa
(b) Marechal Deodoro da Fonseca
(c) Pedro Alvares Cabral
''')

while True:
    resposta = input('Sua Resposta: ')

    if resposta == 'a':
        print ('Você errou')

    elif resposta == 'b':
        print ('você errou' )
                      
    elif resposta == 'c':  
        print ('Você acertou!!!')
        break

