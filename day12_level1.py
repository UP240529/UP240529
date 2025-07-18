import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def user_id_gen_by_user():
    num_chars = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Cantidad de IDs a generar: "))
    for _ in range(num_ids):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)))

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# Ejemplo de uso:
# print(random_user_id())
# user_id_gen_by_user()
# print(rgb_color_gen())