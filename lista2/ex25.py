nota1 = float(input("insira a primeira nota: "))

if 0 <= nota1 <= 10:
    nota2 = float(input("insira a segunda nota: "))
    if 0 <= nota2 <= 10:
        media = (nota1 + nota2)/2
        if media >= 7 and media < 10:
            print("Aprovado")
        else:
            if media < 7:
                print("Reprovado")
            else:
                print("Aprovado com distinção")
    else:
        print("nota inválida inserida")
else:
    print("nota inválida inserida")






