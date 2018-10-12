#Filipe Fernandes Araujo
#Ra: 21800169


def verificar(num1, num2):
    inversor = str(num2)
    reversed(inversor)
    inverso = ''.join(reversed(inversor))
    print(inverso)
    print(num1)
    if num1 == int(inverso):
        return True
    else:
        return False


print(verificar(123, 321))