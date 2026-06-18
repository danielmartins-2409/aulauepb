soma = 0
valor= 1000
for i in range(1, 51):
    soma += valor/i
    print(i, valor)
    valor -= 3
   
print(soma)
