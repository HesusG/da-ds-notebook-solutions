# Criterios de Evaluación: Proyecto 6 — Proyecto Integrado 1 (Videojuegos)

## Objetivo

Analizar datos históricos de ventas de videojuegos para identificar patrones de éxito, comparar plataformas y géneros por región, y probar hipótesis estadísticas para informar estrategias de marketing para 2017.

**Requisitos previos**: Completar SP1-SP5 (Python, pandas, data wrangling, análisis estadístico, pruebas de hipótesis).

**Competencias que desarrollarás**: Análisis exploratorio completo, limpieza de datos complejos, cálculo de métricas derivadas, análisis de ciclo de vida de productos, segmentación regional, correlaciones, visualizaciones avanzadas, pruebas de hipótesis, conclusiones de negocio

> **Nota**: Este es el primer proyecto integrado del bootcamp. Combina TODAS las habilidades aprendidas hasta ahora: limpieza de datos, análisis exploratorio, visualizaciones y pruebas de hipótesis estadísticas.

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Trabajas para la tienda online Ice que vende videojuegos a nivel mundial. Los datos disponibles incluyen reseñas de usuarios y expertos, géneros, plataformas y datos históricos de ventas hasta 2016. Tu objetivo es identificar patrones que determinen si un juego tiene éxito o no, para detectar proyectos prometedores y planificar campañas publicitarias para 2017.

## Instrucciones del proyecto

1. **Preparar los datos:**
   - Cargar y explorar el dataset
   - Convertir nombres de columnas a minúsculas
   - Manejar valores ausentes y tipos de datos
   - Calcular ventas globales (total_sales)
   - Filtrar datos relevantes (período de análisis)

2. **Analizar los datos:**
   - Evolución de lanzamientos por año
   - Ciclo de vida de plataformas
   - Plataformas más rentables
   - Impacto de reseñas en ventas (correlación)
   - Distribución de ventas por género

3. **Crear perfil de usuario por región:**
   - Top 5 plataformas por región (NA, EU, JP)
   - Top 5 géneros por región
   - Impacto del rating ESRB por región

4. **Probar hipótesis:**
   - H1: Calificaciones de usuarios Xbox One vs PC
   - H2: Calificaciones de usuarios Action vs Sports

## Descripción de los datos

- `Name`: nombre del juego
- `Platform`: plataforma (PS4, Xbox, PC, etc.)
- `Year_of_Release`: año de lanzamiento
- `Genre`: género del juego
- `NA_sales`, `EU_sales`, `JP_sales`, `Other_sales`: ventas por región (millones USD)
- `Critic_Score`: puntuación de críticos (0-100)
- `User_Score`: puntuación de usuarios (0-10, puede ser "tbd")
- `Rating`: clasificación ESRB (E, T, M, etc.)

## Clasificaciones ESRB

| Rating | Significado | Edad |
|--------|-------------|------|
| **E** | Everyone | Para todos |
| **E10+** | Everyone 10+ | 10 años o más |
| **T** | Teen | 13 años o más |
| **M** | Mature | 17 años o más |
| **AO** | Adults Only | Solo adultos (18+) |
| **RP** | Rating Pending | Pendiente de clasificar |
| **EC** | Early Childhood | Primera infancia |
| **K-A** | Kids to Adults | Niños a adultos (obsoleto) |

</details>

## Glosario de Términos Técnicos

**Ventas globales (total_sales/global_sales)**: Suma de ventas en todas las regiones (NA + EU + JP + Other).

**Ciclo de vida de plataforma**: Período desde el primer lanzamiento hasta el último, indicando longevidad en el mercado.

**ESRB Rating**: Entertainment Software Rating Board - Sistema de clasificación de videojuegos por edad.

**Correlación**: Medida estadística (-1 a 1) que indica la fuerza y dirección de la relación lineal entre dos variables.

**tbd (To Be Determined)**: Valor especial en user_score que indica calificación pendiente, debe tratarse como NaN.

**Cuota de mercado**: Porcentaje de ventas que representa una plataforma/género del total de su categoría.

**Outlier**: Valor atípico que se aleja significativamente del resto de los datos.

**Boxplot (diagrama de caja)**: Visualización que muestra la distribución de datos mediante cuartiles.

**Scatterplot (diagrama de dispersión)**: Visualización que muestra la relación entre dos variables numéricas.

**ttest_ind**: Prueba t de Student para comparar medias de dos grupos independientes.

**Prueba de Shapiro-Wilk**: Prueba para verificar si los datos siguen una distribución normal.

---

# Rúbrica de Evaluación por Secciones

---

## BÁSICO

### Checklist

**Carga y Exploración de Datos**
- [ ] **[OBLIGATORIO]** Carga correctamente el archivo CSV
- [ ] **[OBLIGATORIO]** Examina el DataFrame con info() y head()
- [ ] Usa describe() para estadísticas básicas
- [ ] Identifica tipos de datos incorrectos
- [ ] Identifica valores ausentes por columna

**Limpieza de Datos**
- [ ] **[OBLIGATORIO]** Convierte nombres de columnas a minúsculas
- [ ] **[OBLIGATORIO]** Maneja 'tbd' en user_score (reemplaza por NaN)
- [ ] **[OBLIGATORIO]** Convierte user_score a tipo numérico (float)
- [ ] Convierte year_of_release a int (manejando NaN)
- [ ] Identifica y maneja filas sin nombre o género

**Estructura del Código**
- [ ] **[OBLIGATORIO]** El código ejecuta sin errores de sintaxis
- [ ] **[OBLIGATORIO]** Todas las celdas están ejecutadas secuencialmente

---

<details>
<summary><strong>📋 Resultados Esperados - BÁSICO</strong></summary>

