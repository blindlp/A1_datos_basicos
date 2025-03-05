
def min_max(numero_1, numero_2):
    """funcion que retorna el minimo y maximo de dos numeros

    Args:
        numero_1 (float): 10.5
        numero_2 (float): 25.5

    Returns:
        float: _description_retorna el cual es el mayor y menor de los dos numeros
    """
    return (f"minimo {numero_1} maximo {numero_2}" if numero_1 < numero_2 else "minimo {numero_2} maximo {numero_1}")


print(min_max(25,30))   