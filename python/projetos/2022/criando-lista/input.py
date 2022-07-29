

import time

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' Criando Lista '))
print('{:-^40}'.format(''))
print()

arq = open('lista.txt', 'a')

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
sexo = input("Informe seu sexo: ")

buffer = 'Nome: '+ str(nome)  + ' Idade:' + str(idade) + ' Sexo: ' + str(sexo)
print(buffer)

arq.write(time.asctime() + ' ' +str(nome) + ' ' + str(idade) + ' ' + str(sexo)+ '\n')
arq.close()