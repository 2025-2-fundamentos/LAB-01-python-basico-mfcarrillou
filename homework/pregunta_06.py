"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        key_min_max = {}
        for row in reader:
            keys = row[4].split(',')
            for key in keys:
                key_name, key_value = key.split(':')
                if key_name in key_min_max:
                    min_ = min(key_min_max[key_name][0], int(key_value))
                    max_ = max(key_min_max[key_name][1], int(key_value))
                    key_min_max[key_name] = (min_,max_)
                else:
                    key_min_max[key_name] = (int(key_value), int(key_value))

    result = sorted(key_min_max.items())

    return [(key, min_, max_) for key, (min_, max_) in result]
