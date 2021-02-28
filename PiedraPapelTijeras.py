from random import randint

elecion = ["roca","papel","tijeras"]
def main():
    computadora = elecion[randint(0,2)]

    print("Bienvenido al juego de roca, papel o tijeras\n")
    jugador = input("Seleciona entre roca, papel o tijera: ").lower()
    print("La computadora eigio:", computadora)

    if jugador == computadora:
        print("Empate")
    elif jugador == "roca" and computadora == "papel":
        print("Perdistes")
    elif jugador == "roca" and computadora == "tijeras":
        print("Ganaste")
    elif jugador == "papel" and computadora == "tijeras":
        print("Perdistes")
    elif jugador == "papel" and computadora == "roca":
        print("Ganaste")
    elif jugador == "tijeras" and computadora == "roca":
        print("Perdistes")
    elif jugador == "tijeras" and computadora == "papel":  
        print("Ganaste")

main()