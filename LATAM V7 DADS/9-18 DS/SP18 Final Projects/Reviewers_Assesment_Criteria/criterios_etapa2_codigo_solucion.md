# Criterios de Evaluación: DS_Final - Etapa 2: Código de Solución (Versión Completa)


> **ESTA ES LA ETAPA DE EJECUCIÓN**
> En esta entrega se espera la implementación técnica completa de la solución planificada.
> El código debe ser funcional, reproducible y estar bien documentado.

## Objetivo

Implementar la solución completa de ciencia de datos planificada en la Etapa 1, incluyendo procesamiento exhaustivo de datos, preparación rigurosa para modelamiento, entrenamiento de múltiples modelos con optimización, y selección fundamentada del mejor modelo basado en los KPIs definidos.

**Requisitos previos**: Aprobación de la Etapa 1 (Plan de Trabajo)

**Competencias que desarrollarás**: Limpieza avanzada de datos, feature engineering, pipelines de ML, comparación sistemática de modelos, optimización de hiperparámetros, análisis de overfitting, interpretabilidad de modelos

<details>
<summary>Requisitos del Entregable</summary>

## Contenido esperado del entregable

Para que tu entregable sea aprobado, el mismo deberá ser realizado en **Jupyter Notebook** y contener al menos lo siguiente:

### 1. Procesamiento y limpieza de datos
Se espera que seas capaz de:
- **Identificar y ajustar los tipos de datos** correspondientes con la naturaleza de cada variable.
- **Identificar y dar tratamiento a valores duplicados, perdidos o inconsistencias lógicas** derivadas del contexto del caso.
- Dado que contarás con distintas fuentes de información, deberás **vincular las variables relevantes en un solo dataset** mediante procesos de concatenación y/o unión.
- **Crear o modificar variables** que te aseguren contar con atributos confiables y completos, y una variable objetivo (o enfoque de análisis) claramente definida.

### 2. Preparación de datos para modelamiento
La generalidad de algoritmos de aprendizaje computacional requieren que los datos de los que aprenden cumplan con ciertos criterios técnicos mínimos. Entonces, tu deberás asegurar esto ejecutando las siguientes actividades:
- **Codificar atributos no numéricos** de tal manera que sean comprensibles por los algoritmos que utilices.
- **Particionar los datos** considerando la potencial naturaleza temporal de los mismos y de forma que sea factible una debida evaluación técnica.
- **Escalar o transformar variables** de tal forma que se eviten sesgos por un mal dimensionamiento de los datos y/o las magnitudes.
- **Balancear las clases** en caso que exista una distribución no uniforme de los casos observados en la variable objetivo (si aplica).

### 3. Modelamiento
Utilizando los datos limpios y preparados, deberás ahora iniciar con el entrenamiento de los algoritmos que hayas definido en tu plan de trabajo. Con este propósito es importante que incluyas lo siguiente:
- **Un modelo básico (Baseline)** cuyos resultados de rendimiento en cuanto a los KPIs establecidos en tu plan de trabajo, sirvan como referencia mínima de calidad. En este punto es recomendable la utilización de algoritmos básicos como pueden ser los clasificadores o regresores dummy, o reglas heurísticas simples según sea el caso.
- **Construcción, entrenamiento y validación técnica** de los diferentes algoritmos definidos en el plan de trabajo y contrastar su rendimiento en cuanto a los KPIs con el modelo base.
- **Calibración de umbrales y ajuste de hiperparámetros** como mecanismo para mejorar los resultados alcanzados.
- **Determinación de la importancia relativa de los atributos** en el pronóstico alcanzado del mejor modelo creado.

### 4. Resumen de resultados
Describe finalmente las principales conclusiones alcanzadas. Recuerda que una buena conclusión no es una descripción de los resultados sino una **interpretación de los mismos en el contexto del caso**. En esta etapa igualmente podrías incluir las limitaciones encontradas en cuanto a los datos y los modelos implementados.

</details>

