def raiz(numero, potencia = 2):
    """funcion que retorna 

    Args:
        numero (int):numero postiivo 
        potencia (int, optional):raiz a la que se elevara. Defaults to 2.
    Returns:
        float: retorna la riaz de un numero
    """
    return pow(numero, 1 / potencia)


print(raiz(5))
print(raiz(5, 2))
print(raiz(5, 3))



    