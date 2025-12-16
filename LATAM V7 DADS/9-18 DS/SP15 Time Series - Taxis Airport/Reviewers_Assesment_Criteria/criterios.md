# Criterios de Evaluación: Proyecto Sweet Lift Taxi - Predicción de Pedidos

## Objetivo

Desarrollar modelo de pronóstico de series temporales para predecir número de pedidos de taxi en la próxima hora, aplicando feature engineering temporal (lags, rolling means, features de calendario), usando validación con TimeSeriesSplit, y cumpliendo umbral RMSE ≤ 48 en conjunto de prueba.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Series temporales, feature engineering temporal, prevención de data leakage con shift(), TimeSeriesSplit para validación, resampling de datos, análisis de tendencia y estacionalidad, modelos de regresión para forecasting

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

La compañía Sweet Lift Taxi necesita predecir la cantidad de pedidos de taxi para la próxima hora en los aeropuertos. Si pueden predecir picos de demanda, pueden atraer más conductores durante las horas de mayor actividad.

Necesitas construir un modelo para dicha predicción. La métrica RMSE en el conjunto de prueba no debe ser superior a 48.

## Instrucciones del proyecto

1. Descarga los datos y haz el remuestreo por una hora
2. Analiza los datos
3. Entrena diferentes modelos con diferentes hiperparámetros. La muestra de prueba debe ser el 10% del conjunto de datos inicial
4. Prueba los datos usando la muestra de prueba y proporciona una conclusión

## Descripción de los datos

**Archivo:** `/datasets/taxi.csv`

**Columnas:**
- `datetime`: Fecha y hora de la observación
- `num_orders`: Número de pedidos de taxi (target)

**Datos:** El número de pedidos está en la columna 'num_orders'. Los datos están recopilados cada 10 minutos.

</details>


## Glosario de Términos Técnicos

**Series Temporales (Time Series)**: Secuencia de observaciones ordenadas cronológicamente. Requiere manejo especial porque observaciones consecutivas están correlacionadas.

**Resampling**: Cambiar la frecuencia de muestreo de datos temporales. Ejemplo: agregar datos de 10 minutos a 1 hora usando median(), mean() o sum().

**Lag Features**: Variables creadas usando valores pasados de la serie temporal. Ejemplo: lag_1 = valor de hora anterior. Se usan para capturar dependencias temporales.

**Rolling Mean/Moving Average**: Promedio móvil calculado sobre ventana deslizante. Ejemplo: promedio de últimas 24 horas. Captura tendencias suaves.

**Data Leakage**: Error donde información del futuro contamina el entrenamiento. Se previene usando .shift() para que features solo usen datos del pasado.

**TimeSeriesSplit**: Estrategia de validación cruzada que respeta orden temporal. Divide datos en múltiples folds donde train siempre precede a validation.

**Temporal Train/Test Split**: División de datos cronológica sin shuffle. Train = datos antiguos, Test = datos recientes (simulando predicción futura).

**Tendencia (Trend)**: Patrón de largo plazo en serie temporal (crecimiento/decrecimiento sostenido).

**Estacionalidad (Seasonality)**: Patrón que se repite en intervalos regulares (diario, semanal, mensual).

**Calendar Features**: Variables extraídas de timestamp: hour, day, dayofweek, month. Capturan patrones cíclicos.

**RMSE Threshold**: Umbral máximo aceptable de RMSE en test set. En este proyecto: RMSE ≤ 48.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Preprocesamiento**
- [ ] **[OBLIGATORIO]** Carga taxi.csv correctamente
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores
- [ ] **[OBLIGATORIO]** Resamplea datos de 10 minutos a 1 hora usando resample('1H')
- [ ] Usa función de agregación apropiada (median, mean, sum)


### INTERMEDIO