## Glosario de Términos Técnicos

**One-Hot Encoding (OHE)**: Convierte categóricas en columnas binarias (0/1). `drop='first'` evita multicolinealidad. `handle_unknown='ignore'` maneja categorías nuevas en test.

**Label Encoding**: Convierte categóricas en enteros. Útil para modelos basados en árboles. Cuidado: implica orden que puede no existir.

**StandardScaler**: Transforma a media=0, std=1. Esencial para Logistic Regression, SVM, KNN, K-Means. Fórmula: (x - mean) / std.

**Train/Test Split**: División para entrenamiento (ajuste) y evaluación (generalización). Típico: 75/25 o 80/20.

**DummyClassifier**: Baseline que ignora features. Strategies: 'stratified' (proporcional), 'most_frequent' (clase mayoritaria), 'uniform' (aleatorio).

**GridSearchCV**: Búsqueda exhaustiva de hiperparámetros con validación cruzada. Prueba todas las combinaciones del grid definido.

**Overfitting**: Modelo memoriza training pero no generaliza. Se detecta cuando train_score >> test_score.

**Data Leakage**: Información de test contamina training. Ejemplos: escalar antes de split, usar target en features.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**Carga y Validación**
- [ ] **[OBLIGATORIO]** Carga correctamente todos los datasets/tablas
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores en celdas secuenciales
- [ ] **[OBLIGATORIO]** Identifica y ajusta tipos de datos por variable

**Limpieza de Datos**
- [ ] **[OBLIGATORIO]** Identifica y trata valores ausentes con justificación
- [ ] **[OBLIGATORIO]** Identifica y trata duplicados e inconsistencias
- [ ] **[OBLIGATORIO]** Vincula variables relevantes en un solo dataset (unión/concatenación)

**Preparación Básica**
- [ ] **[OBLIGATORIO]** Define variable objetivo o enfoque de análisis claramente
- [ ] **[OBLIGATORIO]** Crea/modifica variables derivadas necesarias

**Modelamiento Mínimo**
- [ ] **[OBLIGATORIO]** Implementa al menos 1 modelo funcional
- [ ] **[OBLIGATORIO]** Calcula métricas básicas de evaluación

### INTERMEDIO - Preparación de Datos (8 criterios)

**Codificación y Escalamiento**
- [ ] **[OBLIGATORIO]** Codifica atributos no numéricos (OHE/Label)
- [ ] **[OBLIGATORIO]** Particiona los datos (Train/Test) respetando temporalidad si aplica
- [ ] **[OBLIGATORIO]** Escala o transforma variables para evitar sesgos
- [ ] Aplica transformaciones adicionales si necesario (log, sqrt, etc.)

**Manejo de Desbalanceo y Reproducibilidad**
- [ ] Balancea clases si hay distribución no uniforme (si aplica)
- [ ] Usa random_state consistente para reproducibilidad
- [ ] No comete data leakage (escala después de split, fit solo en train)
- [ ] Documenta decisiones de preparación con markdown cells

### INTERMEDIO - Modelamiento (10 criterios)

**Modelos Base y Comparación**
- [ ] **[OBLIGATORIO]** Implementa modelo básico (Baseline/Dummy/Heurístico)
- [ ] **[OBLIGATORIO]** Construye y entrena los algoritmos definidos en el plan
- [ ] **[OBLIGATORIO]** Contrasta rendimiento con KPIs frente al modelo base
- [ ] **[OBLIGATORIO]** Compara todos los modelos usando los KPIs de Etapa 1

**Optimización**
- [ ] Aplica validación técnica (cruzada o similar)
- [ ] Calibra umbrales y ajusta hiperparámetros
- [ ] Documenta comparación en tabla resumen clara

**Visualización de Resultados**
- [ ] Visualiza resultados (confusion matrix, curvas ROC, clusters, etc.)
- [ ] Selecciona mejor modelo con justificación basada en KPIs

### AVANZADO (7 criterios)

