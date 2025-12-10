# Criterios de Evaluación: Proyecto Crankshaft List - Análisis de Precios de Vehículos

## Objetivo

Determinar qué factores influyen en el precio de un vehículo mediante análisis exploratorio de datos (EDA), tratamiento de valores ausentes, detección de outliers, análisis de correlaciones, y generación de insights sobre el mercado automotriz usando datos de anuncios.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Análisis exploratorio de datos (EDA), tratamiento de valores ausentes con imputación contextual, detección y filtrado de outliers usando percentiles, análisis de correlaciones, visualizaciones comparativas, interpretación de factores influyentes en precios

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Crankshaft List es un sitio web de anuncios gratuitos de vehículos. El objetivo es determinar qué factores influyen en el precio de un vehículo usando datos recopilados en los últimos años.

Dispones del archivo `vehicles_us.csv` con 51,525 registros de anuncios de vehículos. Tu tarea es realizar un análisis exploratorio completo, limpiar los datos, detectar valores atípicos, y determinar los factores más influyentes en el precio.

## Instrucciones del proyecto

1. **Prepara los datos:**
   - Abre el archivo y examina los datos generales
   - Identifica valores ausentes y determina estrategias de tratamiento
   - Analiza valores únicos en columnas categóricas para detectar inconsistencias
   - Estandariza nombres de modelos y valores textuales repetitivos
   - Corrige tipos de datos (date_posted a datetime, is_4wd a booleano)
   - Enriquece datos creando variables derivadas (vehicle_age, avg_mileage_per_year)
   - Convierte condition a escala numérica

2. **Analiza los datos:**
   - Examina la distribución de parámetros principales (price, vehicle_age, odometer, cylinders, condition)
   - Detecta y trata valores atípicos usando percentiles
   - Compara distribuciones antes y después del tratamiento de outliers
   - Calcula correlaciones entre precio y variables numéricas
   - Analiza precio promedio por tipo de vehículo
   - Investiga factores específicos en tipos predominantes (Sedan y SUV)

3. **Genera conclusiones:**
   - Identifica los factores más influyentes en el precio
   - Jerarquiza factores por coeficiente de correlación
   - Presenta insights específicos sobre el mercado automotriz
   - Documenta diferencias entre tipos de vehículos

## Descripción de los datos

- `price` - precio del vehículo
- `model_year` - año del modelo
- `model` - marca y modelo del vehículo
- `condition` - condición del vehículo (new, like new, excellent, good, fair, salvage)
- `cylinders` - número de cilindros
- `fuel` - tipo de combustible (gas, diesel, electric, hybrid, other)
- `odometer` - millaje del vehículo cuando el anuncio fue publicado
- `transmission` - tipo de transmisión (automatic, manual, other)
- `type` - tipo de vehículo (sedan, SUV, pickup, truck, etc.)
- `paint_color` - color de la pintura
- `is_4wd` - si el vehículo tiene tracción a las 4 ruedas (booleano)
- `date_posted` - fecha en que el anuncio fue publicado
- `days_listed` - días desde la publicación hasta que se eliminó

</details>


## Glosario de Términos Técnicos

**EDA (Exploratory Data Analysis)**: Análisis exploratorio de datos que examina datasets para resumir características principales mediante estadísticas y visualizaciones antes de aplicar técnicas de modelado.

**Outliers/Valores atípicos**: Observaciones que se desvían significativamente del patrón general de los datos. Pueden ser errores o valores legítimos pero extremos que afectan el análisis.

**Percentiles**: Valores que dividen un conjunto ordenado de datos en 100 partes iguales. El percentil 95 indica que 95% de los datos están por debajo de ese valor.

**Imputación contextual**: Técnica de rellenar valores ausentes usando información de grupos relacionados (ej: mediana por año del modelo) en lugar de usar un solo valor global.

**Correlación de Pearson**: Coeficiente que mide la relación lineal entre dos variables numéricas. Varía entre -1 (correlación negativa perfecta) y +1 (correlación positiva perfecta). Valores cerca de 0 indican poca relación lineal.

