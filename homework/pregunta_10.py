"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open('files/input/data.csv', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        column_1_4_5 = []
        for row in reader:
            c_1 = row[0]
            letters = len(row[3].split(','))
            print(letters)
            keys = len(row[4].split(','))
            print(keys)
            column_1_4_5.append((c_1, letters, keys))

    return column_1_4_5
