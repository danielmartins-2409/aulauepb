resp1 = int(input(""))
resp2 = int(input(""))
resp3 = int(input(""))
resp4 = int(input(""))
resp5 = int(input(""))

somaResp = resp1 + resp2 + resp3 +resp4 + resp5

if somaResp == 2:
    print("suspeito")
else:
    if somaResp == 3 or somaResp ==4:
        print("cumplice")
    else:
        if somaResp == 5:
            print("assassino")
        else:
            print("inocente")