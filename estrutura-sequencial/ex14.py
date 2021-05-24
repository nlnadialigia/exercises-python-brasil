peso = float(input('Digite o peso do peixe em kg: '))
excesso = 0
multa = 0
if peso > 50:
    excesso = peso - 50
    multa = float(excesso * 4)
    print(f'''Um peixe de {peso:.2f}kg excede o peso permitido pelo regulamento de pesca em {excesso:.2f}kg 
  e deverá pagar uma multa de R${multa:.2f}''')
else:
    print('O peixe não excedeu o peso estabelecido pelo regulamento de pesca.')
