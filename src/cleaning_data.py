# pseudo codigo
# main()
#   datos = leer_datos(nombre del archivo : str) -- pd.dataframe
#   datos = remover_duplicados_y_nulos(datos : pd.dataframe) --pd.dataframe
#   datos = convertir_str_a_num(datos,col='EDAD') --pd.dataframe
#   datos = corregir_fechas (datos,col='FECHA1') --pd.dataframe
#   datos = corregir_fechas (datos,col='FECHA2') --pd.dataframe
#   save_data(datos)


import numpy as np
from pathlib import Path
import os
from dateutil.parser import parse
from etl_reporte_llamadas import get_data
import pandas as pd


root_dir = Path('.').resolve()


def remover_duplicados_y_nulos(datos):

    datos = datos.drop_duplicates()
    datos.reset_index(inplace=True, drop=True)
    print('forma final', datos.shape)
    col = "UNIDAD"
    datos[col].fillna('SIN_DATO', inplace=True)


def convertir_str_a_num(datos):

    col = "EDAD"
    datos[col].replace({'SIN_DATO': np.nan}, inplace=True)
    str_num = '28'
    f(str_num)
    def f(x): return x if pd.isna(x) else int(x)
    datos[col] = datos[col].apply(f)


def main():
    datos = get_data(filename='llamadas123_julio_2022.csv')
    datos = remover_duplicados_y_nulos(datos)
    datos = convertir_str_a_num(datos)


main()


# Tratamiento de valores nulos
# nulo de string = sin_dato - n/a
# nulo numeros = numpy utilizar funcion nan(not_asigned_name) (np.nan)
# nulo de fechas = nat (not_asigned_time)
# libreria para encontrar fecha en ualquier formato, conservando el formato
