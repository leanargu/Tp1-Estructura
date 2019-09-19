import math
import csv
from time import time

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
    posicion_casillero_vacio = buscar_vacios(tablero)
    if not posicion_casillero_vacio:
        return True
    else:
        fila, columna = posicion_casillero_vacio

    for numero_a_probar in range(1, longitud_tablero + 1):
        if validar(tablero, numero_a_probar, (fila, columna)):
            tablero[fila][columna] = numero_a_probar
            escribir_csv(tablero)
            if numero_a_probar == 3:
                break
            if resolver(tablero):
                return True
            tablero[fila][columna] = 0

    return False


def leer_csv(archivo_csv_importado):
    tablero_csv = []
    with open(archivo_csv_importado, "r") as archivo_csv:
        # Creamos la lista de listas separando cada valor por ","
        csv_reader = csv.reader(archivo_csv, delimiter=',')

        tablero_csv = [[int(numero) for numero in lista] for lista in csv_reader]

    return tablero_csv




def escribir_csv(tablero):
    with open('csv_resultado.csv', 'w', newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows(tablero)

def resolver_desde_cero():
    imprimir_tablero(leer_csv("tablero.csv"))
    tiempo_inicial = time()
    resolver(leer_csv("tablero.csv"))
    tiempo_final = time()
    print("************************************")
    imprimir_tablero(leer_csv("tablero.csv"))
    # print(tiempo_final-tiempo_inicial)


def resolver_recuperando():
    imprimir_tablero(leer_csv("csv_resultado.csv"))
    tiempo_inicial = time()
    resolver(leer_csv("csv_resultado.csv"))
    tiempo_final = time()
    print("************************************")
    imprimir_tablero(leer_csv("csv_resultado.csv"))
    # print(tiempo_final-tiempo_inicial)


resolver(leer_csv("csv_resultado.csv"))

# Tamaño fuera de rango, vacio, numero fuera de rango, caracter invalido, archivo inexistente,
