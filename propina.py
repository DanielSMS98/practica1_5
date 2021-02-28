#Solicitar la factura
fac = float(input("De cuanto es la fectura: "))

#La propina con el 18%
num = (fac * 0.18)
print(f"Su total con el 18% ({num}) seria de {round (fac + num , 2) }")
#La propina con el 20%
num = (fac * 0.20)
print(f"Su total con el 20% ({num}) seria de {round (fac + num , 2) }")
#La propina con el 25
num = (fac * 0.25)
print(f"Su total con el 25% ({num}) seria de {round (fac + num , 2) }")