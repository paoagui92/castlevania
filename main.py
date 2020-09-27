from models import Donante
import json
nuevo_donante= Donante.registrarse("20605517", "PAOLA", "aGUIRRE")

print(nuevo_donante.serializar())

main_menu = """
    1.- Donante
    2.- Perfiles
    3.- Visitas
    4.- Salir
"""

donante_options = """
    1.- Ver todos los donantes
    2.- Crear un donante
    3.- Buscar donante
    4.- Menu principal
"""

donantes = []


def get_choice(options):
    """Devuelve como entero la opcion seleccionada para el input con mensaje message"""

    print(options)
    try:
        return int(input("Por favor, escoja una opción: "))
    except ValueError:
        return 0


def crear_donante():
    """recibe insumos del usuario a traves de input y ejecuta el metodo de clase registrarse de la clase Donante"""
    cedula = input("\nCedula: ")
    nombre = input("\nNombre: ")
    apellido = input("\nApellido: ")
    return Donante.registrarse(cedula,nombre,apellido)


choice = get_choice(main_menu)
while choice != 4:
    if choice == 1:
        second_choice = get_choice(donante_options)
        if second_choice == 1:
            #Listar donantes
            for donante in donantes:
                print(str(donante))
        elif second_choice == 2:
            #Crear donantes
            nuevo_donante = crear_donante()
            donantes.append(nuevo_donante)
            print(f"{nuevo_donante.nombre_completo} fue creado con éxito")
        elif  second_choice == 3:
            #Buscar donantes
            pass
        elif  second_choice == 4:
            #Menu princiapl
            break  
    elif choice == 2:
        #Actualizar donante
        pass
    elif choice == 3:
        #Visitas
        pass
    else:
        print("Por favor, escoja una opcion valida")
        pass
    choice = get_choice(main_menu)

#salvar modelos

with open("./donante.json", "w") as donante_archivo:
    donantes_serealizados = []
    for donante in donantes:
        donantes_serializados.append(donante.serializar())
    json.dump(donantes_serializados, donante_archivo)

print("chao!")