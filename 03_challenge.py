#ESTRUCTURAS DE DATOS

"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

#list
import math


lists = ["verde","negro","blanco","azul"]
lists.append("rojo") #Add element
lists.remove("negro") #Del element
lists[lists.index("azul")] = "amarillo" #Update elemnt
lists.sort() #sort ordenar

#dict
dicts = {"clave_1":"valor_1", "clave_2":"valor_2"}
dicts["clave_3"] = "valor_3" #Add element
del dicts["clave_1"] #Del element
dicts["clave_3"] = "nuevo_valor_3" #Update element
dicts.update({"clave_0":"valor_0","clave_-1":"valor-1"}) #Update and Add varius elemnt
dicts = sorted(dicts.items()) #Ordena element but convert in list

#tuple
tuples = ("kenier","noriega","navarr",32,1993,False)

#set
sets = {11,22,33,44,55,66,77,88,99,99,00000,"hola"}
sets.add(11) #Add element
sets.remove("hola") #Del element   #lanza error si no esta
sets.discard(12421) #no lanza eror a no conseguirlo
sets.update([11,12,20,888]) #add variou elements
sets = sorted(sets) #ordenando sets pero lo convierte en lists

print(lists)
print(dicts)
print(tuples)
print(sets)

# * DIFICULTAD EXTRA (opcional):
""""

Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */"""

def agenda_contact():
    agenda = {}

    def numero_telefono():
        while True:
            telefono = input("Intruduce el numero de telefono: ")
            if telefono.isalnum() and len(telefono) == 11:
                return telefono
            else:
                print("El numero tiene que tener 11 digitos numericos: ")

    while True:
        print("""
1- Introduce (1): Para Buscar
2- Introduce (2): Para Agregar
3- Introduce (3): Para Actualizar
4- Introduce (4): Para Eliminar
1- Introduce (5): Para Salir
              """)
        
        option = input("Introduzca una opticón (1-5): ")
        match option:
            #búsqueda
            case "1":
                nombre = input("Introduzca el nombre a buscar: ")
                found = False

                for nombre_agenda, movil in agenda.items():
                    if nombre in nombre_agenda:
                        print(f"Contacto localizado:\n{nombre_agenda}: {movil}")
                        found = True

                if not found:
                    print("No se encontró ningún usuario.")
            #inserción
            case "2":
                nombre = input("Introduce el nombre a agregar: ")
                telefono = numero_telefono() 

                if nombre not in agenda:
                    agenda[nombre] = telefono
                    print("Contacto añadido.")
                else:
                    print("Ya existe un usuario con este nombre.")
            #actualización
            case "3":
             nombre = input("Introduce el contacto a actualizar: ")
             if nombre in agenda:
                telefono = numero_telefono()

                agenda[nombre] = telefono
                print("Contacto actualizado.")
             else:
                    print("No se consiguio ningun contacto con ese nombre.")
                #eliminación
            case "4":
             nombre = input("Introduce el contacto a eliminar: ")
             if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado")
             else:
                print("No se encontró el contacto.")

            case "5":
                print("Saliendo")
                break
            case _:
                print("Introduzca una opción valida.")

                

agenda_contact()