**Interpretabilidad**
- [ ] Determina importancia relativa de atributos del mejor modelo
- [ ] Analiza overfitting comparando métricas train vs test

**Análisis Profundo**
- [ ] Identifica casos mal clasificados/agrupados y analiza patrones
- [ ] Supera baseline por margen significativo (documentar mejora)
- [ ] Cumple umbrales de KPIs definidos en plan (o justifica si no)

**Conclusiones**
- [ ] Resumen de resultados: conclusiones interpretan resultados en contexto del caso
- [ ] Identifica limitaciones de datos y modelos implementados

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 17/17
  - Al menos 4 criterios adicionales de los 18 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 17/17
  - Al menos 9 criterios adicionales de los 18 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 17/17 (Básico + Intermedio)
  - Al menos 4 criterios de la sección AVANZADO

---

## Aspectos negativos a evitar en el entregable

Un entregable adecuado debería evitar lo siguiente:

- **Enfoque exclusivo en aspectos técnicos** sin una aclaración respecto a su relación o impacto en el contexto del caso.
- **Copiado literal de código generado por IA** sin una debida comprensión de tu parte.
- **Código que genere errores o interrupciones inesperadas** en la ejecución.
- **Falta de celdas markdown** que den un mayor contexto y profundidad al código.
- **Código que no tenga ninguna relación con la solución** o que aporte poco o nada al proceso de limpieza, preparación y modelamiento planificado.
- **Modelos sobreajustados** (Overfitting evidente no tratado).

---

## Ejemplos de Cumplimiento (Contexto: CallMeMaybe)

**Tratamiento completo de valores ausentes:**
```python
# 1. Identificar valores ausentes
print("=" * 60)
print("ANÁLISIS DE VALORES AUSENTES")
print("=" * 60)
# ... (código de análisis)

# 2. Estrategia de tratamiento por columna
# Columnas críticas (operator_id): eliminar filas si no se puede imputar
df = df.dropna(subset=['operator_id'])

# Numéricas: imputar con mediana (robusta a outliers)
# ...
```

**Preparación completa de datos (sin data leakage):**
```python
# 1. Definir features y target (o preparar para clustering)
# ...

# 2. Identificar tipos de columnas
# ...

# 3. PRIMERO hacer split, DESPUÉS preparar (evita data leakage)
# Nota: En clustering a veces se escala todo el dataset si no hay split supervisado,
# pero si hay validación externa, se debe respetar el split.
X_train, X_test = train_test_split(X, test_size=0.25, random_state=12345)

# 4. Crear preprocessor (fit solo en train)
# ...
```

**Implementación de modelo baseline:**
```python
# Baseline: Regla Heurística Simple
# "Si tiene > 10% de llamadas perdidas, es ineficaz"
def baseline_heuristic(row):
    return 1 if row['missed_call_ratio'] > 0.10 else 0

y_pred_baseline = X_test.apply(baseline_heuristic, axis=1)
# ...
```

**Comparación sistemática de modelos:**
```python
# Evaluar K-Means vs DBSCAN vs Baseline
# ...
```

**Importancia de features:**
```python
# Importancia del mejor modelo (ej: Random Forest sobre etiquetas de cluster)
# ...
```

**Resumen de resultados:**
```markdown
## RESUMEN DE RESULTADOS

### Conclusiones en contexto:
El modelo de Clustering (K-Means con K=3) logró identificar exitosamente un segmento de operadores (Cluster 2) que presentan:
1. Alta tasa de llamadas perdidas (>15%).
2. Tiempos de espera superiores a 45 segundos.
3. Baja cantidad de llamadas salientes.

Este grupo representa el 12% de la fuerza laboral y es el objetivo prioritario para re-entrenamiento.

### Limitaciones:
- La falta de datos sobre satisfacción del cliente impide validar si la "ineficacia" técnica se traduce en quejas reales.
- El modelo asume que los patrones actuales se mantendrán, pero cambios estacionales podrían afectar la segmentación.
```
