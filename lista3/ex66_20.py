divida = float(input("Qual o valor da dívida?: "))

while divida < 0:
    print("Valor inválido")
    divida = float(input("Qual o valor da dívida?: "))

print("Valor da Dívida      % Juros      Parcelas      Valor da Parcela")


juros = 0
parcelas = 1
valor_divida = divida + (divida * juros / 100)
valor_parcela = valor_divida / parcelas
print(f"R$ {valor_divida:.2f}            {juros}           {parcelas}             R$ {valor_parcela:.2f}")

juros = 10
parcelas = 3
valor_divida = divida + (divida * juros / 100)
valor_parcela = valor_divida / parcelas
print(f"R$ {valor_divida:.2f}            {juros}          {parcelas}             R$ {valor_parcela:.2f}")


juros = 15
parcelas = 6
valor_divida = divida + (divida * juros / 100)
valor_parcela = valor_divida / parcelas
print(f"R$ {valor_divida:.2f}            {juros}          {parcelas}             R$ {valor_parcela:.2f}")
