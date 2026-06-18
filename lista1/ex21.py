valorHora = float(input("valor ganho por hora: "))
horasTrabalhadas = float(input("Horas trabalhadas: "))

valorBruto = valorHora * horasTrabalhadas

impostoDeRenda = 0.11 * valorBruto
inss = 0.08 * valorBruto
sindicato = 0.05 * valorBruto

valorLiquido = valorBruto - (inss + impostoDeRenda + sindicato)




print(f"""
Salário Bruto:         R${valorBruto:.2f}
IR:                    R${impostoDeRenda:.2f}
INSS:                  R${inss:.2f}
Sindicato:             R${sindicato:.2f}
Salário Liquído:       R${valorLiquido:.2f}
""")
