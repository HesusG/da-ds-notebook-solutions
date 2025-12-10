# Criterios de Evaluación: Proyecto Rusty Bargain - Predicción de Precios de Autos

## Objetivo

Desarrollar modelo de predicción de precios de autos usados que equilibre tres parámetros críticos: tiempo de entrenamiento, velocidad de predicción y calidad (RMSE), comparando múltiples algoritmos de regresión para seleccionar el modelo óptimo según criterios balanceados.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Comparación de modelos de regresión, optimización multi-objetivo (tiempo vs calidad), preprocesamiento de datos categóricos (OHE), medición de tiempos de ejecución, análisis de trade-offs, toma de decisiones basada en múltiples métricas

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

El servicio de venta de autos usados "Rusty Bargain" está desarrollando una aplicación para ayudar a los clientes a determinar rápidamente el valor de mercado de sus autos. Tienes acceso a datos históricos: especificaciones técnicas, versiones de equipamiento y precios.

Necesitas crear un modelo que pueda determinar el valor de mercado. A Rusty Bargain le interesan:
- La calidad de la predicción
- La velocidad de la predicción
- El tiempo requerido para el entrenamiento

## Instrucciones del proyecto

1. Descarga y examina los datos
2. Entrena diferentes modelos con varios hiperparámetros (debes hacer al menos dos modelos diferentes, pero más es mejor)
3. El objetivo principal es comparar diferentes modelos para equilibrar rápidamente calidad y velocidad
4. Para cada modelo mide:
   - Tiempo de entrenamiento
   - Tiempo de predicción
   - RMSE (calidad)
5. Analiza los resultados y selecciona el mejor modelo según los tres criterios

## Descripción de los datos

**Archivo:** `/datasets/car_data.csv`

**Features:**
- `DateCrawled` - fecha de descarga del perfil de la base de datos
- `VehicleType` - tipo de carrocería del vehículo
- `RegistrationYear` - año de matriculación del vehículo
- `Gearbox` - tipo de caja de cambios
- `Power` - potencia (CV)
- `Model` - modelo del vehículo
- `Mileage` - kilometraje (medido en km)
- `RegistrationMonth` - mes de matriculación del vehículo
- `FuelType` - tipo de combustible
- `Brand` - marca del vehículo
- `NotRepaired` - vehículo reparado o no
- `DateCreated` - fecha de creación del perfil
- `NumberOfPictures` - número de fotos del vehículo
- `PostalCode` - código postal del propietario del perfil
- `LastSeen` - fecha de la última actividad del usuario

**Target:**
- `Price` - precio (en euros)

</details>


## Glosario de Términos Técnicos

**One-Hot Encoding (OHE)**: Técnica que convierte variables categóricas en columnas binarias (0/1). Cada categoría se convierte en una columna. Se usa `drop='first'` para evitar multicolinealidad.

**StandardScaler**: Normalización que transforma features a media 0 y desviación estándar 1. Esencial para modelos sensibles a escalas.

**RMSE (Root Mean Squared Error)**: Raíz del error cuadrático medio. Mide el error promedio de predicción en las mismas unidades que el target (euros). Valores más bajos son mejores.

**Tiempo de entrenamiento**: Duración del proceso de ajuste del modelo (.fit()). Se mide en segundos con time.time().

**Tiempo de predicción**: Duración del proceso de generación de predicciones (.predict()). Se mide en milisegundos. Crítico para aplicaciones en tiempo real.

**Multi-objective optimization**: Optimización con múltiples objetivos conflictivos (ejemplo: velocidad vs precisión). Requiere balancear trade-offs.

**GridSearchCV**: Búsqueda exhaustiva de hiperparámetros probando todas las combinaciones posibles. Útil para optimizar modelos como Decision Tree.

**Gradient Boosting**: Familia de algoritmos (LightGBM, CatBoost, XGBoost) que construyen modelos de forma secuencial. Generalmente más precisos pero más lentos.

**High cardinality**: Variables categóricas con muchas categorías únicas (ejemplo: Model con cientos de modelos de autos). Complican OHE creando muchas columnas.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Preprocesamiento**
- [ ] **[OBLIGATORIO]** Carga car_data.csv correctamente
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores
- [ ] Maneja valores ausentes (elimina filas o imputa valores)
- [ ] Elimina valores anómalos (Price <= 0, Power <= 0, etc.)


### INTERMEDIO

**Preprocesamiento Completo**
- [ ] **[OBLIGATORIO]** Aplica One-Hot Encoding a variables categóricas
- [ ] Aplica StandardScaler a variables numéricas
- [ ] Elimina features irrelevantes (DateCrawled, NumberOfPictures, etc.)
- [ ] Usa train/validation split (75/25 o similar)

