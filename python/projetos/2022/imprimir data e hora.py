from datetime import datetime

now = datetime.now()

print (datetime.now())

print ('Ano: ', now.year)
print ('Mês: ', now.month)
print ('Dia: ', now.day)
print ('Hora: ', now.hour)
print ('Minuto: ', now.minute)
print ('Segundo: ', now.second)

print (now.day, '/', now.month, '/', now.year, '-', now.hour, ':', now.minute, ':', now.second)