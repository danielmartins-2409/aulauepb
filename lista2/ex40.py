num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operacao = input(f"""
Qual operação voce deseja realizar?
----------------------------------
SOMA +
SUBTRAÇÃO -
MULTIPLICAÇÃO *
DIVISÃO / """)

validador = True

valorFinal = 0
if operacao == "+":
    valorFinal = num1+num2
elif operacao == "-":
    valorFinal = num1 - num2
elif operacao == "*":
    valorFinal = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Impossível dividir por 0")
        validador = False
    else:
        valorFinal = num1 / num2
else:
    print("operação inválida")
    validador = False

if validador:
    print(valorFinal)
    if valorFinal%1 == 0:
        print("inteiro")
        if valorFinal%2 == 0:
            print("é par")
        else:
            print("é ímpar")
    else:
        print("decimal")
        print("é decimal, não é ímpar nem par")

    if valorFinal == 0:
        print("é zero, não é positivo nem negativo")
    elif valorFinal > 0:
        print("positivo")
    else:
        print("negativo")
            
