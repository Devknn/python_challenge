#OPERADORES Y ESTRUCTURAS DE CONTROL


"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

values_one = 4
values_two = 4
values_two = values_one
index = "learing python"

#Aritméticos
addition = values_one + values_two
subtraction = values_one - values_two
multiplication = values_one * values_two
division = values_one / values_two
module = values_one % values_two
exponential = values_one ** values_two
floor_division = values_one // values_two

#logico
ands = (values_one == 0) and (values_two == 0)
ors = (values_one == 0) or (values_two == 0)
#nots = values_one not values_two == 0

#de comparación
greater_than = values_one > values_two
greater_than_or_equal = values_one >= values_two
less_than = values_one < values_two
less_than_or_equal = values_one <= values_two
equal = values_one == values_two

#asignación
values_one += values_two
values_one -= values_two
values_one *= values_two
values_one /= values_two
values_one %= values_two
values_one **= values_two
values_one //= values_two

#identidad
#iss = "python" is index
#isnot = "python" is not index

#pertenencia
ins = "python" in index
#inot = "python" not in index

#Condicionales iterativas
if values_one == values_two:
    print(True)
elif values_two != values_one:
    print(False)
else:
    print("exit")

#excepciones

try:
    n1,n2 = 4,0
    if n1 / n2:
        print(n1/n2)
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("else")
finally:
    print("finally")

print(f"suma: {addition}")
print(f"resta: {subtraction}")
print(f"multiplicación: {multiplication}")
print(f"división: {division}")
print(f"porcentaje: {module}")
print(f"exponencial: {exponential}")
print(f"división de piso: {floor_division}")

print(f"operador and: {ands}")
print(f"operador or: {ors}")

print(f"mayor que: {greater_than}")
print(f"mayor o igual que: {greater_than_or_equal}")
print(f"menor que: {less_than}")
print(f"menor o igual que: {less_than_or_equal}")

print(f"operador is: {values_one is values_two}")
print(f"operador is not: {values_one is not values_two}")


print(f"operador in: {ins}")
print(f"operador not in: {'python' not in index}")


# * DIFICULTAD EXTRA (opcional):

def numeros_comprendidos():
    for numero in range(10,56):
        if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
            print(numero)

numeros_comprendidos() 

