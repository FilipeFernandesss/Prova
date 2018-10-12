class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtde_combustivel = 0
        self.capacidade = 200000

    def set_qtd_combus(self, qtd_retirada):
        if self.qtde_combustivel > 0:
            self.qtde_combustivel -= qtd_retirada
            return True
        else:
            return False

    def get_qtd_combus(self):
        return self.qtde_combustivel

    def abastecer_por_valor(self, valor):
        qtd_litros = valor / self.valor_litro #retorna a qtd de litros
        #Verificar se a quantidade de combustivel é maior que  a quantidade de litros
        if self.qtde_combustivel >= qtd_litros:
            self.qtde_combustivel -= qtd_litros
            return qtd_litros
        else:
            return 0

    def abastecer_por_litro(self, litro):
        valor_abastecimento = litro * self.valor_litro #retorna o valor que tem q ser pago
        if self.qtde_combustivel >= litro:
            self.qtde_combustivel -= litro
            return valor_abastecimento
        else:
            return 0

    def consultar_valor(self):
        return self.valor_litro

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_tipo):

        #Garantir que a bomba estpa vazia

        if self.qtde_combustivel == 0:
            self.tipo_combustivel = novo_tipo
            return True
        else:
            return False

    def get_tipo_combus(self):
        return self.tipo_combustivel

    def recarregar_bomba(self, qtd_alterada):
        if (self.qtde_combustivel + qtd_alterada) <= self.capacidade:
            self.qtde_combustivel += qtd_alterada
            return True
        else:
            return False



bomba1 = BombaCombustivel('alcool', 4.50)
print(bomba1.get_tipo_combus())
bomba1.abastecer_por_valor(10)
bomba1.abastecer_por_litro(5)
print(bomba1.consultar_valor())
print('{:.2f}'.format(bomba1.get_qtd_combus()))
bomba1.alterar_valor(4.90)
print(bomba1.consultar_valor())
bomba1.alterar_combustivel('Gasolina')
print(bomba1.get_tipo_combus())

bomba2 = BombaCombustivel('Álcool', 2.90)
bomba2.abastecer_por_valor(15)
bomba2.abastecer_por_litro(20)
print(bomba2.consultar_valor())
print('{:.2f}'.format(bomba2.get_qtd_combus()))