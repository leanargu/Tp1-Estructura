import math
import csv

# tablero = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7],
# ]


tablero = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]


def imprimir_tablero(tablero):
    longitud_tablero = len(tablero)
    longitud_cuadrante = int(math.sqrt(longitud_tablero))

    for numero_fila in range(longitud_tablero):
        # cada 3 filas imprime una linea horizontal
        if numero_fila % longitud_cuadrante == 0 and numero_fila != 0:
            print("- - - " * longitud_cuadrante)

        for numero_columna in range(longitud_tablero):
            # cada 3 columnas imprime un pipe formando una linea horizontal
            if numero_columna % longitud_cuadrante == 0 and numero_columna != 0:
                print(" | ", end="")

            # si el numero es el ultimo de la fila imprime con un salto de linea
            if numero_columna == (longitud_tablero - 1):
                print(tablero[numero_fila][numero_columna], end="\n")

            # sino solo con un espacio
            else:
                print(str(tablero[numero_fila][numero_columna]), end=" ")


# Busca en un tablero las coordenadas vacias y las retorna
def buscar_vacios(tablero):
    longitud_tablero = len(tablero)

    for numero_fila in range(longitud_tablero):
        for numero_columna in range(longitud_tablero):

            if tablero[numero_fila][numero_columna] == 0:
                return numero_fila, numero_columna
    return None


def validar(tablero, numero, posicion):
    return (validar_filas(tablero, numero, posicion)
            & validar_columnas(tablero, numero, posicion)
            & validar_cuadrante(tablero, numero, posicion))


# bien
def validar_filas(tablero, numero, posicion):
    longitud_tablero = len(tablero)
    for fila in range(longitud_tablero):
        if tablero[posicion[0]][fila] == numero and posicion[1] != fila:
            return False
    return True


# bien
def validar_columnas(tablero, numero, posicion):
    longitud_tablero = len(tablero)
    for columna in range(longitud_tablero):
        if tablero[columna][posicion[1]] == numero and posicion[0] != columna:
            return False
    return True


def validar_cuadrante(tablero, numero, posicion):
    longitud_tablero = len(tablero)
    longitud_cuadrante = int(math.sqrt(longitud_tablero))

    posicion_columna = posicion[1] // longitud_cuadrante
    posicion_fila = posicion[0] // longitud_cuadrante

    for fila in range(posicion_fila * longitud_cuadrante, posicion_fila * longitud_cuadrante + longitud_cuadrante):
        for columna in range(posicion_columna * longitud_cuadrante,
                             posicion_columna * longitud_cuadrante + longitud_cuadrante):
            if tablero[fila][columna] == numero and (fila, columna) != posicion:
                return False
    return True


def resolver(tablero):
    longitud_tablero = len(tablero)
    # longitud_cuadrante = int(math.sqrt(longitud_tablero))
    posicion_casillero_vacio = buscar_vacios(tablero)
    if not posicion_casillero_vacio:
        return True
    else:
        fila, columna = posicion_casillero_vacio

    for numero_a_probar in range(1, longitud_tablero + 1):
        if validar(tablero, numero_a_probar, (fila, columna)):
            tablero[fila][columna] = numero_a_probar
            escribir_csv(tablero)
            if resolver(tablero):
                return True
            tablero[fila][columna] = 0

    return False


def leer_csv(archivo_csv_importado):
    tablero_csv = []
    with open(archivo_csv_importado, "r") as archivo_csv:
        # Creamos la lista de listas separando cada valor por ","
        csv_reader = csv.reader(archivo_csv, delimiter=',')
        # Borramos los espacios en blanco
        str(csv_reader).strip()
        for fila in csv_reader:
            tablero_csv.append(fila)
    return tablero


def escribir_csv(tablero):
    with open('csv_resultado.csv', 'w') as archivo_csv:
        for line in tablero:
            archivo_csv.write(str(line))
            archivo_csv.write('\n')


imprimir_tablero(leer_csv("tablero.csv"))
resolver(tablero)
print("************************************")
imprimir_tablero(tablero)
