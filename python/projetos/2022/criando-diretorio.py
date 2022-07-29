import os

os.system('clear')

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' Criando diretório '))
print('{:-^40}'.format(''))
print()

diretorio = input('Digite o nome do diretório a ser criado: ')
print(diretorio)
os.system('mkdir ' + diretorio)
# os.system('cd ' + diretorio) não funcionou
# os.system('ls')

