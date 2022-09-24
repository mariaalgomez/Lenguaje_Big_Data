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
from src.etl_reporte_llamadas import get_data, save_data
import pandas as pd


def remover_duplicados_y_nulos(data: pd.DataFrame):
    # llenar la funcion
    # Eliminar registros duplicados
    print('forma inicial', data.shape)
    data = data.drop_duplicates()
    data.reset_index(inplace=True, drop=True)
    print('forma final', data.shape)
    return data


def main():
    datos = get_data(filename='llamadas123_julio_2022.csv')
    datos = remover_duplicados_y_nulos(df=datos)
    save_data


# Tratamiento de valores nulos
# nulo de string = sin_dato - n/a
# nulo numeros = numpy utilizar funcion nan(not_asigned_name) (np.nan)
# nulo de fechas = nat (not_asigned_time)
# libreria para encontrar fecha en ualquier formato, conservando el formato

root_dir = Path('.').resolve().parent
filename = 'llamadas123_julio_2022.csv'
data_dir = 'raw'

file_path = os.path.join(root_dir, 'data', 'raw', filename)
# file_path
# Trae archivo de llamadas desde ubicacion
data = pd.read_csv(file_path, sep=';', encoding='latin-1')

data = data.drop_duplicates()  # drop desechar duplicados desde pandas
# Elimina columas dulicadas desde el indice
data.reset_index(inplace=True, drop=True)

col = 'UNIDAD'
# data [col].value_counts(dropna=False, normalize=True) ---- # dropna = mostrar nulos (dropna=false, no ignorar los nulos) - normalize = porcentualizar la frecuencia de repeticion de los datos
# fillna (incluye a una variable definida nombrandola coo campo ya establecido en)
data[col].fillna('SIN_DATO', inplace=True)
data[col].value_counts(dropna=False, normalize=True)

fecha = '2022-07-01 00:08:59'
pd.to_datetime(fecha)

col = 'FECHA_INICIO_DESPLAZAMIENTO_MOVIL'
data[col]

fecha = ' 0000-00-00 00:00:00'
# format (asigna formato fecha)
pd.to_datetime(fecha, errors='coerce', format='%Y/%m/%d')

col = 'FECHA_INICIO_DESPLAZAMIENTO_MOVIL'
# pd.to_datetime (convierte formato a valor fecha) --- coerce (cuando encuentra error asigna valor nulo)
data[col] = pd.to_datetime(data[col], errors='coerce')

col = 'EDAD'
data[col]

col = 'EDAD'
data[col].value_counts()

col = 'EDAD'
# .replace({'SIN_DATO': np.nan} (reemplaza campos sin dato a valor nulo)
data[col].replace({'SIN_DATO': np.nan}, inplace=True)
data[col]

data[col].unique()

# funciones lambda (siepre con ':' para syntaxis)
str_num = '28'
# convertir formato con lambda (si x es nulo, ejecute el entero de x)
def f(x): return x if pd.isna(x) else int(x)


f(str_num)

data[col] = data[col].apply(f)

col = 'RECEPCION'
data[col]

# Date time
fecha = 'may 29th 2021'
parse(fecha)


def echas(x): return parse(x)


list_fechas = list()

for fecha in data[col]:
    try:
        new_fecha = parse(fecha)
    except Exception as e:
        new_fecha = pd.to_datetime(fecha, errors='coerce')
    list_fechas.append(new_fecha)

data['RECEPCION_Corregida'] = list_fechas