**Feature Engineering Temporal**
- [ ] **[OBLIGATORIO]** Crea lag features (al menos lag_1, lag_2, lag_3)
- [ ] Usa .shift() correctamente para prevenir data leakage
- [ ] Crea rolling mean feature (ventana de 24 horas o similar)
- [ ] **[OBLIGATORIO]** Crea calendar features (hour, day, dayofweek, month)
- [ ] Maneja NaN resultantes de shift() y rolling (dropna o fillna)

**Temporal Train/Test Split**
- [ ] **[OBLIGATORIO]** Train/test split con shuffle=False (orden cronológico preservado)
- [ ] Test set = 10% de datos (aproximadamente 440 observaciones)
- [ ] Train set = 90% de datos

**Comparación de Modelos**
- [ ] **[OBLIGATORIO]** Implementa al menos 2 modelos de regresión
- [ ] Calcula RMSE en conjunto de prueba
- [ ] **[OBLIGATORIO]** RMSE en test set ≤ 48 (cumple umbral)
- [ ] **[OBLIGATORIO]** Calcula RMSE en train y test para todos los modelos
- [ ] Compara modelos y selecciona el mejor justificando con RMSE test
- [ ] Incluye modelo baseline (predicción constante con median)

### AVANZADO

**Análisis de Serie Temporal**
- [ ] Visualiza serie temporal original y resampled
- [ ] Analiza tendencia (trend) de la serie
- [ ] Analiza estacionalidad (seasonality) - patrones diarios/semanales
- [ ] Identifica patrones de demanda por hora del día

**Validación Robusta**
- [ ] Usa TimeSeriesSplit para validación cruzada
- [ ] Optimiza hiperparámetros con GridSearchCV + TimeSeriesSplit
- [ ] Prueba modelos avanzados (CatBoost, LightGBM, XGBoost)

**Feature Engineering Avanzado**
- [ ] Crea 5 o más lag features (lag_1 hasta lag_5 o más)
- [ ] Experimenta con diferentes ventanas de rolling mean
- [ ] Crea features adicionales (weekend flag, peak hour indicator)

**Código Profesional**
- [ ] Visualizaciones de predicciones vs valores reales en test set
- [ ] Tabla comparativa de todos los modelos con RMSE train/test
- [ ] Análisis de errores (residuales)


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 2 criterios adicionales de los 17 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 4 criterios adicionales de los 17 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 8 criterios adicionales de los 17 no obligatorios


## Ejemplos de Cumplimiento

**Resampling correcto:**
```python
# Leer datos
data = pd.read_csv('/datasets/taxi.csv', parse_dates=['datetime'], index_col='datetime')

# Resamplear de 10 minutos a 1 hora usando median
data_hourly = data.resample('1H').median()

print(f"Datos originales: {len(data)} registros (cada 10 min)")
print(f"Datos resampled: {len(data_hourly)} registros (cada hora)")
```

**Feature engineering temporal con prevención de data leakage:**
```python
# Lag features (usar shift para prevenir data leakage)
data_hourly['lag_1'] = data_hourly['num_orders'].shift(1)
data_hourly['lag_2'] = data_hourly['num_orders'].shift(2)
data_hourly['lag_3'] = data_hourly['num_orders'].shift(3)
data_hourly['lag_4'] = data_hourly['num_orders'].shift(4)
data_hourly['lag_5'] = data_hourly['num_orders'].shift(5)

# Rolling mean de 24 horas (usar shift para no incluir valor actual)
data_hourly['rolling_mean'] = data_hourly['num_orders'].shift(1).rolling(window=24).mean()

# Calendar features
data_hourly['hour'] = data_hourly.index.hour
data_hourly['day'] = data_hourly.index.day
data_hourly['dayofweek'] = data_hourly.index.dayofweek
data_hourly['month'] = data_hourly.index.month

# Eliminar NaN resultantes de shift y rolling
data_hourly = data_hourly.dropna()

print(f"Features creadas: {data_hourly.columns.tolist()}")
```

