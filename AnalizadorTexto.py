noticia = input("Por favor, introduce la última notia deportiva de tu equipo favorito: ")
letras = []

noticia = noticia.lower()

letras.append(input("Por favor, intoduce la primera letra de tu nombre: ").lower())
letras.append(input("Por favor, intoduce la segunda letra de tu nombre: ").lower())
letras.append(input("Por favor, intoduce la tercera letra de tu nombre: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = noticia.count(letras[0])
cantidad_letras2 = noticia.count(letras[1])
cantidad_letras3 = noticia.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = noticia.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = noticia[0]
letra_final = noticia[-1]
print(f"La letra inicial es '{letra_inicio}' y laletra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
noticia_invertida = " ".join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{noticia_invertida}'")

print("\n")
print("BUSCANDO LA PALABARA PYTHON")
buscar_python = 'python' in noticia
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python'{dic[buscar_python]} se encuentra en el texto")