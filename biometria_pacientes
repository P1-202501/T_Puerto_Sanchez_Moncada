import pandas as pd

#PARTE 1

#1. Cargar el archivo 
df = pd.read_csv('biometria_pacientes.csv', sep=';', encoding='latin1')

# mostrar las primeras 10 filas.
print("primeras 10 filas:")
print(df.head(10))


#2.  Identificar la cantidad de duplicados
Cantidad_duplicados = df.duplicated().sum()
# print("Duplicados encontrados:", Cantidad_duplicados)

# Identificar la cantidad de nulos por columna
nulos_por_columna = df.isnull().sum()
# print("Nulos por columna", nulos_por_columna)

# Valores únicos en la columna 'Fuma'
valores_columna_fuma = df['Fuma'].unique()
# print("Valores únicos en la columna 'Fuma':", valores_columna_fuma)

#3. Eliminar duplicados
df = df.drop_duplicates()
# print(df.head(10))

#4. Eliminar filas con valores nulos en columnas críticas (Peso, Talla, Glucosa, Colesterol).
columnas_criticas = ['Peso', 'Talla', 'Glucosa', 'Colesterol']
df = df.dropna(subset=columnas_criticas)
print("nueva con filas con valores nulos eliminados")
print(df.head(10))

#5. Corregir la columna Fuma: Homologar los valores ingresados por True y False. Por ejemplo, reemplazando "desconocido" por "False" por defecto
df['Fuma'] = df['Fuma'].str.strip().str.lower()
df['Fuma'] = df['Fuma'].replace({
    'sí': True, 'si': True, 'sí ': True, 'si ': True,
    'no': False, 'no ': False, 'n': False, 'desconocido': False,
    '': False, 'false': False, 'true': True
})
#6. Extraer columna Mes en una nueva columna
df['Fecha de tamizaje'] = pd.to_datetime(df['Fecha de tamizaje'], dayfirst=True, errors='coerce')
df['Mes'] = df['Fecha de tamizaje'].dt.month