**Forward fill (ffill)**: Técnica de imputación que rellena valores faltantes con el último valor válido observado, útil en series temporales.

**Matriz de dispersión (scatter matrix)**: Visualización que muestra gráficos de dispersión para cada par de variables numéricas, permitiendo identificar relaciones multivariadas.

**Boxplot/Diagrama de caja**: Visualización que muestra distribución de datos mediante cuartiles, mediana, y valores atípicos.

**Histograma**: Gráfico de barras que representa la distribución de frecuencias de una variable continua dividida en intervalos (bins).

**One-Hot Encoding**: Técnica que convierte variables categóricas en múltiples columnas binarias (0/1), una por cada categoría.

**StandardScaler**: Normalización de features que transforma cada característica a media 0 y desviación estándar 1.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Carga**
- [ ] **[OBLIGATORIO]** Carga vehicles_us.csv correctamente (51,525 registros)
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores (todas las celdas ejecutadas secuencialmente)
- [ ] Examina estructura de datos con info(), describe(), head()

**Identificación de Valores Ausentes**
- [ ] **[OBLIGATORIO]** Identifica y documenta valores ausentes por columna
- [ ] Calcula porcentajes de valores ausentes
- [ ] Identifica patrones en datos faltantes

**Exploración de Datos Textuales**
- [ ] Explora valores únicos en columnas categóricas (condition, fuel, transmission, type, paint_color)
- [ ] Identifica inconsistencias en datos textuales

### INTERMEDIO

**Tratamiento de Valores Ausentes**
- [ ] **[OBLIGATORIO]** Implementa estrategias de imputación apropiadas
- [ ] Justifica decisiones de tratamiento por columna
- [ ] Maneja is_4wd correctamente (NaN → 0/False)
- [ ] Maneja paint_color (NaN → 'unknown')

**Estandarización de Datos**
- [ ] Estandariza nombres de modelos repetitivos (chevrolet silverado variants, ford f-series)
- [ ] Implementa función para reemplazar valores duplicados
- [ ] Reduce variabilidad en nombres de modelos

**Detección y Tratamiento de Outliers**
- [ ] **[OBLIGATORIO]** Detecta outliers usando percentiles en price, vehicle_age, odometer
- [ ] Establece límites apropiados (ej: percentil 2% y 95%)
- [ ] Documenta porcentaje de outliers identificados
- [ ] Crea DataFrame filtrado sin outliers

**Visualizaciones**
- [ ] **[OBLIGATORIO]** Crea histogramas y boxplots para variables numéricas clave
- [ ] Compara distribuciones antes y después del tratamiento de outliers
- [ ] Presenta gráficos claros con títulos y etiquetas

**Análisis de Correlaciones**
- [ ] **[OBLIGATORIO]** Calcula correlaciones entre precio y variables numéricas
- [ ] Presenta matriz de correlación
- [ ] Interpreta coeficientes de correlación obtenidos

**Tipos de Datos**
- [ ] Convierte date_posted a tipo datetime
- [ ] Convierte is_4wd a tipo booleano
- [ ] Asegura tipos de datos apropiados para el análisis

**Variables Derivadas**
- [ ] Calcula vehicle_age basado en model_year y date_posted
- [ ] Crea avg_mileage_per_year
- [ ] Transforma condition a escala numérica (0-5)

**Análisis por Tipo de Vehículo**
- [ ] **[OBLIGATORIO]** Calcula precio promedio por tipo de vehículo
- [ ] Presenta conteo de anuncios por tipo
- [ ] Identifica tipos más comunes (sedan, SUV)

### AVANZADO

**Imputación Contextual Avanzada**
- [ ] Aplica mediana por model_year para imputar odometer
- [ ] Usa moda por tipo de vehículo para imputar cylinders
- [ ] Usa estrategias contextuales agrupadas para datos faltantes
- [ ] Documenta efectividad de la imputación

**Eliminación Justificada de Datos**
- [ ] Identifica y elimina filas con datos críticos ausentes (model_year y odometer ambos NaN)
- [ ] Documenta criterios para eliminación de registros
- [ ] Calcula impacto de la eliminación (≈1%)

