# Suma de todos los números del 0 al 100
total = 0
for i in range(101):
    total += i
print("La suma de todos los números es", total)

# Suma de pares e impares del 0 al 100
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print("La suma de todos los pares es", suma_pares)
print("La suma de todos los impares es", suma_impares)