**Comparación de Modelos**
- [ ] **[OBLIGATORIO]** Implementa al menos 2 modelos diferentes de regresión
- [ ] **[OBLIGATORIO]** Mide tiempo de entrenamiento, tiempo de predicción y RMSE para todos los modelos
- [ ] Crea tabla o visualización comparativa de resultados
- [ ] **[OBLIGATORIO]** Selecciona mejor modelo justificando con los 3 criterios (tiempo entrenamiento, tiempo predicción, RMSE)

### AVANZADO

**Optimización de Modelos**
- [ ] Optimiza hiperparámetros con GridSearchCV para al menos 1 modelo
- [ ] Prueba modelos avanzados (LightGBM, CatBoost, XGBoost)
- [ ] Implementa 6 o más modelos diferentes

**Análisis de Trade-offs**
- [ ] Analiza explícitamente trade-offs entre velocidad y calidad
- [ ] Crea visualizaciones de tiempo vs RMSE
- [ ] Justifica por qué modelo con mejor RMSE puede no ser la mejor opción
- [ ] Documenta claramente ventajas y desventajas de cada modelo


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 2 criterios adicionales de los 11 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 4 criterios adicionales de los 11 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 7 criterios adicionales de los 11 no obligatorios


## Ejemplos de Cumplimiento

**Preprocesamiento de datos categóricos:**
```python
# One-Hot Encoding
categorical_features = ['VehicleType', 'Gearbox', 'FuelType', 'Brand', 'NotRepaired']
encoder = OneHotEncoder(drop='first', sparse=False)
X_categorical_encoded = encoder.fit_transform(X_train[categorical_features])

# Scaling de features numéricas
numerical_features = ['RegistrationYear', 'Power', 'Mileage']
scaler = StandardScaler()
X_numerical_scaled = scaler.fit_transform(X_train[numerical_features])

# Combinar
X_train_processed = np.hstack([X_numerical_scaled, X_categorical_encoded])
```

**Medición de tiempos:**
```python
import time

def train_and_evaluate(model, X_train, y_train, X_val, y_val, model_name):
    # Medir tiempo de entrenamiento
    start_train = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - start_train

    # Medir tiempo de predicción
    start_pred = time.time()
    y_pred = model.predict(X_val)
    pred_time = (time.time() - start_pred) * 1000  # En milisegundos

    # Calcular RMSE
    rmse = mean_squared_error(y_val, y_pred, squared=False)

    print(f"{model_name}:")
    print(f"  Tiempo de entrenamiento: {train_time:.2f} s")
    print(f"  Tiempo de predicción: {pred_time:.2f} ms")
    print(f"  RMSE: {rmse:,.0f}")

    return {'model': model_name, 'train_time': train_time,
            'pred_time': pred_time, 'rmse': rmse}
```

**Comparación de modelos:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from lightgbm import LGBMRegressor

results = []

# Linear Regression
lr = LinearRegression()
results.append(train_and_evaluate(lr, X_train, y_train, X_val, y_val, "Linear Regression"))

# Decision Tree
dt = DecisionTreeRegressor(max_depth=10, random_state=12345)
results.append(train_and_evaluate(dt, X_train, y_train, X_val, y_val, "Decision Tree"))

# Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=12345)
results.append(train_and_evaluate(rf, X_train, y_train, X_val, y_val, "Random Forest"))

# LightGBM
lgbm = LGBMRegressor(random_state=12345)
results.append(train_and_evaluate(lgbm, X_train, y_train, X_val, y_val, "LightGBM"))

# Crear tabla comparativa
results_df = pd.DataFrame(results)
print("\n" + "="*60)
print("COMPARACIÓN DE MODELOS")
print("="*60)
print(results_df.to_string(index=False))
```

**Salida esperada:**
```
COMPARACIÓN DE MODELOS
============================================================
          model  train_time  pred_time         rmse
Linear Regression        0.34       0.09   10,508,270
   Decision Tree        1.01       0.03    3,712,084
   Random Forest        1.22       0.08    4,836,478
        LightGBM        3.14       0.68    3,478,603
```

**Selección justificada del mejor modelo:**
```
CONCLUSIÓN:

Selecciono Decision Tree como el modelo óptimo porque:

1. CALIDAD: RMSE de 3,712,084 - segundo mejor (solo 6.7% peor que LightGBM)
2. VELOCIDAD DE ENTRENAMIENTO: 1.01 segundos - 3x más rápido que LightGBM
3. VELOCIDAD DE PREDICCIÓN: 0.03 ms - la MÁS RÁPIDA de todos los modelos