**Temporal train/test split correcto:**
```python
from sklearn.model_selection import train_test_split

# Separar features y target
X = data_hourly.drop('num_orders', axis=1)
y = data_hourly['num_orders']

# Split temporal SIN shuffle (preservar orden cronológico)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.1,  # 10% para test
    shuffle=False,   # CRÍTICO: no mezclar datos
    random_state=12345
)

print(f"Train: {X_train.index.min()} a {X_train.index.max()}")
print(f"Test:  {X_test.index.min()} a {X_test.index.max()}")
print(f"Train size: {len(X_train)}, Test size: {len(X_test)}")
```

**Modelo baseline:**
```python
# Baseline: predicción constante con median del train set
baseline_pred = np.full(len(y_test), y_train.median())
rmse_baseline = mean_squared_error(y_test, baseline_pred, squared=False)
print(f"Baseline RMSE: {rmse_baseline:.2f}")
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
lr.fit(X_train, y_train)
rmse_train = mean_squared_error(y_train, lr.predict(X_train), squared=False)
rmse_test = mean_squared_error(y_test, lr.predict(X_test), squared=False)
results.append({'Model': 'Linear Regression', 'RMSE Train': rmse_train, 'RMSE Test': rmse_test})

# Decision Tree
dt = DecisionTreeRegressor(max_depth=6, random_state=12345)
dt.fit(X_train, y_train)
rmse_train = mean_squared_error(y_train, dt.predict(X_train), squared=False)
rmse_test = mean_squared_error(y_test, dt.predict(X_test), squared=False)
results.append({'Model': 'Decision Tree', 'RMSE Train': rmse_train, 'RMSE Test': rmse_test})

# Random Forest
rf = RandomForestRegressor(n_estimators=10, max_depth=10, random_state=12345)
rf.fit(X_train, y_train)
rmse_train = mean_squared_error(y_train, rf.predict(X_train), squared=False)
rmse_test = mean_squared_error(y_test, rf.predict(X_test), squared=False)
results.append({'Model': 'Random Forest', 'RMSE Train': rmse_train, 'RMSE Test': rmse_test})

# LightGBM
lgbm = LGBMRegressor(n_estimators=30, learning_rate=0.1, num_leaves=20, random_state=12345)
lgbm.fit(X_train, y_train)
rmse_train = mean_squared_error(y_train, lgbm.predict(X_train), squared=False)
rmse_test = mean_squared_error(y_test, lgbm.predict(X_test), squared=False)
results.append({'Model': 'LightGBM', 'RMSE Train': rmse_train, 'RMSE Test': rmse_test})

# Mostrar resultados
results_df = pd.DataFrame(results)
results_df['Cumple Umbral'] = results_df['RMSE Test'] <= 48
print(results_df)
```

**Salida esperada:**
```
            Model  RMSE Train  RMSE Test  Cumple Umbral
 Linear Regression        5.37       8.88           True
     Decision Tree        4.16       8.95           True
     Random Forest        3.13       8.69           True
          LightGBM        3.69       8.36           True

✓ Todos los modelos cumplen el umbral RMSE ≤ 48
Mejor modelo: LightGBM (RMSE Test = 8.36)
```

