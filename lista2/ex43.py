quantMorango = float(input("Diga a quantidade em kg de morangos: "))
quantMaca = float(input("Diga a quantidade em kg de maçãs: "))
valorTotal = 0

if quantMaca >= 0 and quantMorango >= 0:

    if quantMorango <= 5:
        valorTotal += quantMorango*2.5
    else:
        valorTotal +=quantMorango*2.2
    
    if quantMaca <= 5:
        valorTotal += quantMaca *1.8
    else:
        valorTotal += quantMaca * 1.5

    if (quantMaca+quantMorango) > 8 or valorTotal > 25:
        valorTotal = valorTotal * 0.9

    print(f"deverá pagar R${valorTotal}")

else:
    print("Quantidade inválida inserida")
