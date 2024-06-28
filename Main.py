from Funcion_Archivos import cargar_archivo_json, guardar_archivo
from Manipulacion_de_lista import asignar_totales, filtrar_por_tipo, imprimir_lista, mostrar_servicios_ordenados


# Menú principal
def menu():
    """
    Menu interactivo para hacer uso de las funciones
    """
    servicios = []
    while True:
        print("\nMenú:")
        print("1) Cargar archivo")
        print("2) Imprimir lista")
        print("3) Asignar totales")
        print("4) Filtrar por tipo")
        print("5) Mostrar servicios ordenados")
        print("6) Guardar servicios")
        print("7) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            servicios = cargar_archivo_json(r"compu.json")
            print("Se cargo el archivo correctamente")
        elif opcion == "2":
            imprimir_lista(servicios)
        elif opcion == "3":
            if len(servicios) != 0:
                servicios = asignar_totales(servicios)
                print("Se han asignado los totales a los servicios.")
            else:
                print("La lista de servicios esta vacia")
        elif opcion == "4":
            tipo = ""
            letra = input("Ingrese el tipo de servicio a filtrar (H-Hardware, S-Software): ")
            if letra == "H":
                tipo = "Hardware"
            elif letra == "S":
                tipo = "Software"
            else:
                print("Ingrese un valor correcto")
            if tipo != "":
                servicios_filtrados = filtrar_por_tipo(servicios, tipo)
                imprimir_lista(servicios_filtrados)
        elif opcion == "5":
            servicios = mostrar_servicios_ordenados(servicios)
        elif opcion == "6":
            nombre_archivo_salida = input("Ingrese el nombre del archivo de salida JSON: ")
            guardar_archivo(nombre_archivo_salida, servicios)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
