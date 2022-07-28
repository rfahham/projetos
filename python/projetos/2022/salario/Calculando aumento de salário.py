print ()
print ('-'*50)
print ('Calculando aumento de salário')
print ('-'*50)
print ()
salario = int(input('Digite seu salário: '))

#Se o salario for menor que 280
if salario < 280:
        por = (20 / 100) * salario
        resultado = salario + por
        print ()
        print ('-'*50)
        print ('Seu salário base é de: R$',salario)
        print ('Seu salário receberá um aumento de: ', 20, '%')
        print ('O valor do aumento será de: R$', por)
        print ('Com o reajuste, o seu salário atual será de: R$',resultado)
        print ('-'*50)
        print ()

#Se o salario é maior que 280 e menor que 700
elif salario > 280 and salario <= 700:
        por = (15 / 100) * salario
        resultado = salario + por
        print ()
        print ('-'*50)
        print ('Seu salário base é de: R$ ',salario)
        print ('Seu salário receberá um aumento de: ',15,'%')
        print ('O valor do aumento será de: R$',por)
        print ('Com o reajuste, o seu salário será de: R$',resultado)
        print ('-'*50)
        print ()

#Se o salario é maior que 700 e menor que 1500
elif salario > 700 and salario <= 1500:
        por = (10 / 100) * salario
        resultado = salario + por
        print ()
        print ('-'*50)
        print ('Seu salário base é de: R$',salario)
        print ('Seu salário receberá um aumento de: ',10,'%')
        print ('O valor do aumento será de: R$',por)
        print ('Com o reajuste, o seu salário será de: R$',resultado)
        print ('-'*50)
        print ()

#Se o salario é maior que 1500
elif salario > 1500.00:
        por = (5 / 100.0) * salario
        resultado = salario + por
        print ()
        print ('-'*50)
        print ('Seu salário base é de: R$',salario)
        print ('Seu salário receberá um aumento de: ',5, '%')
        print ('O valor do aumento será de: R$',por)
        print ('Com o reajuste, o seu salário será de: R$',resultado)
        print ('-'*50)
        print ()