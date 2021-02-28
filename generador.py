print("Bienvenido a la eleccion de musica")
print("---------------------------------------------------------------------------------------------")
opcion = 0

while opcion == 0:
    print("1.-Metallica - Nothing else matters")
    print("2.-Bon jovi - You give love a bad name")
    print("3.-Kansas - Carry on Wayward Son")
    print("4.-Deep Purple - Hush")
    print("5.-Salir\n")
    
    opcion = int(input("seleciona una de las opciones mostradas:"))
    
    print("---------------------------------------------------------------------------------------------")
    
    if opcion == 1:
        print('Usted seleciono "Metallica - Nothing else matters", que lo disfrute: \n')
        print("So close, no matter how far\n",
            "Couldn't be much more from the heart\n",
            "Forever trusting who we are\n",
            "And nothing else matters\n")
        opcion = int(input("Si quierevolver a intentalo seleciona 0: "))
    
    elif opcion == 2:
        print('Usted seleciono "Bon Jovi - You give love a bad name", que lo disfrute: \n')
        print("Shot through the heart\n",
            "And you're to blame\n",
            "Darlin', you give love a bad name\n\n",
            "An angel's smile is what you sell\n",
            "You promise me Heaven, then put me through hell\n",
            "Chains of love got a hold on me\n",
            "When passion's a prison, you can't break free\n")
        opcion = int(input("Si quierevolver a intentalo seleciona 0: "))
    
    elif opcion == 3:
        print('Usted seleciono "Kansas - Carry on Wayward Son", que lo disfrute: \n')
        print("Carry on, my wayward son\n",
        "There'll be peace when you are done\n"
        "Lay your weary head to rest\n",
        "Don't you cry no more\n")

        opcion = int(input("Si quierevolver a intentalo seleciona 0: "))
    elif opcion == 4:
        print('Usted seleciono "Deep Purple - Hush", que lo disfrute: \n')
        print("Nah, nah-nah-nah, nah-nah-nah, nah-nah-nah (x2)\n\n",
        "I got a certain little girl she's on my mind\n",
        "No doubt about it she looks so fine\n",
        "She's the best girl that I ever had\n",
        "Sometimes she's gonna make me feel so bad\n")
        opcion = int(input("Si quierevolver a intentalo seleciona 0: "))
    
    elif opcion == 5:
        print("Adios")

    