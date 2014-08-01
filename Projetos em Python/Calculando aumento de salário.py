“As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.”

Para realizar o exercício precisamos saber efetuar porcentagens em Python, que praticamente a mesma coisa em qualquer linguagem programa. Veja:

por = (20 / 100.0) * 150
Analizando:
 por nada mais é que uma variável que recebe o valor da conta
20 é a porcentagem (20%, 30% 15%, etc)
100.0 –> de 100%
* 150 é de quem queremos a porcentagem -> 20 % de 150 ;D

Sabendo realizar porcentagens, o programa praticamente já esta completo, vamos apenas utilizar if e else para realizar testes. Tais como:

salario = input('Digite seu salário: ')

if salario <= 280:      #SE O SALARIO FOR MENOR QUE 280
    {executa alguma função}

salario = input(‘Digite seu salário: ‘)

#Se o salario for maior que 280

if salario <= 280.00:
      por = (20 / 100.0) * salario
      resultado = salario + por
      print ‘Seu salário antes do reajuste: R$’,salario
      print ‘Percentual aumentado: %’,20
      print ‘O valor do aumento é: R$’,por
      print ‘Com o reajuste, o seu salário é: R$’,resultado

#Se o salario é maior que 280 e menor que 700

elif salario > 280.00 and salario <= 700.00:
        por = (15 / 100.0) * salario
        resultado = salario + por
        print ‘Seu salário antes do reajuste: R$’,salario
        print ‘Percentual aumentado: %’,15
        print ‘O valor do aumento é: R$’,por
        print ‘Com o reajuste, o seu salário é: R$’,resultado

#Se o salario é maior que 700 e menor que 1500

elif salario > 700.00 and salario <= 1500.00:
        por = (10 / 100.0) * salario
        resultado = salario + por
        print ‘Seu salário antes do reajuste: R$’,salario
        print ‘Percentual aumentado: %’,10
        print ‘O valor do aumento é: R$’,por
        print ‘Com o reajuste, o seu salário é: R$’,resultado

#Se o salario é maior que 1500

elif salario > 1500.00:
        por = (5 / 100.0) * salario
        resultado = salario + por
        print ‘Seu salário antes do reajuste: R$’,salario
        print ‘Percentual aumentado: %’,5
        print ‘O valor do aumento é: R$’,por
        print ‘Com o reajuste, o seu salário é: R$’,resultado