def potencia(n):
    return n**3

def main():
    num = int(input('Informe o número:'))

    resultado = potencia(num)
    
    print(f'Seu resultado é: {resultado}')

if __name__ == "__main__":
    main()
