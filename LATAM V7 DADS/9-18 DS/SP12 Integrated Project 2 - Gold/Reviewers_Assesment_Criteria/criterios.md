# Criterios de Evaluación: Proyecto Zyfra - Predicción de Extracción de Oro

## Objetivo

Implementar modelos de regresión para predecir recuperación de oro en proceso de flotación, calculando métricas personalizadas (sMAPE), validando datos mediante fórmula de recuperación, y optimizando producción minera eliminando parámetros no rentables.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Regresión multi-objetivo, métricas personalizadas (sMAPE), validación de datos con fórmulas de dominio, feature engineering avanzado, manejo de missing values con justificación, análisis de procesos industriales, interpretación de etapas de purificación

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

La compañía Zyfra desarrolla soluciones de eficiencia para la industria pesada y necesita un prototipo de modelo de machine learning. El modelo debe predecir la cantidad de oro extraído del mineral de oro para optimizar la producción y eliminar parámetros no rentables.

Tienes datos sobre la extracción y purificación de oro. El modelo debe predecir la cantidad de oro recuperado del mineral de oro. Dispones de datos de extracción y purificación.

## Instrucciones del proyecto

1. Prepara los datos:
   - Abre los archivos y examina los datos
   - Verifica que la recuperación se calcule correctamente. Utiliza la siguiente fórmula para evaluar la recuperación: `Recovery = C × (F - T) / (F × (C - T)) × 100%`
   - Analiza las características que no están disponibles en el conjunto de prueba
   - Realiza el preprocesamiento de datos

2. Analiza los datos:
   - Observa cómo cambia la concentración de metales (Au, Ag, Pb) en las diferentes etapas de purificación
   - Compara las distribuciones del tamaño de gránulo de la materia prima en los conjuntos de entrenamiento y de prueba
   - Investiga las concentraciones totales de todas las sustancias en diferentes etapas

3. Construye el modelo:
   - Escribe una función para calcular el valor sMAPE final
   - Entrena diferentes modelos y evalúalos usando validación cruzada
   - Selecciona el mejor modelo y pruébalo usando la muestra de prueba

## Descripción de los datos

**Proceso tecnológico:**
- Rougher feed: materia prima
- Rougher additions: reactivos de flotación (xantato, sulfato, depresante)
- Rougher process: flotación
- Rougher tails: residuos del producto
- Float banks: instalación de flotación
- Cleaner process: purificación
- Rougher Au: concentrado de oro preliminar
- Final Au: concentrado de oro final

**Parámetros de las etapas:**
- air amount: volumen de aire
- fluid levels: nivel del fluido
- feed size: tamaño de partículas de alimentación
- feed rate: velocidad de alimentación

**Convención de nombres:** `[stage].[parameter_type].[parameter_name]`

**Etapas:**
- rougher: flotación
- primary_cleaner: purificación primaria
- secondary_cleaner: purificación secundaria
- final: características finales

**Tipos de parámetros:**
- input: parámetros de la materia prima
- output: parámetros del producto
- state: parámetros que caracterizan el estado actual de la etapa
- calculation: características de cálculo

## Fórmula de recuperación

`Recovery = C × (F - T) / (F × (C - T)) × 100%`

Donde:
- C: concentración de oro en el concentrado después de la flotación/purificación
- F: concentración de oro en la alimentación antes de la flotación/purificación
- T: concentración de oro en las colas después de la flotación/purificación

</details>


## Glosario de Términos Técnicos

**sMAPE (Symmetric Mean Absolute Percentage Error)**: Métrica de error que expresa la diferencia porcentual simétrica entre valores predichos y reales. Fórmula: `mean(|target - pred| / ((|target| + |pred|) / 2)) × 100`. Valores bajos indican mejor predicción.

**sMAPE final en este proyecto**: Combinación ponderada de dos objetivos: `sMAPE_final = 0.25 × sMAPE_rougher + 0.75 × sMAPE_final_output`. Refleja que la recuperación final es más importante que la recuperación en flotación inicial.

**Recovery (Recuperación)**: Porcentaje de metal valioso extraído del mineral durante el proceso de flotación/purificación. Se calcula mediante la fórmula: `Recovery = C × (F - T) / (F × (C - T)) × 100%`.

**Flotación**: Proceso de separación donde partículas de mineral valioso se adhieren a burbujas de aire y flotan, separándose de los residuos (tails).

**Rougher flotation**: Primera etapa de flotación que genera concentrado preliminar de oro.

**Cleaner process**: Etapa de purificación que mejora la calidad del concentrado removiendo impurezas.

**Concentrate**: Producto enriquecido con mineral valioso (oro) después de flotación/purificación.

**Tails/Tailings**: Residuos que quedan después de la extracción, con baja concentración de mineral valioso.

**Forward fill (ffill)**: Técnica de imputación que rellena valores faltantes con el último valor válido observado. Útil en series temporales donde valores cambian gradualmente.

