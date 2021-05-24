from math import ceil, floor

area = 100
area_com_folga = area + (area * 0.10)
litros_por_metro = 6
litros_utilizados = area_com_folga / litros_por_metro
litros_por_lata = 18
latas = ceil(litros_utilizados / litros_por_lata)
print(f'latas = {latas}')
print(f'Valor total das latas: R${(latas * 80):.2f}\n')

litros_por_galao = 3.6
galoes = ceil(litros_utilizados / litros_por_galao)
print(f'galoes = {galoes}')
print(f'Valor total dos galoes: R${(galoes * 25):.2f}\n')

latas = floor(litros_utilizados / litros_por_lata)
valor_latas = latas * 80

litros_faltantes = litros_utilizados % litros_por_lata

galoes = ceil(litros_faltantes / litros_por_galao)
valor_galoes = galoes * 25

total = valor_latas + valor_galoes

print(f'''Você deverá comprar {latas} lata de 18 litros
e {galoes} galões de 3,6 litros, totalizando R${(total):.2f}''')
