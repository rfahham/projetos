#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Código

b = 1
while b < 11:
	print (b)
	b=b+1
print('FIM')

print('=' * 30)

c = 1
while c < 11:
	print(c)
	c = c + 1
print('FIM')

print('=' * 30)

r = 'S'
while r == 'S':
	n = int(input('Digite um valor: '))
	r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!')


# Biblioteca

# print()
# print('')
# print('{}'.format())
# print('{:.2f}'.format())
# 


# variável = int(input(''))
# variável = float(input(''))
# variável = str(input(''))

# cores código ANSI

# STYLE			TEXT				BACK
# 0 none		30 Branco			40 Branco
# 1 bold		31 Vermelho			41 Vermelho
# 4 Underline	32 Verde			42 Verde
# 7 Negative	33 Amarelo			43 Amarelo
#				34 Azul				44 Azul	
#				35 Roxo				45 Roxo
#				36 Azul Claro		46 Azul Claro	
#				37 Cinza			47 Cinza
#
# EXEMPLO			
# print('\033[31mMULTADO!\033[m ')
#
# cores = {
#			'limpa':'\033[m',	
#			'azul':'\033[34m',	
#			'amarelo':'\033[33m',	
#			'pretoebranco':'\033[7;30m',	
#         }
#
# print('Meu nome é {}'.format(cores['pretoebranco'], nome, cores['limpa']))