TRADE-OFFS ANALIZADOS:
- LightGBM tiene el mejor RMSE (3,478,603) pero es 3x más lento en entrenamiento
  y 23x más lento en predicción
- Linear Regression es el más rápido en entrenamiento pero tiene RMSE 3x peor
- Random Forest tiene buen balance pero RMSE 30% peor que Decision Tree

Para una aplicación móvil que requiere respuestas rápidas, Decision Tree ofrece
el mejor equilibrio entre las tres métricas críticas.
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 8/8)
- **No compara al menos 4 modelos diferentes** (mínimo requerido para análisis comparativo)
- **No mide tiempos de entrenamiento o predicción** (objetivo principal del proyecto)
- **No aplica One-Hot Encoding** a variables categóricas (modelos no funcionan correctamente)
- **No selecciona modelo final** o selección sin justificación basada en los 3 criterios

## Errores Frecuentes

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Errores en Preprocesamiento

1. **No aplicar One-Hot Encoding a categóricas (ERROR MÁS COMÚN)**:
   - Incorrecto: Pasar variables categóricas directamente a LinearRegression, DecisionTree
   - Correcto: Aplicar OneHotEncoder o pd.get_dummies() antes de entrenar
   - Consecuencia: Error o modelo con baja calidad

2. **No eliminar features irrelevantes**:
   - Incorrecto: Incluir DateCrawled, PostalCode, NumberOfPictures
   - Correcto: Eliminar features que no aportan información predictiva
   - Consecuencia: Ruido en el modelo, RMSE más alto

3. **No manejar valores ausentes**:
   - Incorrecto: Ignorar NaN, entrenar con datos incompletos
   - Correcto: Eliminar filas con NaN o imputar valores
   - Consecuencia: Error al entrenar o predicciones incorrectas

4. **No eliminar valores anómalos**:
   - Incorrecto: Mantener Price = 0, Power = 0
   - Correcto: Filtrar registros con valores imposibles (Price > 60, Power > 30)
   - Consecuencia: Datos anómalos distorsionan el modelo

5. **No escalar variables numéricas**:
   - Incorrecto: Usar Power (0-1000) y Mileage (0-500000) sin escalar
   - Correcto: Aplicar StandardScaler a features numéricas
   - Consecuencia: Modelos como LinearRegression funcionan mal

### Errores en Modelado


6. **No medir tiempos de ejecución**:
   - Incorrecto: Solo reportar RMSE
   - Correcto: Medir tiempo de entrenamiento y predicción con time.time()
   - Consecuencia: No cumple objetivo principal del proyecto

7. **No usar train/validation split**:
   - Incorrecto: Entrenar y evaluar en mismo conjunto de datos
   - Correcto: train_test_split(test_size=0.25, random_state=12345)
   - Consecuencia: Sobreestima calidad del modelo (overfitting)

8. **Usar diferentes datos para diferentes modelos**:
   - Incorrecto: Preprocesar datos de forma diferente para cada modelo
   - Correcto: Mismo X_train, X_val, y_train, y_val para todos los modelos
   - Consecuencia: Comparación injusta, resultados no comparables

### Errores en Análisis

9. **Seleccionar modelo solo por RMSE**:
    - Incorrecto: "CatBoost tiene mejor RMSE, lo selecciono"
    - Correcto: Balancear RMSE, tiempo entrenamiento y tiempo predicción
    - Consecuencia: Ignora objetivo multi-criterio del proyecto

10. **No justificar selección de modelo**:
    - Incorrecto: "Selecciono Decision Tree" sin explicación
    - Correcto: Explicar trade-offs entre velocidad y calidad
    - Consecuencia: No demuestra comprensión del problema

11. **No crear tabla comparativa**:
    - Incorrecto: Solo imprimir resultados de cada modelo por separado
    - Correcto: Crear DataFrame o tabla con todos los modelos y métricas
    - Consecuencia: Dificulta comparación visual y análisis

### Errores Conceptuales

12. **Confundir tiempo de predicción total vs por elemento**:
    - Incorrecto: Reportar tiempo total de predicción del validation set
    - Correcto: Tiempo total está bien, pero clarificar si es total o promedio
    - Consecuencia: Comparaciones confusas

13. **No entender que modelo más lento puede ser mejor**:
    - Incorrecto: Siempre preferir modelo más rápido
    - Correcto: Evaluar si ganancia en RMSE justifica tiempo extra
    - Consecuencia: Decisión subóptima

14. **Usar modelos sin random_state**:
    - Incorrecto: No especificar random_state en modelos y splits
    - Correcto: Usar random_state=12345 para reproducibilidad
    - Consecuencia: Resultados no reproducibles

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
