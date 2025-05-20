#FUNCIONES Y ALCANCE

"""
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

def sin_parametros():
    pass

def con_varios_parametros(a,b,c):
    def dentro_funcion():
        return print(f"inside of the function.")
    dentro_funcion()
    return a + b + c

#variable local
def funcion_con_variable_local(value_one, text2):
    value_one = "improving of the python skills." #local
    value_two = text2 
    return f"{value_one}\n{value_two}"

##global
value_one = "python"
value_two = "global VARIABLE"

print(sin_parametros())
print(con_varios_parametros(1,2,3))
print(funcion_con_variable_local(value_one,value_two))


# * DIFICULTAD EXTRA (opcional):

def index(txt1,txt2):
    space = " "
    count = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(txt1 + space + txt2)
        elif numero % 3 == 0:
            print(txt1)
        elif numero % 5 == 0:
            print(txt2)
        else:
            count +=1
    return f"El número de veces que se ha impreso el número {count}"

a,b = "learn", "python"
print(index(a,b))

