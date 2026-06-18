base = float(input("Diga a base: "))
expoent = int(input("o Expoente: "))
resultado = 1


for i in range(abs(expoent)):
    resultado *= base

if expoent < 0 :
    if base != 0:
        resultado = 1 / resultado
    else:
        resultado = "indefinido"
        print("Erro: 0 não pode ser elevado a um expoente negativo.")

print("resultado =", resultado)
