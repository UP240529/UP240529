# Obtener la edad del usuario.
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres lo suficientemente mayor para aprender a conducir.")
else:
    print(f"Te faltan {18 - edad} año{'s' if 18 - edad > 1 else ''} para poder aprender a conducir.")

# Comparar mi edad con tu edad.
mi_edad = 25
tu_edad = int(input("Introduce tu edad: "))
if tu_edad > mi_edad:
    diff = tu_edad - mi_edad
    print(f"Eres {diff} año{'s' if diff > 1 else ''} mayor que yo.")
elif tu_edad < mi_edad:
    diff = mi_edad - tu_edad
    print(f"Soy {diff} año{'s' if diff > 1 else ''} mayor que tú.")
else:
    print("Tenemos la misma edad.")

# Comparar dos números
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")