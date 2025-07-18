import random

def lista_de_colores_hexa(num_colores=1):
    """Genera una lista de códigos de colores hexadecimales."""
    colores_hexa = []
    for _ in range(num_colores):
        # Genera 6 caracteres aleatorios entre 0-9 y a-f
        codigo_hex = "#" + ''.join([random.choice('0123456789abcdef') for _ in range(6)])
        colores_hexa.append(codigo_hex)
    return colores_hexa

def lista_de_colores_rgb(num_colores=1):
    """Genera una lista de códigos de colores RGB."""
    colores_rgb = []
    for _ in range(num_colores):
        # Genera valores aleatorios para R, G y B (0-255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores_rgb.append(f"rgb({r}, {g}, {b})")
    return colores_rgb

def generar_colores(tipo_color, num_colores):
    """
    Genera una lista de colores según el tipo especificado ('hexa' o 'rgb').
    
    Args:
        tipo_color (str): Tipo de color a generar ('hexa' o 'rgb').
        num_colores (int): Cantidad de colores a generar.
    
    Returns:
        list: Lista de colores en el formato especificado.
    
    Raises:
        ValueError: Si el tipo de color no es 'hexa' ni 'rgb'.
    """
    if tipo_color == 'hexa':
        return lista_de_colores_hexa(num_colores)
    elif tipo_color == 'rgb':
        return lista_de_colores_rgb(num_colores)
    else:
        raise ValueError("Tipo de color inválido. Usa 'hexa' o 'rgb'.")
