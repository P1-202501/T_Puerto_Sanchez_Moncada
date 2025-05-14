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

