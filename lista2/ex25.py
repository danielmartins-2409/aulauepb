nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))

media = (nota1 + nota2)/2

if (nota1 > 0 and nota2 > 0 and nota1 <=10 and nota2<=10) :
    if media >= 7 and media < 10:
        print("Aprovado")
    else:
        if media < 7:
            print("Reprovado")
        else:
            print("Aprovado com distinção")
else:
    print("nota inválida inserida")







