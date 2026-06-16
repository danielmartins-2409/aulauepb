
sexo = input("M - Masculino ou F - Feminino: ")
pesoIdeal = 0

if sexo == "M":
    altura = float(input("Insira a altura em METROS: "))
    if 0 < altura <= 3: 
        pesoIdeal = (72.7 * altura)-58
        print(f"peso ideal: {pesoIdeal:.2f}")
    else:
        print("altura inválida")


elif sexo == "F":
    altura = float(input("Insira a altura em METROS: "))
    if 0 < altura <= 3: 
        pesoIdeal = (62.1 * altura) - 44.7
        print(f"peso ideal: {pesoIdeal:.2f}")
    else:
        print("altura inválida")
else:
    print("sexo inválido")