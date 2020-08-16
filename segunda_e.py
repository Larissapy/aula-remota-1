altura = int(input('Imforme a altura: '))
comprimento = int(input('Agora o comprimento: '))
largura = int(input('E a lagura: '))

area_piso = largura * comprimento
volume = largura * comprimento * altura
area_parede = (2 * altura * largura) + (2 *altura * comprimento)

print(f'Área do piso da sala: {area_piso}m²')
print(f' Volume da sala: {volume}m³')
print(f' Área das paredes da sala: {area_parede}m²')
