horas = float(input("Quanto você ganha por hora?"))
numero_horas = float(input("Quantas horas você trabalha por mês?"))

salario = horas * numero_horas
inss = (salario * 8)/ 100
imposto_renda = (salario * 11)/ 100
sindicato = (salario * 5)/ 100
descontos = inss + imposto_renda + sindicato
salario_liquido = salario - descontos

print('Seu salário bruto é:', salario)
print('Você pagou ao INSS:{:.2f}'.format(inss))
print('Você pagou ao sindicato:{:.2f}'.format(sindicato))
print('Seu salário liquido:{:.2f}'.format(salario_liquido))

