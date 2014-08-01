print ("Insira as notas bimetrais")
nota1 = input("Primeira nota: ")
nota2 = input("Segunda nota: ")
nota3 = input("Terceira nota: ")
nota4 = input("Quarta nota: ")

media = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) /4

if media >= 6:
	print ("Aprovado")
else:
	print ("Reprovado")