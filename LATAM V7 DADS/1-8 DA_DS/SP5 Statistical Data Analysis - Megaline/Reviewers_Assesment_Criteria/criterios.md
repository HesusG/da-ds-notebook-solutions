# Criterios de Evaluación: Proyecto 5 — Análisis Estadístico (Megaline)

## Objetivo

Analizar el comportamiento de clientes de telecomunicaciones y determinar qué tarifa de prepago (Surf vs Ultimate) genera más ingresos, aplicando análisis estadístico descriptivo, visualizaciones y pruebas de hipótesis.

**Requisitos previos**: Completar SP1-SP4 (Python básico, funciones, pandas, data wrangling).

**Competencias que desarrollarás**: Carga y fusión de múltiples DataFrames, conversión de tipos (datetime), agregación con groupby/pivot_table, cálculo de ingresos con lógica de negocio, estadística descriptiva (media, varianza), visualizaciones (histogramas, boxplots, barras), pruebas de hipótesis (t-test), interpretación de resultados estadísticos

> **Nota**: Este proyecto es uno de los más complejos del bootcamp. Requiere dominar múltiples técnicas: merge de DataFrames, lógica de negocio para cálculo de ingresos, y pruebas de hipótesis estadísticas.

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece dos tarifas de prepago: Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para ajustar el presupuesto de publicidad.

Tienes datos de 500 clientes: quiénes son, de dónde son, qué tarifa usan, y su uso de llamadas, mensajes e internet en 2018.

## Instrucciones del proyecto

1. **Preparar los datos:**
   - Cargar 5 archivos CSV (calls, messages, internet, plans, users)
   - Convertir fechas a datetime
   - Corregir tipos de datos
   - Enriquecer datos (extraer mes, redondear minutos/GB)

2. **Agregar datos por usuario:**
   - Calcular uso mensual por usuario (llamadas, mensajes, internet)
   - Fusionar todos los DataFrames
   - Calcular ingresos mensuales por usuario

3. **Analizar comportamiento:**
   - Estadísticas descriptivas por plan
   - Visualizaciones comparativas
   - Conclusiones sobre diferencias de uso

4. **Probar hipótesis:**
   - Hipótesis 1: Ingresos diferentes entre planes Surf y Ultimate
   - Hipótesis 2: Ingresos diferentes NY-NJ vs otras regiones

## Descripción de los datos

**plans.csv:**
- `plan_name`: nombre del plan (surf, ultimate)
- `usd_monthly_pay`: tarifa mensual
- `minutes_included`, `messages_included`, `mb_per_month_included`: límites incluidos
- `usd_per_minute`, `usd_per_message`, `usd_per_gb`: costos adicionales

**users.csv:**
- `user_id`: identificador único
- `plan`: plan contratado
- `reg_date`, `churn_date`: fechas de registro y baja
- `city`: ciudad del usuario

**calls.csv, messages.csv, internet.csv:**
- Registros de uso individual por usuario y fecha

## Tarifas de los planes

| Plan | Tarifa mensual | Minutos incluidos | Mensajes incluidos | GB incluidos | $/min extra | $/msg extra | $/GB extra |
|------|----------------|-------------------|--------------------|--------------| ------------|-------------|------------|
| **Surf** | $20 | 500 | 50 | 15 | $0.03 | $0.03 | $10 |
| **Ultimate** | $70 | 3000 | 1000 | 30 | $0.01 | $0.01 | $7 |

</details>

## Glosario de Términos Técnicos

**merge()**: Método de pandas para combinar DataFrames basándose en columnas comunes (similar a JOIN en SQL).

**groupby()**: Método para agrupar datos y aplicar funciones de agregación (sum, count, mean).

**pivot_table()**: Alternativa a groupby que permite crear tablas resumen con múltiples agregaciones.

**agg()**: Método para aplicar múltiples funciones de agregación simultáneamente.

**to_datetime()**: Función de pandas para convertir strings a tipo datetime.

**dt.month / dt.to_period('M')**: Accesor para extraer componentes de fecha (mes, año, etc.).

**np.ceil()**: Función de NumPy para redondear hacia arriba al entero más cercano.

**fillna()**: Método para reemplazar valores NaN con un valor específico.

**how='outer'**: Parámetro de merge que conserva todas las filas de ambos DataFrames (no pierde datos).

**Media (mean)**: Promedio aritmético de un conjunto de valores.

**Varianza (var)**: Medida de dispersión que indica qué tan alejados están los valores de la media.

**Desviación estándar (std)**: Raíz cuadrada de la varianza, en las mismas unidades que los datos.

**Hipótesis nula (H₀)**: Afirmación de que no hay diferencia o efecto significativo.

**Hipótesis alternativa (H₁)**: Afirmación de que sí hay diferencia o efecto significativo.

**Valor p (p-value)**: Probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo H₀ verdadera.

**Nivel de significancia (α / alpha)**: Umbral para rechazar H₀, típicamente 0.05 (5%).

**t-test (ttest_ind)**: Prueba estadística para comparar medias de dos grupos independientes.

**Prueba de Levene**: Prueba para verificar igualdad de varianzas antes de aplicar t-test.

---

# Rúbrica de Evaluación por Secciones

---

## BÁSICO

### Checklist

**Carga de Datos**
- [ ] **[OBLIGATORIO]** Carga correctamente los 5 archivos CSV
- [ ] **[OBLIGATORIO]** Examina cada DataFrame con info() y head()
- [ ] Identifica tipos de datos incorrectos
- [ ] Identifica valores ausentes

**Conversión de Fechas**
- [ ] **[OBLIGATORIO]** Convierte columnas de fecha a datetime
- [ ] Usa pd.to_datetime() correctamente
- [ ] Extrae mes de las fechas para análisis mensual

**Estructura del Código**
- [ ] **[OBLIGATORIO]** El código ejecuta sin errores
- [ ] **[OBLIGATORIO]** Todas las celdas están ejecutadas secuencialmente

---