### Carga del archivo CSV

```python
# Cargar datos
df = pd.read_csv('/datasets/games.csv')
```

### Salida esperada: df.info()

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 16715 entries, 0 to 16714
Data columns (total 11 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   Name             16713 non-null  object
 1   Platform         16715 non-null  object
 2   Year_of_Release  16446 non-null  float64  ← Debería ser int
 3   Genre            16713 non-null  object
 4   NA_sales         16715 non-null  float64
 5   EU_sales         16715 non-null  float64
 6   JP_sales         16715 non-null  float64
 7   Other_sales      16715 non-null  float64
 8   Critic_Score     8137 non-null   float64
 9   User_Score       10014 non-null  object   ← Debería ser float
 10  Rating           9949 non-null   object
```

### Tabla: df.head()

| Name | Platform | Year_of_Release | Genre | NA_sales | EU_sales | JP_sales | Other_sales | Critic_Score | User_Score | Rating |
|------|----------|-----------------|-------|----------|----------|----------|-------------|--------------|------------|--------|
| Wii Sports | Wii | 2006.0 | Sports | 41.36 | 28.96 | 3.77 | 8.45 | 76.0 | 8 | E |
| Super Mario Bros. | NES | 1985.0 | Platform | 29.08 | 3.58 | 6.81 | 0.77 | NaN | NaN | NaN |
| Mario Kart Wii | Wii | 2008.0 | Racing | 15.68 | 12.76 | 3.79 | 3.29 | 82.0 | 8.3 | E |

### Salida esperada: df.describe()

| | Year_of_Release | NA_sales | EU_sales | JP_sales | Other_sales | Critic_Score |
|---|-----------------|----------|----------|----------|-------------|--------------|
| count | 16446 | 16715 | 16715 | 16715 | 16715 | 8137 |
| mean | 2006.48 | 0.26 | 0.15 | 0.08 | 0.05 | 68.97 |
| std | 5.88 | 0.81 | 0.50 | 0.31 | 0.19 | 13.94 |
| min | 1980 | 0.00 | 0.00 | 0.00 | 0.00 | 13.00 |
| max | 2016 | 41.36 | 28.96 | 10.22 | 10.57 | 98.00 |

### Resumen de problemas identificados

| Columna | Problema | Valores Ausentes | Solución |
|---------|----------|------------------|----------|
| `Name` | 2 valores NaN | 2/16715 (0.01%) | Eliminar filas |
| `Year_of_Release` | Tipo float (debería ser int) | 269/16715 (1.6%) | Convertir o mantener float |
| `Genre` | 2 valores NaN | 2/16715 (0.01%) | Eliminar filas |
| `Critic_Score` | Muchos NaN | 8578/16715 (51%) | Mantener NaN o filtrar en análisis |
| `User_Score` | Tipo object, contiene "tbd" | 6701/16715 (40%) | Reemplazar "tbd" → NaN, convertir a float |
| `Rating` | Valores NaN | 6766/16715 (40%) | Mantener NaN para análisis |

### Conversión de nombres de columnas a minúsculas

```python
# CORRECTO: Convertir a minúsculas
df.columns = df.columns.str.lower()

# O más completo:
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
```

**Resultado:**
```
['name', 'platform', 'year_of_release', 'genre', 'na_sales', 'eu_sales',
 'jp_sales', 'other_sales', 'critic_score', 'user_score', 'rating']
```

### Manejo de 'tbd' en user_score

#### Nota Metodológica: ¿Por qué "tbd" causa problemas?

La columna `user_score` contiene valores como "8", "8.3", "tbd", etc. Al ser de tipo `object`, Python no puede hacer operaciones numéricas.

```python
# Ver valores únicos
print(df['user_score'].unique())
# ['8', '8.3', 'tbd', '7.9', '8.5', nan, '7.3', ...]

# Contar cuántos "tbd" hay
print((df['user_score'] == 'tbd').sum())  # ~2424
```

**El problema:**
```python
# INCORRECTO: Intentar convertir directamente
df['user_score'] = df['user_score'].astype(float)
# ValueError: could not convert string to float: 'tbd'
```

**La solución:**
```python
# CORRECTO: Primero reemplazar 'tbd' por NaN, luego convertir
df['user_score'] = df['user_score'].replace('tbd', np.nan)
df['user_score'] = df['user_score'].astype(float)

# O en una sola línea:
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
```

### Verificación de valores únicos en columnas categóricas

```python
# Verificar plataformas
print(df['platform'].unique())
# ['Wii', 'NES', 'GB', 'DS', 'X360', 'PS3', 'PS2', 'SNES', 'GBA', 'PS4',
#  '3DS', 'N64', 'PS', 'XB', 'PC', '2600', 'PSP', 'XOne', 'WiiU', 'GC',
#  'GEN', 'DC', 'PSV', 'SAT', 'SCD', 'WS', 'NG', 'TG16', '3DO', 'GG', 'PCFX']

# Verificar géneros (12 géneros)
print(df['genre'].unique())
# ['Sports', 'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Misc',
#  'Shooter', 'Simulation', 'Action', 'Fighting', 'Adventure', 'Strategy']

# Verificar ratings ESRB
print(df['rating'].unique())
# ['E', 'M', 'T', 'E10+', nan, 'K-A', 'AO', 'EC', 'RP']
```

### Manejo de filas con name/genre ausentes

```python
# Ver filas con name ausente
df[df['name'].isna()]
# Solo 2 filas, ambas de la plataforma GEN (1993)

# Eliminar filas sin nombre (también eliminará las que no tienen género)
df = df[df['name'].notna()]
# O usando query:
df = df.query('name.notna()')
```

</details>

---

## INTERMEDIO

### Checklist

**Cálculos Derivados**
- [ ] **[OBLIGATORIO]** Calcula total_sales/global_sales (suma de todas las regiones)
- [ ] **[OBLIGATORIO]** Justifica período de análisis (ej: filtrar desde 2000 o últimos 5-10 años)
- [ ] Analiza cantidad de lanzamientos por año
- [ ] Identifica plataformas activas vs inactivas

**Análisis de Plataformas**
- [ ] **[OBLIGATORIO]** Identifica plataformas con mayores ventas globales
- [ ] **[OBLIGATORIO]** Analiza ciclo de vida de plataformas (duración)
- [ ] Crea gráficos de evolución de ventas por plataforma
- [ ] Identifica plataformas potencialmente rentables para 2017

**Análisis de Correlaciones**
- [ ] **[OBLIGATORIO]** Calcula correlación entre critic_score y ventas
- [ ] **[OBLIGATORIO]** Calcula correlación entre user_score y ventas
- [ ] Interpreta fuerza de las correlaciones (débil, moderada, fuerte)
- [ ] Visualiza relaciones con scatterplots

**Visualizaciones**
- [ ] **[OBLIGATORIO]** Crea boxplots de distribución de ventas por plataforma
- [ ] **[OBLIGATORIO]** Crea gráficos comparativos (barras, líneas)
- [ ] Los gráficos tienen títulos, etiquetas y leyendas claras
- [ ] Usa colores diferenciadores apropiados

---

<details>
<summary><strong>📋 Resultados Esperados - INTERMEDIO</strong></summary>

### Cálculo de ventas globales (total_sales)

```python
# Crear columna de ventas totales
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales'] + df['other_sales']

# Verificar
print(df['total_sales'].describe())
```

**Resultado esperado:**
```
count    16713.000000
mean         0.533935
std          1.548609
min          0.010000
25%          0.060000
50%          0.170000
75%          0.470000
max         82.540000
```

### Justificación del período de análisis

#### Nota Metodológica: ¿Por qué filtrar los datos?

**Problema:** Los datos van desde 1980 hasta 2016. Los juegos antiguos (NES, 2600) ya no son relevantes para predicciones de 2017.

**Análisis de lanzamientos por año:**
```python
df.groupby('year_of_release')['name'].count().plot(kind='bar', figsize=(15,5))
plt.title('Lanzamientos por Año')
plt.show()
```

**Criterios para filtrar:**

| Período | Justificación | Pros | Contras |
|---------|---------------|------|---------|
| **Desde 2000** | Época moderna de videojuegos | Suficientes datos, plataformas actuales | Incluye plataformas ya obsoletas |
| **Últimos 5 años (2012-2016)** | Datos más recientes | Más relevante para 2017 | Menos datos |
| **Últimos 10 años (2007-2016)** | Balance entre relevancia y cantidad | Incluye ciclos completos de PS3/X360 | Puede omitir tendencias |

```python
# Filtrar datos recientes (ejemplo: desde 2013)
df_recent = df[df['year_of_release'] >= 2013].copy()

# O últimos 5 años
df_recent = df[(df['year_of_release'] >= 2012) & (df['year_of_release'] <= 2016)].copy()
```

### Análisis de ciclo de vida de plataformas

```python
# Calcular duración de cada plataforma
platform_life = df.groupby('platform')['year_of_release'].agg(['min', 'max'])
platform_life['duration'] = platform_life['max'] - platform_life['min']
platform_life = platform_life.sort_values('duration', ascending=False)
```

**Tabla esperada: Top 10 plataformas por duración**

| Platform | min | max | duration |
|----------|-----|-----|----------|
| PC | 1985 | 2016 | 31 |
| PS | 1994 | 2016 | 22 |
| DS | 2004 | 2016 | 12 |
| PS2 | 2000 | 2011 | 11 |
| PSP | 2004 | 2015 | 11 |
| Wii | 2006 | 2016 | 10 |
| X360 | 2005 | 2016 | 11 |
| PS3 | 2006 | 2016 | 10 |

**Interpretación:** PC es la plataforma más longeva (31 años). Las consolas típicamente tienen ciclos de 5-10 años.

### Top plataformas por ventas globales

```python
# Ventas totales por plataforma
platform_sales = df.groupby('platform')['total_sales'].sum().sort_values(ascending=False)
print(platform_sales.head(10))
```

**Resultado esperado (DATOS REALES):**

| Platform | total_sales |
|----------|-------------|
| PS2 | 1255.77 |
| X360 | 971.42 |
| PS3 | 939.65 |
| Wii | 907.51 |
| DS | 806.12 |
| PS | 730.86 |
| GBA | 317.85 |
| PS4 | 314.14 |
| PSP | 294.05 |
| PC | 259.52 |

#### Gráfico SVG: Top 10 plataformas por ventas

<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="400" fill="white"/>
  <text x="300" y="25" text-anchor="middle" font-size="14" font-weight="bold">Top 10 Plataformas por Ventas Globales</text>
  <text x="15" y="200" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 200)">Ventas (millones USD)</text>
  <text x="300" y="385" text-anchor="middle" font-size="11">Plataforma</text>

  <!-- Ejes -->
  <line x1="70" y1="50" x2="70" y2="340" stroke="black" stroke-width="1"/>
  <line x1="70" y1="340" x2="570" y2="340" stroke="black" stroke-width="1"/>

  <!-- Etiquetas Y -->
  <text x="65" y="340" text-anchor="end" font-size="9">0</text>
  <text x="65" y="267" text-anchor="end" font-size="9">400</text>
  <text x="65" y="195" text-anchor="end" font-size="9">800</text>
  <text x="65" y="122" text-anchor="end" font-size="9">1200</text>
  <text x="65" y="50" text-anchor="end" font-size="9">1600</text>

  <!-- Barras (proporcionales a ventas) -->
  <!-- PS2: 1233 → altura ~224 -->
  <rect x="80" y="116" width="40" height="224" fill="#3498db"/>
  <!-- X360: 967 → altura ~175 -->
  <rect x="130" y="165" width="40" height="175" fill="#2ecc71"/>
  <!-- PS3: 949 → altura ~172 -->
  <rect x="180" y="168" width="40" height="172" fill="#e74c3c"/>
  <!-- Wii: 907 → altura ~165 -->
  <rect x="230" y="175" width="40" height="165" fill="#9b59b6"/>
  <!-- DS: 806 → altura ~146 -->
  <rect x="280" y="194" width="40" height="146" fill="#f39c12"/>
  <!-- PS: 727 → altura ~132 -->
  <rect x="330" y="208" width="40" height="132" fill="#1abc9c"/>
  <!-- GBA: 316 → altura ~57 -->
  <rect x="380" y="283" width="40" height="57" fill="#34495e"/>
  <!-- PS4: 314 → altura ~57 -->
  <rect x="430" y="283" width="40" height="57" fill="#e67e22"/>
  <!-- PSP: 292 → altura ~53 -->
  <rect x="480" y="287" width="40" height="53" fill="#95a5a6"/>
  <!-- PC: 259 → altura ~47 -->
  <rect x="530" y="293" width="40" height="47" fill="#d35400"/>

  <!-- Etiquetas X -->
  <text x="100" y="355" text-anchor="middle" font-size="9">PS2</text>
  <text x="150" y="355" text-anchor="middle" font-size="9">X360</text>
  <text x="200" y="355" text-anchor="middle" font-size="9">PS3</text>
  <text x="250" y="355" text-anchor="middle" font-size="9">Wii</text>
  <text x="300" y="355" text-anchor="middle" font-size="9">DS</text>
  <text x="350" y="355" text-anchor="middle" font-size="9">PS</text>
  <text x="400" y="355" text-anchor="middle" font-size="9">GBA</text>
  <text x="450" y="355" text-anchor="middle" font-size="9">PS4</text>
  <text x="500" y="355" text-anchor="middle" font-size="9">PSP</text>
  <text x="550" y="355" text-anchor="middle" font-size="9">PC</text>
</svg>

### Análisis de correlación: Reseñas vs Ventas

#### Nota Metodológica: ¿Cómo interpretar correlaciones?

| Valor | Interpretación |
|-------|----------------|
| 0.0 - 0.3 | Correlación débil |
| 0.3 - 0.7 | Correlación moderada |
| 0.7 - 1.0 | Correlación fuerte |

**Valores negativos:** Relación inversa (cuando uno sube, el otro baja).

```python
# Filtrar datos válidos (sin NaN)
df_corr = df.dropna(subset=['critic_score', 'user_score', 'total_sales'])

# Calcular correlaciones
corr_critic = df_corr['critic_score'].corr(df_corr['total_sales'])
corr_user = df_corr['user_score'].corr(df_corr['total_sales'])

print(f'Correlación critic_score vs ventas: {corr_critic:.3f}')
print(f'Correlación user_score vs ventas: {corr_user:.3f}')
```

**Resultados esperados (DATOS REALES):**
```
Correlación critic_score vs ventas: 0.2370 (débil positiva)
Correlación user_score vs ventas: 0.0886 (muy débil positiva)
```

**Interpretación:**
- Las reseñas de críticos tienen una relación DÉBIL con las ventas
- Las reseñas de usuarios tienen una relación MUY DÉBIL con las ventas
- Conclusión: Las reseñas NO son un buen predictor de éxito comercial

### Scatterplot: Critic Score vs Ventas

```python
plt.figure(figsize=(10, 6))
plt.scatter(df_corr['critic_score'], df_corr['total_sales'], alpha=0.3)
plt.xlabel('Puntuación de Críticos')
plt.ylabel('Ventas Globales (millones)')
plt.title(f'Relación entre Puntuación de Críticos y Ventas\nCorrelación: {corr_critic:.3f}')
plt.show()
```

#### Gráfico SVG: Scatterplot Critic Score vs Ventas

<svg viewBox="0 0 500 350" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="350" fill="white"/>
  <text x="250" y="20" text-anchor="middle" font-size="12" font-weight="bold">Critic Score vs Ventas Globales</text>
  <text x="250" y="35" text-anchor="middle" font-size="10" fill="gray">Correlación: 0.24 (débil)</text>

  <text x="15" y="175" text-anchor="middle" font-size="10" transform="rotate(-90, 15, 175)">Ventas (millones)</text>
  <text x="260" y="330" text-anchor="middle" font-size="10">Puntuación de Críticos</text>

  <!-- Ejes -->
  <line x1="60" y1="50" x2="60" y2="300" stroke="black" stroke-width="1"/>
  <line x1="60" y1="300" x2="460" y2="300" stroke="black" stroke-width="1"/>

  <!-- Etiquetas Y -->
  <text x="55" y="300" text-anchor="end" font-size="8">0</text>
  <text x="55" y="237" text-anchor="end" font-size="8">5</text>
  <text x="55" y="175" text-anchor="end" font-size="8">10</text>
  <text x="55" y="112" text-anchor="end" font-size="8">15</text>
  <text x="55" y="50" text-anchor="end" font-size="8">20+</text>

  <!-- Etiquetas X -->
  <text x="60" y="315" text-anchor="middle" font-size="8">0</text>
  <text x="160" y="315" text-anchor="middle" font-size="8">25</text>
  <text x="260" y="315" text-anchor="middle" font-size="8">50</text>
  <text x="360" y="315" text-anchor="middle" font-size="8">75</text>
  <text x="460" y="315" text-anchor="middle" font-size="8">100</text>

  <!-- Puntos dispersos (simulación de scatterplot con correlación débil) -->
  <!-- Grupo bajo (score 30-50, ventas bajas) -->
  <circle cx="140" cy="290" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="150" cy="285" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="145" cy="288" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="155" cy="282" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="160" cy="287" r="3" fill="#3498db" opacity="0.4"/>

  <!-- Grupo medio (score 60-80, ventas variables) -->
  <circle cx="280" cy="275" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="290" cy="260" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="300" cy="280" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="310" cy="250" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="320" cy="270" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="285" cy="240" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="295" cy="265" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="305" cy="255" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="315" cy="230" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="325" cy="275" r="3" fill="#3498db" opacity="0.4"/>

  <!-- Grupo alto (score 80-95, algunos éxitos) -->
  <circle cx="360" cy="250" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="370" cy="200" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="380" cy="240" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="390" cy="180" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="400" cy="220" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="365" cy="260" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="375" cy="150" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="385" cy="230" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="395" cy="100" r="3" fill="#3498db" opacity="0.4"/>
  <circle cx="405" cy="190" r="3" fill="#3498db" opacity="0.4"/>

  <!-- Outliers (éxitos masivos) -->
  <circle cx="300" cy="80" r="4" fill="#e74c3c" opacity="0.6"/>
  <circle cx="340" cy="90" r="4" fill="#e74c3c" opacity="0.6"/>
  <circle cx="380" cy="60" r="4" fill="#e74c3c" opacity="0.6"/>

  <!-- Línea de tendencia (débil positiva) -->
  <line x1="80" y1="285" x2="440" y2="220" stroke="#e74c3c" stroke-width="2" stroke-dasharray="5,5"/>
</svg>

### Boxplot: Distribución de ventas por plataforma

```python
# Filtrar plataformas principales
top_platforms = ['PS4', 'XOne', 'PS3', 'X360', 'PC', 'Wii', 'WiiU', '3DS']
df_top = df[df['platform'].isin(top_platforms)]

plt.figure(figsize=(12, 6))
df_top.boxplot(column='total_sales', by='platform')
plt.title('Distribución de Ventas por Plataforma')
plt.ylabel('Ventas Globales (millones)')
plt.suptitle('')  # Eliminar título automático
plt.show()
```

</details>

---

## AVANZADO

### Checklist

**Análisis por Género**
- [ ] **[OBLIGATORIO]** Identifica géneros más rentables globalmente
- [ ] Analiza tendencias de géneros por año
- [ ] Crea visualizaciones comparativas de géneros

**Perfil de Usuario por Región**
- [ ] **[OBLIGATORIO]** Identifica top 5 plataformas por región (NA, EU, JP)
- [ ] **[OBLIGATORIO]** Identifica top 5 géneros por región
- [ ] **[OBLIGATORIO]** Analiza impacto de rating ESRB por región
- [ ] Compara diferencias entre regiones
- [ ] Explica posibles razones de las diferencias culturales

**Pruebas de Hipótesis**
- [ ] **[OBLIGATORIO]** Formula H₀ y H₁ para Xbox One vs PC
- [ ] **[OBLIGATORIO]** Formula H₀ y H₁ para Action vs Sports
- [ ] **[OBLIGATORIO]** Define alpha (nivel de significancia)
- [ ] **[OBLIGATORIO]** Aplica ttest_ind correctamente
- [ ] Usa equal_var=False cuando corresponda
- [ ] Interpreta correctamente el p-value
- [ ] Concluye si se rechaza o no cada H₀

**Conclusiones**
- [ ] **[OBLIGATORIO]** Presenta conclusiones accionables para marketing
- [ ] Relaciona hallazgos con la pregunta de negocio
- [ ] Identifica limitaciones del análisis
- [ ] Propone recomendaciones específicas por región

---

<details>
<summary><strong>📋 Resultados Esperados - AVANZADO</strong></summary>

### Top 5 géneros más rentables globalmente

```python
genre_sales = df.groupby('genre')['total_sales'].sum().sort_values(ascending=False)
print(genre_sales.head(5))
```

**Resultado esperado (DATOS REALES):**

| Genre | total_sales |
|-------|-------------|
| Action | 1744.17 |
| Sports | 1331.27 |
| Shooter | 1052.45 |
| Role-Playing | 934.56 |
| Platform | 827.77 |

### Perfil de usuario por región: Top 5 plataformas

```python
# Top 5 plataformas por región
regions = ['na_sales', 'eu_sales', 'jp_sales']
for region in regions:
    print(f"\nTop 5 plataformas - {region}:")
    print(df.groupby('platform')[region].sum().sort_values(ascending=False).head(5))
```

**Resultados esperados:**

| Región | #1 | #2 | #3 | #4 | #5 |
|--------|----|----|----|----|-----|
| **NA** | X360 | PS2 | Wii | PS3 | DS |
| **EU** | PS2 | PS3 | X360 | Wii | PS |
| **JP** | DS | PS | PS2 | SNES | 3DS |

**Observaciones clave:**
- NA y EU: Preferencia por Xbox 360 y PlayStation
- JP: Preferencia marcada por consolas Nintendo (DS) y PlayStation portátiles
- Xbox prácticamente NO existe en Japón

#### Gráfico SVG: Comparación de preferencias por región

<svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="700" height="400" fill="white"/>
  <text x="350" y="25" text-anchor="middle" font-size="14" font-weight="bold">Top 5 Plataformas por Región</text>

  <!-- Leyenda -->
  <rect x="550" y="50" width="15" height="15" fill="#3498db"/>
  <text x="570" y="62" font-size="10">NA</text>
  <rect x="550" y="70" width="15" height="15" fill="#2ecc71"/>
  <text x="570" y="82" font-size="10">EU</text>
  <rect x="550" y="90" width="15" height="15" fill="#e74c3c"/>
  <text x="570" y="102" font-size="10">JP</text>

  <!-- NA -->
  <text x="120" y="60" text-anchor="middle" font-size="12" font-weight="bold">Norteamérica</text>
  <rect x="50" y="80" width="140" height="25" fill="#3498db" opacity="0.8"/>
  <text x="55" y="97" font-size="10" fill="white">1. X360</text>
  <rect x="50" y="110" width="130" height="25" fill="#3498db" opacity="0.7"/>
  <text x="55" y="127" font-size="10" fill="white">2. PS2</text>
  <rect x="50" y="140" width="120" height="25" fill="#3498db" opacity="0.6"/>
  <text x="55" y="157" font-size="10" fill="white">3. Wii</text>
  <rect x="50" y="170" width="110" height="25" fill="#3498db" opacity="0.5"/>
  <text x="55" y="187" font-size="10" fill="white">4. PS3</text>
  <rect x="50" y="200" width="100" height="25" fill="#3498db" opacity="0.4"/>
  <text x="55" y="217" font-size="10" fill="white">5. DS</text>

  <!-- EU -->
  <text x="350" y="60" text-anchor="middle" font-size="12" font-weight="bold">Europa</text>
  <rect x="280" y="80" width="140" height="25" fill="#2ecc71" opacity="0.8"/>
  <text x="285" y="97" font-size="10" fill="white">1. PS2</text>
  <rect x="280" y="110" width="130" height="25" fill="#2ecc71" opacity="0.7"/>
  <text x="285" y="127" font-size="10" fill="white">2. PS3</text>
  <rect x="280" y="140" width="120" height="25" fill="#2ecc71" opacity="0.6"/>
  <text x="285" y="157" font-size="10" fill="white">3. X360</text>
  <rect x="280" y="170" width="110" height="25" fill="#2ecc71" opacity="0.5"/>
  <text x="285" y="187" font-size="10" fill="white">4. Wii</text>
  <rect x="280" y="200" width="100" height="25" fill="#2ecc71" opacity="0.4"/>
  <text x="285" y="217" font-size="10" fill="white">5. PS</text>

  <!-- JP -->
  <text x="580" y="60" text-anchor="middle" font-size="12" font-weight="bold">Japón</text>
  <rect x="510" y="80" width="140" height="25" fill="#e74c3c" opacity="0.8"/>
  <text x="515" y="97" font-size="10" fill="white">1. DS</text>
  <rect x="510" y="110" width="120" height="25" fill="#e74c3c" opacity="0.7"/>
  <text x="515" y="127" font-size="10" fill="white">2. PS</text>
  <rect x="510" y="140" width="110" height="25" fill="#e74c3c" opacity="0.6"/>
  <text x="515" y="157" font-size="10" fill="white">3. PS2</text>
  <rect x="510" y="170" width="100" height="25" fill="#e74c3c" opacity="0.5"/>
  <text x="515" y="187" font-size="10" fill="white">4. SNES</text>
  <rect x="510" y="200" width="90" height="25" fill="#e74c3c" opacity="0.4"/>
  <text x="515" y="217" font-size="10" fill="white">5. 3DS</text>

  <!-- Nota -->
  <text x="350" y="280" text-anchor="middle" font-size="11" fill="#666">Nota: Xbox (X360/XOne) es prácticamente inexistente en Japón</text>
  <text x="350" y="300" text-anchor="middle" font-size="11" fill="#666">Japón prefiere consolas portátiles (DS, 3DS) y Nintendo</text>
</svg>

### Perfil de usuario por región: Top 5 géneros

```python
for region in ['na_sales', 'eu_sales', 'jp_sales']:
    print(f"\nTop 5 géneros - {region}:")
    print(df.groupby('genre')[region].sum().sort_values(ascending=False).head(5))
```

**Resultados esperados:**

| Región | #1 | #2 | #3 | #4 | #5 |
|--------|----|----|----|----|-----|
| **NA** | Action | Sports | Shooter | Platform | Misc |
| **EU** | Action | Sports | Shooter | Racing | Misc |
| **JP** | Role-Playing | Action | Sports | Platform | Misc |

**Observación clave:** Japón tiene preferencia marcada por **Role-Playing (RPG)**, mientras que NA y EU prefieren **Action** y **Shooter**.

### Impacto del rating ESRB por región

```python
# Ventas promedio por rating ESRB y región
for region in ['na_sales', 'eu_sales', 'jp_sales']:
    print(f"\nVentas promedio por rating - {region}:")
    print(df.groupby('rating')[region].mean().sort_values(ascending=False))
```

**Resultados esperados (ventas promedio):**

| Rating | NA | EU | JP |
|--------|----|----|-----|
| **E** | Alto | Alto | Medio |
| **M** | Alto | Alto | Bajo |
| **T** | Medio | Medio | Bajo |
| **E10+** | Medio | Medio | Bajo |

**Observación:** En Japón, muchos juegos tienen rating "RP" (pendiente) porque usan el sistema CERO en lugar de ESRB.

---

### PRUEBA DE HIPÓTESIS 1: Xbox One vs PC

#### Nota Metodológica: Proceso completo de prueba de hipótesis

**Paso 1: Formular las hipótesis ANTES de calcular**

```python
# HIPÓTESIS 1: Comparar calificaciones de usuarios entre Xbox One y PC
# H₀: Las calificaciones promedio de usuarios de XOne son IGUALES a las de PC
# H₁: Las calificaciones promedio de usuarios de XOne son DIFERENTES a las de PC
```

**Paso 2: Definir alpha ANTES de calcular**

```python
alpha = 0.05  # Nivel de significancia del 5%
```

**Paso 3: Preparar los datos**

```python
# Filtrar datos válidos (sin NaN ni 'tbd')
user_score_xone = df[(df['platform'] == 'XOne') &
                     (df['user_score'].notna())]['user_score'].astype(float)
user_score_pc = df[(df['platform'] == 'PC') &
                   (df['user_score'].notna())]['user_score'].astype(float)

print(f"Muestra XOne: {len(user_score_xone)} juegos")
print(f"Muestra PC: {len(user_score_pc)} juegos")
print(f"Media XOne: {user_score_xone.mean():.2f}")
print(f"Media PC: {user_score_pc.mean():.2f}")
```

**Resultado esperado (DATOS REALES):**
```
Muestra XOne: 182 juegos
Muestra PC: 770 juegos
Media XOne: 6.52
Media PC: 7.06
```

**Paso 4: (Opcional) Verificar normalidad con Shapiro-Wilk**

```python
from scipy.stats import shapiro

stat_xone, p_xone = shapiro(user_score_xone)
stat_pc, p_pc = shapiro(user_score_pc)

print(f"Shapiro XOne: p-value = {p_xone:.6f}")
print(f"Shapiro PC: p-value = {p_pc:.6f}")
```

**Resultado esperado:**
```
Shapiro XOne: p-value = 0.000015  ← No es normal (p < 0.05)
Shapiro PC: p-value = 0.000000  ← No es normal (p < 0.05)
```

> **Nota:** Aunque los datos NO siguen distribución normal, el t-test es robusto con muestras grandes (n > 30).

**Paso 5: Aplicar t-test**

```python
from scipy import stats as st

result = st.ttest_ind(user_score_xone, user_score_pc, equal_var=False)
print(f"Estadístico t: {result.statistic:.4f}")
print(f"p-value: {result.pvalue:.4f}")
```

**Resultado esperado (DATOS REALES):**
```
Estadístico t: ~-4.2
p-value: ~0.0001
```

**Paso 6: Interpretar y concluir**

```python
if result.pvalue < alpha:
    print("Se rechaza H₀: Las calificaciones SON significativamente diferentes")
else:
    print("No se rechaza H₀: NO hay evidencia de diferencia significativa")
```

**Conclusión Hipótesis 1:**
```
p-value = 0.0001 < 0.05
→ SE RECHAZA H₀
→ Las calificaciones de usuarios SON significativamente diferentes
  entre Xbox One (6.52) y PC (7.06)
→ Los juegos de PC tienen calificaciones más altas que los de Xbox One
```

---

### PRUEBA DE HIPÓTESIS 2: Action vs Sports

```python
# HIPÓTESIS 2: Comparar calificaciones de usuarios entre géneros Action y Sports
# H₀: Las calificaciones promedio de Action son IGUALES a las de Sports
# H₁: Las calificaciones promedio de Action son DIFERENTES a las de Sports

alpha = 0.05

# Preparar datos
user_score_action = df[(df['genre'] == 'Action') &
                       (df['user_score'].notna())]['user_score'].astype(float)
user_score_sports = df[(df['genre'] == 'Sports') &
                       (df['user_score'].notna())]['user_score'].astype(float)

print(f"Media Action: {user_score_action.mean():.2f}")
print(f"Media Sports: {user_score_sports.mean():.2f}")

# Aplicar t-test
result = st.ttest_ind(user_score_action, user_score_sports, equal_var=False)
print(f"p-value: {result.pvalue:.6f}")
```

**Resultado esperado (DATOS REALES):**
```
Muestra Action: 1830 juegos
Muestra Sports: 1103 juegos
Media Action: 7.05
Media Sports: 6.96
p-value: ~0.08 (mayor que 0.05)
```

**Conclusión Hipótesis 2:**
```
p-value ≈ 0.08 > 0.05
→ NO SE RECHAZA H₀
→ No hay evidencia suficiente para afirmar que las calificaciones
  de usuarios son diferentes entre Action y Sports
→ Las medias son muy similares (7.05 vs 6.96)
```

---

### Resumen de pruebas de hipótesis (DATOS REALES)

| Hipótesis | H₀ | p-value | Alpha | Decisión | Conclusión |
|-----------|-----|---------|-------|----------|------------|
| **H1: XOne vs PC** | μ_XOne = μ_PC | ~0.0001 | 0.05 | **Rechazar H₀** | PC tiene calificaciones mayores (7.06 vs 6.52) |
| **H2: Action vs Sports** | μ_Action = μ_Sports | ~0.08 | 0.05 | **No rechazar H₀** | Sin diferencia significativa (7.05 vs 6.96) |

---

### Conclusión General del Proyecto

```markdown
## Conclusiones para Marketing 2017

### Plataformas recomendadas
1. **PS4 y Xbox One** son las plataformas en crecimiento (2013-2016)
2. **PS3 y X360** están en declive pero aún generan ventas
3. **PC** tiene un mercado estable y longevo

### Diferencias regionales importantes
- **Norteamérica (NA)**: Xbox tiene fuerte presencia, Action y Shooter dominan
- **Europa (EU)**: Similar a NA pero con más preferencia por Racing
- **Japón (JP)**: Mercado MUY diferente:
  - Xbox prácticamente no existe
  - RPGs son el género favorito
  - Preferencia por consolas portátiles (3DS, Vita)

### Géneros más rentables
1. **Action** - Líder global
2. **Sports** - Fuerte en NA y EU
3. **Shooter** - Popular en occidente
4. **Role-Playing** - Domina en Japón

### Recomendaciones de marketing
1. Para NA/EU: Enfocarse en Action, Shooter, Sports para PS4/XOne
2. Para JP: Enfocarse en RPG para PS4/3DS, evitar Xbox
3. Los juegos con buenas críticas (>75) tienden a vender mejor
4. Las calificaciones de usuarios NO son buen predictor de ventas

### Limitaciones del análisis
- Datos hasta 2016, pueden no reflejar tendencias actuales
- Muchos valores NaN en critic_score y user_score
- Ventas pueden no incluir ventas digitales completas
```

</details>

---

## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS de BÁSICO: 8/8
  - Al menos 3 criterios adicionales de los no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 18/18
  - Al menos 8 criterios adicionales de los no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 28/28
  - Al menos 12 criterios adicionales de los no obligatorios

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook con celdas sin ejecutar
- **Imports dispersos en el notebook** (todos los imports deben estar en la primera celda)
- No calcula ventas globales (total_sales/global_sales)
- No maneja 'tbd' en user_score
- No realiza análisis por región
- No realiza pruebas de hipótesis
- No formula H₀ y H₁
- Código genera errores de sintaxis sin corregir
- No presenta conclusiones
- Plagio o copia directa sin comprensión

---

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

### Errores en Limpieza de Datos

1. **No manejar 'tbd' en user_score:**
   - Incorrecto: `df['user_score'].astype(float)` sin reemplazar 'tbd'
   - Correcto: `df['user_score'].replace('tbd', np.nan).astype(float)`
   - Consecuencia: ValueError al intentar convertir 'tbd' a float

2. **Eliminar todas las filas con NaN en lugar de columnas específicas:**
   - Incorrecto: `df.dropna()` elimina demasiados datos (~50% del dataset)
   - Correcto: `df.dropna(subset=['name', 'genre'])` solo donde es crítico
   - Consecuencia: Pérdida masiva de datos válidos

3. **No crear copia al filtrar (SettingWithCopyWarning):**
   - Incorrecto: `df_filtered = df[df['year'] >= 2000]`
   - Correcto: `df_filtered = df[df['year'] >= 2000].copy()`
   - Consecuencia: Warnings y posible comportamiento inesperado

### Errores en Cálculos

4. **No calcular total_sales antes del análisis:**
   - Incorrecto: Usar solo ventas regionales
   - Correcto: Crear columna sumando todas las regiones
   - Consecuencia: Análisis incompleto, no se puede comparar globalmente

5. **No justificar período de análisis:**
   - Incorrecto: Usar todos los datos desde 1980 sin explicación
   - Correcto: Filtrar período relevante (ej: desde 2000) con justificación
   - Consecuencia: Datos antiguos sesgan el análisis para predicciones 2017

### Errores en Correlaciones

6. **Calcular correlación sin eliminar NaN:**
   - Incorrecto: `df['critic_score'].corr(df['total_sales'])` con NaN
   - Correcto: Filtrar con `dropna(subset=['critic_score', 'total_sales'])`
   - Consecuencia: Resultado puede ser NaN o incorrecto

7. **Malinterpretar fuerza de correlación:**
   - Incorrecto: "Correlación de 0.24 es fuerte"
   - Correcto: 0-0.3 débil, 0.3-0.7 moderada, 0.7-1.0 fuerte
   - Consecuencia: Conclusiones erróneas sobre relaciones

### Errores en Análisis Regional

8. **No calcular porcentajes para comparar regiones:**
   - Incorrecto: Comparar valores absolutos entre regiones
   - Correcto: Calcular cuota de mercado (% del total)
   - Consecuencia: Comparaciones sesgadas por tamaño de mercado

9. **Ignorar diferencias culturales en conclusiones:**
   - Incorrecto: Asumir mismas preferencias en todas las regiones
   - Correcto: Notar diferencias (ej: RPG dominante en Japón, Xbox inexistente)
   - Consecuencia: Recomendaciones de marketing inadecuadas

### Errores en Pruebas de Hipótesis

10. **No filtrar datos antes del t-test:**
    - Incorrecto: `st.ttest_ind(df['user_score'], ...)` con NaN
    - Correcto: Usar `.dropna()` antes de la prueba
    - Consecuencia: Resultados incorrectos o errores

11. **Confundir plataformas en hipótesis:**
    - Incorrecto: Filtrar por 'Xbox' cuando se pide 'XOne' (Xbox One)
    - Correcto: Verificar nombre exacto en datos (`df['platform'].unique()`)
    - Consecuencia: Prueba realizada con datos incorrectos

12. **No formular hipótesis antes de la prueba:**
    - Incorrecto: Correr test y luego decidir qué significan los resultados
    - Correcto: Definir H₀, H₁ y alpha ANTES de calcular
    - Consecuencia: Interpretación sesgada (p-hacking)

13. **Interpretar p-value incorrectamente:**
    - Incorrecto: "p = 0.13, se rechaza H₀ porque es positivo"
    - Correcto: "p = 0.13 > 0.05, NO se rechaza H₀"
    - Consecuencia: Conclusión completamente opuesta

### Errores en Conclusiones

14. **Conclusiones genéricas sin datos:**
    - Incorrecto: "Los juegos de acción venden bien"
    - Correcto: "Action genera $1,745M globalmente, siendo el género #1"
    - Consecuencia: Recomendaciones vagas, no accionables

15. **No conectar análisis con pregunta de negocio:**
    - Incorrecto: Solo reportar estadísticas
    - Correcto: Recomendar plataformas/géneros específicos para marketing 2017
    - Consecuencia: Análisis sin valor práctico

---

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
