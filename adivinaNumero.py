import random

numero = random.randrange(1,50)
num = int(input("Seleciona un numero del 1 al 50: "))

while num != numero:
    if num < numero:
        print("Tu numero es mas alto, intentalo otra vez")
        num = int(input("Seleciona un numero del 1 al 50: "))
    else:
        print("Tu numero es menor, intentalo otra vez")
        num = int(input("Seleciona un numero del 1 al 50: "))

print(f"El numero {num} es el correcto")