<details>
<summary><strong>📋 Resultados Esperados - BÁSICO</strong></summary>

### Carga de los 5 archivos CSV

```python
# Cargar los 5 DataFrames
calls    = pd.read_csv('/datasets/megaline_calls.csv')
internet = pd.read_csv('/datasets/megaline_internet.csv')
messages = pd.read_csv('/datasets/megaline_messages.csv')
plans    = pd.read_csv('/datasets/megaline_plans.csv')
users    = pd.read_csv('/datasets/megaline_users.csv')
```

### Salida esperada: plans.info()

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 8 columns):
 #   Column                 Non-Null Count  Dtype
---  ------                 --------------  -----
 0   messages_included      2 non-null      int64
 1   mb_per_month_included  2 non-null      int64
 2   minutes_included       2 non-null      int64
 3   usd_monthly_pay        2 non-null      int64
 4   usd_per_gb             2 non-null      int64
 5   usd_per_message        2 non-null      float64
 6   usd_per_minute         2 non-null      float64
 7   plan_name              2 non-null      object
```

### Tabla: plans.head()

| messages_included | mb_per_month_included | minutes_included | usd_monthly_pay | usd_per_gb | usd_per_message | usd_per_minute | plan_name |
|-------------------|----------------------|------------------|-----------------|------------|-----------------|----------------|-----------|
| 50 | 15360 | 500 | 20 | 10 | 0.03 | 0.03 | surf |
| 1000 | 30720 | 3000 | 70 | 7 | 0.01 | 0.01 | ultimate |

### Salida esperada: users.info()

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   user_id     500 non-null    int64
 1   first_name  500 non-null    object
 2   last_name   500 non-null    object
 3   age         500 non-null    int64
 4   city        500 non-null    object
 5   reg_date    500 non-null    object   ← DEBE CONVERTIRSE A DATETIME
 6   plan        500 non-null    object
 7   churn_date  34 non-null     object   ← DEBE CONVERTIRSE A DATETIME
```

### Salida esperada: calls.info()

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 137735 entries, 0 to 137734
Data columns (total 4 columns):
 #   Column     Non-Null Count   Dtype
---  ------     --------------   -----
 0   id         137735 non-null  object
 1   user_id    137735 non-null  int64
 2   call_date  137735 non-null  object   ← DEBE CONVERTIRSE A DATETIME
 3   duration   137735 non-null  float64  ← DEBE REDONDEARSE HACIA ARRIBA
```

### Salida esperada: internet.info()

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 104825 entries, 0 to 104824
Data columns (total 4 columns):
 #   Column        Non-Null Count   Dtype
---  ------        --------------   -----
 0   id            104825 non-null  object
 1   user_id       104825 non-null  int64
 2   session_date  104825 non-null  object   ← DEBE CONVERTIRSE A DATETIME
 3   mb_used       104825 non-null  float64  ← DEBE CONVERTIRSE A GB
```

### Conversión de fechas a datetime

```python
# Convertir fechas en calls
calls['call_date'] = pd.to_datetime(calls['call_date'], format='%Y-%m-%d')

# Convertir fechas en messages
messages['message_date'] = pd.to_datetime(messages['message_date'], format='%Y-%m-%d')

# Convertir fechas en internet
internet['session_date'] = pd.to_datetime(internet['session_date'], format='%Y-%m-%d')

# Convertir fechas en users
users['reg_date'] = pd.to_datetime(users['reg_date'], format='%Y-%m-%d')
users['churn_date'] = pd.to_datetime(users['churn_date'], format='%Y-%m-%d')
```

### Extracción del mes (dos opciones válidas)

```python
# OPCIÓN 1: Solo mes (funciona si todos los datos son del mismo año)
calls['month'] = calls['call_date'].dt.month

# OPCIÓN 2: Año-mes (más robusta, recomendada)
calls['month_year'] = calls['call_date'].dt.to_period('M').astype(str)
```

### Resumen de problemas a identificar

| DataFrame | Problema | Solución |
|-----------|----------|----------|
| **calls** | `call_date` es object | `pd.to_datetime()` |
| **calls** | `duration` tiene decimales | `np.ceil()` |
| **calls** | Hay llamadas con duration=0 | Eliminar (opcional) |
| **messages** | `message_date` es object | `pd.to_datetime()` |
| **internet** | `session_date` es object | `pd.to_datetime()` |
| **internet** | `mb_used` debe ser GB | Dividir entre 1024 + ceil |
| **users** | `reg_date` es object | `pd.to_datetime()` |
| **users** | `churn_date` es object | `pd.to_datetime()` |

</details>

---

## INTERMEDIO

### Checklist

**Preprocesamiento de Datos**
- [ ] **[OBLIGATORIO]** Redondea minutos de llamadas hacia arriba (ceil)
- [ ] **[OBLIGATORIO]** Convierte MB a GB y redondea hacia arriba
- [ ] Elimina o maneja llamadas con duración 0
- [ ] Maneja valores NaN apropiadamente (fillna con 0 para uso)

**Agregación de Datos**
- [ ] **[OBLIGATORIO]** Agrupa datos por usuario y mes usando groupby
- [ ] **[OBLIGATORIO]** Calcula total de minutos, mensajes y GB por usuario/mes
- [ ] Usa merge/join para combinar DataFrames
- [ ] Usa how='outer' para no perder datos de usuarios sin actividad

**Cálculo de Ingresos**
- [ ] **[OBLIGATORIO]** Implementa función para calcular ingreso mensual
- [ ] **[OBLIGATORIO]** Aplica lógica correcta: tarifa base + excedentes
- [ ] Calcula excedentes solo cuando se supera el límite incluido
- [ ] Multiplica excedentes por el precio correcto de cada plan

**Visualizaciones Básicas**
- [ ] **[OBLIGATORIO]** Crea histogramas de distribución por plan
- [ ] **[OBLIGATORIO]** Crea gráficos de barras comparativos por mes
- [ ] Los gráficos tienen títulos y etiquetas claras

