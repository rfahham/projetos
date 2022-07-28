print ()
print ('-'*16)
print ('Calculando Idade')
print ('-'*16)
print ()
idade = input('Entre com sua idade: ')

try:
  idade_convertida = int(idade)
  if idade_convertida > 30:
    print('Você é velho pra caramba!')
  else:
    print('Parabéns, você é novo!')
except ValueError:
  print('Você entrou com uma idade inválida')
