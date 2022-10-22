import pandas as pd
import os
import re
from etl_reporte_llamadas import save_data


def generar_consolidado(archivo):
    return (archivo)


def save_datos(archivo, filename, step='consolidado'):

    out_name = step + '_' + filename
    out_path = os.path.join(
        'C:/Users/Dell/OneDrive/Documentos/Universidad/Lenguaje_Big_Data/data/processed', out_name)
    archivo.to_csv(out_path)


def main():
    filename = 'llamadas123'
    path = 'C:/Users/Dell/OneDrive/Documentos/Universidad/Lenguaje_Big_Data/data/processed'
    os.chdir(path)
    archivos = [x for x in os.listdir() if re.search('Limpieza', x)]

    df = pd.DataFrame()

    for i in archivos:
        archivo = pd.read_csv(i)
        df = pd.concat([archivo, df])

    archivo = generar_consolidado(archivo)
    archivo = save_datos(archivo, filename)


main()
