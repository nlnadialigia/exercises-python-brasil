h = float(input('Digite a altura: '))
sexo = str(input('Digite o sexo [M/F]: ')).upper()
if sexo == 'M':
  peso =  (72.7 * h) - 58
  print(f'O pesso ideal para uma pessoa de {h:.2f}m do sexo masculino é {peso:.2f}kg')
if sexo == 'F':
  peso = (62.1 * h) - 44.7
  print(f'O pesso ideal para uma pessoa de {h:.2f}m do sexo feminino é {peso:.2f}kg')
