"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('files/input/data.csv', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        c_4_sum = {}
        for row in reader:
            letter = row[3].split(',')
            for l in letter:
                if l in c_4_sum:
                    c_4_sum[l] += int(row[1])
                else:
                    c_4_sum[l] = int(row[1])

    result = dict(sorted(c_4_sum.items()))

    return result
