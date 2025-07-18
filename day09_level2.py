# Calificación según la puntuación
score = int(input("Introduce la puntuación del estudiante (0-100): "))
if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
elif 0 <= score <= 49:
    print("F")
else:
    print("Puntuación no válida")

# Determinar la estación del año
mes = input("Introduce el mes: ").strip().capitalize()
if mes in ['September', 'October', 'November']:
    print("La estación es Otoño.")
elif mes in ['December', 'January', 'February']:
    print("La estación es Invierno.")
elif mes in ['March', 'April', 'May']:
    print("La estación es Primavera.")
elif mes in ['June', 'July', 'August']:
    print("La estación es Verano.")
else:
    print("Mes no válido.")

# Lista de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
nueva_fruta = input("Introduce una fruta: ").strip().lower()
if nueva_fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(nueva_fruta)
    print("Fruta añadida a la lista:", fruits)  
    