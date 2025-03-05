"""
Un nombre propio ha de escribirse con la primera letra mayúscula. Diseña
instrucciones para que, en el caso de que se dé con minúscula, lo arregle:
>>> nombre_propio = “blacky”
...
>>> print(nombre_propio)
Blacky

En este ejercicio lo que te pido en realidad es que investigues la forma de
hacerlo, anticipándote al uso de strings. Hay una función pensada para
lograrlo (capitalize). Y también, de otro modo, puedes separar la inicial de
una cadena de caracteres (cadena[0]) del resto de una cadena de caracteres
(cadena[1:]) , poner la inicial con mayúscula (upper) y unir ambos (+).

"""
"""aqui lo realizamos utilizando la fucion capitalize"""
nombre_propio = input("Ingrese su nombre: ")
print(nombre_propio.capitalize())

"""aqui lo realizamos separando la cadena de caracteres"""
print("---------------------------------------")
nombre_propio = input("Ingrese su nombre: ")
print(nombre_propio[0].upper()+nombre_propio[1:])