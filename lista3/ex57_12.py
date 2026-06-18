count = 0
otimo = bom = regular = 0
idadeOtimo = 0
mediaOtimo = 0

while count < 5:
    idade = int(input("insira sua idade: "))
    if 0 < idade < 130:

        opiniao = input("diga sua opiniao: Otimo - 3, Bom - 2, regular - 1: ")
        if opiniao == '3':
            otimo += 1
            idadeOtimo += idade
            count += 1
        elif opiniao == '2':
            bom += 1
            count += 1
        elif opiniao == '1':
            regular += 1
            count += 1
        else:
            print("opiniao inválida")
   
    else:
        print("idade inválida")


if otimo > 0:
    mediaOtimo = idadeOtimo/otimo
else:
    mediaOtimo = 0
print(f"""
        Média da idade das pessoas que responderam ótimo: {mediaOtimo}
        -----------------------------------------------
        Quantidade de pessoa que responderam regular: {regular}
        -----------------------------------------------
        porcentagem de pessoas que responderam bom entre todos: {(bom/(otimo+bom+regular))*100}%""")
       