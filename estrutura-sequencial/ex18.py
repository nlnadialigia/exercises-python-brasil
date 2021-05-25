file = float(input('Informe do tamanho do arquivo em MegaByte: '))
link = float(input('Informe a velocidade do link em Mbps: '))
time = ((file * 8) / link) / 60
print(f'O tempo aproximado de download é de {time:.2f} minutos')