**StandardScaler**: Normalización de features que transforma cada característica a media 0 y desviación estándar 1, esencial cuando las escalas varían significativamente.

**Multi-output regression**: Predicción simultánea de múltiples variables objetivo (rougher.output.recovery y final.output.recovery).

**Cross-validation**: Técnica de validación que divide datos en múltiples folds para evaluar robustez del modelo.

**MAE (Mean Absolute Error)**: Error absoluto promedio entre valores predichos y reales. Se usa para verificar la correcta implementación de la fórmula de recuperación.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Carga**
- [ ] **[OBLIGATORIO]** Carga 3 archivos CSV correctamente (gold_recovery_train, gold_recovery_test, gold_recovery_full)
- [ ] Examina estructura de datos con info(), describe(), head() basta con mostrar una exploración representativa

### INTERMEDIO

**Validación de Datos con Fórmula de Recuperación**
- [ ] **[OBLIGATORIO]** Implementa correctamente la fórmula de recuperación: `Recovery = C × (F - T) / (F × (C - T)) × 100%`
- [ ] **[OBLIGATORIO]** Calcula MAE entre recuperación calculada y recuperación proporcionada en datos


**Preprocesamiento**
- [ ] Identifica features ausentes en test set que existen en train set
- [ ] Implementa forward fill (ffill) para manejo de valores ausentes
- [ ] Justifica uso de forward fill basado en cambios graduales entre filas consecutivas
- [ ] Aplica StandardScaler a features numéricas
- [ ] Escala correctamente: fit en train, transform en test

**Análisis de Concentraciones**
- [ ] **[OBLIGATORIO]** Analiza concentración de Au (oro) en diferentes etapas
      

**Modelos**
- [ ] **[OBLIGATORIO]** Mínimo 2 modelos diferentes implementados (DecisionTree, RandomForest, LinearRegression)
- [ ] **[OBLIGATORIO]** Implementa sMAPE correctamente: `sMAPE_final = 0.25 × sMAPE_rougher + 0.75 × sMAPE_final`
- [ ] Predice ambas variables objetivo (rougher.output.recovery y final.output.recovery)

**Evaluación**
- [ ] Selección justificada del mejor modelo

### AVANZADO

**Análisis Exploratorio Profundo**
- [ ] Analiza concentraciones de múltiples metales (Au, Ag, Pb) en todas las etapas
- [ ] Compara distribuciones de tamaño de gránulos entre train y test sets
- [ ] Genera visualizaciones de evolución de concentraciones

**Validación Robusta**
- [ ] Implementa cross-validation (cv=5 o similar) para evaluación robusta
- [ ] Optimiza hiperparámetros con GridSearchCV o similar
- [ ] Analiza overfitting comparando resultados de train/validation/test

**Código Profesional**
- [ ] Funciones modulares (cálculo de recovery, sMAPE, evaluación de modelos)
- [ ] Documentación detallada con markdown cells
- [ ] Visualizaciones profesionales con títulos, etiquetas y leyendas


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 6/6
  - Al menos 3 criterios adicionales de los 24 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 6/6
  - Al menos 6 criterios adicionales de los 24 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 6/6
  - Al menos 12 criterios adicionales de los 24 no obligatorios

## Ejemplos de Cumplimiento

**Implementación correcta de fórmula de recuperación:**
```python
def calculate_recovery(df, stage):
    """
    Calcula recuperación usando la fórmula:
    Recovery = C × (F - T) / (F × (C - T)) × 100%
    """
    C = df[f'{stage}.output.concentrate_au']  # Concentración en concentrado
    F = df[f'{stage}.input.feed_au']           # Concentración en alimentación
    T = df[f'{stage}.output.tail_au']          # Concentración en colas

    recovery = C * (F - T) / (F * (C - T)) * 100
    return recovery

# Calcular recuperación para rougher
calculated_recovery = calculate_recovery(train_df, 'rougher')
provided_recovery = train_df['rougher.output.recovery']

# Verificar con MAE
mae = np.mean(np.abs(calculated_recovery - provided_recovery))
print(f"MAE entre recuperación calculada y proporcionada: {mae:.4f}")
# Esperado: MAE < 1 (idealmente < 0.1)
```

**Implementación correcta de sMAPE:**
```python
def smape(y_true, y_pred):
    """Calcula sMAPE para un objetivo"""
    numerator = np.abs(y_true - y_pred)
    denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
    return np.mean(numerator / denominator) * 100

def final_smape(y_true_rougher, y_pred_rougher, y_true_final, y_pred_final):
    """Calcula sMAPE final ponderado"""
    smape_rougher = smape(y_true_rougher, y_pred_rougher)
    smape_final = smape(y_true_final, y_pred_final)

    return 0.25 * smape_rougher + 0.75 * smape_final

# Para usar con sklearn
from sklearn.metrics import make_scorer
smape_scorer = make_scorer(final_smape, greater_is_better=False)
```

