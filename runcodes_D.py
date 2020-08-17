def segundos(h,m,s):
    return ((h * 60) + m) * 60 + s

def main():
    hora = int(input())
    minuto = int(input())
    segundo = int(input())

    resultado = segundos(hora,minuto,segundo)

    print(f'{resultado}')

if __name__ == "__main__":
    main()
