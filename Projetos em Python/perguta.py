# coding=utf-8

print "Entre com sua idade: "
idade = raw_input()

try:
  idade_convertida = int(idade)
  if idade_convertida > 30:
    print "Voce é velho pra caramba!"
  else:
    print "Parabens, voce é novo!"
except ValueError:
  print "Voce entrou com uma idade invalida"
