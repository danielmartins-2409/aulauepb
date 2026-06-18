tamanho = float(input("tamanho do arquivo em MB: "))
velocidade = float(input("velocidade em MBps: "))

tempoS = tamanho/velocidade
tempoM = tempoS / 60

print("Durará", tempoM, "minutos")
