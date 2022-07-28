import random

print ()
print ('-'*10)
print ("Sorteio")
print ('-'*10)
print ()

j1 = input('Digite o nome do 1° jogador: ')
j2 = input('Digite o nome do 2° jogador: ')
j3 = input('Digite o nome do 3° jogador: ')

sort = random.randint(1,3)

if sort == 1:
    print ('Parabéns',j1,', você Ganhou!!')
elif sort == 2:
    print ('Parabéns',j2,', você Ganhou!!')
elif sort == 3:
    print ('Parabéns',j3,', você Ganhou!!')