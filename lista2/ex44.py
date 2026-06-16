idade = int(input("Diga a idade do nadador: "))


if 0 < idade < 130:
    if 5 <= idade <= 7:
        print("Infantil A")
    elif 8 <= idade <= 10:
        print("Infantil B")
    elif 11 <= idade <= 13:
        print("juvenil A")
    elif 14 <= idade <= 17:
        print("juvenil B")
    elif idade >= 18:
        print("adulto")
    else:
        print("fora de categoria")
else:
    print("idade inválida")