def media(a,b,c):
    return (a + b + c) /3

def main():    
    a = int(input('Digite o primeiro número:'))
    b = int(input('Digite o segundo número:'))
    c = int(input('Digite o terceiro número:'))

    resultado = media(a,b,c)

    print(f'A média é: {resultado}')

if __name__ == "__main__":
    main()
