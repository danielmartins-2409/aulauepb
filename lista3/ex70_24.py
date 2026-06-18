total = 0
codigo = input("Código do produto (0 para encerrar): ")

while codigo != "0":
    quantidade = int(input("Quantidade: "))

    if quantidade < 0:
        print("Quantidade inválida")
    else:
        if codigo == "100":
            preco = 1.20
        elif codigo == "101":
            preco = 1.30
        elif codigo == "102":
            preco = 1.50
        elif codigo == "103":
            preco = 1.20
        elif codigo == "104":
            preco = 1.30
        elif codigo == "105":
            preco = 1.00
        else:
            print("Código inválido")
            preco = 0

        if preco != 0:
            valor = preco * quantidade
            total += valor
            print(f"Valor do item: R$ {valor:.2f}")

    codigo = input("Código do produto (0 para encerrar): ")

print(f"Total geral: R$ {total:.2f}")