---

<details>
<summary><strong>📋 Resultados Esperados - INTERMEDIO</strong></summary>

### Redondear minutos hacia arriba

#### Nota Metodológica: ¿Por qué redondear hacia arriba?

**Lógica de negocio:** Las compañías telefónicas cobran por **minuto completo**. Si una llamada dura 8.52 minutos, se cobra como 9 minutos.

```python
# INCORRECTO: round() redondea al más cercano
calls['duration'] = round(calls['duration'])  # 8.52 → 9, pero 8.49 → 8

# CORRECTO: ceil() siempre redondea hacia arriba
calls['duration'] = np.ceil(calls['duration'])  # 8.52 → 9, 8.49 → 9
```

**Antes del redondeo:**
```
duration: min=0.00, max=37.60, mean=6.75
```

**Después del redondeo (y eliminar duration=0):**
```
duration: min=1.0, max=38.0, mean=8.88
```

### Eliminar llamadas con duración 0 (opcional pero recomendado)

```python
# Verificar cuántas llamadas tienen duración 0
print((calls['duration'] == 0).sum())  # ~26,834 llamadas

# Eliminar llamadas con duración 0
calls = calls[calls['duration'] != 0]
```

### Convertir MB a GB y redondear

#### Nota Metodológica: ¿Por qué redondear GB hacia arriba?

**Lógica de negocio:** Se cobra por **GB completo**. Si usaste 1901.47 MB (1.86 GB), se cobra como 2 GB.

```python
# INCORRECTO: Solo dividir (quedará como decimal)
internet['gb_used'] = internet['mb_used'] / 1024  # 1901.47 → 1.86

# CORRECTO: Dividir Y redondear hacia arriba
internet['gb_used'] = np.ceil(internet['mb_used'] / 1024)  # 1901.47 → 2.0
```

> **IMPORTANTE**: El redondeo de GB debe hacerse **después de agregar por mes**, no por sesión individual.

### Agregación por usuario y mes

#### Agregar llamadas

```python
# SOLUCIÓN 1: groupby básico (dos pasos)
total_minutes = calls.groupby(['user_id', 'month_year'])['duration'].sum().reset_index()
total_minutes.rename(columns={'duration': 'minutes_used'}, inplace=True)

call_counts = calls.groupby(['user_id', 'month_year'])['duration'].count().reset_index()
call_counts.rename(columns={'duration': 'calls_made'}, inplace=True)

month_calls = pd.merge(total_minutes, call_counts, on=['user_id', 'month_year'])

# SOLUCIÓN 2: groupby + agg (un paso)
month_calls = calls.groupby(['user_id', 'month_year']).agg(
    minutes_used=('duration', 'sum'),
    calls_made=('duration', 'count')
).reset_index()

# SOLUCIÓN 3: pivot_table
month_calls = calls.pivot_table(
    index=['user_id', 'month_year'],
    values='duration',
    aggfunc=['sum', 'count']
).reset_index()
month_calls.columns = ['user_id', 'month_year', 'minutes_used', 'calls_made']
```

#### Tabla esperada: month_calls.head()

| user_id | month_year | minutes_used | calls_made |
|---------|------------|--------------|------------|
| 1000 | 2018-12 | 124.0 | 16 |
| 1001 | 2018-08 | 182.0 | 22 |
| 1001 | 2018-09 | 315.0 | 38 |

#### Agregar mensajes

```python
month_mess = messages.groupby(['user_id', 'month_year'])['id'].count().reset_index()
month_mess.rename(columns={'id': 'num_mess'}, inplace=True)
```

#### Agregar internet (con redondeo de GB)

```python
# Primero: sumar MB por usuario y mes
month_int = internet.groupby(['user_id', 'month_year'])['mb_used'].sum().reset_index()

# Después: convertir a GB y redondear hacia arriba
month_int['gb_used'] = np.ceil(month_int['mb_used'] / 1024)
```

### Fusión de DataFrames

#### Nota Metodológica: ¿Por qué usar how='outer'?

**Problema:** Si un usuario no hizo llamadas en un mes pero sí envió mensajes, un `merge` normal (inner) lo perdería.

**Solución:** Usar `how='outer'` conserva todas las combinaciones usuario-mes de cualquier DataFrame.

```python
# CORRECTO: how='outer' no pierde datos
df_monthly = month_calls.merge(month_mess, on=['user_id', 'month_year'], how='outer')
df_monthly = df_monthly.merge(month_int, on=['user_id', 'month_year'], how='outer')

# INCORRECTO: merge sin how (default='inner') pierde datos
df_monthly = month_calls.merge(month_mess, on=['user_id', 'month_year'])  # ¡PIERDE DATOS!
```

### Rellenar NaN con 0

```python
# Después del merge, habrá NaN donde un usuario no usó un servicio
df_monthly.fillna(0, inplace=True)
```

**Antes de fillna:**
```
minutes_used  2256 non-null   ← faltan 37 registros
num_mess      1806 non-null   ← faltan 487 registros
gb_used       2277 non-null   ← faltan 16 registros
```

**Después de fillna:**
```
minutes_used  2293 non-null
num_mess      2293 non-null
gb_used       2293 non-null
```

### Añadir información del plan

```python
# Añadir plan del usuario
df_monthly = df_monthly.merge(users[['user_id', 'city', 'plan']], on='user_id', how='left')

# Añadir tarifas del plan
df_monthly = df_monthly.merge(plans, how='left', left_on='plan', right_on='plan_name')
```

### Cálculo de ingresos mensuales

#### Nota Metodológica: Lógica de negocio para calcular ingresos

**Fórmula:**
```
Ingreso = Tarifa base + Excedente minutos + Excedente mensajes + Excedente GB
```

**Donde:**
```
Excedente X = max(0, usado - incluido) × precio_extra
```

#### Función de cálculo

