numero = int(input("numero de empregado "))
meses = int(input("numero de meses "))

if meses > 0:
    maisRecente = maisAntigo = numero
    mesAntigo = mesRecente = meses
    while numero != 0 or meses != 0:

        numero = int(input("numero de empregado "))
        meses = int(input("numero de meses "))

        if numero != 0 or meses != 0:
            if meses > 0:
                if meses > mesAntigo:
                    mesAntigo = meses
                    maisAntigo = numero
                elif meses < mesRecente:
                    mesRecente = meses
                    maisRecente = numero

            else:
                print("valor inválido")
else:
    print("Valor inválido")

print("o mais recente é o funcionario", maisRecente, "e o mais antigo é o funcionário", maisAntigo)
    
