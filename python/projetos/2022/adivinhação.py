import random

print("")
print("-"*15)
print ("Seja bem vindo !!!")
print("-"*15)
print("")

guess = 0
x = random.randint(1,5)
print(x)
while guess != x:
	g=input("Insira um numero: ")
	guess = int(g)
	if guess == x:
		print ("Você Acertou, Parabéns!")
	else:
		if guess > x:
			print ("Valor muito alto!")
		else:
			print ("Valor muito baixo!")
print ("Fim do Jogo")
