v1 = input(‘Digite o valor da primeira nota: ‘)
v2 = input(‘Digite o valor da segunda nota: ‘)

nota = (v1 + v2) /2

#nota A

if nota >= 9 and nota <= 10:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————’
    print ‘Você tirou um A!’
    print ‘Sua media é de:’,nota
    print ‘você foi aprovado!!’

#nota B

elif nota >= 7.5 and nota < 9:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————’
    print ‘Você tirou um B!’
    print ‘Sua media é de:’,nota
    print ‘você foi aprovado!!’

#nota C

elif nota >= 6.5 and nota < 7.5:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————’
    print ‘Você tirou um C!’
    print ‘Sua media é de:’,nota
    print ‘você foi aprovado!!’

#nota D

elif nota >= 4 and nota < 6:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————’
    print ‘Você tirou um D!’
    print ‘Sua media é de:’,nota
    print ‘você foi reprovado!!’

#nota E

elif nota < 4:
    print ‘A nota da primeira prova: ‘,v1
    print ‘A nota da segunda prova: ‘,v2
    print ‘——————————’
    print ‘Você tirou um E!’
    print ‘Sua media é de:’,nota
    print ‘você foi reprovado!!’

