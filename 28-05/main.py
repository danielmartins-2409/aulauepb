valor = int(input(""))
print(f"Tabuada do {valor}")


if valor < 0: 
    print("invalido")
else:
    for i in range(1, 11):
        print(valor,'X' ,i, "=", valor * i)