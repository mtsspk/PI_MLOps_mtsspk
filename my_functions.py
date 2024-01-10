import pandas as pd
import re

import pandas as pd

def describe_df(df):
    # Calcular cantidad total de registros
    cantidad_total_registros = len(df)
    print("Cantidad Registros: ", cantidad_total_registros)
    print('Cantidad Campos: ', len(df.columns))

    # Obtener tipos de datos de cada columna
    tipos_de_datos = df.dtypes

    # Contar valores nulos y no nulos en cada columna
    conteo_nulos = df.isnull().sum()
    conteo_no_nulos = df.notnull().sum()
    
    # Calcular porcentaje de nulos y no nulos
    porcentaje_nulos = ((conteo_nulos / len(df)) * 100).round(2)
    porcentaje_no_nulos = ((conteo_no_nulos / len(df)) * 100).round(2)

    # Contar valores únicos en cada columna
    conteo_unicos = df.nunique()

    # Calcular porcentaje de únicos
    porcentaje_unicos = ((conteo_unicos / len(df)) * 100).round(2)

    # Crear un DataFrame con los resultados
    resultados = pd.DataFrame({
        'Campo': df.columns,
        'Tipo de Dato': tipos_de_datos.values,
        'Valores Nulos': conteo_nulos.values,
        '% Nulos': porcentaje_nulos.values,
        'Valores No Nulos': conteo_no_nulos.values,
        '% No Nulos': porcentaje_no_nulos.values,
        'Valores Únicos': conteo_unicos.values,
        '% Únicos': porcentaje_unicos.values
    })

    return resultados




def duplicates(df, column):
    """
    Encuentra y devuelve los duplicados en un DataFrame basándose en una columna específica.

    Parameters:
    - df: DataFrame de pandas
    - columna: Nombre de la columna para buscar duplicados

    Returns:
    - DataFrame con los registros duplicados, ordenados por la columna especificada
    """

    duplicates = df[df.duplicated(subset=column, keep=False)].sort_values(by=column)

    duplicates_unique = duplicates[column].unique()

    duplicates_count = duplicates[column].nunique()

    print("Cantidad de valores duplicados para",column,":",duplicates_count)
    print("Valores duplicados: \n", duplicates_unique)



    return duplicates




def stats(df, campo):
    # Obtener estadísticas descriptivas
    estadisticas = df[campo].describe()

    # Calcular el promedio
    promedio = df[campo].mean()

    # Mostrar los resultados
    print(f"Campo: {campo}")
    print(f"Valor Máximo: {estadisticas['max']}")
    print(f"Valor Mínimo: {estadisticas['min']}")
    print(f"Promedio: {promedio}")

