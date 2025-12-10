# Criterios de Evaluación: Proyecto Beta Bank - Predicción de Churn

## Objetivo

Implementar y comparar modelos de machine learning para predecir abandono de clientes bancarios (churn), manejando datos desbalanceados y optimizando modelos para alcanzar F1-score ≥0.59 mediante técnicas de balanceo y evaluación sistemática.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Manejo de clases desbalanceadas, técnicas de balanceo (upsampling, class_weight), optimización con GridSearchCV, evaluación con múltiples métricas (F1-score, ROC-AUC), interpretación de resultados en contexto de retención bancaria

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Beta Bank enfrenta un problema de abandono de clientes. Se ha descubierto que es más barato retener a los clientes existentes que atraer nuevos. El objetivo es predecir si un cliente dejará el banco pronto para poder tomar acciones preventivas.

Tienes acceso a datos históricos sobre el comportamiento de los clientes y la terminación de contratos con el banco. Tu tarea es construir un modelo con el mejor F1-score posible. Necesitas alcanzar un F1-score de al menos 0.59 en el conjunto de prueba.

Además, debes medir la métrica AUC-ROC y compararla con el F1-score.

## Instrucciones del proyecto

1. Descarga y prepara los datos: `/datasets/Churn.csv`
2. Examina el balance de clases. Entrena el modelo sin tener en cuenta el desequilibrio. Describe brevemente tus hallazgos.
3. Mejora la calidad del modelo. Asegúrate de utilizar al menos dos enfoques para corregir el desequilibrio de clases. Entrena diferentes modelos y encuentra el mejor. Describe brevemente tus hallazgos.
4. Realiza la prueba final con el conjunto de prueba.

## Descripción de los datos

- `RowNumber` - índice de fila de datos
- `CustomerId` - identificador único de cliente
- `Surname` - apellido
- `CreditScore` - puntaje de crédito
- `Geography` - país de residencia
- `Gender` - género
- `Age` - edad
- `Tenure` - período durante el cual ha madurado el depósito a plazo fijo (años)
- `Balance` - saldo de la cuenta
- `NumOfProducts` - número de productos bancarios utilizados
- `HasCrCard` - el cliente tiene tarjeta de crédito (1 - sí; 0 - no)
- `IsActiveMember` - actividad del cliente (1 - sí; 0 - no)
- `EstimatedSalary` - salario estimado

**Variable objetivo:**
- `Exited` - el cliente se ha ido (1 - sí; 0 - no)

</details>


## Glosario de Términos Técnicos

**Churn**: Abandono de clientes del servicio bancario. Métrica crítica en fintech que mide la pérdida de clientes.

**Upsampling**: Técnica de sobremuestreo que aumenta artificialmente la cantidad de ejemplos de la clase minoritaria para balancear el dataset.

**class_weight**: Parámetro que ajusta automáticamente los pesos de las clases durante el entrenamiento para compensar el desbalanceo sin modificar los datos.

**F1-score**: Métrica que balancea precisión (precision) y exhaustividad (recall), especialmente útil para datasets desbalanceados. Es la media armónica entre ambas.

**ROC-AUC**: Área bajo la curva ROC (Receiver Operating Characteristic). Mide la capacidad del modelo para distinguir entre clases. Valor de 0.5 = aleatorio, 1.0 = perfecto.

**One-Hot Encoding**: Técnica que convierte variables categóricas en múltiples columnas binarias (0/1), una por cada categoría.

**StandardScaler**: Normalización de features que transforma cada característica a media 0 y desviación estándar 1, esencial cuando las escalas varían significativamente.

**GridSearchCV**: Búsqueda exhaustiva de hiperparámetros que prueba todas las combinaciones especificadas y usa validación cruzada para seleccionar la mejor.

**random_state**: Parámetro que fija la semilla aleatoria para garantizar reproducibilidad en los resultados.

**Reproducibilidad**: Capacidad de obtener exactamente los mismos resultados al ejecutar el código múltiples veces, fundamental en ML para validar experimentos y comparar modelos.

**Train/validation/test split**: División del dataset en 3 partes: entrenamiento (60%), validación (20%) para optimizar, y prueba (20%) para evaluación final.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Carga**
- [ ] **[OBLIGATORIO]** Carga correctamente el archivo `Churn.csv`.
- [ ] **[OBLIGATORIO]** El código ejecuta sin errores y todas las celdas se ejecutan en orden secuencial.
- [ ] **[OBLIGATORIO]** Identifica correctamente la variable objetivo `Exited`.

**Modelos**
- [ ] **[OBLIGATORIO]** Implementa al menos **un modelo de clasificación simple** (sin optimización ni balanceo).
- [ ] **[OBLIGATORIO]** Divide los datos en **entrenamiento y prueba** utilizando `train_test_split`.
- [ ] **[OBLIGATORIO]** Calcula correctamente el **F1-score** e interpreta brevemente su significado.



