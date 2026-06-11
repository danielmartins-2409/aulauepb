lado1 = float(input("Insira o lado do triangulo: "))
lado2 = float(input("Insira outro lado do triangulo: "))
lado3 = float(input("Insira o outro lado do triangulo: "))

if (lado1 + lado2) > lado3 and (lado2 +lado3) > lado1 and (lado1 + lado3) > lado2:
    if lado1 == lado2 == lado3:
        print("EQUILATERO")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("ISOSCELES")
    else:
        print("ESCALENO")
else:
    print("Nao é um triangulo")