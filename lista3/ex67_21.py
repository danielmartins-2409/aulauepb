numero = int(input("Número do empregado: "))
meses = int(input("Número de meses: "))

if numero != 0 or meses != 0:

    maisRecente = maisAntigo = numero
    mesRecente = mesAntigo = meses

    numero = int(input("Número do empregado: "))
    meses = int(input("Número de meses: "))

    while numero != 0 or meses != 0:

        if meses > mesAntigo:
            mesAntigo = meses
            maisAntigo = numero

        if meses < mesRecente:
            mesRecente = meses
            maisRecente = numero

        numero = int(input("Número do empregado: "))
        meses = int(input("Número de meses: "))

    print("Mais recente:", maisRecente)
    print("Mais antigo:", maisAntigo)

else:
    print("Nenhum funcionário informado")