**Umbrales Estadísticos para Outliers**
- [ ] Establece límites basados en percentiles específicos (2%, 95%)
- [ ] Documenta metodología de selección de umbrales
- [ ] Valida efectividad del filtrado

**Análisis Comparativo Sedan vs SUV**
- [ ] Realiza análisis detallado de los dos tipos principales
- [ ] Crea matrices de dispersión separadas por tipo
- [ ] Calcula correlaciones específicas por tipo
- [ ] Identifica diferencias en factores de precio

**Análisis de Transmisión**
- [ ] Analiza precio por tipo de transmisión
- [ ] Crea boxplots comparativos
- [ ] Valida tamaño muestral (>50) para conclusiones

**Análisis de Color**
- [ ] Evalúa relación precio-color con muestras suficientes
- [ ] Excluye colores con pocas observaciones (<50)
- [ ] Presenta ranking de precios por color
- [ ] Compara medias y medianas por color

**Análisis de days_listed**
- [ ] Analiza distribución de días de publicación
- [ ] Identifica anuncios con tiempos atípicos (>100 días)
- [ ] Caracteriza vehículos con publicación prolongada

**Interpretación de Resultados**
- [ ] Documenta e interpreta coeficientes de correlación
- [ ] Establece significado práctico de las correlaciones
- [ ] Relaciona hallazgos con contexto de mercado automotriz

**Jerarquización de Factores**
- [ ] **[OBLIGATORIO]** Establece orden de importancia basado en correlaciones
- [ ] Identifica los 3 factores más influyentes en precio
- [ ] Presenta ranking consistente entre tipos de vehículo

**Conclusiones Específicas**
- [ ] **[OBLIGATORIO]** Presenta conclusiones detalladas sobre determinantes de precio
- [ ] Cuantifica impacto de cada factor con coeficientes
- [ ] Proporciona insights accionables para mercado automotriz
- [ ] Documenta diferencias entre sedan y SUV


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 3 criterios adicionales de los 27 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 8 criterios adicionales de los 27 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 16 criterios adicionales de los 27 no obligatorios


## Ejemplos de Cumplimiento

**Función de estandarización de modelos:**
```python
def replace_wrong_values(wrong_values, correct_value):
    for wrong_value in wrong_values:
        df['model'] = df['model'].replace(wrong_value, correct_value)

# Agrupar variantes de chevrolet silverado
chevrolet = ['chevrolet silverado 1500', 'chevrolet silverado 2500hd',
             'chevrolet silverado 3500hd']
replace_wrong_values(chevrolet, 'chevrolet silverado')

# Agrupar variantes de ford f-150
ford_150 = ['ford f150', 'ford f150 supercrew cab xlt']
replace_wrong_values(ford_150, 'ford f-150')
```

**Imputación contextual por grupos:**
```python
# Imputar odometer con mediana por año del modelo
odom_median = df.groupby('model_year')['odometer'].transform('median')
df['odometer'].fillna(odom_median, inplace=True)

# Imputar cylinders con moda por tipo de vehículo
cyl_mode = df.groupby('type')['cylinders'].transform(lambda x: x.mode()[0])
df['cylinders'].fillna(cyl_mode, inplace=True)

# Imputar model_year con moda por rango de millaje
model_year_mode = df.groupby('odom_range')['model_year'].transform(lambda x: x.mode()[0])
df['model_year'].fillna(model_year_mode, inplace=True)
```

**Detección de outliers con percentiles:**
```python
# Determinar límites usando percentiles
price_lim_inf = int(df['price'].quantile(0.02))  # 371
price_lim_sup = int(df['price'].quantile(0.95))  # 30,300
v_age_lim_sup = int(df['vehicle_age'].quantile(0.95))  # 20
odom_lim_sup = int(df['odometer'].quantile(0.95))  # 217,000

# Calcular porcentaje de outliers
outliers_pct = (df.query('price < @price_lim_inf or price > @price_lim_sup').shape[0]
                / len(df) * 100)
print(f"Porcentaje de outliers en precio: {outliers_pct:.2f}%")  # ~6.91%

# Crear DataFrame filtrado
df_with_limits = df.query('@price_lim_inf < price < @price_lim_sup and '
                          'vehicle_age < @v_age_lim_sup and '
                          'odometer < @odom_lim_sup')
```

