def imprimir_lista(servicios):
    """
    Imprime la lista deseada en forma de columnas

    Por parametro recibe la lista que se desea imprimir

    Retorna la lista impresa en forma de columnas
    """
    if servicios:
        print("{:<5} {:<40} {:<15} {:<15} {:<10} {:<15}".format("ID", "Descripción", "Tipo", "Precio Unitario", "Cantidad", "Total"))
        for servicio in servicios:
            print("{:<5} {:<40} {:<15} {:<15} {:<10} {:<15}".format(servicio["id_servicio"], servicio["descripcion"], servicio["tipo"], servicio["precioUnitario"], servicio["cantidad"], servicio["totalServicio"]))
    else:
        print("La lista de servicios está vacía.")


def asignar_totales(servicios):
    """
    Asigna a una lista de servicios, el total de cada uno de los servicios

    Por parametro recibe la lista con los servicios en forma de datos

    Retorna la lista con los totales de los servicios aplicados
    """
    calcular_total_servicio = lambda cantidad, precio_unitario: cantidad * precio_unitario
    for servicio in servicios:
        servicio["totalServicio"] = calcular_total_servicio(float(servicio["precioUnitario"]), float(servicio["cantidad"]))
        servicio["totalServicio"] = round(servicio["totalServicio"], 2)
    return servicios


def filtrar_por_tipo(servicios, tipo):
    """
    Filtra los datos de una lista en base al tipo pasado

    Por parametro recibe la lista de servicios que se quiere filtrar, y el tipo de servicio que se filtrara

    Retorna la lista filtrada basada en el tipo de dato pasado
    """
    servicios_filtrados = []
    for servicio in servicios:
        if servicio["tipo"] == tipo:
            servicios_filtrados.append(servicio)
    return servicios_filtrados


def mostrar_servicios_ordenados(servicios):
    """
    Ordena de forma ascendente la descripcion de la lista pasada

    Por parametros recibe la lista de servicios la cual va a ser ordenada

    Retorna la lista ordenada impresa
    """
    n = len(servicios)
    for i in range(n):
        for j in range(0, n - i - 1):
            if servicios[j]["descripcion"] > servicios[j + 1]["descripcion"]:
                servicios[j]["descripcion"], servicios[j + 1]["descripcion"] = servicios[j + 1]["descripcion"], servicios[j]["descripcion"]
    imprimir_lista(servicios)
    return servicios