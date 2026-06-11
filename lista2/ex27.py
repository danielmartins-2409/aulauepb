num1 = float(input("Insira o preco do produto 1: "))
num2 = float(input("insira o preco do produto 2: "))
num3 = float(input("insira o preço do produto 3: "))

if num1 == num2 == num3:
    print("o preço do tres produtos são iguais")
else:
    if num1 < num2 and num1 < num3:
        print("deve comprar o primeiro")
    else:
        if num2 < num1 and num2 < num3:
            print("deve comprar o segundo")
        else:
            if num3 < num2 and num3 < num1:
                print("deve comprar o terceiro")
            else:
                print("não há um produto mais barato")