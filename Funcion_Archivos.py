import json

def cargar_archivo_json(nombre_archivo):
    """
    Carga archivos JSON

    Por parametro recibe un string que seria el nombre del archivo a recuperar

    retorna una lista con los datos del archivo
    """
    try:
        with open(nombre_archivo, 'r') as file:
            datos = json.load(file)
        return datos
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None
    
def guardar_archivo(nombre_archivo, servicios):
    """
    Guarda o sobreescribe archivos JSON

    Por parametros recibe el nombre del archivo a guardar y la lista de datos que se quiere guardar

    Retorna un archivo JSON con los datos pasados
    """
    try:
        with open(nombre_archivo, 'w') as file:
            json.dump(servicios, file, indent=4)
        print("Se han guardado los servicios en el archivo:", nombre_archivo)
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
