nome = input("nome do vendedor: ")
salarioFixo = float(input("salario fixo: "))
vendas = float(input("total de vendas em dinheiro: "))

comissao = 0.15
salarioFinalDoMes = salarioFixo + (vendas(1+comissao))

print(nome, salarioFixo, salarioFinalDoMes)