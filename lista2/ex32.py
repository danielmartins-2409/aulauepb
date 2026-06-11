nota1 = float(input("Digite sua nota: "))

if nota1 > 10 or nota1 < 0:
    print("Valor inválido")
else:
   nota2 = float(input("Digite sua outra nota: "))    
   if nota2 > 10 or nota2 < 0:
      print("Valor inválido") 
   else:
      media = (nota1 + nota2)/2
      if media <= 10 and media > 9:
         print(f"Media: {media}, Conceito: A, APROVADO")
      elif media > 7.5 and media <= 9:
         print(f"Media: {media}, Conceito = B, APROVADO")
      elif media > 6 and media <=7.5:
         print(f"Media: {media}, Conceito: C, APROVADO")
      elif media > 4 and media <= 6:
         print(f"Media: {media}, Conceito: D, REPROVADO")
      else:
         print(f"Media: {media}, Conceito: E, REPROVADO") 

