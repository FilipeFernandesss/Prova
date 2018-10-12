import random

def gerar():

    numero = random.randint(100, 999)
    return numero


numero = gerar()
for i in range(0, 7):
    valor = float(input("Escolha o número:\n"))

    #print(numero)
    if valor == numero:
        print('Você acertou')
        break
    else:
        print('Tente Novamente')
        print('Tentativa número', i+1)

