num = int(input("insira um numero positivo: "))
pares = impares = count = somaPares = somaImpares =  0

if num > 0:
    count += 1
    if num % 2 == 0:
        pares += 1
        somaPares += num
        
    else:
        impares +=1
        somaImpares += num
    while num != 0:
        num = int(input("insira um numero positivo: "))
        if num > 0:
            if num % 2 ==0:
                pares += 1
                somaPares += num
            else:
                impares +=1
                somaImpares += num
            count += 1

if count > 0:
    if pares > 0:
        mediaPares = somaPares / pares
    else:
        mediaPares = 0

    print("Pares:", pares)
    print("Ímpares:", impares)
    print("Média dos pares:", mediaPares)
    print("Média geral:", (somaPares + somaImpares) / count)

else:
    print("nenhum numero inserido")