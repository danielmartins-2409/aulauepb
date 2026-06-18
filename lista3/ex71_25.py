pontos = 0

gol1 = int(input())
gol2 = int(input())

if gol1 < 0 or gol2 < 0:
    print("Não houve nenhum jogo")
else:
    while gol1 >= 0 and gol2 >= 0:

        if gol1 > gol2:
            pontos += 3
        elif gol1 == gol2:
            pontos += 1

        gol1 = int(input())
        gol2 = int(input())

    print("O time fez", pontos, "pontos")