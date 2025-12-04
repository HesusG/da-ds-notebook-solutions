# Criterios de Evaluación: DS_Final - Etapa 1: Plan de Trabajo (Versión Completa)


> **ESTA ES UNA ETAPA DE PLANIFICACIÓN**
> En esta entrega **NO** se espera la ejecución completa del proyecto, ni el entrenamiento de modelos, ni la obtención de resultados finales.
> El objetivo es demostrar que se ha entendido el problema y se tiene un plan sólido para resolverlo.
> **Entregar el proyecto ya finalizado con código de modelos no es adecuado y se debe gestionar con el estudiante.**

## Objetivo

Elaborar un documento exhaustivo de planificación que demuestre comprensión profunda del problema de negocio, análisis exploratorio completo de los datos disponibles, hipótesis de modelamiento (o análisis avanzado) bien fundamentadas, y una estrategia detallada para abordar el proyecto de ciencia de datos.

**Requisitos previos**: Haber completado todos los sprints previos del bootcamp de Data Science. **Importante de verificar, pues hay veces que se activa el proyecto final sin haber completado todos los sprints previos**.

**Competencias que desarrollarás**: Análisis de problemas de negocio, exploración de datos (EDA), formulación de hipótesis, definición de KPIs, diseño experimental, planificación de proyectos de ML/Clustering, identificación de stakeholders

<details>
<summary>Requisitos del Entregable</summary>

## Contenido esperado del entregable

Para que tu entregable sea aprobado, el mismo deberá contener al menos lo siguiente:

### 1. Identificación del problema de negocio
Indica de forma concreta qué se necesita hacer en el proyecto desde la perspectiva del negocio, y explica porqué realizarlo brindará valor. Para esto, es recomendable que por tu cuenta investigues acerca del sector en el que opera la empresa del caso.

### 2. Descripción de los datos
Realiza una descripción de los datos con los que trabajarás; en concreto, deberás indicar al menos lo siguiente:
- El detalle del volumen de tus datos (número de filas y columnas).
- El nivel de calidad de los datos (existencia de valores perdidos, duplicados, tipos de variables incorrectos, etc.)
- Un resumen estadístico de las variables existentes (estadísticos de centralidad, dispersión y posición, distribuciones, tablas de frecuencias, etc.).
- Cuáles son las variables de mayor interés en el contexto del caso, especificando cuál sería el objetivo de pronóstico de los modelos que construyas, y cuáles serían los mejores atributos a emplear.

### 3. Hipótesis de modelamiento
Plantea y justifica cuáles serían los mejores algoritmos a utilizar de acuerdo a tu criterio, y que permitan dar solución al problema de negocio expuesto. Recuerda que más que la cantidad de algoritmos que plantees, interesa que los mismos sean capaces de pronosticar adecuadamente la variable objetivo (o agrupar correctamente), ante lo cual es recomendable que cumplan con los siguientes requisitos:
- Deben pertenecer al tipo correspondiente en cuanto a la necesidad de clasificar, agrupar o hacer regresión.
- Debes ser capaz de implementarlos con los datos disponibles.
- Se deben cumplir los supuestos básicos en cuanto a atributos y variable objetivo.
- Deben ser verificables utilizando criterios rigurosos y robustos de validación técnica.

Vale señalar que deberás especificar **al menos 3 algoritmos distintos**, pudiendo estos ser los vistos en el curso u otros que investigues por tu propia cuenta.

### 4. Indicadores clave (KPIs)
Define claramente los indicadores que vas a utilizar para comprobar la validez de los algoritmos que implementes. Si ves conveniente, incluso puedes describir estos KPIs a modo de fórmulas matemáticas. Junto con cada uno de los indicadores, recuerda establecer cuáles serían los **umbrales aceptables** que deberían alcanzar los resultados del modelamiento, y que satisfacerían los criterios esperables en el contexto del caso.

### 5. Diseño experimental
Especifica las estrategias que utilizarás en cada uno de los algoritmos para mejorar los resultados. Recuerda incluir métodos como validación cruzada, ajuste de hiperparámetros, balanceo de variables, entre otros. Da una breve explicación de cómo estas estrategias serán útiles para alcanzar los umbrales definidos en cada uno de los KPIs.