```python
def calculate_revenue(row):
    # Tarifa base del plan
    income = row['usd_monthly_pay']

    # Excedente de minutos (solo si supera el límite)
    if row['minutes_used'] > row['minutes_included']:
        income += (row['minutes_used'] - row['minutes_included']) * row['usd_per_minute']

    # Excedente de mensajes
    if row['num_mess'] > row['messages_included']:
        income += (row['num_mess'] - row['messages_included']) * row['usd_per_message']

    # Excedente de GB
    if row['gb_used'] > row['gb_per_month']:
        income += (row['gb_used'] - row['gb_per_month']) * row['usd_per_gb']

    return income

# Aplicar función a cada fila
df_monthly['income'] = df_monthly.apply(calculate_revenue, axis=1)
```

#### Ejemplo de cálculo manual (Plan Surf)

| Usuario | minutos_used | num_mess | gb_used | Cálculo |
|---------|--------------|----------|---------|---------|
| 1001 | 393 | 53 | 22 | Base: $20 |
| | | | | Min: 393 < 500 → $0 |
| | | | | Msg: 53 - 50 = 3 × $0.03 = $0.09 |
| | | | | GB: 22 - 15 = 7 × $10 = $70 |
| | | | | **Total: $90.09** |

### Histograma: Distribución de minutos por plan

```python
df_monthly[df_monthly['plan'] == 'surf']['minutes_used'].plot(kind='hist', bins=50, alpha=0.7, label='Surf')
df_monthly[df_monthly['plan'] == 'ultimate']['minutes_used'].plot(kind='hist', bins=50, alpha=0.7, label='Ultimate')
plt.xlabel('Minutos Usados')
plt.ylabel('Frecuencia')
plt.title('Distribución de Minutos por Plan')
plt.legend()
plt.show()
```

#### Gráfico SVG: Histograma de minutos por plan

<svg viewBox="0 0 600 350" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="350" fill="white"/>
  <text x="300" y="25" text-anchor="middle" font-size="14" font-weight="bold">Distribución de Minutos Usados por Plan</text>
  <text x="15" y="175" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 175)">Frecuencia</text>
  <text x="300" y="335" text-anchor="middle" font-size="11">Minutos Usados</text>

  <!-- Leyenda -->
  <rect x="450" y="45" width="15" height="15" fill="#1f77b4" opacity="0.7"/>
  <text x="470" y="57" font-size="10">Surf</text>
  <rect x="450" y="65" width="15" height="15" fill="#ff7f0e" opacity="0.7"/>
  <text x="470" y="77" font-size="10">Ultimate</text>

  <!-- Ejes -->
  <line x1="60" y1="50" x2="60" y2="300" stroke="black" stroke-width="1"/>
  <line x1="60" y1="300" x2="550" y2="300" stroke="black" stroke-width="1"/>

  <!-- Etiquetas eje Y -->
  <text x="55" y="300" text-anchor="end" font-size="9">0</text>
  <text x="55" y="237" text-anchor="end" font-size="9">50</text>
  <text x="55" y="175" text-anchor="end" font-size="9">100</text>
  <text x="55" y="112" text-anchor="end" font-size="9">150</text>
  <text x="55" y="50" text-anchor="end" font-size="9">200</text>

  <!-- Etiquetas eje X -->
  <text x="60" y="315" text-anchor="middle" font-size="9">0</text>
  <text x="158" y="315" text-anchor="middle" font-size="9">300</text>
  <text x="256" y="315" text-anchor="middle" font-size="9">600</text>
  <text x="354" y="315" text-anchor="middle" font-size="9">900</text>
  <text x="452" y="315" text-anchor="middle" font-size="9">1200</text>
  <text x="550" y="315" text-anchor="middle" font-size="9">1500</text>

  <!-- Barras Surf (azul) - distribución con pico ~400-500 -->
  <rect x="70" y="270" width="15" height="30" fill="#1f77b4" opacity="0.7"/>
  <rect x="88" y="250" width="15" height="50" fill="#1f77b4" opacity="0.7"/>
  <rect x="106" y="220" width="15" height="80" fill="#1f77b4" opacity="0.7"/>
  <rect x="124" y="180" width="15" height="120" fill="#1f77b4" opacity="0.7"/>
  <rect x="142" y="140" width="15" height="160" fill="#1f77b4" opacity="0.7"/>
  <rect x="160" y="100" width="15" height="200" fill="#1f77b4" opacity="0.7"/>
  <rect x="178" y="80" width="15" height="220" fill="#1f77b4" opacity="0.7"/>
  <rect x="196" y="110" width="15" height="190" fill="#1f77b4" opacity="0.7"/>
  <rect x="214" y="150" width="15" height="150" fill="#1f77b4" opacity="0.7"/>
  <rect x="232" y="190" width="15" height="110" fill="#1f77b4" opacity="0.7"/>
  <rect x="250" y="220" width="15" height="80" fill="#1f77b4" opacity="0.7"/>
  <rect x="268" y="250" width="15" height="50" fill="#1f77b4" opacity="0.7"/>
  <rect x="286" y="270" width="15" height="30" fill="#1f77b4" opacity="0.7"/>
  <rect x="304" y="280" width="15" height="20" fill="#1f77b4" opacity="0.7"/>
  <rect x="322" y="288" width="15" height="12" fill="#1f77b4" opacity="0.7"/>

  <!-- Barras Ultimate (naranja) - distribución similar pero desplazada -->
  <rect x="75" y="275" width="15" height="25" fill="#ff7f0e" opacity="0.7"/>
  <rect x="93" y="255" width="15" height="45" fill="#ff7f0e" opacity="0.7"/>
  <rect x="111" y="225" width="15" height="75" fill="#ff7f0e" opacity="0.7"/>
  <rect x="129" y="185" width="15" height="115" fill="#ff7f0e" opacity="0.7"/>
  <rect x="147" y="145" width="15" height="155" fill="#ff7f0e" opacity="0.7"/>
  <rect x="165" y="115" width="15" height="185" fill="#ff7f0e" opacity="0.7"/>
  <rect x="183" y="95" width="15" height="205" fill="#ff7f0e" opacity="0.7"/>
  <rect x="201" y="125" width="15" height="175" fill="#ff7f0e" opacity="0.7"/>
  <rect x="219" y="165" width="15" height="135" fill="#ff7f0e" opacity="0.7"/>
  <rect x="237" y="205" width="15" height="95" fill="#ff7f0e" opacity="0.7"/>
  <rect x="255" y="235" width="15" height="65" fill="#ff7f0e" opacity="0.7"/>
  <rect x="273" y="260" width="15" height="40" fill="#ff7f0e" opacity="0.7"/>
  <rect x="291" y="278" width="15" height="22" fill="#ff7f0e" opacity="0.7"/>
