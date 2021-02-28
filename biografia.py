nom = input("Introduca su nombre: ")
fec = input("Introduce su fecha: ")
dire = input("Introduce su direccion: ")
met = input("Alguna meta personal: ")


ban = 0
nom2 = input("Introduca su nombre de nuevo: ")
while (ban < 1):
    if nom == nom2:
        ban = 1
    else:
        print("Nombre captutado incorrectamente, vuelve a introducirlo")
        nom2 = input("Introduca su nombre de nuevo: ")

ban = 0
fec2 = input("Introduce su fecha de nuevo: ")
while (ban < 1):
    if fec == fec2:
        ban = 1
    else:
        print("Fecha captutado incorrectamente, vuelve a introducirlo")
        fec2 = input("Introduce su fecha de nuevo: ")

ban = 0
dire2 = input("Introduce su direccion de nuevo: ")
while (ban < 1):
    if dire == dire2:
        ban = 1
    else:
        print("Direccion captutado incorrectamente, vuelve a introducirlo")
        dire2 = input("Introduce su direccion de nuevo: ")

ban = 0
met2 = input("Alguna meta personal de nuevo: ")
while (ban < 1):
    if met == met2:
        ban = 1
    else:
        print("Fecha captutado incorrectamente, vuelve a introducirlo")
        met2 = input("Alguna meta personal de nuevo: ")

print(f"Nombre: {nom}")
print(f"Fecha: {fec}")
print(f"Direccion: {dire}")
print(f"Metas personales: {met}")