**Análisis de correlaciones por tipo de vehículo:**
```python
# Análisis para Sedan
df_sedan = df_with_limits.query('type == "sedan"')
corr_sedan = df_sedan[['price', 'condition', 'odometer', 'vehicle_age']].corr()
print(corr_sedan['price'].sort_values(ascending=False))

# Resultado esperado:
# price          1.000000
# condition      0.310851
# odometer      -0.626363
# vehicle_age   -0.694672

# Análisis para SUV
df_suv = df_with_limits.query('type == "SUV"')
corr_suv = df_suv[['price', 'condition', 'odometer', 'vehicle_age']].corr()
print(corr_suv['price'].sort_values(ascending=False))

# Resultado esperado:
# price          1.000000
# condition      0.263642
# odometer      -0.597280
# vehicle_age   -0.668164
```

**Jerarquización de factores influyentes:**
```
"Los factores más influyentes en el precio de vehículos son:

**Para Sedan:**
1. vehicle_age (r = -0.69): La edad es el factor más determinante
2. odometer (r = -0.63): El millaje tiene fuerte impacto negativo
3. condition (r = 0.31): La condición influye positivamente

**Para SUV:**
1. vehicle_age (r = -0.67): Consistente con sedans
2. odometer (r = -0.60): Similar impacto que en sedans
3. condition (r = 0.26): Menor influencia que en sedans

**Conclusión:** En ambos tipos, el orden de influencia es:
1° Edad del vehículo (factor más importante)
2° Millaje del vehículo
3° Condición del vehículo"
```

