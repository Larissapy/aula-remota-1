def data(d,m,a):
    return(f'{d}/{m}/{a}')
def main():
    dia = int(input('Digite a dia:'))
    mes = int(input('Digite o mês:'))
    ano = int(input('Digite o ano:'))

    resultado = data(dia,mes,ano)

    print(f'Data:{resultado}')

if __name__ == "__main__":
    main()
