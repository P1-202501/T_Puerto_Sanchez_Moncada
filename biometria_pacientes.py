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