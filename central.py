# Parte 1: Cargar los datos
def cargar_datos(lineas_archivo):
    # Completar
    #print(lineas_archivo)
    generos_peliculas = []
    peliculas_por_genero = {}
    info_peliculas = []

    for x in lineas_archivo:
        fila            = x.split(',')
        titulo          = fila[0]
        popularidad     = fila[1]
        voto_promedio   = fila[2]
        cantidad_votos  = fila[3]
        generos         = fila[4]
        listGeneros = generos.split(';')

        for genero in listGeneros:
            #listGenerosTodos.add(genero)
            if genero not in generos_peliculas:
                generos_peliculas.append(genero)

            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = []
            peliculas_por_genero[genero].append(titulo)

        info_peliculas.append([
            titulo,
            popularidad,
            voto_promedio,
            cantidad_votos,
            listGeneros
        ])

    peliculas_por_genero_tuplas = [(genero, peliculas) for genero, peliculas in peliculas_por_genero.items()]

    print(f"Generos encontrados: {generos_peliculas}")
    print(f"Peliculas por Generos: {peliculas_por_genero_tuplas}")
    print(f"Informacion Peliculas: {info_peliculas}")

    print(type(generos_peliculas))
    print(type(peliculas_por_genero_tuplas))
    print(type(info_peliculas))

    return generos_peliculas,peliculas_por_genero_tuplas,info_peliculas
    #pass


# Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    resultado = ()
    # Completar con lo que falta aquí
    for x in lineas_archivo:
        fila            = x.split(',')
        titulo          = fila[0]
        voto_promedio   = fila[2]
        cantidad_votos  = fila[3]

        if titulo.upper() == nombre_pelicula.upper():
            print('Es igual')
            resultado = (voto_promedio,cantidad_votos)

    return resultado


def filtrar_y_ordenar(genero_pelicula):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    peliculas_por_genero = {}
    ordenados = {}
    valor = {}
    # Completar con lo que falta aquí
    for x in lineas_archivo:
        fila            = x.split(',')
        titulo          = fila[0]
        generos         = fila[4]
        listGeneros = generos.split(';')

        for genero in listGeneros:
            # listGenerosTodos.add(genero)
            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = []
            peliculas_por_genero[genero].append(titulo)

    for clave in peliculas_por_genero:
        if clave.upper() == genero_pelicula.upper():
            valor = peliculas_por_genero[clave]

    ordenados = sorted(valor, reverse=True)

    return ordenados



def obtener_estadisticas(genero_pelicula, criterio):
    # Cargar las lineas con la data del archivo
    lineas_archivo = leer_archivo()
    # Completar con lo que falta aquí
    estadistica = []

    for x in lineas_archivo:
        fila            = x.split(',')
        titulo          = fila[0]
        popularidad     = fila[1]
        voto_promedio   = fila[2]
        cantidad_votos  = fila[3]
        generos         = fila[4]
        listGeneros = generos.split(';')

        for genero in listGeneros:
            # listGenerosTodos.add(genero)
            if genero_pelicula.upper() == genero.upper():
                #print(genero_pelicula)
                match criterio:
                    case 'popularidad':
                        estadistica.append(float(popularidad))
                    case 'voto promedio':
                        estadistica.append(float(voto_promedio))
                    case 'cantidad votos':
                        estadistica.append(float(cantidad_votos))

    valor_max = max(estadistica)
    valor_min = min(estadistica)
    valor_prom = sum(estadistica) / len(estadistica)

    return [valor_max,valor_min,valor_prom]


# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("movies.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
            #print(lineas_peliculas)
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )


    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
