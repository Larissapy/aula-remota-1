def area_piso(l,c):
    return l * c
def area_parede(l,c,a):
    return (2 * a * l) + (2 * a * c)
def volume(l,c,a):
    return l * c * a

def main():
    altura = int(input('Imforme a altura: '))
    comprimento = int(input('Agora o comprimento: '))
    largura = int(input('E a lagura: '))

    area_pi = area_piso(largura,comprimento)
    volume_sala = volume(largura,comprimento,altura)
    area_pa = area_parede(largura,comprimento,altura)

    print(f'Área do piso da sala: {area_pi}m²')
    print(f' Volume da sala: {volume_sala}m³')
    print(f' Área das paredes da sala: {area_pa}m²')

if __name__ == "__main__":
    main()
