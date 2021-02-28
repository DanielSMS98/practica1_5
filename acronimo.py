frase = input('Introduce la oracion: ')
palabras = frase.split(' ') 
letras = ''

for palabra in palabras:
   letras += palabra[0]

letras = letras.upper()
print(letras)