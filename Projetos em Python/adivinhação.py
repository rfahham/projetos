print ("Seja bem vindo")
guess = 0
while guess != 5:
	g=input("Insira um numero:")
	guess = int(g)
	if guess == 5:
		print ("Voce Acertou, Parabéns!")
	else:
		if guess > 5:
			print ("Valor muito alto!")
		else:
			print ("Valor muito baixo!")
print ("Fim do Jogo")
