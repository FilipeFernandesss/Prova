def tinta(area):
    litros = area / 3
    qtd_litros = litros / 18

    arredondar = round(qtd_litros + 0.499)


    if litros <= 18:
        valor = 80
    else:
        valor = arredondar * 80

    print("Quantidade de tinta:{:.2f}".format(litros))
    print("Quantidade de latas de tintas:", arredondar)
    print("Valor a ser pago: ${:.2f}".format(valor))


area = float(input("Digite os metros quadrados da área a ser pintada:\n"))
tinta(area)