**Optimización con TimeSeriesSplit:**
```python
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

# TimeSeriesSplit para validación temporal
tscv = TimeSeriesSplit(n_splits=3)

# GridSearchCV para Decision Tree
param_grid = {
    'max_depth': [4, 6, 8, 10]
}

dt = DecisionTreeRegressor(random_state=12345)
grid_search = GridSearchCV(dt, param_grid, cv=tscv, scoring='neg_root_mean_squared_error')
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best CV RMSE: {-grid_search.best_score_:.2f}")
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 10/10)
- **RMSE en test set > 48** (no cumple umbral requerido)
- **Usa shuffle=True en train/test split** (data leakage crítico en series temporales)
- **No resamplea datos a 1 hora** (usa datos de 10 minutos directamente)
- **Data leakage en features**: No usa shift() en lags o rolling, usa valores futuros
- **No crea lag features o calendar features** (feature engineering básico ausente)

## Errores Frecuentes

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Errores Críticos de Data Leakage

1. **Usar shuffle=True en train/test split (ERROR MÁS COMÚN)**:
   - Incorrecto: `train_test_split(X, y, shuffle=True)`
   - Correcto: `train_test_split(X, y, shuffle=False)`
   - Consecuencia: Datos futuros contaminan entrenamiento, RMSE artificialmente bajo

2. **No usar shift() en lag features**:
   - Incorrecto: `data['lag_1'] = data['num_orders']` (copia misma columna)
   - Correcto: `data['lag_1'] = data['num_orders'].shift(1)`
   - Consecuencia: Modelo usa valor actual para predecirse a sí mismo (RMSE casi 0)

3. **No usar shift() en rolling mean**:
   - Incorrecto: `data['rolling_mean'] = data['num_orders'].rolling(24).mean()`
   - Correcto: `data['rolling_mean'] = data['num_orders'].shift(1).rolling(24).mean()`
   - Consecuencia: Rolling mean incluye valor actual, contamina predicción

### Errores en Preprocesamiento

4. **No resamplear datos a 1 hora**:
   - Incorrecto: Usar datos de 10 minutos directamente
   - Correcto: `data.resample('1H').median()`
   - Consecuencia: No cumple especificación del proyecto

5. **No manejar NaN de shift() y rolling()**:
   - Incorrecto: Entrenar con NaN en features
   - Correcto: `data.dropna()` después de crear features
   - Consecuencia: Error al entrenar o predicciones incorrectas

6. **Test set no es 10% del dataset**:
   - Incorrecto: `test_size=0.2` o `test_size=0.25`
   - Correcto: `test_size=0.1`
   - Consecuencia: No cumple especificación del proyecto

### Errores en Feature Engineering

7. **No crear lag features**:
   - Incorrecto: Solo usar calendar features
   - Correcto: Crear lag_1, lag_2, lag_3, etc.
   - Consecuencia: Modelo no captura dependencias temporales de corto plazo

8. **No crear calendar features**:
   - Incorrecto: Solo usar lag features
   - Correcto: Crear hour, dayofweek, month
   - Consecuencia: Modelo no captura patrones cíclicos (horas pico, días de semana)

9. **Crear features después de split**:
   - Incorrecto: Split primero, luego crear lags en train y test separadamente
   - Correcto: Crear features en dataset completo, luego split
   - Consecuencia: Lags en test set usan solo datos de test (data leakage inverso)

### Errores en Validación

10. **Usar KFold o validación aleatoria**:
    - Incorrecto: `cross_val_score(model, X, y, cv=5)`
    - Correcto: `cross_val_score(model, X, y, cv=TimeSeriesSplit(n_splits=5))`
    - Consecuencia: Datos futuros contaminan validación

11. **No comparar múltiples modelos**:
    - Incorrecto: Solo entrenar 1 modelo
    - Correcto: Comparar al menos 4 modelos diferentes
    - Consecuencia: No explora alternativas, no cumple objetivo del proyecto

12. **No incluir modelo baseline**:
    - Incorrecto: Solo modelos complejos
    - Correcto: Incluir baseline con predicción constante (median)
    - Consecuencia: No tiene referencia de qué tan bueno es el modelo

### Errores Conceptuales

13. **Creer que RMSE < 10 es normal**:
    - Incorrecto: Aceptar RMSE de 2-3 sin cuestionar
    - Correcto: RMSE realista está en rango 8-15, valores muy bajos indican data leakage
    - Consecuencia: No detecta errores de implementación

14. **No visualizar predicciones**:
    - Incorrecto: Solo reportar RMSE numérico
    - Correcto: Graficar y_test vs y_pred para ver errores
    - Consecuencia: No identifica patrones de error o problemas

15. **Interpretar RMSE sin contexto**:
    - Incorrecto: "RMSE = 8.36 es bueno" sin referencia
    - Correcto: Comparar con baseline (14.04), con umbral (48), y con rango de y (0-80)
    - Consecuencia: No entiende qué tan bueno es realmente el modelo

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
