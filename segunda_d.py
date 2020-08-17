def segundos(h,m,s):
    return ((h * 60) + m) * 60 + s

def main():
    hora = int(input('Digite a hora: '))
    minuto = int(input('Os minutos: '))
    segundo = int(input('E os segundos: '))

    resultado = segundos(hora,minuto,segundo)

    print(f'Já se passaram {resultado} segundos desde a meia noite')

if __name__ == "__main__":
    main()
