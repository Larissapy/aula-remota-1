h = int(input('Digite a hora'))
m = int(input('Os minutos'))
s = int(input('E os segundos'))

segundos = ((h * 60) + m ) * 60
resultado = segundos + s

print(f'Já se passaram {resultado} segundos desde a meia noite')
