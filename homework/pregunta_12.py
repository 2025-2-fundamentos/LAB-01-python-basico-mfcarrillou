"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('files/input/data.csv', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        c_1_5 = {}
        for row in reader:
            letter = row[0]
            keys = row[4].split(',')
            value = sum([int(x.split(':')[1]) for x in keys])
            if letter in c_1_5:
                c_1_5[letter] += value
            else:
                c_1_5[letter] = value

    result = dict(sorted(c_1_5.items()))

    return result