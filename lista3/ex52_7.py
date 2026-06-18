n = int(input("Digite um número: "))

if n <= 0:
    print("n deve ser maior que zero.")
else:
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
    print(h)
