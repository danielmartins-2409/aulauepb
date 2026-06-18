n = int(input("Diga a quantidade de termos: "))
termo1 = float(input("Diga o primeiro termo "))
termo2 = float(input("Doga o segundo termo "))
proximoTermo = 0




if n >= 3:
    print("A1 =", termo1)
    print("A2 =", termo2)
    for i in range(3, n+1):
        if i%2 == 0:
            proximoTermo = termo2 + termo1
            termo1 = termo2
            termo2 = proximoTermo
            print(f"A{i} = {proximoTermo}")
        else: 
            proximoTermo = termo2 - termo1
            termo1 = termo2
            termo2 = proximoTermo
            print(f"A{i} = {proximoTermo}")


      


