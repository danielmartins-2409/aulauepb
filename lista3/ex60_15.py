num = int(input("Digite um número inteiro: "))
contador = 0

if num > 0:
    for i in range(1, num +1):
        if num%i == 0:
            contador +=1

    if contador == 2:
        print("é primo")
    else: 
        print("Não é primo")
else:
    print("nao existe primo negativo")