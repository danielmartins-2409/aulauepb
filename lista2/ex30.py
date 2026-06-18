valorHora = float(input("Insira o valor ganho por hora: "))




if valorHora > 0:
    horas = float(input("Quantidade de horas trabalhadas: "))
    if horas >= 0:
        salarioBruto = valorHora * horas
        if salarioBruto <= 900: 
            ir_p = 0
            
        elif salarioBruto <= 1500:
            ir_p = 0.05
        elif salarioBruto <= 2500:
            ir_p = 0.10
        else:
            ir_p = 0.2 
        ir = salarioBruto *ir_p
        inss = salarioBruto * 0.10
        fgts = salarioBruto * 0.11
        descontos = ir + inss
        salarioLiquido = salarioBruto - descontos

        print(f"""
                  Salário Bruto = R$ {salarioBruto}
-------------------------------------------------
                  (-) IR({ir_p*100:.0f}%) = R$ {ir}
-------------------------------------------------
                  (-) INSS (10%)  = R$ {inss}
-------------------------------------------------
                  FGTS (11%) = R$ {fgts}
-------------------------------------------------
                  Total de Descontos = R$ {descontos}
-------------------------------------------------
                  Salário Líquido = R$ {salarioLiquido}""")

    else:
        print("Valor inválido")

else:
    print("Valor inválido")
