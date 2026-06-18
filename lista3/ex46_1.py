
count = 0

while count < 30:

    nota = float(input("Insira a primeira nota: "))
    if 0 <= nota <= 10:
        nota2 = float(input("Insira a segunda nota: "))
        if 0 <= nota2 <= 10:
            media = (nota + nota2)/2
            print(media)
            count += 1
            if 7 <= media <= 10:
                print("APROVADO")
            elif 4 <= media:
                print("RECUPERAÇÃO")
            else:
                print("REPROVADO")
        else: 
            print("nota inválida")    
    else:
        print("nota inválida")
    