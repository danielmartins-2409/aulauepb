salario = float(input("Insira o salário: "))

if salario >= 0:
    filho = int(input("insira a quantidade de filhos: "))
    somaSalario = maiorSalario = salario 
    somaFilhos = filho
    populacao = 1
    salarioAte250 = 0
    if salario <= 250:
        salarioAte250 += 1

    while salario >= 0:
        salario = float(input("Insira o salário: "))
        if salario >= 0:
            if salario > maiorSalario:
                maiorSalario = salario
            if salario <= 250:
                salarioAte250 += 1
        
            somaSalario += salario
            filho = int(input("insira a quantidade de filhos: "))
            somaFilhos += filho
            populacao += 1

    print(f"""média dos salários: {somaSalario/populacao}, média do número de filhos: {somaFilhos/populacao}, maior salário: {maiorSalario}, Percentual de pessoas com salárrio de ate 250: {salarioAte250/populacao * 100:.2f}%""")
