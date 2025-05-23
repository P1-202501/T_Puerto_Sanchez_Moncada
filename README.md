# 📊 Taller Biometría de Pacientes

**Integrantes del equipo:**

* Danna Sofía Puerto
* Alisson Moncada
* Daniel Alejandro Sánchez

---

## 📝 Descripción general del trabajo

Este trabajo realizamos un análisis  del archivo `biometria_pacientes.csv`, el cual contiene datos de tamizaje de pacientes, incluyendo variables biométricas (peso, talla, presión arterial, glucosa, colesterol), conductuales (actividad física, hábito de fumar) y demográficas (edad, sexo, región, fecha de tamizaje).

---

### 🎯 Objetivos generales del trabajo

1. **Diagnóstico y limpieza de la base de datos:**
   Identificar y corregir problemas en los datos como duplicados, valores nulos, formatos inconsistentes o entradas desorganizadas

2. **Transformación de variables y creación de nuevas métricas clínicas:**
   A partir de los datos existentes, se generaron nuevas variables de valor clínico, como el Índice de Masa Corporal (IMC), estado de hipertensión, nivel de sedentarismo, y una clasificación de alteración metabólica. Estas transformaciones permiten construir indicadores de riesgo para realizar inferencias de salud poblacional.

3. **Análisis por segmentos y agrupaciones:**
   Se utilizaron funciones como `groupby()` y `agg()` para segmentar los datos por región geográfica y por mes, con el fin de identificar patrones epidemiológicos como mayor riesgo metabólico en ciertas regiones o estacionalidad en el sedentarismo.

4. **Visualización y síntesis de resultados clínicos relevantes:**
   A partir de los análisis realizados, se generaron gráficos y reportes que permiten comunicar de forma clara los hallazgos, destacando comportamientos relevantes y posibles focos de intervención desde la salud pública o la gestión clínica.

---

### 🧠 Enfoque metodológico

El trabajo se desarrolló usando Python y bibliotecas como 'pandas' realizando una explicación de cada paso. Además, se incluyo el uso de IA y de la documentacion de PANDAS para resolver preguntas específicas, y se registraron los cambios en capturas de pantalla.
