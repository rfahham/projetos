#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Código

print()
print('-'*20)
print('Imprimindo colorido')
print('-'*20)
print()

cores = {
			'limpa':'\033[m',
			'vermelho':'\033[31m',
			'verde':'\033[32m',
			'amarelo':'\033[33m',
			'azulescuro':'\033[34m',	
			'roxo':'\033[35m',
			'azulclaro':'\033[36m',	
			'pretoebranco':'\033[7;30m',	
        }

nome = input('Qual é o seu nome? ')
print()
print('Meu nome é {}{}{}'.format(cores['vermelho'],nome, cores['limpa']))
print()





# Biblioteca

# print()
# print('')
# print('{}'.format())
# print('{:.2f}'.format())
# 

# variável = int(input(''))
# variável = float(input(''))
# variável = str(raw_input(''))

# 

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