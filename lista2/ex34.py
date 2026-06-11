import math
valorA = float(input("Valor de A: "))


if valorA == 0:
    print("Não é uma equação do segundo grau")
else:
    valorB = float(input("Valor de B: "))
    valorC = float(input("Valor de C: "))

    delta = math.pow(valorB, 2) - 4 * valorA * valorC
    if delta < 0:
        print("Nao possui raízes reais")
    else:
        if delta > 0:
            raiz1 = ((-valorB)+math.sqrt(delta))/ 2 * valorA
            raiz2 = ((-valorB)-math.sqrt(delta))/ 2 * valorA

            print(f", Possui duas raízes reaisRaízes: {raiz1, raiz2}")
        else:
            raiz = -valorB/(2* valorA)
            print(f"Possui uma raíz real: {raiz}")
