num1 = float(input("Insira um numero: "))
num2 = float(input("insira outro número: "))

if num1 > num2:
    print(f"o primeiro número é maior")
else:
    if num1 < num2:
        print(f"o segundo número é maior")
    else: 
        print("os dois numeros sao iguais")