### 6. Acciones a ejecutar
Describe una lista las tareas que vas a realizar a fin de ejecutar los modelamientos y por consiguiente dar solución al problema planteado. Es recomendable que este plan incluya de manera ordenada lo siguiente:
- Al menos tres actividades vinculadas al procesamiento y limpieza de los datos.
- Al menos tres actividades vinculadas a la preparación de datos para los distintos algoritmos (i.e codificación, escalamiento, transformación, particionamiento, etc.).
- Actividades vinculadas al desarrollo de modelos, incluyendo la creación de modelos base, y modelos optimizados mediante las estrategias del diseño experimental definidas.
- Al menos dos actividades vinculadas a la comunicación de resultados (visualizaciones, informe final, etc.)
- **Tiempos estimados para cada una de las actividades**. Recuerda que para TODO el proyecto final cuentas con dos semanas, por lo que estos tiempos deberían ajustarse a esta limitante.

### 7. Stakeholders impactados
Menciona a qué roles o áreas del negocio dentro de la empresa le serán de interés los resultados alcanzados, y explica por qué seleccionaste estos stakeholders.

</details>

## Glosario de Términos Técnicos

**Variable Objetivo (Target)**: La variable que el modelo intentará predecir (en aprendizaje supervisado).

**Clustering (Agrupamiento)**: Técnica de aprendizaje no supervisado para agrupar datos (ej: operadores) en clusters basados en similitud de comportamiento.

**KPI (Key Performance Indicator)**: Métrica clave para evaluar el éxito. Clasificación: F1, Recall. Clustering: Silhouette Score, Davies-Bouldin. Negocio: Tasa de llamadas perdidas, Tiempo de espera.

**EDA (Exploratory Data Analysis)**: Análisis exploratorio mediante estadísticas descriptivas y visualizaciones.

**Hipótesis de Modelamiento**: Suposición fundamentada sobre qué tipo de modelo, features y configuraciones serán más efectivos.

**Baseline**: Modelo o regla simple de referencia. En este caso, podría ser una regla heurística simple (ej: "quien tenga >20% llamadas perdidas es ineficaz").

**Validación Cruzada**: Técnica para evaluar la robustez del modelo.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (8 criterios obligatorios)

**Identificación del Problema**
- [ ] **[OBLIGATORIO]** Identifica problema de negocio concreto (identificar operadores ineficaces)
- [ ] **[OBLIGATORIO]** Explica el valor/importancia del análisis para el negocio

**Descripción de Datos**
- [ ] **[OBLIGATORIO]** Describe volumen de datos (número de filas, columnas, tablas/archivos)
- [ ] **[OBLIGATORIO]** Identifica calidad de datos (valores NaN, duplicados, tipos incorrectos)
- [ ] **[OBLIGATORIO]** Incluye resumen estadístico (describe(), distribuciones básicas)

**Hipótesis de Modelamiento**
- [ ] **[OBLIGATORIO]** Define enfoque claramente (Variable objetivo para supervisado O criterios de agrupación para no supervisado)
- [ ] **[OBLIGATORIO]** Propone mínimo 3 algoritmos/enfoques distintos con justificación básica

**Código**
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores en celdas secuenciales (Solo EDA y carga de datos)

### INTERMEDIO (12 criterios)

**Análisis de Contexto**
- [ ] Investiga contexto del sector (Contact Centers, eficiencia operativa)
- [ ] Identifica mejores atributos (features) candidatos (ej: agregaciones por operador)

**Hipótesis Detalladas**
- [ ] Justifica tipo de problema (Clasificación vs Clustering vs Reglas)
- [ ] Verifica supuestos básicos de algoritmos propuestos

**KPIs y Métricas**
- [ ] **[OBLIGATORIO]** Define KPIs específicos con fórmulas claras (Técnicos o de Negocio)
- [ ] **[OBLIGATORIO]** Establece umbrales de aceptación (ej: Silhouette > 0.5 o Tasa de error < 10%)

**Diseño Experimental**
- [ ] Describe estrategia de validación (Cross-validation, estabilidad de clusters, etc.)
- [ ] Describe estrategia de ajuste de hiperparámetros (K en K-Means, profundidad en árboles, etc.)
- [ ] Describe estrategia de preprocesamiento (escalado es crítico para clustering)

**Plan de Acción**
- [ ] Lista al menos 3 actividades específicas de limpieza de datos
- [ ] Lista al menos 3 actividades específicas de preparación de datos (ej: pivot tables, group by)
- [ ] Lista actividades de desarrollo de modelos/análisis

### AVANZADO (8 criterios)

**Comunicación y Planificación**
- [ ] Lista al menos 2 actividades de comunicación de resultados
- [ ] Incluye cronograma o secuencia lógica de actividades (ajustada a 2 semanas)

