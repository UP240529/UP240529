# 1. Filtrar solo negativos y ceros usando comprensión de listas
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numbers if n <= 0]
print(negativos_y_ceros)

# 2. Aplanar la siguiente lista de listas de listas a una lista unidimensional
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [num for sublist in list_of_lists for inner in sublist for num in inner]
print(lista_aplanada)

# 3. Crear la siguiente lista de tuplas usando comprensión de listas
lista_tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(lista_tuplas)

# 4. Aplanar la siguiente lista a una nueva lista
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises_aplanados = [[pais.upper(), pais[:3].upper(), ciudad.upper()] for lista in countries for (pais, ciudad) in lista]
print(paises_aplanados)

# 5. Cambiar la lista a una lista de diccionarios
paises_dicc = [{'country': pais.upper(), 'city': ciudad.upper()} for lista in countries for (pais, ciudad) in lista]
print(paises_dicc)

# 6. Cambiar la lista de listas a una lista de cadenas concatenadas
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for lista in names for (nombre, apellido) in lista]
print(nombres_completos)

# 7. Función lambda para pendiente y ordenada al origen de funciones lineales
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
ordenada = lambda x, y, m: y - m * x

# Ejemplo de uso:
print(pendiente(1, 2, 3, 4))        # Salida: 1.0
print(ordenada(1, 2, 1))            # Salida: 1.0