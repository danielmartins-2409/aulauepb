n = int(input("Quanto quadrílateros quer calcular a área: "))

while n > 0:
    lado = float(input("Diga o lado do quadrado: "))
    if lado > 0:
        area = lado**2
        print("area =", area)
        n -=1
    else:
        print("valor inválido")