**Stakeholders**
- [ ] Identifica stakeholders impactados por la solución con justificación

**Calidad del Análisis**
- [ ] Incluye visualizaciones exploratorias (histogramas, boxplots, scatter plots)
- [ ] Analiza correlaciones entre variables
- [ ] Markdown cells contextualizan cada sección adecuadamente

**Comprensión Demostrada**
- [ ] Reformula el problema demostrando comprensión propia
- [ ] Propone algoritmos adicionales investigados por cuenta propia

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 11/11
  - Al menos 3 criterios adicionales de los 18 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 11/11
  - Al menos 8 criterios adicionales de los 18 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 11/11 (Básico + Intermedio)
  - Al menos 5 criterios de la sección AVANZADO

---

## Ejemplos de Cumplimiento (Contexto: CallMeMaybe)

**Identificación completa del problema de negocio:**
```markdown
## 1. Identificación del Problema de Negocio

### 1.1 Contexto del Sector
Los servicios de telefonía virtual como CallMeMaybe dependen de la eficiencia de sus operadores.
Un operador ineficaz no solo genera costos, sino que afecta la satisfacción del cliente final.

### 1.2 El Problema Específico
Se necesita identificar a los operadores que:
1. Tienen muchas llamadas perdidas (entrantes).
2. Tienen tiempos de espera largos.
3. Realizan pocas llamadas salientes (si aplica).

### 1.3 Mi Reformulación del Problema
Desarrollaré un modelo analítico para segmentar a los operadores según su rendimiento diario.
El objetivo es etiquetar automáticamente a los operadores como "Ineficaces" o "Eficaces"
basándonos en patrones de comportamiento en los datos.

### 1.4 Valor del Análisis
Identificar proactivamente a estos operadores permitirá a los supervisores:
- Ofrecer capacitación focalizada.
- Mejorar la asignación de turnos.
- Reducir la tasa de abandono de llamadas en un 15%.
```

**Descripción exhaustiva de datos:**
```python
# 1. Volumen de datos
print("=" * 60)
print("VOLUMEN DE DATOS")
# Carga de datasets
df_dataset = pd.read_csv('telecom_dataset_us.csv')
df_clients = pd.read_csv('telecom_clients_us.csv')

print(f"Dataset Principal: {df_dataset.shape} (Filas, Columnas)")
print(f"Dataset Clientes: {df_clients.shape} (Filas, Columnas)")

# 2. Calidad de datos
print("\nCALIDAD DE DATOS (Dataset Principal)")
print(df_dataset.isnull().sum())
print(f"\nDuplicados: {df_dataset.duplicated().sum()}")

# Análisis específico de columnas clave
# user_id, operator_id, is_missed_call, call_duration
```

**Definición completa de KPIs:**
```markdown
## 4. KPIs y Umbrales de Éxito

### 4.1 Métricas de Negocio (Para definir la etiqueta)
| Métrica | Fórmula | Umbral de Ineficacia |
|---------|---------|----------------------|
| **Tasa de Llamadas Perdidas** | `missed / total_incoming` | > 10% |
| **Tiempo de Espera Promedio** | `avg(wait_time)` | > 30 segundos |

### 4.2 Métricas del Modelo (Si se usa Clustering)
| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| **Silhouette Score** | Mide cohesión y separación de clusters | > 0.5 |
| **Estabilidad** | Consistencia de clusters en subsamples | Alta |

### 4.3 Baseline
Compararé mi modelo avanzado contra una regla simple:
"Cualquier operador con >5 llamadas perdidas al día es ineficaz".
```

**Diseño experimental completo:**
```markdown
## 5. Diseño Experimental

### 5.1 Estrategia de Análisis
Dado que no tenemos una etiqueta "Ineficaz" predefinida, propongo dos enfoques:

1.  **Enfoque Supervisado (Heurístico)**:
    -   Crear la etiqueta `target` basada en las reglas del negocio (ej: si cumple 2 de 3 condiciones de ineficacia).
    -   Entrenar modelos de clasificación (Logistic Regression, Random Forest) para predecir esta etiqueta.

2.  **Enfoque No Supervisado (Clustering)**:
    -   Agrupar operadores usando K-Means.
    -   Analizar los centroides para identificar cuál cluster corresponde a "Ineficaces".

### 5.2 Validación
-   Para Supervisado: Stratified K-Fold (K=5).
-   Para Clustering: Método del Codo (Elbow Method) y Silhouette Score para elegir K óptimo.
```

