s = float(input('Digite o valor do salário/hora: R$ '))
h = int(input('Digite as horas trabahadas no mês: '))
sb = float(s * h)
ir = float(sb * 0.11)
inss = float(sb * 0.08)
sindicato = float(sb * 0.05)
sl = float(sb - ir - inss - sindicato)
print(f'''
+ Salário Bruto: R${sb:.2f}
- IR (11%): R${ir:.2f}
- INSS (8%): R${inss:.2f}
- Sindicato (5%): R${sindicato:.2f}
= Salário Líquido: R${sl:.2f}
''')