</svg>

### Gráfico de barras: Ingreso promedio por mes y plan

```python
df_monthly.groupby(['month_year', 'plan'])['income'].mean().unstack().plot(kind='bar')
plt.xlabel('Mes')
plt.ylabel('Ingreso Promedio ($)')
plt.title('Ingreso Promedio Mensual por Plan')
plt.legend(['Surf', 'Ultimate'])
plt.xticks(rotation=45)
plt.show()
```

#### Gráfico SVG: Ingreso promedio por mes y plan

<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg">
  <rect width="700" height="380" fill="white"/>
  <text x="350" y="25" text-anchor="middle" font-size="14" font-weight="bold">Ingreso Promedio Mensual por Plan</text>

  <!-- Leyenda -->
  <rect x="550" y="45" width="15" height="15" fill="#1f77b4"/>
  <text x="570" y="57" font-size="10">Surf</text>
  <rect x="550" y="65" width="15" height="15" fill="#ff7f0e"/>
  <text x="570" y="77" font-size="10">Ultimate</text>

  <text x="15" y="190" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 190)">Ingreso Promedio ($)</text>
  <text x="350" y="365" text-anchor="middle" font-size="11">Mes</text>

  <!-- Ejes -->
  <line x1="60" y1="50" x2="60" y2="320" stroke="black" stroke-width="1"/>
  <line x1="60" y1="320" x2="650" y2="320" stroke="black" stroke-width="1"/>

  <!-- Etiquetas Y -->
  <text x="55" y="320" text-anchor="end" font-size="9">$0</text>
  <text x="55" y="252" text-anchor="end" font-size="9">$25</text>
  <text x="55" y="185" text-anchor="end" font-size="9">$50</text>
  <text x="55" y="117" text-anchor="end" font-size="9">$75</text>
  <text x="55" y="50" text-anchor="end" font-size="9">$100</text>

  <!-- Barras por mes (Surf ~$40-50, Ultimate ~$70-75) -->
  <!-- Enero -->
  <rect x="70" y="200" width="20" height="120" fill="#1f77b4"/>
  <rect x="92" y="115" width="20" height="205" fill="#ff7f0e"/>

  <!-- Febrero -->
  <rect x="120" y="190" width="20" height="130" fill="#1f77b4"/>
  <rect x="142" y="110" width="20" height="210" fill="#ff7f0e"/>

  <!-- Marzo -->
  <rect x="170" y="185" width="20" height="135" fill="#1f77b4"/>
  <rect x="192" y="108" width="20" height="212" fill="#ff7f0e"/>

  <!-- Abril -->
  <rect x="220" y="178" width="20" height="142" fill="#1f77b4"/>
  <rect x="242" y="105" width="20" height="215" fill="#ff7f0e"/>

  <!-- Mayo -->
  <rect x="270" y="165" width="20" height="155" fill="#1f77b4"/>
  <rect x="292" y="102" width="20" height="218" fill="#ff7f0e"/>

  <!-- Junio -->
  <rect x="320" y="160" width="20" height="160" fill="#1f77b4"/>
  <rect x="342" y="100" width="20" height="220" fill="#ff7f0e"/>

  <!-- Julio -->
  <rect x="370" y="155" width="20" height="165" fill="#1f77b4"/>
  <rect x="392" y="98" width="20" height="222" fill="#ff7f0e"/>

  <!-- Agosto -->
  <rect x="420" y="150" width="20" height="170" fill="#1f77b4"/>
  <rect x="442" y="95" width="20" height="225" fill="#ff7f0e"/>

  <!-- Septiembre -->
  <rect x="470" y="152" width="20" height="168" fill="#1f77b4"/>
  <rect x="492" y="97" width="20" height="223" fill="#ff7f0e"/>

  <!-- Octubre -->
  <rect x="520" y="148" width="20" height="172" fill="#1f77b4"/>
  <rect x="542" y="94" width="20" height="226" fill="#ff7f0e"/>

  <!-- Noviembre -->
  <rect x="570" y="145" width="20" height="175" fill="#1f77b4"/>
  <rect x="592" y="92" width="20" height="228" fill="#ff7f0e"/>

  <!-- Diciembre -->
  <rect x="620" y="140" width="20" height="180" fill="#1f77b4"/>
  <rect x="642" y="90" width="20" height="230" fill="#ff7f0e"/>

  <!-- Etiquetas X -->
  <text x="92" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 92, 335)">2018-01</text>
  <text x="142" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 142, 335)">2018-02</text>
  <text x="192" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 192, 335)">2018-03</text>
  <text x="242" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 242, 335)">2018-04</text>
  <text x="292" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 292, 335)">2018-05</text>
  <text x="342" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 342, 335)">2018-06</text>
  <text x="392" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 392, 335)">2018-07</text>
  <text x="442" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 442, 335)">2018-08</text>
  <text x="492" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 492, 335)">2018-09</text>
  <text x="542" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 542, 335)">2018-10</text>
  <text x="592" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 592, 335)">2018-11</text>
  <text x="642" y="335" text-anchor="middle" font-size="8" transform="rotate(45, 642, 335)">2018-12</text>
</svg>

### Interpretación de las visualizaciones

