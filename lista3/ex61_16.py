n = int(input(""))
count = n
idadeSoma = 0

if n > 0:
    while count > 0:

        idade = int(input("diga sua idade "))
        if 0 < idade < 130:
            idadeSoma += idade
            count -= 1
        else:
            print("idade inválida")

    media = idadeSoma / n
    if media <= 25:
        print("JOVEM")
    elif media <= 60:
        print("ADULTA")
    else:
        print("IDOSA")
else:
    print("numero invalido")