**Análisis de color con filtrado de muestra:**
```python
# Verificar tamaño de muestra por color
color_counts = df_sedan.groupby('paint_color')['price'].count()
print(color_counts)

# Excluir colores con muestras pequeñas (<50)
df_sedan_filtered = df_sedan.query('paint_color not in ["orange", "purple", "yellow"]')

# Calcular media y mediana por color
color_stats = df_sedan_filtered.groupby('paint_color')['price'].agg(['mean', 'median'])
print(color_stats.sort_values('mean', ascending=False))

# Interpretación:
# "Colores con precios más altos: blanco ($7,846), negro ($7,758), rojo ($7,344)
#  Colores con precios más bajos: verde ($5,254), café ($5,530), azul ($6,841)"
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 10/10)
- **No identifica ni trata valores ausentes** en model_year, cylinders, odometer
- **No detecta outliers** o no filtra datos para análisis
- **No calcula correlaciones** entre precio y variables numéricas
- **No analiza por tipo de vehículo** o no identifica sedan/SUV como principales
- **No presenta conclusiones** sobre factores influyentes en precio
- Elimina más del 20% de datos sin justificación
- No crea variables derivadas básicas (vehicle_age)

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Errores Críticos en Tratamiento de Datos

1. **Eliminar todas las filas con valores ausentes**:
   - Incorrecto: `df.dropna()` elimina 60%+ de datos
   - Correcto: Imputar valores ausentes con estrategias contextuales
   - Consecuencia: Pérdida masiva de información valiosa

2. **Imputación global sin contexto**:
   - Incorrecto: `df['odometer'].fillna(df['odometer'].mean())` usa media global
   - Correcto: `df['odometer'].fillna(df.groupby('model_year')['odometer'].transform('median'))`
   - Consecuencia: Introduce sesgo, vehículos viejos con millaje irreal

3. **No estandarizar nombres de modelos**:
   - Incorrecto: Dejar 'chevrolet silverado 1500', 'chevrolet silverado 2500hd' separados
   - Correcto: Agrupar como 'chevrolet silverado'
   - Consecuencia: Fragmentación artificial de datos, análisis por modelo incorrecto

4. **No detectar outliers o usar métodos arbitrarios**:
   - Incorrecto: `df.query('price < 100000')` umbral sin justificación
   - Correcto: Usar percentiles documentados (2%, 95%)
   - Consecuencia: Retiene outliers extremos o elimina datos válidos

### Errores en Análisis

5. **No comparar distribuciones antes/después de filtrado**:
   - Incorrecto: Mostrar solo histogramas finales
   - Correcto: Visualizar lado a lado (antes/después)
   - Consecuencia: No demuestra efectividad de limpieza

6. **Calcular correlaciones sin filtrar outliers**:
   - Incorrecto: `df.corr()` con datos originales
   - Correcto: `df_with_limits.corr()` con datos filtrados
   - Consecuencia: Coeficientes distorsionados por valores extremos

7. **No analizar por tipo de vehículo**:
   - Incorrecto: Análisis global ignorando type
   - Correcto: Análisis separado para sedan y SUV
   - Consecuencia: Conclusiones genéricas, pierde insights específicos

8. **Interpretar correlaciones sin contexto**:
   - Incorrecto: "vehicle_age tiene correlación -0.69"
   - Correcto: "vehicle_age (r=-0.69) es el factor MÁS influyente, indica que a mayor edad, menor precio"
   - Consecuencia: Reporte meramente descriptivo sin interpretación de negocio

### Errores en Visualizaciones

9. **Analizar colores con muestras pequeñas**:
   - Incorrecto: Incluir colores con <10 observaciones en análisis
   - Correcto: Excluir colores con muestra insuficiente (<50)
   - Consecuencia: Conclusiones estadísticamente no significativas

10. **Boxplots sin verificar tamaño de muestra**:
    - Incorrecto: Crear boxplot por transmission sin verificar counts
    - Correcto: Verificar `df.groupby('transmission')['price'].count()` primero
    - Consecuencia: Comparaciones con grupos demasiado pequeños

### Errores de Tipos de Datos

11. **No convertir date_posted a datetime**:
    - Incorrecto: Dejar como string
    - Correcto: `pd.to_datetime(df['date_posted'], format='%Y-%m-%d')`
    - Consecuencia: No puede extraer year/month para calcular vehicle_age

12. **Tratar is_4wd como numérico en lugar de booleano**:
    - Incorrecto: Dejar como float (1.0, NaN)
    - Correcto: Convertir a bool después de fillna(0)
    - Consecuencia: Tipo de dato inapropiado para análisis categórico

### Errores en Variables Derivadas

13. **No crear vehicle_age correctamente**:
    - Incorrecto: `df['vehicle_age'] = 2019 - df['model_year']` usa año fijo
    - Correcto: `df['vehicle_age'] = df['year'] - df['model_year'] + 1` usa year de date_posted
    - Consecuencia: Cálculo incorrecto, no refleja edad real al momento del anuncio

14. **Transformar condition sin documentar escala**:
    - Incorrecto: Reemplazar con números sin explicar mapeo
    - Correcto: Documentar dict: new=5, like new=4, excellent=3, good=2, fair=1, salvage=0
    - Consecuencia: Escala arbitraria difícil de interpretar

### Errores en Conclusiones

15. **No jerarquizar factores por correlación**:
    - Incorrecto: Listar factores sin orden
    - Correcto: "1° vehicle_age (r=-0.69), 2° odometer (r=-0.63), 3° condition (r=0.31)"
    - Consecuencia: No identifica factor más importante

16. **Conclusiones sin cuantificación**:
    - Incorrecto: "El precio depende de la edad"
    - Correcto: "vehicle_age tiene el mayor impacto (r=-0.69), indicando relación negativa fuerte"
    - Consecuencia: Conclusión vaga sin evidencia estadística

17. **No comparar sedan vs SUV**:
    - Incorrecto: Conclusiones globales sin diferenciar tipos
    - Correcto: Análisis separado mostrando que patrones de correlación son consistentes
    - Consecuencia: Pierde oportunidad de insights comparativos

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
