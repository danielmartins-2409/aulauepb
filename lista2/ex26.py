num1 = float(input("Insira um numero: "))
num2 = float(input("insira outro número: "))
num3 = float(input("insira outro número: "))

if num1 == num2 == num3:
    print("os numeros sao iguais")
else:
    if num1 > num2 and num1 > num3:
        print(" o primeiro é o maior")
    else:
        if num2 > num1 and num2 > num3:
            print("o segundo é o maior")
        else:
            if num3 > num2 and num3 > num1:
                print("o terceiro é o maior")
            else:
                print("Nao ha valor maior unico")