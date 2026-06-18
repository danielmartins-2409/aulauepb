n = int(input(""))
numerate = 1
soma = 0

if n <= 0:
    print("valor inválido")
else:
    for i in range(1, n+1):
        soma += i/numerate    
        numerate += 2
    print(soma)
