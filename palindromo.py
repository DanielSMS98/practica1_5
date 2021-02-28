palabra = input("Introduce una palabra para y identificar si es un palindromo: ")
rec = list(palabra)

conteo = len(rec)
i = conteo -1
rev = ""

for n in range(conteo):
    rev = rev + rec[ i-n ]

if (palabra == rev):
    print(f"La palabra {rev}, es un palindromo")
else:
    print(f"La palabra {palabra}, no es un palidromo")