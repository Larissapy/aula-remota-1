def data(d,m,a):
    return(f'{d}/{m}/{a}')
def main():

    dia = int(input())
    mes = int(input())
    ano = int(input())

    resultado = data(dia,mes,ano)

    print(f'{resultado}')

if __name__ == "__main__":
    main()

