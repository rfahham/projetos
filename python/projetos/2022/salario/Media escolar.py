print ()
print ('-'*26)
print ("Insira as notas bimestrais")
print ('-'*26)
print ()
nota1 = input("Primeira nota: ")
nota2 = input("Segunda nota: ")
nota3 = input("Terceira nota: ")
nota4 = input("Quarta nota: ")

media = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) /4

print ()
if media >= 6:
	print ("O aluno foi Aprovado")
	print ()
else:
	print ("O aluno foi Reprovado")
	print ()