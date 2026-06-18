n = int(input("Digite um número: "))
x = 0
encontrou = 0

while x * (x + 1) * (x + 2) <= abs(n):
    if x * (x + 1) * (x + 2) == abs(n):
        encontrou = 1
    x += 1

if encontrou == 1:
    print("O número é triangular")
else:
    print("O número não é triangular")