**Justificación de forward fill:**
```
"Los valores ausentes (~2% en train) se imputan con forward fill porque:
1) Los datos son series temporales ordenadas por fecha
2) Los parámetros del proceso cambian gradualmente entre mediciones consecutivas
3) Forward fill propaga el último valor válido, reflejando la continuidad del proceso
4) Alternativas como media/mediana ignorarían la naturaleza temporal de los datos"
```

**Análisis de concentraciones:**
```
"La concentración de oro (Au) aumenta correctamente a través de las etapas:
- Materia prima (rougher.input.feed_au): Media = 0.05%
- Concentrado rougher (rougher.output.concentrate_au): Media = 3.5% (70x)
- Concentrado final (final.output.concentrate_au): Media = 7.2% (144x)

Esto confirma que el proceso de flotación y purificación funciona correctamente,
enriqueciendo el oro en el concentrado mientras se eliminan impurezas."
```

**Selección justificada del mejor modelo:**
```
"Selecciono DecisionTree (max_depth=4) como mejor modelo porque:
1) sMAPE más bajo en cross-validation: 10.06 (vs RandomForest: 10.02, LinearRegression: 12.11)
2) Test sMAPE de 13.97 indica razonable generalización
3) La diferencia train-test sMAPE (3.91 puntos) es aceptable
4) Es más interpretable que RandomForest para identificar parámetros críticos del proceso"
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- **No implementa la fórmula de recuperación** o no verifica correcta implementación con MAE
- **No calcula sMAPE ponderado** (0.25 rougher + 0.75 final) - usa solo una métrica simple
- **No predice ambas variables objetivo** (rougher.output.recovery y final.output.recovery)
- **No verifica aumento de concentración de Au** en etapas de purificación
- Data leakage: escalar antes de split, usar features no disponibles en test set
- No entrena al menos 2 modelos diferentes
- No evalúa modelo final en conjunto de prueba

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Errores Críticos en Cálculo de Métricas

1. **No implementar fórmula de recuperación (ERROR MÁS COMÚN)**:
   - Incorrecto: No calcular recovery o saltarse la verificación con MAE
   - Correcto: Implementar `Recovery = C × (F - T) / (F × (C - T)) × 100%` y verificar MAE < 1
   - Consecuencia: No valida la integridad de los datos

2. **sMAPE incorrecto**:
   - Incorrecto: Usar MAE, MSE, RMSE en lugar de sMAPE
   - Incorrecto: No ponderar: `sMAPE = (sMAPE_rougher + sMAPE_final) / 2`
   - Correcto: `sMAPE_final = 0.25 × sMAPE_rougher + 0.75 × sMAPE_final`
   - Consecuencia: Métrica de evaluación incorrecta, modelo optimiza objetivo equivocado

3. **Predecir solo un objetivo**:
   - Incorrecto: Solo predecir final.output.recovery
   - Correcto: Predecir ambos rougher.output.recovery Y final.output.recovery
   - Consecuencia: No puede calcular sMAPE final ponderado correctamente

4. **No verificar aumento de concentración**:
   - Incorrecto: No analizar concentraciones de Au en diferentes etapas
   - Correcto: Verificar que Au aumenta: raw < rougher < final
   - Consecuencia: No valida que el proceso de purificación funciona correctamente

### Errores en Preprocesamiento

5. **Manejo incorrecto de missing values**:
   - Incorrecto: Eliminar filas con NaN (pierde ~2% de datos)
   - Incorrecto: Usar fillna(mean) sin justificación
   - Correcto: Usar fillna(method='ffill') justificando por naturaleza temporal
   - Consecuencia: Pérdida de datos o imputación inapropiada

6. **No identificar features ausentes en test**:
   - Incorrecto: Usar todas las features de train para entrenar
   - Correcto: Seleccionar solo features disponibles en test set
   - Consecuencia: Modelo no puede hacer predicciones en test (error al ejecutar)

7. **Data leakage por escalado incorrecto**:
   - Incorrecto: `scaler.fit(full_data)` antes de split
   - Correcto: Split primero, luego `scaler.fit(train)`, `scaler.transform(test)`
   - Consecuencia: Información de test filtra al entrenamiento, sobreestima performance

### Errores de Interpretación

14. **MAE de recovery alto sin investigar**:
    - Incorrecto: MAE > 5 y continuar sin investigar causa
    - Correcto: MAE < 1 indica implementación correcta; MAE > 1 requiere debugging
    - Consecuencia: Datos corruptos o fórmula mal implementada

15. **sMAPE > 20% sin analizar causas**:
    - Incorrecto: Aceptar sMAPE alto sin investigar por qué
    - Correcto: Analizar casos con mayor error, identificar patrones
    - Consecuencia: No genera insights para mejorar modelo

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
