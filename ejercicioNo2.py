"""
En casi todas partes, es clásico el programa “Hola Mundo”, que simplemente
escribe esta frase en la pantalla. Diséñalo, y haz luego dos versiones o tres
más:
"""


nombre = input("Como te llamas?")
print(f"Hola, {nombre}" )

"""
Otra, que pregunta también la edad y le contesta con su nombre, la edad y
los años que cumplirá la próxima vez. (Esto es simplemente para que
convierta la edad en un número…)
"""

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
next_age = int(edad)+1
print(f"Hola {nombre} , pronto cumplirás {next_age} años")
