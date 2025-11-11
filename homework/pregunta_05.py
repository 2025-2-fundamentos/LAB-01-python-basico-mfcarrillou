"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        letter_max_min = {}
        for row in reader:
            letter = row[0]
            if letter in letter_max_min:
                max_ = max(letter_max_min[letter][0], int(row[1]))
                min_ = min(letter_max_min[letter][1], int(row[1]))
                letter_max_min[letter] = (max_, min_)
            else:
                letter_max_min[letter] = (int(row[1]), int(row[1]))

    result = sorted(letter_max_min.items())
    
    return [(letter, max_, min_) for letter, (max_, min_) in result]