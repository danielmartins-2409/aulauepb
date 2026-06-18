temp = float(input("Digite a temperatura, digite um numero menor que -273 para parar: "))
media = maior = menor = temp
count = 1

if temp < -273:
    print("nenhum valor informado")
else:
    while temp >= -273 :
        temp = float(input("Digite a temperatura: "))
        if temp >= -273:
            count += 1
            media += temp
            if temp > maior:
                maior = temp
            elif temp < menor:
                menor = temp

    media = media/count
    print(f"""Maior temperatura: {maior}, Menor temperatura: {menor}, Média das temperaturas: {media}""")
