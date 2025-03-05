

def cada_ves_mas_cara(precio, porcentaje):
    """_summary_
    funcion que sube o baje el precio de un articulo en base a un %
    Args:
        precio (float): precio 100
        porcentaje (float): porcentaje 10

    Returns:
        float: 100 + ( 100 * (10 % ) / 100 ) )
    """
    return round(precio + ( precio * (porcentaje / 100)),2)


print(cada_ves_mas_cara(113.50,10.5))

print(cada_ves_mas_cara(100,-10))