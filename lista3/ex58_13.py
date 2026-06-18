num1 = int(input("digite um número inteiro: "))
num2 = int(input("digite outro número inteiro: "))

if num1 == num2:
    print("nao há números entre eles")
elif num1 > num2:
    for i in range(num2 + 1, num1):
        print(i)
elif num2 > num1:
    for i in range(num1 + 1, num2):
        print(i)