**Histograma de minutos:**
- Ambos planes tienen distribuciones similares centradas alrededor de 400-500 minutos
- La mayoría de usuarios de ambos planes NO exceden el límite de Surf (500 min)
- Los usuarios de Ultimate casi nunca exceden su límite (3000 min)

**Gráfico de barras de ingresos:**
- Ultimate genera ~$70 por usuario (cerca de la tarifa base)
- Surf genera ~$40-50 por usuario, pero con más variabilidad
- Los usuarios de Surf frecuentemente pagan excedentes

</details>

---

## AVANZADO

### Checklist

**Estadísticas Descriptivas**
- [ ] **[OBLIGATORIO]** Calcula media y varianza por plan
- [ ] Usa describe() para resumen estadístico
- [ ] Compara estadísticas entre planes
- [ ] Interpreta las diferencias encontradas

**Visualizaciones Avanzadas**
- [ ] **[OBLIGATORIO]** Crea boxplots para comparar distribuciones
- [ ] Diferencia visualmente entre planes (colores, leyendas)
- [ ] Visualiza evolución temporal del uso

**Pruebas de Hipótesis**
- [ ] **[OBLIGATORIO]** Formula correctamente H₀ y H₁ para ambas hipótesis
- [ ] **[OBLIGATORIO]** Define nivel de significancia (alpha = 0.05)
- [ ] **[OBLIGATORIO]** Aplica ttest_ind de scipy.stats
- [ ] Usa equal_var=False para t-test con varianzas desiguales
- [ ] Interpreta correctamente el valor p

**Interpretación de Resultados**
- [ ] **[OBLIGATORIO]** Concluye si se rechaza o no H₀
- [ ] **[OBLIGATORIO]** Responde a la pregunta de negocio (cuál plan es más rentable)
- [ ] Documenta decisiones y suposiciones
- [ ] Presenta conclusiones claras y accionables

---

<details>
<summary><strong>📋 Resultados Esperados - AVANZADO</strong></summary>

### Estadísticas descriptivas por plan

```python
df_monthly.groupby('plan')['income'].describe()
```

#### Tabla esperada: Estadísticas de ingresos por plan (DATOS REALES)

| Plan | count | mean | std | min | 25% | 50% | 75% | max |
|------|-------|------|-----|-----|-----|-----|-----|-----|
| **surf** | 1573 | $60.71 | $55.39 | $20 | $20 | $40.36 | $80.36 | $590.37 |
| **ultimate** | 720 | $72.31 | $11.40 | $70 | $70 | $70.00 | $70.00 | $182.00 |

**Interpretación clave:**
- Surf tiene mayor variabilidad (std $55.39) porque los usuarios pagan excedentes frecuentemente
- Ultimate es muy estable (std $11.40) porque casi nadie excede los límites generosos
- La media de Surf ($60.71) está por debajo de Ultimate ($72.31)

### Varianza de ingresos

```python
# Varianza por plan
print(f"Varianza Surf: {np.var(df_monthly.query('plan == \"surf\"')['income']):.2f}")
print(f"Varianza Ultimate: {np.var(df_monthly.query('plan == \"ultimate\"')['income']):.2f}")
```

**Resultado esperado (DATOS REALES):**
```
Varianza Surf: 3067.83
Varianza Ultimate: 129.85
```

**Las varianzas son MUY diferentes (23x)** → Esto es importante para la prueba t-test.

### Boxplot de ingresos por plan

```python
sns.boxplot(data=df_monthly, x='plan', y='income')
plt.xlabel('Plan')
plt.ylabel('Ingreso Mensual ($)')
plt.title('Distribución de Ingresos por Plan')
plt.show()
```

#### Gráfico SVG: Boxplot de ingresos por plan

<svg viewBox="0 0 500 350" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="350" fill="white"/>
  <text x="250" y="25" text-anchor="middle" font-size="14" font-weight="bold">Distribución de Ingresos por Plan</text>
  <text x="15" y="175" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 175)">Ingreso Mensual ($)</text>
  <text x="250" y="335" text-anchor="middle" font-size="11">Plan</text>

  <!-- Ejes -->
  <line x1="80" y1="50" x2="80" y2="300" stroke="black" stroke-width="1"/>
  <line x1="80" y1="300" x2="450" y2="300" stroke="black" stroke-width="1"/>

  <!-- Etiquetas Y -->
  <text x="75" y="300" text-anchor="end" font-size="9">$0</text>
  <text x="75" y="237" text-anchor="end" font-size="9">$50</text>
  <text x="75" y="175" text-anchor="end" font-size="9">$100</text>
  <text x="75" y="112" text-anchor="end" font-size="9">$150</text>
  <text x="75" y="50" text-anchor="end" font-size="9">$200</text>

  <!-- Boxplot Surf (izquierda) -->
  <!-- Caja (Q1 a Q3): $20 a $55 -->
  <rect x="120" y="200" width="80" height="70" fill="#1f77b4" stroke="black" stroke-width="1"/>
  <!-- Mediana: $30 -->
  <line x1="120" y1="260" x2="200" y2="260" stroke="black" stroke-width="2"/>
  <!-- Bigote inferior: min $20 -->
  <line x1="160" y1="270" x2="160" y2="275" stroke="black" stroke-width="1"/>
  <line x1="140" y1="275" x2="180" y2="275" stroke="black" stroke-width="1"/>
  <!-- Bigote superior: ~$100 -->
  <line x1="160" y1="200" x2="160" y2="175" stroke="black" stroke-width="1"/>
  <line x1="140" y1="175" x2="180" y2="175" stroke="black" stroke-width="1"/>
  <!-- Outliers (puntos): $150, $180 -->
  <circle cx="160" cy="115" r="3" fill="none" stroke="black"/>
  <circle cx="160" cy="90" r="3" fill="none" stroke="black"/>
  <circle cx="160" cy="70" r="3" fill="none" stroke="black"/>
  <text x="160" y="315" text-anchor="middle" font-size="11">Surf</text>

  <!-- Boxplot Ultimate (derecha) -->
  <!-- Caja muy comprimida: casi todos pagan $70 -->
  <rect x="300" y="160" width="80" height="20" fill="#ff7f0e" stroke="black" stroke-width="1"/>
  <!-- Mediana: $70 -->
  <line x1="300" y1="170" x2="380" y2="170" stroke="black" stroke-width="2"/>
  <!-- Bigote inferior: $70 -->
  <line x1="340" y1="180" x2="340" y2="170" stroke="black" stroke-width="1"/>
  <!-- Bigote superior: ~$85 -->
  <line x1="340" y1="160" x2="340" y2="145" stroke="black" stroke-width="1"/>
  <line x1="320" y1="145" x2="360" y2="145" stroke="black" stroke-width="1"/>
  <!-- Outliers -->
  <circle cx="340" cy="125" r="3" fill="none" stroke="black"/>
  <circle cx="340" cy="105" r="3" fill="none" stroke="black"/>
  <text x="340" y="315" text-anchor="middle" font-size="11">Ultimate</text>

  <!-- Línea de referencia $70 -->
  <line x1="85" y1="170" x2="450" y2="170" stroke="gray" stroke-width="1" stroke-dasharray="5,5"/>
  <text x="455" y="173" font-size="9" fill="gray">$70</text>
