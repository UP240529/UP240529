def add_two_numbers(a, b):
    return a + b

def area_of_circle(r):
    import math
    return math.pi * r * r

def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números."

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def check_season(month):
    month = month.strip().capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Mes no válido'

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Pendiente indefinida"
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    import math
    d = b**2 - 4*a*c
    if d < 0:
        return "No hay soluciones reales"
    elif d == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return (x1, x2)

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]

def add_item(lst, item):
    return lst + [item]

def remove_item(lst, item):
    return [x for x in lst if x != item]

def sum_of_numbers(n):
    return sum(range(n+1))

def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)