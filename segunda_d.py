hora = int(input('Digite a hora:'))
minuto = int(input('Digite o minuto:'))

minutos = (hora * 60) + minuto
segundos = minutos * 60

print(f'Já se passaram {segundos} segundos desde a meia noite')
