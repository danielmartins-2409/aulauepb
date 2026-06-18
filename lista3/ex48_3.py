num = int(input("Diga o número: "))
count = num
fatorial = 1

if num < 0:
    print("impossível calcular fatorial de número negativo")
elif num == 0:
    print(f"{num}! é igual a {fatorial}")
else:
    while count > 0:
        fatorial *= count
        count -= 1

    print(f"{num}! é igual a {fatorial}")