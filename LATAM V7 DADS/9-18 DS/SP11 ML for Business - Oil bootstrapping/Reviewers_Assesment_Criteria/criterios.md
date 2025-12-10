# Criterios de Evaluación: Proyecto OilyGiant - Selección de Región para Pozos Petroleros

## Objetivo

Implementar modelos de regresión lineal para predecir volumen de reservas petroleras en 3 regiones, aplicar técnica Bootstrapping para análisis de riesgo-ganancia, y seleccionar la región óptima que maximice beneficios y minimice riesgo de pérdidas.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Regresión lineal, Bootstrapping para análisis de riesgo, cálculo de métricas RMSE, análisis costo-beneficio, toma de decisiones con incertidumbre, interpretación de intervalos de confianza, evaluación de riesgo financiero en contexto de energía

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

La compañía minera OilyGiant está buscando el mejor lugar para un nuevo pozo. Para elegir la ubicación, se recolectan parámetros de 3 regiones seleccionadas y se analizan las características: calidad del petróleo y volumen de reservas.

El objetivo de este análisis es construir un modelo para predecir el volumen de reservas en los nuevos pozos y elegir la región con el mayor beneficio total para los pozos de petróleo seleccionados.

Se tienen datos sobre muestras de crudo de tres regiones para los cuales se analizan los beneficios y riesgos potenciales.

## Instrucciones del proyecto

1. Descarga y prepara los datos para las tres regiones: `/datasets/geo_data_0.csv`, `/datasets/geo_data_1.csv`, `/datasets/geo_data_2.csv`
2. Entrena y prueba un modelo para cada región:
   - Divide los datos en conjunto de entrenamiento y validación en proporción 75:25
   - Entrena el modelo y haz predicciones para el conjunto de validación
   - Guarda las predicciones y las respuestas correctas para el conjunto de validación
   - Imprime el volumen promedio de reservas previsto y el RMSE del modelo
   - Analiza los resultados
3. Prepara el cálculo de ganancias:
   - Todas las variables clave para los cálculos están en las instrucciones
   - Calcula el volumen suficiente de reservas para el desarrollo sin pérdidas
   - Compara el volumen obtenido con el volumen promedio de reservas en cada región
4. Calcula riesgos y ganancias para cada región:
   - Usa la técnica Bootstrapping con 1000 muestras para encontrar la distribución de ganancias
   - Encuentra la ganancia promedio, intervalo de confianza del 95% y el riesgo de pérdidas (probabilidad de que la ganancia sea negativa)

## Descripción de los datos

- `id` - identificador único de pozo de petróleo
- `f0`, `f1`, `f2` - características de los puntos (su significado específico no es importante pero hay que tomarlas en cuenta)
- `product` - volumen de reservas en el pozo de petróleo (miles de barriles)

## Condiciones del proyecto

- El presupuesto para el desarrollo de 200 pozos petroleros es de 100 millones de dólares
- Un barril de materias primas genera 4.5 USD de ingresos (el volumen de reservas está expresado en miles de barriles)
- Al explorar la región, se lleva a cabo un estudio de 500 puntos con la selección de los mejores 200 para el cálculo de ganancias
- Selecciona la región con el mayor margen de ganancia promedio
- Analiza las posibles ganancias y riesgos utilizando la técnica Bootstrapping

</details>


## Glosario de Términos Técnicos

**RMSE (Root Mean Squared Error)**: Raíz del error cuadrático medio. Métrica que mide la diferencia promedio entre valores predichos y reales. Valores bajos indican mejor precisión del modelo.

**Bootstrapping**: Técnica estadística de remuestreo que genera múltiples submuestras aleatorias (con reemplazo) del dataset original, permitiendo estimar la distribución muestral de cualquier estadístico (media, mediana, correlación) y calcular intervalos de confianza robustos sin necesidad de supuestos paramétricos. Esencial para validar la estabilidad de modelos y obtener estimaciones confiables cuando el dataset es pequeño o no sigue distribuciones conocidas.

   **Bootstrapping en este proyecto**: El proceso correcto es: (1) Crear 1000 iteraciones, (2) En cada iteración, tomar muestra aleatoria de 500 predicciones CON REEMPLAZO del conjunto de validación, (3) De esas 500 predicciones, ordenar y seleccionar los mejores 200 pozos según predicciones, (4) Calcular ganancia usando los valores REALES de esos 200 pozos, (5) Repetir 1000 veces para obtener distribución de ganancias.

**Intervalo de Confianza del 95%**: Rango de valores donde hay 95% de probabilidad de que se encuentre el valor real. Se calcula con los percentiles 2.5% y 97.5% de la distribución.

**Riesgo de pérdidas**: Probabilidad de que la ganancia sea negativa. Se calcula como el porcentaje de submuestras bootstrapping donde la ganancia es menor a cero. Un riesgo de 0% indica implementación incorrecta del bootstrapping (muy improbable estadísticamente).

