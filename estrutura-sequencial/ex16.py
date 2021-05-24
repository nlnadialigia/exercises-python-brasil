area = float(input('Área a ser pintada em m²: '))
litros = int(area / 3)
latas = 0
preco = 0
print(f'Você precisa de {litros} litros de tintas para pintar essa área.')
if litros > 18:
    latas = int((litros % 18) + 1)
    preco = float(latas * 80)
    print(f'Devem ser compradas {int(latas)} latas de tinta, totalizando R${preco:.2f}')
else:
    print('1 lata de tinta é o suficiente com valor de R$80.00')
