nota1 = float(input("Digite a primeira nota: "))

if nota1 >= 0 and nota1 <=10:
    nota2 = float(input("Digite a segunda nota: "))
    if nota2 >= 0 and nota2 <= 10:
        nota3 = float(input("Digite a terceira nota: "))
        if nota3 >= 0 and nota3 <= 10:
            media = (nota1 + nota2 + nota3)/3
            if media == 10:
                print("APROVADO COM DISTINÇÃO", media)
            elif media >= 7 :
                print("APROVADO", media)
            else:
                 print("REPROVADO", media)
                
        else:
            print("nota inválida")
    else: 
        print("nota inválida")
else:
    print("nota inválida")