**Plan de acción detallado:**
```markdown
## 6. Plan de Acción

### 6.1 Limpieza de Datos
1. Tratar valores nulos en `operator_id` (decidir si eliminar o imputar).
2. Convertir columna `date` a datetime.
3. Unificar tipos de datos en `is_missed_call` (bool/int).

### 6.2 Preparación de Datos (Feature Engineering)
1.  **Agregación**: Crear un dataset por operador (`groupby('operator_id')`).
2.  Calcular métricas diarias: `total_calls`, `missed_ratio`, `avg_duration`.
3.  Escalar variables numéricas (StandardScaler) - Crítico para K-Means.

### 6.3 Desarrollo de Modelos (Planificación)
1.  Implementar K-Means con diferentes valores de K (2 a 5).
2.  Probar DBSCAN para detectar anomalías (operadores muy atípicos).
3.  Entrenar Random Forest sobre las etiquetas generadas para entender importancia de features.

### 6.4 Comunicación
1.  Graficar clusters en 2D (PCA/t-SNE).
2.  Reporte de "Top 10 Operadores Ineficaces" para supervisores.

### 6.5 Cronograma
| Fase | Actividad | Tiempo Estimado |
|------|-----------|-----------------|
| 1 | Limpieza y Agregación de datos | 2 días |
| 2 | Análisis Exploratorio (EDA) | 2 días |
| 2 | Implementación de Clustering | 4 días |
| 2 | Interpretación y Reporte | 2 días |
```

**Identificación de stakeholders:**
```markdown
## 7. Stakeholders

### 7.1 Stakeholders Directos
| Stakeholder | Rol | Impacto del Proyecto |
|-------------|-----|----------------------|
| Supervisores de Call Center | Usuario Final | Recibirán lista diaria de operadores a revisar |
| Gerente de Operaciones | Tomador de Decisión | Evaluará la mejora en eficiencia global |
```

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**

- **Subir el archivo como enlace de Google Drive** (el archivo .ipynb debe subirse directamente a la plataforma).
- **Subir 2 archivos con el mismo nombre** (ej: dos archivos .ipynb), esto rompe la plataforma.
- **Entregar el proyecto completo ya ejecutado** (con modelos entrenados y código final). Esta etapa es SOLO PLANIFICACIÓN.
- Notebook cargado como link de Google Colab (debe ser archivo .ipynb descargado).
- Celdas sin ejecutar de forma secuencial (Out[] deben ser consecutivos).
- No cumple criterios OBLIGATORIOS (menos de 11/11).
- Copia literal del enunciado sin reformulación del problema.
- No define enfoque (variable objetivo o clustering).
- No propone mínimo 3 algoritmos/enfoques con justificación.
- Hipótesis genéricas no relacionadas al problema específico.
- No define KPIs con umbrales específicos.

---

## Errores Frecuentes

### En Identificación del Problema

1. **Copiar el enunciado textualmente**:
   - Incorrecto: Pegar el texto del ejercicio.
   - Correcto: Explicar qué significa "ineficacia" en el contexto de CallMeMaybe.

### En Descripción de Datos

2. **Ignorar la estructura de los datos**:
   - Incorrecto: Analizar cada llamada individualmente sin agrupar.
   - Correcto: Entender que la ineficacia es una propiedad del *operador*, por lo que se debe agregar la información (groupby operator_id).

### En Hipótesis de Modelamiento

3. **Confundir el objetivo**:
   - Incorrecto: "Predecir si una llamada será perdida" (El objetivo es evaluar al *operador*, no la llamada).
   - Correcto: "Clasificar/Agrupar operadores según su desempeño agregado".

4. **No justificar el enfoque**:
   - Incorrecto: "Usaré K-Means".
   - Correcto: "Usaré K-Means para encontrar grupos naturales de comportamiento sin sesgo de etiquetas predefinidas".

### En KPIs

5. **KPIs genéricos**:
   - Incorrecto: "Usaré Accuracy".
   - Correcto: "Usaré Silhouette Score para evaluar la calidad de los clusters" o "Tasa de detección de ineficaces".

### En Plan de Acción

6. **Ejecutar el proyecto en lugar de planificar**:
   - Incorrecto: Entregar el análisis ya hecho.
   - Correcto: Describir los pasos que se tomarán en la siguiente etapa.

---

## Notas Importantes

- Esta es la **Etapa 1 de 3** del proyecto final
- **Requiere aprobación** antes de continuar a la Etapa 2 (Código de Solución)
- El plan debe ser **realista y ejecutable**
- Los algoritmos y KPIs definidos aquí **serán evaluados en la Etapa 2**