### INTERMEDIO

**Preprocesamiento**
- [ ] Identifica y maneja valores ausentes en Tenure (9.09%)
- [ ] Elimina columnas irrelevantes (RowNumber, CustomerId, Surname)
- [ ] Implementa One-Hot Encoding para Geography y Gender
- [ ] Aplica StandardScaler a features numéricas
- [ ] Verifica que HasCrCard y IsActiveMember estén en formato 0/1

  > Nota: Las variables booleanas generalmente NO requieren StandardScaler porque ya están en escala 0-1, ni One-Hot Encoding porque ya son binarias.


**Segmentación**
- [ ] Usa random_state para reproducibilidad

**Manejo de Desbalanceo**
- [ ] Identifica desbalanceo de clases
- [ ] Implementa al menos una técnica de balanceo (upsampling o class_weight)

**Modelos**
- [ ] Implementa un segundo o tercer modelos diferentes (DecisionTree, RandomForest, LogisticRegression)
- [ ] Utiliza GridSearchCV para optimización de hiperparámetros
    
- [ ] Compara al menos 2 enfoques: datos originales vs datos balanceados

**Evaluación**
- [ ] Comparación entre modelos con tablas o visualizaciones y su interpretación
- [ ] Selección justificada del mejor modelo


### AVANZADO

**Métricas Avanzadas**
- [ ] Calcula ROC-AUC del modelo final


**Análisis de Técnicas**
- [ ] Compara efectividad de upsampling vs class_weight
- [ ] Compara al menos 3 enfoques: datos originales, upsampling, class_weight
- [ ] Justifica selección de técnica de balanceo basado en resultados

**Interpretación de Negocio**
- [ ] Genera insights sobre retención de clientes
- [ ] Identifica features más importantes para predicción de churn
- [ ] Cuantifica o discute valor de negocio del modelo (costo retención vs adquisición)


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 6/6
  - Al menos 3 criterios adicionales 
  - 
- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 6/6
  - Al menos 6 criterios adicionales

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 6/6
  - Al menos 12 criterios adicionales


## Ejemplos de Cumplimiento

**Selección justificada del mejor modelo:**
```
"Selecciono RandomForest con class_weight='balanced' (F1: 0.624) sobre
DecisionTree (F1: 0.514) y LogisticRegression (F1: 0.503) porque:
1) Alcanza el mejor F1-score en el conjunto de prueba
2) Muestra balance entre train (0.837) y test (0.624), indicando menor overfitting
3) El ROC-AUC de 0.83 confirma buena capacidad de discriminación entre clases"
```

**Manejo de valores ausentes:**
```
"La columna Tenure tiene 909 valores ausentes (9.09%). Como la media (5.0)
y mediana (5.0) coinciden, se imputan con el valor 5 que representa
apropiadamente el centro de la distribución sin introducir sesgo."
```

**Comparación de técnicas de balanceo:**
```
Técnica              | F1 Train | F1 Valid | F1 Test
---------------------|----------|----------|---------
Sin balanceo         | 0.711    | 0.558    | 0.583
Upsampling           | 0.810    | 0.585    | 0.617
class_weight         | 0.837    | 0.592    | 0.624

Conclusión: class_weight='balanced' ofrece el mejor desempeño general
con menor overfitting y mejor generalización al conjunto de prueba.
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 8/8)
- Evaluación solo en datos de entrenamiento (sin conjunto de prueba)
- Data leakage evidente: entrenar con datos de test, o escalar antes de split
- No maneja el desbalanceo de clases de ninguna forma

## Errores Frecuentes

*Esta sección será completada basándose en feedback de revisores y estudiantes.*

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:


1. **Data leakage por escalado incorrecto**: Aplicar StandardScaler antes de dividir los datos, causando que información del test "filtre" al entrenamiento
   - ❌ Incorrecto: `scaler.fit(df)` → luego `train_test_split()`
   - ✅ Correcto: `train_test_split()` → luego `scaler.fit(train)` → `scaler.transform(valid/test)`

2. **Evaluación solo con datos balanceados**: Entrenar con upsampling pero olvidar que validation/test deben mantener distribución original

3. **Confundir métricas**: Usar accuracy en lugar de F1-score para evaluar modelos en datasets desbalanceados

4. **Imputación de valores ausentes sin justificación**: Rellenar Tenure sin analizar media/mediana o sin documentar la decisión

5. **No eliminar columnas irrelevantes**: Incluir RowNumber, CustomerId o Surname en el entrenamiento, introduciendo ruido

6. **GridSearchCV sin validación cruzada**: Usar GridSearchCV pero con cv=2 o sin especificar, reduciendo robustez

**📝 Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)

