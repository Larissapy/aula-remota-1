largura = int(input('Imforme a largura da sua sala: '))
comprimento = int(input('Agora o comprimento: '))
altura = int(input('E a altura da parede: '))

area_piso = largura * comprimento
area_parede = 2 * altura * largura + 2 * altura * comprimento
volume = largura * comprimento * altura

print(f'Área do piso da sala: {area_piso}m²')
print(f' Volume da sala: {volume}m³ ')
print(f' Área das paredes da sala: {area_parede}m² ')