</svg>

**Interpretación del boxplot:**
- **Surf**: Caja grande (alta variabilidad), mediana ~$30, muchos outliers arriba
- **Ultimate**: Caja muy pequeña (baja variabilidad), mediana = $70 exacto
- Los outliers de Surf son usuarios que excedieron mucho sus límites

---

### PRUEBA DE HIPÓTESIS 1: Surf vs Ultimate

#### Nota Metodológica: ¿Cómo hacer una prueba de hipótesis correctamente?

**Paso 1: Formular las hipótesis ANTES de calcular**

```python
# HIPÓTESIS 1: Comparar ingresos entre planes
# H₀: El ingreso promedio de Surf es igual al de Ultimate (μ_surf = μ_ultimate)
# H₁: El ingreso promedio de Surf es diferente al de Ultimate (μ_surf ≠ μ_ultimate)
```

**Paso 2: Definir alpha ANTES de calcular**

```python
alpha = 0.05  # Nivel de significancia del 5%
```

**Paso 3: Separar los datos**

```python
df_surf = df_monthly[df_monthly['plan'] == 'surf']['income']
df_ultimate = df_monthly[df_monthly['plan'] == 'ultimate']['income']
```

**Paso 4: (Opcional) Prueba de Levene para verificar varianzas**

```python
stat, p_levene = st.levene(df_surf, df_ultimate)
print(f'Levene p-value: {p_levene}')

# Si p < 0.05 → varianzas diferentes → usar equal_var=False
# Si p >= 0.05 → varianzas iguales → usar equal_var=True
```

**Resultado esperado:**
```
Levene p-value: 5.03e-83  ← Mucho menor que 0.05
→ Las varianzas son diferentes → usar equal_var=False
```

**Paso 5: Aplicar t-test**

```python
result = st.ttest_ind(df_surf, df_ultimate, equal_var=False)
print(f'p-value: {result.pvalue}')
```

**Resultado esperado:**
```
p-value: 3.17e-15  ← Mucho menor que 0.05
```

**Paso 6: Interpretar el resultado**

```python
if result.pvalue < alpha:
    print("Se rechaza H₀: Los ingresos promedio SON significativamente diferentes")
else:
    print("No se rechaza H₀: No hay evidencia de diferencia significativa")
```

**Conclusión Hipótesis 1:**
```
p-value = 3.17e-15 < 0.05
→ SE RECHAZA H₀
→ Los ingresos de Surf y Ultimate SON significativamente diferentes
→ Ultimate genera más ingresos por usuario ($72.31 vs $60.71)
```

---

### PRUEBA DE HIPÓTESIS 2: NY-NJ vs Otras regiones

```python
# HIPÓTESIS 2: Comparar ingresos entre regiones
# H₀: El ingreso promedio de NY-NJ es igual al de otras regiones
# H₁: El ingreso promedio de NY-NJ es diferente al de otras regiones

alpha = 0.05

# Separar datos por región
df_ny = df_monthly[df_monthly['city'] == 'New York-Newark-Jersey City, NY-NJ-PA MSA']['income']
df_other = df_monthly[df_monthly['city'] != 'New York-Newark-Jersey City, NY-NJ-PA MSA']['income']

# Aplicar t-test
result = st.ttest_ind(df_ny, df_other)
print(f'p-value: {result.pvalue}')
```

**Resultado esperado:**
```
p-value: 0.0436  ← Menor que 0.05 (pero cercano)
```

**Conclusión Hipótesis 2:**
```
p-value = 0.0436 < 0.05
→ SE RECHAZA H₀ (marginalmente)
→ Los ingresos de NY-NJ SON significativamente diferentes de otras regiones
→ Pero la diferencia es pequeña y el p-value está cerca del umbral
```

---

### Resumen de pruebas de hipótesis

| Hipótesis | H₀ | p-value | Alpha | Decisión | Conclusión |
|-----------|-----|---------|-------|----------|------------|
| **H1: Surf vs Ultimate** | μ_surf = μ_ultimate | 3.17e-15 | 0.05 | **Rechazar H₀** | Ingresos diferentes (Ultimate mayor) |
| **H2: NY-NJ vs Otros** | μ_NY = μ_otros | 0.0436 | 0.05 | **Rechazar H₀** | Ingresos diferentes (marginalmente) |

---

### Conclusión General del Proyecto (DATOS REALES)

