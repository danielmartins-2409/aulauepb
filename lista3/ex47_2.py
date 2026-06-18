menor = maior = num = float(input("insira outro número: "))

for i in range(9):
    num2 = float(input("insira outro número: "))
    if num2 > maior:
        maior = num2
    elif num2 < menor:
        menor = num2
    
print("o maior número é ", maior, "e o menor é ", menor)