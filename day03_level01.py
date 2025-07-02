edad = 18
altura = 1.69
no = 10+3


#Área de un trinángulo
print("Escriba la base del triángulo:")
base = float(input())
print("Escriba la altura del triángulo:")
altura = float(input())
area= 0.5 * base * altura
print("El área del triángulo es:", area)


#Perímetro de un triángulo
print("Escriba el primer lado del triángulo:")
lado1 = float(input())
print("Escriba el segundo lado del triángulo:")
lado2 = float(input())
print("Escriba el tercer lado del triángulo:")
lado3 = float(input())
perimetro = lado1 + lado2 + lado3
print("El perímetro del triángulo es:", perimetro)


#pront
longitud = float(input("Introduce la longitud del rectángulo: "))
anchura = float(input("Introduce la anchura del rectángulo: "))

print(f"La longitud es {longitud} y la anchura es {anchura}")

# Obtener el radio de un círculo y calcular el área y la circunferencia
radio = float(input("Escribe el radio del círculo: "))
pi = 3.14
area = pi * radio * radio
circunferencia = 2 * pi * radio
print("Área del círculo:", area)
print("Circunferencia del círculo:", circunferencia)

# Trabajar con la ecuación y = 2x - 2
print("\nEcuación: y = 2x - 2")
pendiente = 2  # ya está en la forma y = mx + b, donde m = pendiente
interseccion_y = -2
interseccion_x = 1  # cuando y = 0, 0 = 2x - 2 => x = 1
print("Pendiente:", pendiente)
print("Intersección con x:", interseccion_x)
print("Intersección con y:", interseccion_y)

# Calcular la pendiente y la distancia entre dos puntos
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pendiente2 = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("\nPendiente entre (2,2) y (6,10):", pendiente2)
print("Distancia entre los puntos:", distancia)

# Comparar pendientes
print("\n¿Las pendientes son iguales?", pendiente == pendiente2)

# Evaluar y = x^2 + 6x + 9 para ver cuándo y es 0
print("\nBuscando valores de x donde y = x^2 + 6x + 9 sea 0:")
for x in range(-10, 1):
    y = x**2 + 6*x + 9
    print("x =", x, "y =", y)
    if y == 0:
        print("¡y es 0 cuando x =", x, "!")

# Longitud de las palabras
palabra1 = "python"
palabra2 = "dragon"
print("\nLongitud de 'python':", len(palabra1))
print("Longitud de 'dragon':", len(palabra2))
print("¿Las longitudes son diferentes?", len(palabra1) != len(palabra2))

# Revisar si 'on' está en ambas palabras
print("¿'on' está en 'python' y 'dragon'?", 'on' in palabra1 and 'on' in palabra2)

# Revisar si 'jargon' está en la oración
frase = "I hope this course is not full of jargon"
print("¿'jargon' está en la frase?", 'jargon' in frase)

# Afirmación falsa: que 'on' no está en ninguna
print("¿'on' NO está en 'python' y 'dragon'?", 'on' not in palabra1 and 'on' not in palabra2)

# Convertir la longitud de 'python' a float y luego a string
longitud = len(palabra1)
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print("\nLongitud como float:", longitud_float)
print("Longitud como texto:", longitud_str)

# Ver si un número es par
numero = int(input("Escribe un número para ver si es par: "))
es_par = numero % 2 == 0
print("¿Es par?", es_par)

# Ver si 7 // 3 es igual a int(2.7)
print("¿7 // 3 es igual a int(2.7)?", 7 // 3 == int(2.7))

# Comparar tipos de datos
print("¿El tipo de '10' es igual al tipo de 10?", type('10') == type(10))

# Ver si int('9.8') == 10
try:
    print("¿int(float('9.8')) es igual a 10?", int(float('9.8')) == 10)
except:
    print("No se puede convertir '9.8' directamente a int.")

# Calcular salario semanal
horas = float(input("\nEscribe las horas trabajadas: "))
tarifa = float(input("Escribe la tarifa por hora: "))
pago = horas * tarifa
print("Tu pago semanal es:", pago)

# Calcular segundos vividos
años = int(input("\nEscribe cuántos años has vivido: "))
segundos = años * 365 * 24 * 60 * 60
print("Has vivido aproximadamente", segundos, "segundos.")

# Mostrar una tabla
print("\nTabla:")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")