year = int(input("Digite o número coorrespondente a algum ano: "))

if year > 0:

    if year%100 == 0 and year%400 == 0:
            print("Este ano é bissexto")
    else:
        if year % 4 == 0 and year%100 != 0:
            print("Este ano é bissexto")
        else:
            print("Este ano não é bissexto")
else:
    print("Ano inválido")
    