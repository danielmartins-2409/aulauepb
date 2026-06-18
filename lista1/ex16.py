nome = input("nome do vendedor: ")
salarioFixo = float(input("salario fixo: "))
vendas = float(input("total de vendas em dinheiro: "))

comissao = 0.15
salarioFinalDoMes = salarioFixo + (vendas * comissao)

print(f"nome: {nome}, salário fixo: {salarioFixo}, salário final: {salarioFinalDoMes}")
