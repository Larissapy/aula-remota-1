def area_piso(l,c):
    return l * c
def area_parede(l,c,a):
    return (2 * a * l) + (2 * a * c)
def volume(l,c,a):
    return l * c * a

def main():
    altura = int(input())
    comprimento= int(input())
    largura = int(input())

    area_pi = area_piso(largura,comprimento)
    volume_sala = volume(largura,comprimento,altura)
    area_pa = area_parede(largura,comprimento,altura)

    print(f'{area_pi}')
    print(f'{volume_sala}')
    print(f'{area_pa}')

if __name__ == "__main__":
    main()
