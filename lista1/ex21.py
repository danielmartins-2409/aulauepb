valorHora = float(input("valor ganho por hora: "))
horasTrabalhadas = float(input("Horas trabalhadas: "))

valorBruto = valorHora * horasTrabalhadas

impostoDeRenda = 0.11
inss = 0.08
sindicato = 0.05

valorLiquido = valorBruto - (valorBruto*(inss + impostoDeRenda + sindicato))
print(f"""
      salário bruto = R${valorBruto} 
------------------------------------------
      IR = R${valorBruto*(impostoDeRenda)}
------------------------------------------
      INSS = R${valorBruto*(inss)}
------------------------------------------
      Sindicato = R${valorBruto*sindicato}
------------------------------------------
      Salário Líquido = R${valorLiquido}
""")