**Prueba de cordura/Sanity check**: Verificación básica que confirma que el modelo funciona mejor que una predicción simple (como usar la media).

**StandardScaler**: Normalización de features que transforma cada característica a media 0 y desviación estándar 1, esencial cuando las escalas varían significativamente.

**random_state**: Parámetro que fija la semilla aleatoria para garantizar reproducibilidad en los resultados.

**Train/validation split**: División del dataset en 2 partes: entrenamiento (75%) para ajustar el modelo, y validación (25%) para evaluación.

**LinearRegression**: Modelo de aprendizaje supervisado que encuentra la relación lineal entre features y target, minimizando el error cuadrático.

**Ganancia/Beneficio**: Ingresos totales menos costos totales. Ingresos = volumen predicho × precio por barril (4500 USD). Costos = número de pozos × costo por pozo (500,000 USD).

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Carga**
- [ ] **[OBLIGATORIO]** Carga 3 archivos CSV correctamente (geo_data_0, geo_data_1, geo_data_2)
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores (todas las celdas ejecutadas secuencialmente)
- [ ] Reconoce product como la variable target

### INTERMEDIO

**Preprocesamiento**
- [ ] Elimina columna id de los 3 datasets
- [ ] Implementa StandardScaler para features f0, f1, f2
- [ ] Escala correctamente: fit en train, transform en validation

**Segmentación**
- [ ] **[OBLIGATORIO]** Train/validation split correcto (75/25) para las 3 regiones
- [ ] Usa random_state para reproducibilidad

**Modelos para 3 Regiones**
- [ ] **[OBLIGATORIO]** Modelo de regresión lineal implementado para las 3 regiones
- [ ] Calcula RMSE para las 3 regiones
- [ ] Calcula volumen promedio predicho para las 3 regiones
- [ ] Prueba de cordura implementada (comparación con predicción usando media)

**Cálculo de Ganancias**
- [ ] Calcula volumen mínimo para cubrir costos (111.11 miles de barriles)
- [ ] Implementa función para calcular ganancias de un conjunto de pozos

**Bootstrapping - Implementación Crítica**
- [ ] **[OBLIGATORIO]** Implementa 1000 iteraciones de bootstrapping para las 3 regiones
- [ ] **[OBLIGATORIO]** En cada iteración: toma muestra de 500 predicciones CON REEMPLAZO (replace=True)
- [ ] **[OBLIGATORIO]** De las 500 predicciones muestreadas, selecciona los mejores 200 pozos ordenando por predicciones descendentes
- [ ] Calcula ganancia usando valores REALES (target) de los 200 pozos seleccionados

### AVANZADO

**Análisis de Datos**
- [ ] Explora distribuciones de f0, f1, f2, product con histogramas
- [ ] Analiza correlaciones entre features y product
- [ ] Compara características de las 3 regiones
- [ ] Identifica diferencias en escalas de features entre regiones

**Bootstrapping - Análisis de Resultados**
- [ ] **[OBLIGATORIO]** Calcula porcentaje de riesgo de pérdidas (% de ganancias negativas)
- [ ] Verifica que el riesgo NO sea 0% (indicaría error en implementación)
- [ ] Genera visualizaciones de distribuciones de ganancias con histogramas

**Interpretación de Negocio**
- [ ] Compara RMSE vs prueba de cordura para evaluar confiabilidad del modelo
- [ ] Selecciona región óptima justificando con ganancia promedio Y riesgo
- [ ] Analiza trade-off entre ganancia esperada y riesgo de pérdidas
- [ ] Compara volumen promedio real vs predicho por región
- [ ] Genera conclusión de negocio clara con recomendación de región

**Código Profesional**
- [ ] Funciones modulares (model_analysis, ganancia, ganancia_bootstrapping)
- [ ] Documentación con markdown cells explicativos
- [ ] Visualizaciones claras con títulos y etiquetas


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 3 criterios adicionales

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 7 criterios adicionales

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 14 criterios adicionales


## Ejemplos de Cumplimiento

**Implementación correcta de Bootstrapping:**
```python
state = np.random.RandomState(12345)
values = []

for i in range(1000):  # 1000 iteraciones
    # Paso 1: Muestra 500 predicciones CON REEMPLAZO
    pred_subsample = predictions.sample(n=500, replace=True, random_state=state)

    # Paso 2: Obtener los valores reales correspondientes a esas predicciones
    target_subsample = target[pred_subsample.index]

    # Paso 3: Ordenar las 500 predicciones de mayor a menor
    sorted_pred = pred_subsample.sort_values(ascending=False)

    # Paso 4: Seleccionar los mejores 200 pozos según predicciones
    selected_target = target_subsample[sorted_pred.index][:200]

    # Paso 5: Calcular ganancia usando volúmenes REALES de esos 200 pozos
    profit = (sum(selected_target) * 4500) - (200 * 500000)
    values.append(profit)

# Calcular métricas
mean_profit = np.mean(values)
lower_ci = np.quantile(values, 0.025)
upper_ci = np.quantile(values, 0.975)
risk = (np.sum(np.array(values) < 0) / len(values)) * 100

print(f"Ganancia promedio: {mean_profit:,.2f}")
print(f"IC 95%: [{lower_ci:,.2f}, {upper_ci:,.2f}]")
print(f"Riesgo de pérdidas: {risk:.1f}%")
```

