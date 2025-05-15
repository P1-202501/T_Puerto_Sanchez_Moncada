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
# print("nueva con filas con valores nulos eliminados")
# print(df.head(10))

#5. Corregir la columna Fuma: Homologar los valores ingresados por True y False. Por ejemplo, reemplazando "desconocido" por "False" por defecto
df['Fuma'] = df['Fuma'].str.strip().str.lower()
df['Fuma'] = df['Fuma'].replace({
    'sí': True, 'si': True, 'sí ': True, 'si ': True,
    'no': False, 'no ': False, 'n': False, 'desconocido': False,
    '': False, 'false': False, 'true': True
})
# print("columna Fuma corregida")
# print(df.head(10))

#6. Extraer columna Mes en una nueva columna
df['Fecha de tamizaje'] = pd.to_datetime(df['Fecha de tamizaje'], dayfirst=True, errors='coerce')
df['Mes'] = df['Fecha de tamizaje'].dt.month

print("columna Mes creada")
print(df.head(10))

# PARTE 2

# 7. columna IMC
df['IMC'] = df['Peso'] / (df['Talla']/100)**2
print("\nColumna IMC creada:")
print(df[['Peso', 'Talla', 'IMC']].head())

# 8. clasificación de IMC
def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif 18.5 <= imc < 25:
        return 'Normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

df['Clasificacion_IMC'] = df['IMC'].apply(clasificar_imc)
print("\nClasificación IMC:")
print(df[['IMC', 'Clasificacion_IMC']].head())

# 9. variable binaria Sedentario
df['Sedentario'] = df['Actividad física (min/sem)'] < 60
print("\nColumna Sedentario creada:")
print(df[['Actividad física (min/sem)', 'Sedentario']].head())

# 10. variable Hipertenso
df['Hipertenso'] = (df['PAS'] >= 140) | (df['PAD'] >= 90)
print("\nColumna Hipertenso creada:")
print(df[['PAS', 'PAD', 'Hipertenso']].head())

# 11. variable Metabólicamente alterado
cond1 = df['Glucosa'] > 126
cond2 = df['Colesterol'] > 240
cond3 = df['IMC'] > 30
cond4 = df['Sedentario']

df['Metabolicamente_alterado'] = (cond1 + cond2 + cond3 + cond4) >= 2
print("\nColumna Metabólicamente alterado creada:")
print(df[['Glucosa', 'Colesterol', 'IMC', 'Sedentario', 'Metabolicamente_alterado']].head())

# PARTE 3

# 12. Agrupacion por Región y calcular riesgo metabólico
riesgo_por_region = df.groupby('Región')['Metabolicamente_alterado'].sum().reset_index()
region_max_riesgo = riesgo_por_region.loc[riesgo_por_region['Metabolicamente_alterado'].idxmax()]
print(f"\nRegión con mayor riesgo metabólico: {region_max_riesgo['Región']} ({region_max_riesgo['Metabolicamente_alterado']} casos)")

# 13. Agrupacion por Mes y calcular sedentarismo
sedentarismo_por_mes = df.groupby('Mes')['Sedentario'].sum().reset_index()
mes_max_sedentarismo = sedentarismo_por_mes.loc[sedentarismo_por_mes['Sedentario'].idxmax()]
print(f"\nMes con más sedentarismo: Mes {mes_max_sedentarismo['Mes']} ({mes_max_sedentarismo['Sedentario']} casos)")


# PARTE 4

print(df['Metabolicamente_alterado'].value_counts())

# 14. Generar gráfica de riesgo metabólico por región
import matplotlib.pyplot as plt

# Gráfica de sedentarismo por mes
sedentarismo_por_mes.plot(kind='line', x='Mes', y='Sedentario', marker='o')
plt.title('Sedentarismo por mes')
plt.ylabel('Número de casos')
plt.xticks(range(1,13))
plt.grid(True)
plt.tight_layout()
plt.show()
