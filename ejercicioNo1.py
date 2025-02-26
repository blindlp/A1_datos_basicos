# Ejercicios tipos Basico 
# Un país tiene monedas de 1 U, 5 U y 25 U.
# #

# declaramos denominacion de monerdas
mon_1 , mon_2 , mon_3 = 1, 5, 25

# escrimos a pantalla la cantidad de dinero
dinero = input("Dame la cantidad de dinero que deseas cambiar:")
#desplegamos en pantalla
den_1 = int(dinero) // mon_3
den_2 = (int(dinero) % mon_3) // mon_2
den_3= ((int(dinero) % mon_3) % mon_2) // mon_1
print(f"Desgloce de {dinero} U:")
print(f" {den_1} monedas de {mon_3} U")
print(f" {den_2} monedas de {mon_2} U")
print(f" {den_3} monedas de {mon_1} U")


