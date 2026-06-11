turno = input("Em que turno voce estuda? 'M', 'V' ou 'N': ")

if turno == "M":
    print("Bom Dia!")
else:
    if turno == "V":
        print("Boa Tarde!")
    else:
        if turno == "N":
            print("Boa Noite!")
        else:
            print("Valor inválido!")