```markdown
## Conclusiones

### Comportamiento de usuarios
1. Los usuarios de ambos planes usan cantidades similares de minutos (~429 Surf vs ~430 Ultimate)
2. Los usuarios de Ultimate usan más mensajes (~38 vs ~31)
3. El uso de internet es similar entre planes (~17 GB/mes)

### Ingresos por plan
1. **Ultimate genera más ingresos por usuario** ($72.31 vs $60.71 en promedio)
2. Surf tiene alta variabilidad (std=$55.39) porque los usuarios pagan excedentes frecuentemente
3. Ultimate es muy predecible (std=$11.40), casi todos pagan solo la tarifa base

### Pruebas de hipótesis
1. **Surf vs Ultimate**: Los ingresos SON significativamente diferentes (p = 3.17e-15)
2. **NY-NJ vs Otros**: Los ingresos SON marginalmente diferentes (p = 0.044)

### Recomendación de negocio
- **Ultimate es más rentable por usuario** → Enfocar publicidad en Ultimate
- Sin embargo, Surf tiene más usuarios (339 vs 161 usuarios) → Mayor base de clientes
- **Estrategia sugerida**: Promover upgrades de Surf a Ultimate para usuarios que exceden límites
```

</details>

---

## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS de BÁSICO: 6/6
  - Al menos 2 criterios adicionales de los no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 14/14
  - Al menos 6 criterios adicionales de los no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 22/22
  - Al menos 10 criterios adicionales de los no obligatorios

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook con celdas sin ejecutar
- **Imports dispersos en el notebook** (todos los imports deben estar en la primera celda)
- No carga los 5 archivos CSV
- No convierte fechas a datetime
- No calcula ingresos mensuales por usuario
- No realiza pruebas de hipótesis
- No formula H₀ y H₁
- No interpreta el valor p
- Código genera errores de sintaxis sin corregir
- Plagio o copia directa sin comprensión

---

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

### Errores en Preparación de Datos

1. **No redondear minutos hacia arriba**:
   - Incorrecto: Usar `round()` o dejar decimales
   - Correcto: `np.ceil(calls['duration'])`
   - Consecuencia: Cálculo de ingresos incorrecto (se cobra por minuto completo)

2. **Convertir MB a GB sin redondear**:
   - Incorrecto: `internet['gb_used'] = internet['mb_used'] / 1024`
   - Correcto: `internet['gb_used'] = np.ceil(internet['mb_used'] / 1024)`
   - Consecuencia: Cálculo de excedentes incorrecto

3. **Redondear GB por sesión en lugar de por mes**:
   - Incorrecto: Redondear cada sesión individual
   - Correcto: Primero sumar MB del mes, luego convertir a GB y redondear
   - Consecuencia: Sobreestimación del uso de GB

4. **Usar merge con how='inner' (default)**:
   - Incorrecto: `df.merge(other, on='user_id')` pierde usuarios sin actividad
   - Correcto: `df.merge(other, on='user_id', how='outer')`
   - Consecuencia: Pérdida de datos de usuarios que no usaron todos los servicios

5. **No manejar NaN después del merge**:
   - Incorrecto: Dejar NaN en columnas de uso
   - Correcto: `df.fillna(0)` para columnas de uso (0 = no usó el servicio)
   - Consecuencia: Errores en cálculos o visualizaciones

### Errores en Cálculo de Ingresos

6. **No respetar límites incluidos**:
   - Incorrecto: Cobrar todos los minutos/mensajes/GB
   - Correcto: Solo cobrar lo que excede el límite incluido
   - Consecuencia: Ingresos sobrestimados

7. **Hardcodear valores de planes**:
   - Incorrecto: `if plan == 'surf': base = 20; limit = 500`
   - Correcto: Usar valores de la tabla `plans` mediante merge
   - Consecuencia: Código no escalable si cambian las tarifas

8. **Calcular excedentes negativos**:
   - Incorrecto: `extra = row['minutes'] - 500` puede ser negativo
   - Correcto: `extra = max(0, row['minutes'] - 500)` o usar `.clip(lower=0)`
   - Consecuencia: Descuentos incorrectos en la tarifa

### Errores en Análisis Estadístico

9. **No calcular varianza/desviación estándar**:
   - Incorrecto: Solo reportar la media
   - Correcto: Calcular media, varianza y/o std
   - Consecuencia: Análisis incompleto de la distribución

10. **Usar t-test con varianzas iguales cuando no lo son**:
    - Incorrecto: `st.ttest_ind(a, b)` asume varianzas iguales
    - Correcto: `st.ttest_ind(a, b, equal_var=False)` cuando varianzas difieren
    - Consecuencia: Resultado estadístico potencialmente incorrecto

### Errores en Pruebas de Hipótesis

11. **No formular H₀ y H₁ explícitamente**:
    - Incorrecto: Aplicar test sin definir hipótesis
    - Correcto: Documentar H₀ (no hay diferencia) y H₁ (sí hay diferencia)
    - Consecuencia: No queda claro qué se está probando

12. **No definir alpha antes del test**:
    - Incorrecto: Decidir alpha después de ver el p-value
    - Correcto: Definir alpha = 0.05 (o 0.01) antes de la prueba
    - Consecuencia: Sesgo en la interpretación (p-hacking)

13. **Interpretar p-value incorrectamente**:
    - Incorrecto: "p < 0.05, no se rechaza H₀"
    - Correcto: "p < alpha → se rechaza H₀; p ≥ alpha → no se rechaza H₀"
    - Consecuencia: Conclusión completamente opuesta

14. **Confundir significancia estadística con práctica**:
    - Incorrecto: "p < 0.05, el plan Ultimate es mucho mejor"
    - Correcto: Considerar tamaño del efecto, no solo significancia
    - Consecuencia: Decisiones de negocio basadas solo en p-value

### Errores en Visualizaciones

15. **Gráficos sin título ni etiquetas**:
    - Incorrecto: `plt.show()` sin configurar ejes
    - Correcto: `plt.title()`, `plt.xlabel()`, `plt.ylabel()`
    - Consecuencia: Gráficos difíciles de interpretar

16. **No diferenciar planes en visualizaciones**:
    - Incorrecto: Un solo histograma para todos los datos
    - Correcto: Separar por plan con colores/leyendas
    - Consecuencia: No se puede comparar comportamiento entre planes

---

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