**Selección justificada de región óptima:**
```
"Selecciono Región 1 como la mejor opción para crear nuevos pozos petroleros porque:
1) Ganancia promedio más alta: $5,182,594.94 (vs $4,259,385 región 0 y $4,201,940 región 2)
2) Riesgo mínimo de pérdidas: 0.3% (vs 6% en regiones 0 y 2)
3) Intervalo de confianza totalmente positivo [1,281,232 , 9,536,129]
4) RMSE más bajo (0.893) indica mayor confiabilidad del modelo vs prueba de cordura (46.021)"
```

**Cálculo de volumen mínimo:**
```
"Volumen mínimo para cubrir costos = Costo por pozo / Ingreso por barril
= $500,000 / $4,500 = 111.11 miles de barriles

Este volumen supera el promedio de las 3 regiones (92.5, 68.8, 95.0 miles de barriles),
por lo que es crítico seleccionar los mejores 200 pozos de 500 estudiados."
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- **Bootstrapping mal implementado: riesgo de 0% en todas las regiones** (indica uso de replace=False, no usar random_state correctamente, o no implementar correctamente el remuestreo)
- **No implementa las 1000 submuestras** de bootstrapping (usa menos iteraciones o no implementa el loop)
- **No toma 500 predicciones en cada iteración** (toma todas las predicciones o número incorrecto)
- **No selecciona los mejores 200 de las 500 muestreadas** (selecciona 200 directamente sin ordenar, u ordena incorrectamente)
- Data leakage: escalar antes de split, o usar datos de validación en entrenamiento
- No entrena modelos para las 3 regiones
- No calcula intervalo de confianza del 95%
- No selecciona región final o selección sin justificación

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Errores Críticos en Bootstrapping

1. **Bootstrapping sin reemplazo (ERROR MÁS COMÚN)**:
   - Incorrecto: `sample(n=500, replace=False)` o sin especificar replace
   - Correcto: `sample(n=500, replace=True, random_state=state)`
   - Consecuencia: Riesgo de 0% o valores irreales, descalifica automáticamente

2. **No implementar las 1000 iteraciones**:
   - Incorrecto: `for i in range(100)` o no tener loop
   - Correcto: `for i in range(1000)`
   - Consecuencia: Estimación no robusta de la distribución

3. **No tomar 500 predicciones por iteración**:
   - Incorrecto: Usar todas las predicciones o tomar 200 directamente
   - Correcto: En cada iteración, `sample(n=500, replace=True)` del conjunto de validación completo
   - Consecuencia: No simula el escenario real de explorar 500 puntos

4. **No seleccionar los mejores 200 de las 500**:
   - Incorrecto: Tomar 200 aleatorios o primeros 200 sin ordenar
   - Correcto: Ordenar las 500 predicciones descendentemente y tomar los primeros 200
   - Consecuencia: Subestima severamente las ganancias potenciales

5. **Usar predicciones en lugar de valores reales para calcular ganancias**:
   - Incorrecto: `profit = sum(selected_predictions) * 4500 - costs`
   - Correcto: `profit = sum(selected_target_real_values) * 4500 - costs`
   - Consecuencia: Sobreestima las ganancias, no refleja incertidumbre real

6. **Calcular riesgo incorrectamente**:
   - Incorrecto: `risk = (values < 0).sum()` (sin dividir por total)
   - Correcto: `risk = (values < 0).sum() / len(values) * 100`
   - Consecuencia: Porcentaje de riesgo incorrecto

### Otros Errores Comunes

7. **Data leakage por escalado incorrecto**:
   - Incorrecto: `scaler.fit(df)` luego `train_test_split()`
   - Correcto: `train_test_split()` luego `scaler.fit(train)` luego `scaler.transform(valid)`

8. **Cálculo erróneo de ganancias**:
   - Olvidar restar costos: `profit = sum(volumes) * 4500` (falta `- 200 * 500000`)
   - Calcular costos de 500 pozos: `- 500 * 500000` (debe ser 200)

9. **Interpretar RMSE sin contexto**:
   - No comparar RMSE del modelo vs prueba de cordura, perdiendo información sobre confiabilidad

10. **No eliminar columna id**:
    - Incluir id en el entrenamiento, introduciendo ruido y reduciendo precisión

11. **Confundir train/validation/test**:
    - El proyecto usa solo train/validation (75/25), no train/validation/test (60/20/20)

12. **Random state no consistente**:
    - Usar diferentes random_state en split y bootstrapping, reduciendo reproducibilidad
    - Correcto: Usar mismo random_state (12345) en todo el notebook

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
