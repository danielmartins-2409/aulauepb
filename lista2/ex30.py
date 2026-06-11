valorHora = float(input("Insira o valor ganho por hora: "))




if valorHora > 0:
    horas = float(input("Quantidade de horas trabalhadas: "))
    if horas > 0:
        salarioBruto = valorHora * horas
        ir = salarioBruto * 0.05
        inss = salarioBruto * 0.10
        fgts = salarioBruto * 0.11
        descontos = ir + inss
        salarioLiquido = salarioBruto - descontos

        print(f"""
                  Salário Bruto = R$ {salarioBruto}
-------------------------------------------------
                  (-) IR = R$ {ir}
-------------------------------------------------
                  (-) INSS = R$ {inss}
-------------------------------------------------
                  FGTS = R$ {fgts}
-------------------------------------------------
                  Total de Descontos = R$ {descontos}
-------------------------------------------------
                  Salário Líquido = R$ {salarioLiquido}""")

    else:
        print("Valor inválido")

else:
    print("Valor inválido")
