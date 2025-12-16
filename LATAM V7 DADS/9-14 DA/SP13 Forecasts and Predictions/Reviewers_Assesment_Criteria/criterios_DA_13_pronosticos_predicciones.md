# Criterios de Evaluación: DA_13 - Pronósticos y Predicciones (Gimnasio Model Fitness)


## Objetivo

Analizar la pérdida de clientes (churn) en la cadena de gimnasios "Model Fitness" para desarrollar una estrategia de retención basada en datos. Esto incluye predecir la probabilidad de pérdida futura de cada cliente y segmentar a los usuarios para ofrecer estrategias personalizadas.

**Requisitos previos**: Conocimientos de Python, Pandas, Scikit-learn (Clasificación y Clustering), Visualización de datos.

**Competencias que desarrollarás**: Entrenamiento de modelos de clasificación supervisada, evaluación de modelos (métricas), clustering no supervisado (K-Means, Dendrogramas), interpretación de modelos para negocio.

<details>
<summary>Requisitos del Entregable</summary>

## Contenido esperado del entregable

Para que tu entregable sea aprobado, el mismo deberá ser realizado en **Jupyter Notebook** y contener al menos lo siguiente:

### 1. Análisis Exploratorio de Datos (EDA)
Se espera que seas capaz de:
- **Cargar y explorar el dataset** (`gym_churn_us.csv`).
- **Comparar las características** de los usuarios que cancelaron vs. los que se quedaron.
- **Visualizar la distribución** de las características.
- **Analizar la correlación** entre variables para detectar multicolinealidad.

### 2. Modelo de Predicción de Churn (Clasificación)
- **Preparar los datos**: Dividir en conjuntos de entrenamiento y prueba (Train/Test Split).
- **Entrenar modelos**: Implementar Regresión Logística y Bosque Aleatorio (Random Forest).
- **Evaluar modelos**: Calcular y comparar métricas como Accuracy, Precision y Recall.

### 3. Clustering de Usuarios (Segmentación)
- **Estandarizar los datos**: Paso crucial antes de aplicar algoritmos de distancia.
- **Construir un dendrograma**: Para visualizar la jerarquía y estimar el número de clusters.
- **Aplicar K-Means**: Agrupar a los usuarios en 5 clusters (o el número óptimo encontrado).
- **Perfilar los clusters**: Analizar las características promedio de cada grupo y su tasa de cancelación.

### 4. Conclusiones y Recomendaciones
- **Interpretar los resultados**: ¿Qué características predicen mejor la fuga? ¿Cómo son los grupos de usuarios?
- **Proponer estrategias**: Recomendaciones de marketing específicas para retener a los grupos en riesgo.

</details>

## Glosario de Términos Técnicos

**Churn**: Tasa de cancelación o abandono de clientes. Variable objetivo binaria (0: se queda, 1: se va).

**Regresión Logística**: Algoritmo de clasificación lineal útil para predecir probabilidades binarias.

**Random Forest**: Algoritmo de ensamble basado en múltiples árboles de decisión. Robusto y preciso.

**K-Means**: Algoritmo de clustering no supervisado que agrupa datos en K grupos basándose en la distancia media.

**Dendrograma**: Diagrama de árbol que muestra la disposición de los clusters producidos por el clustering jerárquico.

**Estandarización (StandardScaler)**: Proceso de escalar las características para que tengan media 0 y desviación estándar 1. Esencial para algoritmos basados en distancia como K-Means.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**EDA y Preparación**
- [ ] **[OBLIGATORIO]** Muestra estadísticas descriptivas y medias por grupo (Churn)
- [ ] **[OBLIGATORIO]** Genera matriz de correlación
- [ ] **[OBLIGATORIO]** Divide datos en Train/Test

**Modelos de Clasificación**
- [ ] **[OBLIGATORIO]** Entrena Regresión Logística
- [ ] **[OBLIGATORIO]** Entrena Random Forest
- [ ] **[OBLIGATORIO]** Calcula métricas (Accuracy, Precision, Recall) para ambos

**Clustering**
- [ ] **[OBLIGATORIO]** Estandariza los datos (StandardScaler)
- [ ] **[OBLIGATORIO]** Genera dendrograma
- [ ] **[OBLIGATORIO]** Aplica K-Means (n=5 o justificado)
- [ ] **[OBLIGATORIO]** Calcula tasa de churn por cluster

### INTERMEDIO (6 criterios)

**Calidad del Análisis**
- [ ] **[OBLIGATORIO]** Interpreta coeficientes/importancia de características
- [ ] **[OBLIGATORIO]** Describe detalladamente el perfil de cada cluster
- [ ] **[OBLIGATORIO]** Visualiza distribuciones por cluster (boxplots/hist)
- [ ] Elimina variables multicolineales si es necesario

**Profundidad**
- [ ] Compara el rendimiento de los modelos y selecciona el mejor
- [ ] Documenta el proceso de elección de número de clusters

### AVANZADO (5 criterios)

**Excelencia y Valor de Negocio**
- [ ] Recomendaciones de marketing concretas para cada cluster
- [ ] Calcula el impacto potencial de las estrategias propuestas
- [ ] Optimiza hiperparámetros de los modelos (GridSearch/RandomSearch)
- [ ] Presentación ejecutiva y estructura clara
- [ ] Código modular y eficiente

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 1 criterio adicional de los 6 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (incluye los 3 obligatorios de Intermedio)
  - Al menos 3 criterios adicionales de los 4 no obligatorios restantes

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (Básico + Intermedio)
  - Al menos 3 criterios de la sección AVANZADO

---

## Aspectos negativos a evitar en el entregable

- **Fuga de Datos (Data Leakage)**: Incluir la variable `Churn` en el entrenamiento de K-Means (debe ser no supervisado) o en las features del modelo predictivo.
- **No Estandarizar**: Aplicar K-Means sin escalar los datos, lo que hace que las variables con mayor magnitud dominen el clustering.
- **Ignorar Multicolinealidad**: Dejar variables como `contract_period` y `month_to_end_contract` juntas en una Regresión Logística sin analizar su impacto.
- **Falta de Interpretación**: Mostrar "Cluster 0, 1, 2" sin explicar quiénes son (ej. "Cluster 0 son los usuarios nuevos de corto plazo").

---

## Ejemplos de Cumplimiento (Contexto: Model Fitness)

**Estandarización y Clustering:**
```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Estandarizar solo las features (excluyendo Churn)
scaler = StandardScaler()
X_sc = scaler.fit_transform(X)

# K-Means
km = KMeans(n_clusters=5, random_state=0)
labels = km.fit_predict(X_sc)

# Agregar etiquetas al dataframe original para análisis
df['cluster_km'] = labels
```

**Análisis de Perfil de Cluster:**
```python
# Agrupar por cluster y ver medias
cluster_profile = df.groupby('cluster_km').mean()
print(cluster_profile.T)
# Observación: El Cluster 2 tiene la menor tasa de churn (2%) y el mayor contract_period (10.8 meses).
```

**Recomendación de Marketing:**
```markdown
### Estrategia para Cluster 3 (Alto Riesgo):
Este grupo tiene contratos de 1 mes y baja asistencia a clases grupales.
**Acción**: Ofrecer un pase gratuito a una clase grupal "premium" y un descuento del 20% si renuevan por 6 meses.
```
