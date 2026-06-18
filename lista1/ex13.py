precoDeCusto = float(input("Insira o valor de custo do produto: "))
percentual = float(input("Insira o percentual de acréscimo em porcentagem: "))
valorDeVenda = precoDeCusto * (1 + percentual/100)
print(f"o valor de venda é {valorDeVenda}")
