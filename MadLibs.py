#Mad Libs

# Regrese a este punto una vez que finalice el código
ban  =  1

while ( ban  <  3 ):

    # Todas las preguntas que el programa le hace al usuario
    sust = input("Elige un sustantivo:" )
    sust_p = input( "Elige un sustantivo plural:" )
    sust2 = input("Elige un sustantivo:" )
    lugar =  input("Nombra un lugar:" )
    adjetivo = input("Elija un adjetivo (palabra descriptiva):" )
    sust3 = input( "Elige un sustantivo:" )

    # Muestra la historia según la entrada de los usuarios
    print("------------------------------------------")
    print("Sé amable con tu" , sust , "- pies" , sust_p)
    print("Porque un pato puede ser de alguien" , sust2 , ",")
    print("Sea amable con su" , sust_p , "en" , lugar)
    print("Donde siempre está el clima" , adjetivo , ".")
    print()
    print("Puedes pensar que este es el" , sust3 , ",")
    print("Bueno, lo es" )
    print("------------------------------------------")

    # Vuelve a "ban = 1"
    ban += 1