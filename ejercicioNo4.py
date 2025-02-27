import math

"""
Si tenemos los coeficientes (𝑎, 𝑏, 𝑐) de una ecuación de segundo grado de la
forma 𝑎𝑥􀬶 + bx + 𝑐 = 0 y suponiendo que tiene dos raíces reales, expresa
instrucciones para calcular dichas fórmulas.

"""
print("Calcular el cuadrado de aX^2 + bx + c = 0")
user_input = input(" ingrese ( a, b, c): ")
input_1, input_2, input_3 = user_input.split()
a, b, c = int(input_1), int(input_2), int(input_3)
print(a,b,c)
print("Paso 1") 
print("Divide entre a ambos lados de la ecuación para que el coeficiente de x2 sea 1.")
print("x^2 +b/a + c/a = 0")
print("Paso 2")
print("Reescribe de modo que el lado izquierdo sea x2 + bx (aunque en este caso bx realmente es (b/x)*x ).")
print("x^2 +b/a = -c/a")
print("Paso 3")
print("Como el coeficiente de x es b/a , el valor a sumar a ambos lados es (b/2a)^2")
print("(x^2 + (b/a)x + (b/2a)^2 = - c/a + (b/2a)^2")
print("Paso 4")
print("Escribe el lado izquierdo como un binomio cuadrado.")
print("(x + (b/2a)^2 = - c/a + (b/2a)^2")
print("Paso 5")
print("Evalúa como (b/2a)^2 como b^2/4a^2")
print("(x + (b/2a)^2 = - c/a + (b/2a)^2")
print("Paso 6")
print("Escribe las fracciones en el lado derecho usando un común denominador.")
print("(x + (b/2a))^2 = - 4ac/4a^2 + b^2/4a^2")
print("Paso 7")
print("Suma las fracciones de la derecha.")
print("(x + (b/2a))^2 = - (b^2 - 4ac) / 4a^2")
print("Paso 8")
print("Usa la Propiedad de la Raíz Cuadrada. ¡Recuerda que quieres las dos raíces, positiva y negativa!")
print("(x + b/2a = +- √((b^2 - 4ac) / 4a^2)")
print("Paso 9")
print("Resta  b//a de ambos lados para despejar x")
print("(x = - b/2a +- √((b^2 - 4ac) / 4a^2)")
print("Paso 10")
print("El denominador dentro del radical es un cuadrado perfecto, entonces: √((b^2 - 4ac) / 4a^2) = √((b^2 - 4ac)) / √(4a^2) = √(b^2 -4ac) / 2a")
print("(x = - b/2a +- √((b^2 - 4ac) / 4a^2)")
print("Paso 11")
print("Respuesta")
print("(x = - ( b +- √(b^2 -4ac)) / 2a")
print(f" x1 = ( {b}+ √({b}^2-4x{a}x{c})/2x{a}")
x1 =  (- b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
print(f"x1 = {x1}")
print(f" x2 = ( {b}' √({b}^2-4x{a}x{c})/2x{a}")
x2 =  (- b - math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
print(f"x2 = {x2}")



