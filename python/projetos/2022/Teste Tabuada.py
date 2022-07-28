print ('Quanto é 23 x 5?')

print ('Digite a letra correspondente a resposta certa')

print ('A - se a resposta for 201')
print ("B - se a resposta for 115")
print ("C - se a resposta for 320")

opcao = {
    'A': '201',
    'B': '115',
    'C': '320'
}

r = input('Escolha a opção!')

A = 'A'
B = 'B'
C = 'C'

if r == A:
    print ("Você Errou")
elif r == B:
    print ("Você Acertou")          
elif r == C:
    print ("Você Errou")
