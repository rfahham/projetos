import random #1

j1 = raw_input('(1° jogador) Digite seu nome: ')#2
j2 = raw_input('(2° jogador) Digite seu nome: ')#3
j2 = raw_input('(3° jogador) Digite seu nome: ')#4

sort = random.randint(1,3) #5

if sort == 1:#6
    print 'Parabéns',j1,'Você Ganhou!!'
elif sort == 2:#7
    print 'Parabéns',j2,'Você Ganhou!!'
elif sort == 3: #8
    print 'Parabéns',j3,'Você Ganhou!!'

Na linha 1, importamos a biblioteca Random ( que em inglês significa aleatório) , vai nos proporcionar o essencial dessa aplicação o sorteio (vamos ver melhor mais adiante)

Na linha 2 – Pede o nome do 2° usuário
Na linha 3 – Pede o nome do 3° usuário
Na linha 4 – Pede o nome do 4° usuário

Criamos uma variável que vai conter o valor sorteado com o seguinte comando:

sort = random.randint(1,3)
sort – nome da variável
random.randint(1,3) – Sorte- ia um numero de 1 a 3

Na linha 6,  fazemos um teste para saber se o numero sorteado é  1, se for escreve que o vencedor é o jogador 1
Na linha 7, fazemos um teste para saber se o numero sorteado é 2, se for o vencedor é o jogador 2
Na linha 8, fazemos um teste para saber se o numero sorteado é 3, se for, então ganhador é o jogador 3