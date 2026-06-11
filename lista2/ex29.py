salario = float(input("insira o salario: "))
salarioReajustado = 0
percentual = 0
if salario <= 0:
    print("Valor inválido")
else:
    if salario <= 250:
        percentual = 20
        salarioReajustado = salario*(percentual/100 + 1)
    else:
        if salario <= 700:
                percentual = 15
                salarioReajustado = salario*(percentual/100 + 1)
        else:
            if salario <= 1500:
                    percentual = 10
                    salarioReajustado = salario*(percentual/100 + 1)
            else:
                   percentual = 5
                   salarioReajustado = salario*(percentual/100 + 1)

print(f"""Salario antes do reajuste = {salario}
-------------------------------------------------
          Percentual aplicado = {percentual}
-------------------------------------------------
          Valor do aumento = {salario * percentual/100}
-------------------------------------------------
          Salário após reajuste = {salarioReajustado}""")

            