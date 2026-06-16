valorSaque = int(input("Digite o valor do saque, o valor mínimo é de R$10 e o máximo é de R$600: "))


if valorSaque >= 10 and valorSaque <=600:

    nota100 = valorSaque//100 
    valorSaque = valorSaque%100

    nota50 = valorSaque//50
    valorSaque = valorSaque%50 

    nota10 = valorSaque//10
    valorSaque = valorSaque%10

    nota5 = valorSaque//5  
    valorSaque = valorSaque%5

    nota1 = valorSaque//1

    print(f"""
------------------
{nota100} notas de R$100
 ------------------
{nota50} notas de R$50
-------------------
{nota10} notas de R$10
-------------------
{nota5} notas de R$5
-------------------
{nota1} notas de R$1""")

else:
    print("Valor de saque inválido")