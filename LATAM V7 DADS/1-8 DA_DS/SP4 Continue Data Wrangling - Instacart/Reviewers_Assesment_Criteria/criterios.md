# Criterios de Evaluación: Proyecto 4 — ¡Llena ese carrito! (Instacart)

## Objetivo

Analizar datos de pedidos de la plataforma Instacart para identificar patrones de compra, productos populares, y comportamiento de clientes usando técnicas de preprocesamiento y análisis exploratorio de datos.

**Requisitos previos**: Completar SP1-SP3 (Python básico, estructuras de datos, pandas, data wrangling).

**Competencias que desarrollarás**: Carga y exploración de múltiples DataFrames, identificación y tratamiento de duplicados y valores ausentes, merge de DataFrames, agrupación con groupby, visualizaciones con matplotlib, análisis de patrones de comportamiento

> **Nota**: Este sprint está estructurado en **Pasos secuenciales** (Paso 1, 2, 3). Los pasos se dividen en sub-secciones [A], [B], [C]. Cada paso/sección representa una etapa obligatoria del proyecto.

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.

El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados.

Debes completar tres pasos. Para cada uno de ellos, escribe una breve introducción que refleje con claridad cómo pretendes resolver cada paso, y escribe párrafos explicatorios que justifiquen tus decisiones.

## Instrucciones del proyecto

1. **Paso 1 - Descripción de los datos:**
   - Cargar los 5 archivos CSV
   - Examinar cada DataFrame con info() y head()

2. **Paso 2 - Preprocesamiento de los datos:**
   - Verificar y corregir tipos de datos
   - Identificar y eliminar duplicados
   - Identificar y completar valores ausentes

3. **Paso 3 - Análisis de los datos:**
   - [A] Análisis básico (obligatorio)
   - [B] Análisis intermedio (obligatorio)
   - [C] Análisis avanzado (obligatorio)

## Descripción de los datos

**instacart_orders.csv** (cada fila = un pedido):
- `order_id`: ID único del pedido
- `user_id`: ID único del cliente
- `order_number`: número de veces que el cliente ha hecho un pedido
- `order_dow`: día de la semana (0 = domingo)
- `order_hour_of_day`: hora del día
- `days_since_prior_order`: días desde el pedido anterior

**products.csv** (cada fila = un producto):
- `product_id`: ID único del producto
- `product_name`: nombre del producto
- `aisle_id`: ID del pasillo
- `department_id`: ID del departamento

**order_products.csv** (cada fila = un artículo pedido):
- `order_id`: ID del pedido
- `product_id`: ID del producto
- `add_to_cart_order`: orden en que se añadió al carrito
- `reordered`: 0 si nunca se ha pedido, 1 si se ha pedido antes

**aisles.csv**:
- `aisle_id`: ID del pasillo
- `aisle`: nombre del pasillo

**departments.csv**:
- `department_id`: ID del departamento
- `department`: nombre del departamento

</details>

## Glosario de Términos Técnicos

**DataFrame merge**: Operación que combina dos DataFrames basándose en una columna común (similar a JOIN en SQL).

**groupby()**: Método de pandas que agrupa datos por una o más columnas para realizar cálculos agregados.

**value_counts()**: Método que cuenta las ocurrencias únicas de cada valor en una columna.

**pivot_table()**: Método que crea una tabla dinámica resumiendo datos por categorías.

**sort_index()**: Ordena un DataFrame o Series por su índice.

**sort_values()**: Ordena un DataFrame o Series por los valores de una columna.

**isin()**: Método que filtra filas donde los valores están en una lista específica.

**unique()**: Retorna los valores únicos de una columna.

**duplicated()**: Identifica filas duplicadas en un DataFrame.

**fillna()**: Rellena valores NaN con un valor especificado.

**reset_index()**: Reinicia el índice de un DataFrame a valores numéricos secuenciales.

**unstack()**: Pivotea el nivel más interno del índice para convertirlo en columnas.

---

# Rúbrica de Evaluación por Pasos

---

## Paso 1: Descripción de los datos

### Checklist
- [ ] **[OBLIGATORIO]** Importa pandas y matplotlib
- [ ] **[OBLIGATORIO]** Carga los 5 archivos CSV correctamente (con sep=';')
- [ ] **[OBLIGATORIO]** Examina cada DataFrame con info()
- [ ] **[OBLIGATORIO]** Examina cada DataFrame con head()

### Código Correcto

```python
# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los 5 DataFrames
orders         = pd.read_csv('/datasets/instacart_orders.csv', sep=';')
products       = pd.read_csv('/datasets/products.csv', sep=';')
departments    = pd.read_csv('/datasets/departments.csv', sep=';')
aisles         = pd.read_csv('/datasets/aisles.csv', sep=';')
order_products = pd.read_csv('/datasets/order_products.csv', sep=';')

# Examinar cada DataFrame
orders.info()
orders.head()

products.info()
products.head()

departments.info()
departments.head()

aisles.info()
aisles.head()

order_products.info()
order_products.head()
```

### Salida Esperada (orders)

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 478967 entries, 0 to 478966
Data columns (total 6 columns):
 #   Column                  Non-Null Count   Dtype
---  ------                  --------------   -----
 0   order_id                478967 non-null  int64
 1   user_id                 478967 non-null  int64
 2   order_number            478967 non-null  int64
 3   order_dow               478967 non-null  int64
 4   order_hour_of_day       478967 non-null  int64
 5   days_since_prior_order  450148 non-null  float64
dtypes: float64(1), int64(5)

   order_id  user_id  order_number  order_dow  order_hour_of_day  days_since_prior_order
0   1515936   183418            11          6                 13                    30.0
1   1690866   163593             5          5                 12                     9.0
2   1454967    39980             4          5                 19                     2.0
3   1768857    82516            56          0                 20                    10.0
4   3007858   196724             2          4                 12                    17.0
```

### Salida Esperada (products)

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 49694 entries, 0 to 49693
Data columns (total 4 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   product_id     49694 non-null  int64
 1   product_name   48436 non-null  object
 2   aisle_id       49694 non-null  int64
 3   department_id  49694 non-null  int64
```

### Salida Esperada (order_products)

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4545007 entries, 0 to 4545006
Data columns (total 4 columns):
 #   Column             Non-Null Count    Dtype
---  ------             --------------    -----
 0   order_id           4545007 non-null  int64
 1   product_id         4545007 non-null  int64
 2   add_to_cart_order  4544171 non-null  float64
 3   reordered          4545007 non-null  int64
```

---

## Paso 2: Preprocesamiento de los datos

### 2.1 Encuentra y elimina duplicados

#### Checklist
- [ ] **[OBLIGATORIO]** Verifica duplicados en `orders` DataFrame
- [ ] **[OBLIGATORIO]** Elimina los duplicados encontrados en `orders`
- [ ] **[OBLIGATORIO]** Verifica duplicados en `products` DataFrame
- [ ] **[OBLIGATORIO]** Verifica duplicados en `order_products` DataFrame
- [ ] Verifica duplicados en `departments` y `aisles`

#### Código Correcto (orders)

```python
# Revisar duplicados en orders
orders[orders.duplicated()]

# Los duplicados son pedidos del miércoles a las 2am
# Verificar todos los pedidos de ese horario
orders[(orders['order_dow'] == 3) & (orders['order_hour_of_day'] == 2)]

# Eliminar duplicados
orders = orders.drop_duplicates().reset_index(drop=True)

# Verificar que no quedan duplicados
orders[orders.duplicated()]
```

#### Salida Esperada

```
# Duplicados encontrados: 15 filas
# Todos tienen order_dow=3 y order_hour_of_day=2 (miércoles 2am)
# Después de eliminar:
Empty DataFrame
```

#### Código Correcto (products)

```python
# Verificar duplicados totales
products[products.duplicated()]  # No hay

# Verificar duplicados por product_id
products[products.duplicated(subset='product_id')]  # No hay

# Verificar nombres duplicados (pueden ser productos diferentes)
products[products['product_name'].str.upper().duplicated()]  # Hay 1361
```

#### Salida Esperada

```
# Duplicados totales: 0
# Duplicados por ID: 0
# Nombres duplicados: 1361 (incluye NaN y productos con mismo nombre en diferentes ubicaciones)
# Decisión: NO eliminar porque tienen IDs diferentes y ubicaciones distintas
```

### 2.2 Encuentra y elimina valores ausentes

#### Checklist
- [ ] **[OBLIGATORIO]** Identifica valores ausentes en `products['product_name']`
- [ ] **[OBLIGATORIO]** Identifica valores ausentes en `orders['days_since_prior_order']`
- [ ] **[OBLIGATORIO]** Identifica valores ausentes en `order_products['add_to_cart_order']`
- [ ] **[OBLIGATORIO]** Rellena `product_name` con 'Unknown'
- [ ] **[OBLIGATORIO]** Justifica mantener NaN en `days_since_prior_order`
- [ ] **[OBLIGATORIO]** Rellena `add_to_cart_order` con 999 y convierte a int

#### Código Correcto (products)

```python
# Encontrar valores ausentes
products[products['product_name'].isna()]  # 1258 filas

# Verificar si todos están en aisle_id=100 y department_id=21
products[(products['product_name'].isna()) & (products['aisle_id'] == 100)]
products[(products['product_name'].isna()) & (products['department_id'] == 21)]

# Ver qué significan esos IDs
print(departments[departments['department_id'] == 21])  # 'missing'
print(aisles[aisles['aisle_id'] == 100])  # 'missing'

# Rellenar con 'Unknown'
products['product_name'] = products['product_name'].fillna('Unknown')
```

#### Salida Esperada

```
# 1258 productos sin nombre
# Todos están en department_id=21 ('missing') y aisle_id=100 ('missing')
# Después de fillna: 0 valores ausentes
```

#### Código Correcto (orders)

```python
# Encontrar valores ausentes
orders[orders['days_since_prior_order'].isna()]  # 28817 filas

# Verificar si son primer pedido (order_number == 1)
orders[(orders['days_since_prior_order'].isna()) & (orders['order_number'] != 1)]
# Empty DataFrame → Todos son primer pedido

# Decisión: Mantener NaN porque es el primer pedido del cliente
# No tiene sentido rellenar porque no hay pedido anterior
```

#### Salida Esperada

```
# 28817 valores ausentes en days_since_prior_order
# Todos corresponden a order_number=1 (primer pedido)
# Decisión: Mantener como NaN (comportamiento esperado)
```

#### Código Correcto (order_products)

```python
# Encontrar valores ausentes
order_products[order_products['add_to_cart_order'].isna()]  # 836 filas

# Verificar valores mínimo y máximo
print(order_products['add_to_cart_order'].min())  # 1.0
print(order_products['add_to_cart_order'].max())  # 64.0

# Guardar IDs de pedidos con valores ausentes
miss_cart_order_ids = order_products[order_products['add_to_cart_order'].isna()]['order_id'].unique().tolist()

# Verificar si todos los pedidos tienen más de 64 productos
order_products[order_products['order_id'].isin(miss_cart_order_ids)].groupby('order_id')['product_id'].count().min()
# Resultado: 65 → Todos tienen más de 64 productos

# Rellenar con 999 y convertir a int
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].fillna(999).astype('int')
```

#### Salida Esperada

```
# 836 valores ausentes en add_to_cart_order
# Valor mínimo: 1.0, máximo: 64.0
# Todos los pedidos con NaN tienen más de 64 productos
# El sistema solo registra orden hasta producto 64
# Después de fillna(999): 0 valores ausentes, tipo int32
```

---

## Paso 3: Análisis de los datos

---

## [A] Análisis Fácil (Obligatorio para aprobar)

### [A1] Verificar valores razonables

#### Checklist
- [ ] **[OBLIGATORIO]** Verifica que `order_hour_of_day` esté entre 0-23
- [ ] **[OBLIGATORIO]** Verifica que `order_dow` esté entre 0-6

#### Código Correcto

```python
# Verificar horas (debe ser 0-23)
print(sorted(orders['order_hour_of_day'].unique()))

# Verificar días (debe ser 0-6)
print(sorted(orders['order_dow'].unique()))
```

#### Salida Esperada

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
[0, 1, 2, 3, 4, 5, 6]
```

---

### [A2] Pedidos por hora del día

#### Checklist
- [ ] **[OBLIGATORIO]** Calcula número de pedidos por hora
- [ ] **[OBLIGATORIO]** Crea gráfico de barras
- [ ] **[OBLIGATORIO]** El gráfico tiene título y etiquetas

#### Código Correcto

```python
# SOLUCIÓN 1: value_counts()
pedidos_por_hora = orders['order_hour_of_day'].value_counts().sort_index()

# SOLUCIÓN 2: groupby()
pedidos_por_hora = orders.groupby('order_hour_of_day')['order_id'].count()

# SOLUCIÓN 3: pivot_table()
pedidos_por_hora = orders.pivot_table(index='order_hour_of_day', values='order_id', aggfunc='count')

# Crear gráfico
pedidos_por_hora.plot(kind='bar',
                      title='Pedidos por Hora del Día',
                      xlabel='Hora del Día',
                      ylabel='Número de Pedidos')
plt.show()
```

#### Tabla de Datos Esperada

| Hora | Pedidos |
|------|---------|
| 0    | 5,527   |
| 1    | 3,058   |
| 2    | 1,799   |
| 3    | 1,378   |
| 4    | 1,418   |
| 5    | 2,158   |
| 6    | 6,386   |
| 7    | 16,785  |
| 8    | 31,193  |
| 9    | 43,851  |
| **10** | **50,091** |
| 11   | 49,519  |
| 12   | 46,628  |
| 13   | 46,495  |
| 14   | 47,413  |
| **15** | **50,811** |
| 16   | 49,302  |
| 17   | 41,315  |
| 18   | 33,649  |
| 19   | 25,810  |
| 20   | 18,501  |
| 21   | 14,360  |
| 22   | 11,568  |
| 23   | 7,937   |

#### Gráfico Esperado

<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="400" fill="white"/>
  <text x="300" y="30" text-anchor="middle" font-size="16" font-weight="bold">Pedidos por Hora del Día</text>
  <text x="20" y="200" text-anchor="middle" font-size="12" transform="rotate(-90, 20, 200)">Número de Pedidos</text>
  <text x="300" y="385" text-anchor="middle" font-size="12">Hora del Día</text>
  <line x1="60" y1="50" x2="60" y2="350" stroke="black" stroke-width="1"/>
  <line x1="60" y1="350" x2="580" y2="350" stroke="black" stroke-width="1"/>
  <text x="55" y="350" text-anchor="end" font-size="9">0</text>
  <text x="55" y="275" text-anchor="end" font-size="9">10k</text>
  <text x="55" y="200" text-anchor="end" font-size="9">20k</text>
  <text x="55" y="125" text-anchor="end" font-size="9">30k</text>
  <text x="55" y="50" text-anchor="end" font-size="9">40k</text>
  <rect x="65" y="338" width="18" height="12" fill="#1f77b4"/>
  <rect x="87" y="343" width="18" height="7" fill="#1f77b4"/>
  <rect x="109" y="346" width="18" height="4" fill="#1f77b4"/>
  <rect x="131" y="347" width="18" height="3" fill="#1f77b4"/>
  <rect x="153" y="347" width="18" height="3" fill="#1f77b4"/>
  <rect x="175" y="345" width="18" height="5" fill="#1f77b4"/>
  <rect x="197" y="335" width="18" height="15" fill="#1f77b4"/>
  <rect x="219" y="305" width="18" height="45" fill="#1f77b4"/>
  <rect x="241" y="250" width="18" height="100" fill="#1f77b4"/>
  <rect x="263" y="175" width="18" height="175" fill="#1f77b4"/>
  <rect x="285" y="80" width="18" height="270" fill="#1f77b4"/>
  <rect x="307" y="95" width="18" height="255" fill="#1f77b4"/>
  <rect x="329" y="105" width="18" height="245" fill="#1f77b4"/>
  <rect x="351" y="100" width="18" height="250" fill="#1f77b4"/>
  <rect x="373" y="90" width="18" height="260" fill="#1f77b4"/>
  <rect x="395" y="85" width="18" height="265" fill="#1f77b4"/>
  <rect x="417" y="95" width="18" height="255" fill="#1f77b4"/>
  <rect x="439" y="130" width="18" height="220" fill="#1f77b4"/>
  <rect x="461" y="175" width="18" height="175" fill="#1f77b4"/>
  <rect x="483" y="225" width="18" height="125" fill="#1f77b4"/>
  <rect x="505" y="275" width="18" height="75" fill="#1f77b4"/>
  <rect x="527" y="300" width="18" height="50" fill="#1f77b4"/>
  <rect x="549" y="320" width="18" height="30" fill="#1f77b4"/>
  <rect x="571" y="335" width="18" height="15" fill="#1f77b4"/>
  <text x="74" y="365" text-anchor="middle" font-size="8">0</text>
  <text x="140" y="365" text-anchor="middle" font-size="8">3</text>
  <text x="206" y="365" text-anchor="middle" font-size="8">6</text>
  <text x="272" y="365" text-anchor="middle" font-size="8">9</text>
  <text x="338" y="365" text-anchor="middle" font-size="8">12</text>
  <text x="404" y="365" text-anchor="middle" font-size="8">15</text>
  <text x="470" y="365" text-anchor="middle" font-size="8">18</text>
  <text x="536" y="365" text-anchor="middle" font-size="8">21</text>
</svg>

#### Conclusión Esperada

> Los pedidos aumentan a partir de las 8am, alcanzan su pico entre las 10am-4pm (~50k pedidos), y disminuyen en la noche. Las horas de madrugada (0-5am) tienen muy pocos pedidos (<3k).

---

### [A3] Pedidos por día de la semana

#### Checklist
- [ ] **[OBLIGATORIO]** Calcula número de pedidos por día
- [ ] **[OBLIGATORIO]** Crea gráfico de barras
- [ ] **[OBLIGATORIO]** El gráfico tiene título y etiquetas

#### Código Correcto

```python
# SOLUCIÓN 1: value_counts()
pedidos_por_dia = orders['order_dow'].value_counts().sort_index()

# SOLUCIÓN 2: groupby()
pedidos_por_dia = orders.groupby('order_dow')['order_id'].count()

# Crear gráfico
pedidos_por_dia.plot(kind='bar',
                     title='Pedidos por Día de la Semana',
                     xlabel='Día de la Semana (0=Domingo)',
                     ylabel='Número de Pedidos')
plt.show()
```

#### Tabla de Datos Esperada

| Día | Nombre | Pedidos |
|-----|--------|---------|
| 0   | Domingo | **87,374** |
| 1   | Lunes | **83,877** |
| 2   | Martes | 65,061 |
| 3   | Miércoles | 60,897 |
| 4   | Jueves | 63,148 |
| 5   | Viernes | 67,890 |
| 6   | Sábado | 71,705 |

#### Gráfico Esperado

<svg viewBox="0 0 500 350" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="350" fill="white"/>
  <text x="250" y="25" text-anchor="middle" font-size="14" font-weight="bold">Pedidos por Día de la Semana</text>
  <text x="15" y="175" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 175)">Número de Pedidos</text>
  <text x="250" y="335" text-anchor="middle" font-size="11">Día (0=Dom, 1=Lun, ...)</text>
  <line x1="50" y1="40" x2="50" y2="300" stroke="black" stroke-width="1"/>
  <line x1="50" y1="300" x2="480" y2="300" stroke="black" stroke-width="1"/>
  <text x="45" y="300" text-anchor="end" font-size="9">0</text>
  <text x="45" y="235" text-anchor="end" font-size="9">25k</text>
  <text x="45" y="170" text-anchor="end" font-size="9">50k</text>
  <text x="45" y="105" text-anchor="end" font-size="9">75k</text>
  <text x="45" y="40" text-anchor="end" font-size="9">100k</text>
  <rect x="70" y="65" width="45" height="235" fill="#1f77b4"/>
  <rect x="130" y="75" width="45" height="225" fill="#1f77b4"/>
  <rect x="190" y="130" width="45" height="170" fill="#1f77b4"/>
  <rect x="250" y="140" width="45" height="160" fill="#1f77b4"/>
  <rect x="310" y="135" width="45" height="165" fill="#1f77b4"/>
  <rect x="370" y="125" width="45" height="175" fill="#1f77b4"/>
  <rect x="430" y="120" width="45" height="180" fill="#1f77b4"/>
  <text x="92" y="315" text-anchor="middle" font-size="10">0</text>
  <text x="152" y="315" text-anchor="middle" font-size="10">1</text>
  <text x="212" y="315" text-anchor="middle" font-size="10">2</text>
  <text x="272" y="315" text-anchor="middle" font-size="10">3</text>
  <text x="332" y="315" text-anchor="middle" font-size="10">4</text>
  <text x="392" y="315" text-anchor="middle" font-size="10">5</text>
  <text x="452" y="315" text-anchor="middle" font-size="10">6</text>
</svg>

#### Conclusión Esperada

> Los días con más pedidos son domingo (0) y lunes (1) con ~85k pedidos cada uno. Los días de entre semana (martes-jueves) tienen menos actividad (~62k). Esto sugiere que las personas planifican sus compras de la semana los fines de semana.

---

### [A4] Días desde el pedido anterior

#### Checklist
- [ ] **[OBLIGATORIO]** Calcula distribución de días entre pedidos
- [ ] **[OBLIGATORIO]** Crea gráfico de barras
- [ ] **[OBLIGATORIO]** Comenta sobre valores mínimos y máximos
- [ ] Crea gráfico adicional filtrando el valor atípico de 30 días

#### Código Correcto

```python
# Calcular distribución
dias_desde_pedido = orders.groupby('days_since_prior_order')['order_id'].count()

# Crear gráfico
dias_desde_pedido.plot(kind='bar',
                       title='Días Desde el Pedido Anterior',
                       xlabel='Número de Días',
                       ylabel='Número de Pedidos')
plt.show()

# Filtrar valor atípico de 30 días para ver mejor la distribución
dias_filtrado = orders[orders['days_since_prior_order'] < 30]
dias_filtrado['days_since_prior_order'].value_counts().sort_index().plot(kind='bar',
                       title='Días Desde el Pedido Anterior (sin 30)',
                       xlabel='Número de Días',
                       ylabel='Número de Pedidos')
plt.show()
```

#### Gráfico Esperado

<svg viewBox="0 0 700 350" xmlns="http://www.w3.org/2000/svg">
  <rect width="700" height="350" fill="white"/>
  <text x="350" y="25" text-anchor="middle" font-size="14" font-weight="bold">Días Desde el Pedido Anterior</text>
  <text x="15" y="175" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 175)">Número de Pedidos</text>
  <text x="350" y="335" text-anchor="middle" font-size="11">Número de Días</text>
  <line x1="50" y1="40" x2="50" y2="300" stroke="black" stroke-width="1"/>
  <line x1="50" y1="300" x2="680" y2="300" stroke="black" stroke-width="1"/>
  <text x="45" y="300" text-anchor="end" font-size="9">0</text>
  <text x="45" y="235" text-anchor="end" font-size="9">20k</text>
  <text x="45" y="170" text-anchor="end" font-size="9">40k</text>
  <text x="45" y="105" text-anchor="end" font-size="9">60k</text>
  <text x="45" y="40" text-anchor="end" font-size="9">80k</text>
  <rect x="55" y="230" width="17" height="70" fill="#1f77b4"/>
  <rect x="75" y="250" width="17" height="50" fill="#1f77b4"/>
  <rect x="95" y="255" width="17" height="45" fill="#1f77b4"/>
  <rect x="115" y="260" width="17" height="40" fill="#1f77b4"/>
  <rect x="135" y="265" width="17" height="35" fill="#1f77b4"/>
  <rect x="155" y="270" width="17" height="30" fill="#1f77b4"/>
  <rect x="175" y="275" width="17" height="25" fill="#1f77b4"/>
  <rect x="195" y="175" width="17" height="125" fill="#2ca02c"/>
  <rect x="215" y="270" width="17" height="30" fill="#1f77b4"/>
  <rect x="235" y="272" width="17" height="28" fill="#1f77b4"/>
  <rect x="255" y="275" width="17" height="25" fill="#1f77b4"/>
  <rect x="275" y="278" width="17" height="22" fill="#1f77b4"/>
  <rect x="295" y="280" width="17" height="20" fill="#1f77b4"/>
  <rect x="315" y="282" width="17" height="18" fill="#1f77b4"/>
  <rect x="335" y="200" width="17" height="100" fill="#2ca02c"/>
  <rect x="355" y="280" width="17" height="20" fill="#1f77b4"/>
  <rect x="375" y="282" width="17" height="18" fill="#1f77b4"/>
  <rect x="395" y="284" width="17" height="16" fill="#1f77b4"/>
  <rect x="415" y="286" width="17" height="14" fill="#1f77b4"/>
  <rect x="435" y="288" width="17" height="12" fill="#1f77b4"/>
  <rect x="455" y="285" width="17" height="15" fill="#1f77b4"/>
  <rect x="475" y="225" width="17" height="75" fill="#2ca02c"/>
  <rect x="495" y="285" width="17" height="15" fill="#1f77b4"/>
  <rect x="515" y="287" width="17" height="13" fill="#1f77b4"/>
  <rect x="535" y="289" width="17" height="11" fill="#1f77b4"/>
  <rect x="555" y="290" width="17" height="10" fill="#1f77b4"/>
  <rect x="575" y="291" width="17" height="9" fill="#1f77b4"/>
  <rect x="595" y="292" width="17" height="8" fill="#1f77b4"/>
  <rect x="615" y="280" width="17" height="20" fill="#2ca02c"/>
  <rect x="635" y="285" width="17" height="15" fill="#1f77b4"/>
  <rect x="655" y="60" width="17" height="240" fill="#ff7f0e"/>
  <text x="63" y="315" text-anchor="middle" font-size="8">0</text>
  <text x="203" y="315" text-anchor="middle" font-size="8">7</text>
  <text x="343" y="315" text-anchor="middle" font-size="8">14</text>
  <text x="483" y="315" text-anchor="middle" font-size="8">21</text>
  <text x="623" y="315" text-anchor="middle" font-size="8">28</text>
  <text x="663" y="315" text-anchor="middle" font-size="8">30</text>
</svg>

*Nota: Las barras verdes indican picos semanales (7, 14, 21, 28 días). La barra naranja (30) es un valor anómalo.*

#### Conclusión Esperada

> - **Valor mínimo (0 días)**: Clientes que hicieron más de un pedido el mismo día
> - **Valor máximo (30 días)**: Este valor es anómalamente alto, probablemente porque el sistema registra "30 días o más" como 30 (valor tope)
> - **Patrones semanales**: Se observan picos claros en 7, 14, 21, 28 días, indicando que muchos clientes hacen pedidos con frecuencia semanal

---

## [B] Análisis Intermedio (Obligatorio para aprobar)

### [B1] Comparación miércoles vs sábado

#### Checklist
- [ ] **[OBLIGATORIO]** Filtra datos de miércoles (dow=3) y sábado (dow=6)
- [ ] **[OBLIGATORIO]** Calcula pedidos por hora para cada día
- [ ] **[OBLIGATORIO]** Crea gráfico comparativo con ambos días
- [ ] **[OBLIGATORIO]** Describe las diferencias observadas

#### Código Correcto

```python
# SOLUCIÓN 1: Filtrar y concatenar
pedidos_mier = orders[orders['order_dow'] == 3]['order_hour_of_day'].value_counts().sort_index()
pedidos_sab = orders[orders['order_dow'] == 6]['order_hour_of_day'].value_counts().sort_index()

comparacion = pd.concat([pedidos_mier, pedidos_sab], axis=1)
comparacion.columns = ['Miércoles', 'Sábado']

# SOLUCIÓN 2: groupby + unstack
comparacion = orders.groupby(['order_hour_of_day', 'order_dow'])['order_id'].count().unstack()
comparacion = comparacion[[3, 6]]  # Solo miércoles (3) y sábado (6)
comparacion.columns = ['Miércoles', 'Sábado']

# Crear gráfico
comparacion.plot(kind='bar',
                 title='Comparación de Pedidos: Miércoles vs Sábado',
                 xlabel='Hora del Día',
                 ylabel='Número de Pedidos')
plt.show()
```

#### Tabla de Datos Esperada (horas pico)

| Hora | Miércoles | Sábado | Diferencia |
|------|-----------|--------|------------|
| 10   | 5,026     | 4,919  | Mier +107  |
| 11   | 5,004     | 5,116  | Sáb +112   |
| 12   | 4,688     | 5,132  | **Sáb +444** |
| 13   | 4,674     | 5,323  | **Sáb +649** |
| 14   | 4,774     | 5,375  | **Sáb +601** |
| 15   | 5,163     | 5,188  | Sáb +25    |

#### Gráfico Esperado

<svg viewBox="0 0 650 380" xmlns="http://www.w3.org/2000/svg">
  <rect width="650" height="380" fill="white"/>
  <text x="325" y="25" text-anchor="middle" font-size="14" font-weight="bold">Comparación de Pedidos: Miércoles vs Sábado</text>
  <rect x="480" y="45" width="15" height="15" fill="#1f77b4"/>
  <text x="500" y="57" font-size="10">Miércoles</text>
  <rect x="480" y="65" width="15" height="15" fill="#ff7f0e"/>
  <text x="500" y="77" font-size="10">Sábado</text>
  <text x="15" y="200" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 200)">Número de Pedidos</text>
  <text x="300" y="365" text-anchor="middle" font-size="11">Hora del Día</text>
  <line x1="50" y1="50" x2="50" y2="330" stroke="black" stroke-width="1"/>
  <line x1="50" y1="330" x2="600" y2="330" stroke="black" stroke-width="1"/>
  <text x="45" y="330" text-anchor="end" font-size="9">0</text>
  <text x="45" y="260" text-anchor="end" font-size="9">2k</text>
  <text x="45" y="190" text-anchor="end" font-size="9">4k</text>
  <text x="45" y="120" text-anchor="end" font-size="9">6k</text>
  <rect x="230" y="241" width="9" height="89" fill="#1f77b4"/>
  <rect x="240" y="237" width="9" height="93" fill="#ff7f0e"/>
  <rect x="253" y="171" width="9" height="159" fill="#1f77b4"/>
  <rect x="263" y="177" width="9" height="153" fill="#ff7f0e"/>
  <rect x="276" y="152" width="9" height="178" fill="#1f77b4"/>
  <rect x="286" y="156" width="9" height="174" fill="#ff7f0e"/>
  <rect x="299" y="153" width="9" height="177" fill="#1f77b4"/>
  <rect x="309" y="149" width="9" height="181" fill="#ff7f0e"/>
  <rect x="322" y="164" width="9" height="166" fill="#1f77b4"/>
  <rect x="332" y="148" width="9" height="182" fill="#ff7f0e"/>
  <rect x="345" y="165" width="9" height="165" fill="#1f77b4"/>
  <rect x="355" y="141" width="9" height="189" fill="#ff7f0e"/>
  <rect x="368" y="161" width="9" height="169" fill="#1f77b4"/>
  <rect x="378" y="139" width="9" height="191" fill="#ff7f0e"/>
  <rect x="391" y="147" width="9" height="183" fill="#1f77b4"/>
  <rect x="401" y="144" width="9" height="186" fill="#ff7f0e"/>
  <rect x="414" y="154" width="9" height="176" fill="#1f77b4"/>
  <rect x="424" y="152" width="9" height="178" fill="#ff7f0e"/>
  <rect x="437" y="182" width="9" height="148" fill="#1f77b4"/>
  <rect x="447" y="178" width="9" height="152" fill="#ff7f0e"/>
  <text x="85" y="345" text-anchor="middle" font-size="8">0</text>
  <text x="155" y="345" text-anchor="middle" font-size="8">4</text>
  <text x="240" y="345" text-anchor="middle" font-size="8">8</text>
  <text x="332" y="345" text-anchor="middle" font-size="8">12</text>
  <text x="424" y="345" text-anchor="middle" font-size="8">16</text>
  <text x="516" y="345" text-anchor="middle" font-size="8">20</text>
</svg>

#### Conclusión Esperada

> **Diferencias observadas:**
> - Los sábados tienen más pedidos en las horas de la tarde (12-14h) con ~600 pedidos más por hora
> - Los miércoles tienen patrones más uniformes durante el día laboral
> - El pico de los sábados es más tarde (13-14h vs 10h) y más pronunciado
> - Esto sugiere que el sábado la gente tiene más tiempo libre para hacer compras durante el día

---

### [B2] Distribución de pedidos por cliente

#### Checklist
- [ ] **[OBLIGATORIO]** Agrupa pedidos por cliente (user_id)
- [ ] **[OBLIGATORIO]** Cuenta número de pedidos por cliente
- [ ] **[OBLIGATORIO]** Crea histograma o gráfico de barras

#### Código Correcto

```python
# Contar pedidos por cliente
pedidos_por_cliente = orders.groupby('user_id')['order_id'].count()

# SOLUCIÓN 1: Histograma
pedidos_por_cliente.plot(kind='hist',
                         bins=28,
                         title='Distribución de Pedidos por Cliente')
plt.xlabel('Número de Pedidos')
plt.ylabel('Número de Clientes')
plt.show()

# SOLUCIÓN 2: Gráfico de barras
pedidos_por_cliente.value_counts().sort_index().plot(kind='bar')
plt.xlabel('Número de Pedidos')
plt.ylabel('Número de Clientes')
plt.show()
```

#### Gráfico Esperado

<svg viewBox="0 0 550 350" xmlns="http://www.w3.org/2000/svg">
  <rect width="550" height="350" fill="white"/>
  <text x="275" y="25" text-anchor="middle" font-size="14" font-weight="bold">Distribución de Pedidos por Cliente</text>
  <text x="15" y="175" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 175)">Número de Clientes</text>
  <text x="275" y="335" text-anchor="middle" font-size="11">Número de Pedidos</text>
  <line x1="50" y1="40" x2="50" y2="300" stroke="black" stroke-width="1"/>
  <line x1="50" y1="300" x2="530" y2="300" stroke="black" stroke-width="1"/>
  <rect x="60" y="60" width="30" height="240" fill="#1f77b4"/>
  <rect x="95" y="120" width="30" height="180" fill="#1f77b4"/>
  <rect x="130" y="160" width="30" height="140" fill="#1f77b4"/>
  <rect x="165" y="190" width="30" height="110" fill="#1f77b4"/>
  <rect x="200" y="215" width="30" height="85" fill="#1f77b4"/>
  <rect x="235" y="235" width="30" height="65" fill="#1f77b4"/>
  <rect x="270" y="250" width="30" height="50" fill="#1f77b4"/>
  <rect x="305" y="262" width="30" height="38" fill="#1f77b4"/>
  <rect x="340" y="272" width="30" height="28" fill="#1f77b4"/>
  <rect x="375" y="278" width="30" height="22" fill="#1f77b4"/>
  <rect x="410" y="284" width="30" height="16" fill="#1f77b4"/>
  <rect x="445" y="288" width="30" height="12" fill="#1f77b4"/>
  <rect x="480" y="292" width="30" height="8" fill="#1f77b4"/>
  <text x="75" y="315" text-anchor="middle" font-size="9">1-3</text>
  <text x="180" y="315" text-anchor="middle" font-size="9">10</text>
  <text x="285" y="315" text-anchor="middle" font-size="9">20</text>
  <text x="390" y="315" text-anchor="middle" font-size="9">30</text>
  <text x="495" y="315" text-anchor="middle" font-size="9">40+</text>
</svg>

#### Conclusión Esperada

> La mayoría de los clientes hacen pocos pedidos (1-5). Hay una distribución de "cola larga" donde pocos clientes hacen muchos pedidos (algunos llegan a más de 100 pedidos). Esto indica que hay un grupo pequeño de clientes muy frecuentes (posibles clientes premium).

---

### [B3] Top 20 productos más pedidos

#### Checklist
- [ ] **[OBLIGATORIO]** Combina order_products con products (merge)
- [ ] **[OBLIGATORIO]** Agrupa por producto y cuenta pedidos
- [ ] **[OBLIGATORIO]** Muestra los 20 productos más populares con ID y nombre
- [ ] **[OBLIGATORIO]** Crea gráfico de barras

#### Código Correcto

```python
# Combinar DataFrames
df_combinado = order_products.merge(products, on='product_id')

# SOLUCIÓN 1: groupby + count
top_productos = df_combinado.groupby(['product_id', 'product_name'])['order_id'].count().sort_values(ascending=False)

# SOLUCIÓN 2: groupby + size
top_productos = df_combinado.groupby(['product_id', 'product_name']).size().sort_values(ascending=False)

# Mostrar top 20
print(top_productos.head(20))

# Crear gráfico
top_productos.head(20).plot.bar()
plt.xlabel('ID y Nombre del Producto')
plt.ylabel('Número de Pedidos')
plt.title('Top 20 Productos Más Pedidos')
plt.tight_layout()
plt.show()
```

#### Tabla de Datos Esperada

| # | product_id | product_name | Pedidos |
|---|------------|--------------|---------|
| 1 | 24852 | Banana | **66,050** |
| 2 | 13176 | Bag of Organic Bananas | **53,297** |
| 3 | 21137 | Organic Strawberries | 37,039 |
| 4 | 21903 | Organic Baby Spinach | 33,971 |
| 5 | 47209 | Organic Hass Avocado | 29,773 |
| 6 | 47766 | Organic Avocado | 24,689 |
| 7 | 47626 | Large Lemon | 21,495 |
| 8 | 16797 | Strawberries | 20,018 |
| 9 | 26209 | Limes | 19,690 |
| 10 | 27845 | Organic Whole Milk | 19,600 |

#### Gráfico Esperado

<svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="700" height="400" fill="white"/>
  <text x="350" y="25" text-anchor="middle" font-size="14" font-weight="bold">Top 20 Productos Más Pedidos</text>
  <text x="15" y="200" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 200)">Número de Pedidos</text>
  <line x1="50" y1="40" x2="50" y2="320" stroke="black" stroke-width="1"/>
  <line x1="50" y1="320" x2="680" y2="320" stroke="black" stroke-width="1"/>
  <text x="45" y="320" text-anchor="end" font-size="9">0</text>
  <text x="45" y="250" text-anchor="end" font-size="9">20k</text>
  <text x="45" y="180" text-anchor="end" font-size="9">40k</text>
  <text x="45" y="110" text-anchor="end" font-size="9">60k</text>
  <rect x="60" y="58" width="28" height="262" fill="#1f77b4"/>
  <rect x="92" y="108" width="28" height="212" fill="#1f77b4"/>
  <rect x="124" y="173" width="28" height="147" fill="#1f77b4"/>
  <rect x="156" y="185" width="28" height="135" fill="#1f77b4"/>
  <rect x="188" y="202" width="28" height="118" fill="#1f77b4"/>
  <rect x="220" y="222" width="28" height="98" fill="#1f77b4"/>
  <rect x="252" y="235" width="28" height="85" fill="#1f77b4"/>
  <rect x="284" y="240" width="28" height="80" fill="#1f77b4"/>
  <rect x="316" y="242" width="28" height="78" fill="#1f77b4"/>
  <rect x="348" y="242" width="28" height="78" fill="#1f77b4"/>
  <text x="74" y="335" text-anchor="start" font-size="7" transform="rotate(45, 74, 335)">Banana</text>
  <text x="106" y="335" text-anchor="start" font-size="7" transform="rotate(45, 106, 335)">Bag Org...</text>
  <text x="138" y="335" text-anchor="start" font-size="7" transform="rotate(45, 138, 335)">Org Str...</text>
  <text x="170" y="335" text-anchor="start" font-size="7" transform="rotate(45, 170, 335)">Org Baby...</text>
  <text x="202" y="335" text-anchor="start" font-size="7" transform="rotate(45, 202, 335)">Org Hass...</text>
</svg>

#### Conclusión Esperada

> Los productos más populares son frutas y verduras orgánicas. El Banana (66,050 pedidos) y Bag of Organic Bananas (53,297) dominan las ventas. Esto indica una fuerte preferencia por productos frescos y orgánicos en la plataforma.

---

## [C] Análisis Difícil (Obligatorio para aprobar)

> **NOTA PARA REVISORES - SECCIÓN C**: Esta sección requiere operaciones de merge entre DataFrames. Verificar que:
> 1. El estudiante entiende qué columnas se usan para unir (on='product_id', on='order_id')
> 2. El merge se hace ANTES de agrupar/filtrar (no después)
> 3. Se usa el tipo de merge correcto (inner por defecto está bien para este proyecto)
> 4. Los resultados numéricos son coherentes con los datos

---

### [C1] Artículos por pedido

#### Checklist
- [ ] **[OBLIGATORIO]** Agrupa por order_id y cuenta productos
- [ ] **[OBLIGATORIO]** Calcula distribución
- [ ] **[OBLIGATORIO]** Crea gráfico

> **Nota para revisores**: Este ejercicio NO requiere merge. Solo usa `order_products` para contar cuántos productos hay en cada pedido.

---

#### Nota Metodológica: ¿Cómo se calcula esta distribución? (Explicado paso a paso)

**Pregunta que queremos responder:** "¿Cuántos artículos suele tener un pedido típico?"

**Datos de partida:** La tabla `order_products` tiene una fila por cada producto en cada pedido:

| order_id | product_id | add_to_cart_order | reordered |
|----------|------------|-------------------|-----------|
| 100 | 5001 | 1 | 0 |
| 100 | 5002 | 2 | 1 |
| 100 | 5003 | 3 | 0 |
| 101 | 5001 | 1 | 1 |
| 101 | 5004 | 2 | 0 |
| 102 | 5002 | 1 | 1 |

**Paso 1: Contar cuántos productos tiene CADA pedido**

Agrupamos por `order_id` y contamos las filas:

```python
num_articulos = order_products.groupby('order_id')['product_id'].count()
```

Resultado del Paso 1:
| order_id | cantidad_productos |
|----------|-------------------|
| 100 | 3 |
| 101 | 2 |
| 102 | 1 |

*Interpretación: El pedido 100 tiene 3 productos, el 101 tiene 2, el 102 tiene 1.*

**Paso 2: Contar cuántos pedidos tienen X productos**

Ahora queremos saber: "¿Cuántos pedidos tienen exactamente 1 producto? ¿Cuántos tienen 2? ¿Cuántos tienen 3?"

```python
distribucion = num_articulos.value_counts().sort_index()
```

Resultado del Paso 2:
| cantidad_productos | numero_de_pedidos |
|-------------------|-------------------|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |

*Interpretación: Hay 1 pedido con 1 producto, 1 pedido con 2 productos, 1 pedido con 3 productos.*

**Paso 3: Calcular el porcentaje**

El "% del Total" responde: "Del total de pedidos, ¿qué porcentaje tiene X artículos?"

```
% del Total = (pedidos con X artículos / total de pedidos) × 100
```

**Ejemplo con datos reales:**
- Total de pedidos: ~478,000
- Pedidos con exactamente 5 artículos: 31,923
- % del Total = 31,923 / 478,000 × 100 = **6.7%**

Esto significa: **"De cada 100 pedidos que se hacen en Instacart, aproximadamente 7 tienen exactamente 5 productos."**

---

#### Código Correcto

```python
# PASO 1: Contar productos por pedido
num_articulos = order_products.groupby('order_id')['product_id'].count()

# PASO 2: Calcular distribución (cuántos pedidos tienen X productos)
distribucion = num_articulos.value_counts().sort_index()

# PASO 3 (opcional): Calcular porcentaje
total_pedidos = len(num_articulos)  # ~478,000 pedidos
porcentaje = (distribucion / total_pedidos * 100).round(1)

# Crear gráfico
distribucion.plot(kind='bar',
                  title='Artículos por Pedido',
                  xlabel='Número de Artículos',
                  ylabel='Número de Pedidos',
                  figsize=[12, 6])
plt.show()

# Filtrar para ver mejor (sin outliers extremos)
distribucion[distribucion.index < 35].plot(kind='bar',
                  title='Artículos por Pedido (1-34 artículos)',
                  xlabel='Número de Artículos',
                  ylabel='Número de Pedidos')
plt.show()
```

#### Tabla de Datos Esperada

| Artículos en el pedido | Cantidad de pedidos | % del Total | Interpretación |
|------------------------|---------------------|-------------|----------------|
| 1 | 21,847 | 4.6% | "21,847 pedidos tienen solo 1 producto" |
| 2 | 26,292 | 5.5% | "26,292 pedidos tienen exactamente 2 productos" |
| 3 | 29,046 | 6.1% | |
| 4 | 31,054 | 6.5% | |
| **5** | **31,923** | **6.7%** | **← Pico: más pedidos tienen 5 artículos** |
| **6** | **31,860** | **6.7%** | **← Segundo pico** |
| **7** | **30,852** | **6.5%** | **← Tercer pico** |
| 8 | 29,219 | 6.1% | |
| 9 | 27,067 | 5.7% | |
| 10 | 24,659 | 5.2% | |
| ... | ... | ... | La frecuencia disminuye gradualmente |
| 127 (máx) | 1 | <0.01% | "Solo 1 pedido tuvo 127 productos" |

**¿Cómo leer esta tabla?**
- Fila "5 | 31,923 | 6.7%" significa: "Hay 31,923 pedidos que contienen exactamente 5 productos, lo cual representa el 6.7% de todos los pedidos"

#### Gráfico Esperado

<svg viewBox="0 0 650 350" xmlns="http://www.w3.org/2000/svg">
  <rect width="650" height="350" fill="white"/>
  <text x="325" y="25" text-anchor="middle" font-size="14" font-weight="bold">Distribución: ¿Cuántos artículos tiene cada pedido?</text>
  <text x="15" y="175" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 175)">Cantidad de pedidos</text>
  <text x="325" y="335" text-anchor="middle" font-size="11">Número de artículos en el pedido</text>
  <line x1="50" y1="40" x2="50" y2="300" stroke="black" stroke-width="1"/>
  <line x1="50" y1="300" x2="630" y2="300" stroke="black" stroke-width="1"/>
  <text x="45" y="300" text-anchor="end" font-size="9">0</text>
  <text x="45" y="235" text-anchor="end" font-size="9">10k</text>
  <text x="45" y="170" text-anchor="end" font-size="9">20k</text>
  <text x="45" y="105" text-anchor="end" font-size="9">30k</text>
  <!-- Barra 1 artículo: 21,847 pedidos -->
  <rect x="60" y="200" width="15" height="100" fill="#1f77b4"/>
  <!-- Barra 2 artículos: 26,292 pedidos -->
  <rect x="78" y="160" width="15" height="140" fill="#1f77b4"/>
  <!-- Barra 3 artículos -->
  <rect x="96" y="130" width="15" height="170" fill="#1f77b4"/>
  <!-- Barra 4 artículos -->
  <rect x="114" y="105" width="15" height="195" fill="#1f77b4"/>
  <!-- Barra 5 artículos: 31,923 pedidos (PICO) -->
  <rect x="132" y="100" width="15" height="200" fill="#2ca02c"/>
  <!-- Barra 6 artículos: 31,860 pedidos (PICO) -->
  <rect x="150" y="98" width="15" height="202" fill="#2ca02c"/>
  <!-- Barra 7 artículos: 30,852 pedidos (PICO) -->
  <rect x="168" y="105" width="15" height="195" fill="#2ca02c"/>
  <!-- Barras 8-20 artículos (decreciendo) -->
  <rect x="186" y="115" width="15" height="185" fill="#1f77b4"/>
  <rect x="204" y="130" width="15" height="170" fill="#1f77b4"/>
  <rect x="222" y="145" width="15" height="155" fill="#1f77b4"/>
  <rect x="240" y="160" width="15" height="140" fill="#1f77b4"/>
  <rect x="258" y="175" width="15" height="125" fill="#1f77b4"/>
  <rect x="276" y="190" width="15" height="110" fill="#1f77b4"/>
  <rect x="294" y="205" width="15" height="95" fill="#1f77b4"/>
  <rect x="312" y="220" width="15" height="80" fill="#1f77b4"/>
  <rect x="330" y="232" width="15" height="68" fill="#1f77b4"/>
  <rect x="348" y="243" width="15" height="57" fill="#1f77b4"/>
  <rect x="366" y="253" width="15" height="47" fill="#1f77b4"/>
  <rect x="384" y="262" width="15" height="38" fill="#1f77b4"/>
  <rect x="402" y="270" width="15" height="30" fill="#1f77b4"/>
  <!-- Etiquetas del eje X -->
  <text x="67" y="315" text-anchor="middle" font-size="8">1</text>
  <text x="139" y="315" text-anchor="middle" font-size="8">5</text>
  <text x="211" y="315" text-anchor="middle" font-size="8">10</text>
  <text x="283" y="315" text-anchor="middle" font-size="8">15</text>
  <text x="355" y="315" text-anchor="middle" font-size="8">20</text>
  <text x="427" y="315" text-anchor="middle" font-size="8">25</text>
</svg>

**¿Cómo leer este gráfico?**
- Cada barra representa "cuántos pedidos tienen X artículos"
- La barra en posición "5" tiene altura ~32k, significa "32,000 pedidos tienen exactamente 5 artículos"
- Las barras verdes (5, 6, 7) son las más altas → es lo más común
- Las barras disminuyen hacia la derecha → pocos pedidos tienen muchos artículos

#### Conclusión Esperada

> **Hallazgo principal:** La mayoría de pedidos en Instacart contienen entre 4-10 productos.
>
> **Detalle:** El "tamaño típico de carrito" es de 5-7 productos, donde cada uno de estos valores representa ~6.7% de todos los pedidos (~32,000 pedidos cada uno).
>
> **Extremos:**
> - Hay pedidos pequeños de solo 1 producto (21,847 pedidos = 4.6%)
> - El pedido más grande observado tiene 127 productos (solo 1 pedido)
>
> **Implicación de negocio:** Instacart podría optimizar su interfaz para carritos de 5-7 productos, ya que es el comportamiento más común.

---

### [C2] Top 20 productos reordenados

#### Checklist
- [ ] **[OBLIGATORIO]** Filtra productos con reordered=1
- [ ] **[OBLIGATORIO]** Combina con products para obtener nombres
- [ ] **[OBLIGATORIO]** Muestra top 20 con ID y nombre
- [ ] **[OBLIGATORIO]** Crea gráfico

> **Nota para revisores - MERGE CRÍTICO**:
> - El merge debe hacerse con `products` usando `on='product_id'`
> - El filtro `reordered == 1` puede hacerse ANTES o DESPUÉS del merge (ambos son correctos)
> - Verificar que el estudiante usa `groupby` con `product_id` Y `product_name` juntos

---

#### Nota Metodológica: ¿Qué significa "reordenado"? (Explicado paso a paso)

**Pregunta que queremos responder:** "¿Cuáles son los productos que los clientes vuelven a pedir más frecuentemente?"

**¿Qué significa la columna `reordered`?**
- `reordered = 1`: El cliente YA había comprado este producto antes
- `reordered = 0`: Es la primera vez que el cliente compra este producto

**Ejemplo visual:**
| order_id | product_id | product_name | reordered | Significado |
|----------|------------|--------------|-----------|-------------|
| 100 | 24852 | Banana | 1 | "Este cliente ya compró Banana antes" |
| 100 | 47209 | Organic Avocado | 0 | "Primera vez que compra Avocado" |
| 101 | 24852 | Banana | 1 | "Otro cliente que repite Banana" |

**Paso 1: Filtrar solo las filas donde `reordered == 1`**
```python
productos_reordenados = order_products[order_products['reordered'] == 1]
```
Resultado: Solo las filas donde el producto fue comprado por alguien que ya lo había comprado antes.

**Paso 2: Combinar con `products` para obtener nombres**
```python
df_reordenados = productos_reordenados.merge(products, on='product_id')
```
Esto añade la columna `product_name` a cada fila.

**Paso 3: Contar cuántas veces aparece cada producto**
```python
top_reordenados = df_reordenados.groupby(['product_id', 'product_name']).size()
```

**Interpretación del resultado:**
- Si Banana tiene 55,763 → significa que 55,763 veces alguien compró Banana siendo un producto que ya había comprado antes
- NO significa que 55,763 personas diferentes compraron Banana
- Significa que hubo 55,763 "recompras" de Banana

---

#### Código Correcto

```python
# OPCIÓN A: Filtrar primero, luego merge (más eficiente)
productos_reordenados = order_products[order_products['reordered'] == 1]
df_reordenados = productos_reordenados.merge(products, on='product_id')

# OPCIÓN B: Merge primero, luego filtrar (también válido)
df_completo = order_products.merge(products, on='product_id')
df_reordenados = df_completo[df_completo['reordered'] == 1]

# Agrupar y contar
top_reordenados = df_reordenados.groupby(['product_id', 'product_name']).size().sort_values(ascending=False)

# Mostrar top 20
print(top_reordenados.head(20))

# Crear gráfico
top_reordenados.head(20).plot.bar()
plt.xlabel('ID y Nombre del Producto')
plt.ylabel('Número de Reordenes')
plt.title('Top 20 Productos Más Reordenados')
plt.tight_layout()
plt.show()
```

> **ERROR COMÚN A DETECTAR**: Si el estudiante usa solo `product_id` sin `product_name` en el groupby, el resultado será correcto numéricamente pero sin nombres de productos visibles.

#### Tabla de Datos Esperada

| # | product_id | product_name | Reordenes | % vs Total |
|---|------------|--------------|-----------|------------|
| 1 | 24852 | Banana | **55,763** | 84% |
| 2 | 13176 | Bag of Organic Bananas | **44,450** | 83% |
| 3 | 21137 | Organic Strawberries | 28,639 | 77% |
| 4 | 21903 | Organic Baby Spinach | 26,233 | 77% |
| 5 | 47209 | Organic Hass Avocado | 23,629 | 79% |
| 6 | 47766 | Organic Avocado | 18,743 | 76% |
| 7 | 27845 | Organic Whole Milk | 16,251 | 83% |
| 8 | 47626 | Large Lemon | 15,044 | 70% |
| 9 | 27966 | Organic Raspberries | 14,748 | 77% |
| 10 | 16797 | Strawberries | 13,945 | 70% |

*La columna "% vs Total" muestra qué porcentaje de las veces que se pide el producto es un reorden.*

#### Conclusión Esperada

> Los productos más reordenados son casi los mismos que los más pedidos (Banana, Organic Bananas, etc.). Esto confirma que los clientes regresan consistentemente por los mismos productos frescos y orgánicos. La tasa de reorden es alta (70-84%), indicando alta fidelidad a estos productos.

---

### [C3] Tasa de reorden por producto

#### Checklist
- [ ] **[OBLIGATORIO]** Calcula proporción de reordenes por producto
- [ ] **[OBLIGATORIO]** Muestra productos con su tasa de reorden

> **Nota para revisores - LÓGICA DEL CÁLCULO**:
> - Tasa de reorden = `sum(reordered) / count(reordered)` = `mean(reordered)`
> - Ambas fórmulas dan el mismo resultado porque `reordered` solo tiene valores 0 y 1
> - El merge con `products` es necesario para mostrar nombres

---

#### Nota Metodológica: ¿Qué es la "tasa de reorden"? (Explicado paso a paso)

**Pregunta que queremos responder:** "De todas las veces que se compra un producto, ¿qué porcentaje son recompras?"

**Diferencia con C2:**
- C2 cuenta **cantidad absoluta** de reordenes (Banana tiene 55,763 reordenes)
- C3 calcula **porcentaje/proporción** de reordenes (Banana se reordena el 84% de las veces)

**¿Por qué `mean(reordered)` = tasa de reorden?**

Cuando tienes una columna con solo 0s y 1s:
- `sum()` = cuenta cuántos 1s hay (cuántas recompras)
- `count()` = cuenta total de filas (cuántas compras totales)
- `mean()` = `sum() / count()` = proporción de 1s = tasa de reorden

**Ejemplo con datos de Banana:**

| order_id | product_name | reordered |
|----------|--------------|-----------|
| 100 | Banana | 1 |
| 101 | Banana | 1 |
| 102 | Banana | 0 |
| 103 | Banana | 1 |
| 104 | Banana | 1 |

- `sum(reordered)` = 1+1+0+1+1 = **4** recompras
- `count(reordered)` = **5** compras totales
- `mean(reordered)` = 4/5 = **0.80** = 80%

**Interpretación:** "El 80% de las veces que alguien compra Banana, ya la había comprado antes"

**¿Cómo interpretar los valores?**
- `tasa = 1.0 (100%)`: TODAS las compras de este producto son recompras. Nadie lo compra por primera vez.
- `tasa = 0.5 (50%)`: La mitad son recompras, la mitad son compras nuevas.
- `tasa = 0.0 (0%)`: TODAS las compras son de primera vez. Nadie lo vuelve a comprar.

---

#### Código Correcto

```python
# Combinar order_products con products
df_combinado = order_products.merge(products, on='product_id')

# SOLUCIÓN BÁSICA: sumar, después dividir entre el total
agrupado = df_combinado.groupby(['product_id', 'product_name'])['reordered']
tasa_reorden = agrupado.sum() / agrupado.count()

# SOLUCIÓN RÁPIDA: aplicar promedio (mean = sum/count para valores 0/1)
tasa_reorden = df_combinado.groupby(['product_id', 'product_name'])['reordered'].mean()

# Ver como DataFrame ordenado
tasa_reorden_df = tasa_reorden.sort_values(ascending=False).reset_index()
tasa_reorden_df.columns = ['product_id', 'product_name', 'tasa_reorden']
print(tasa_reorden_df)
```

> **ERROR COMÚN A DETECTAR**: Si el estudiante calcula `tasa_reorden.describe()` y obtiene `mean > 1`, algo está mal en el cálculo.

#### Tabla de Datos Esperada (muestra)

| product_id | product_name | tasa_reorden | Interpretación |
|------------|--------------|--------------|----------------|
| 12126 | Chocolate Sandwich Cookies | 0.56 | 56% son reordenes |
| 43403 | All-Seasons Salt | 0.00 | Nunca se reordena |
| 3834 | Robust Golden Unsweetened Oolong Tea | 0.74 | 74% son reordenes |
| ... | ... | ... | ... |

#### Estadísticas Esperadas

```
count    45573.000000    # ~45k productos únicos
mean         0.590000    # En promedio, 59% de compras son reordenes
std          0.280000
min          0.000000    # Algunos productos nunca se reordenan
25%          0.400000
50%          0.610000    # Mediana: 61%
75%          0.800000
max          1.000000    # Algunos siempre se reordenan
```

#### Conclusión Esperada

> La tasa de reorden (proporción de veces que un producto se vuelve a pedir vs total de veces pedido) varía ampliamente:
> - Algunos productos tienen tasa cercana a 1.0 (casi siempre se reordenan) - típicamente productos de uso diario
> - Otros tienen tasa 0.0 (nunca se reordenan) - típicamente compras únicas o productos nuevos
> - La mediana es ~0.61, indicando que en general los clientes son bastante leales a los productos

---

### [C4] Tasa de reorden por cliente

#### Checklist
- [ ] **[OBLIGATORIO]** Calcula proporción de reordenes por cliente
- [ ] **[OBLIGATORIO]** Muestra distribución de tasas de reorden

> **Nota para revisores - MERGE DIFERENTE**:
> - Aquí el merge es con `orders` usando `on='order_id'` (NO con products)
> - El objetivo es obtener `user_id` para agrupar por cliente
> - Verificar que el estudiante agrupa por `user_id`, NO por `order_id`

---

#### Nota Metodológica: ¿Cómo calcular la tasa de reorden por CLIENTE? (Explicado paso a paso)

**Pregunta que queremos responder:** "¿Qué tan leales son los clientes? ¿Qué porcentaje de sus compras son productos que ya habían comprado antes?"

**Diferencia con C3:**
- C3: Agrupa por **producto** → "¿Qué tan frecuentemente se reordena ESTE producto?"
- C4: Agrupa por **cliente** → "¿Qué tan frecuentemente ESTE cliente reordena productos?"

**¿Por qué necesitamos un MERGE diferente?**

La tabla `order_products` tiene `order_id` pero NO tiene `user_id`:
| order_id | product_id | reordered |
|----------|------------|-----------|
| 100 | 24852 | 1 |
| 100 | 47209 | 0 |

La tabla `orders` tiene la relación entre `order_id` y `user_id`:
| order_id | user_id |
|----------|---------|
| 100 | 5001 |
| 101 | 5002 |

**Paso 1: Combinar para obtener `user_id`**
```python
df_combinado = order_products.merge(orders, on='order_id')
```

Resultado:
| order_id | product_id | reordered | user_id |
|----------|------------|-----------|---------|
| 100 | 24852 | 1 | 5001 |
| 100 | 47209 | 0 | 5001 |

**Paso 2: Agrupar por `user_id` y calcular el promedio**
```python
tasa_cliente = df_combinado.groupby('user_id')['reordered'].mean()
```

**Ejemplo con el cliente 5001:**

| order_id | product_id | reordered | user_id |
|----------|------------|-----------|---------|
| 100 | 24852 | 1 | 5001 |
| 100 | 47209 | 0 | 5001 |
| 100 | 21137 | 1 | 5001 |
| 105 | 24852 | 1 | 5001 |

- Productos del cliente 5001: 4
- Reordenes (reordered=1): 3
- Tasa de reorden = 3/4 = **0.75** = 75%

**Interpretación:** "El cliente 5001 reordena el 75% de los productos que compra. Es un cliente bastante leal."

**¿Cómo interpretar los valores?**
- `tasa = 1.0`: Cliente que SOLO compra productos que ya conoce (muy leal, no experimenta)
- `tasa = 0.5`: Cliente balanceado entre productos habituales y nuevos
- `tasa = 0.0`: Cliente que nunca repite productos (nuevo o muy experimental)

---

#### Código Correcto

```python
# Combinar order_products con orders (para obtener user_id)
# IMPORTANTE: merge con orders, NO con products
df_combinado = order_products.merge(orders, on='order_id')

# SOLUCIÓN BÁSICA: sumar, después dividir entre el total
agrupado_cliente = df_combinado.groupby('user_id')['reordered']
tasa_cliente = agrupado_cliente.sum() / agrupado_cliente.count()

# SOLUCIÓN RÁPIDA: aplicar promedio
tasa_cliente = df_combinado.groupby('user_id')['reordered'].mean()

# Ver estadísticas
print(tasa_cliente.describe())

# Ver como DataFrame
tasa_cliente_df = tasa_cliente.sort_values(ascending=False).reset_index()
tasa_cliente_df.columns = ['user_id', 'tasa_reorden']
print(tasa_cliente_df)
```

> **ERROR COMÚN A DETECTAR**:
> - Si usa `merge(products)` en lugar de `merge(orders)`, no tendrá acceso a `user_id`
> - Si agrupa por `order_id` en lugar de `user_id`, calculará tasa por pedido, no por cliente

#### Tabla de Datos Esperada

| user_id | tasa_reorden | Interpretación |
|---------|--------------|----------------|
| 137587  | 1.00 | 100% de sus productos son reordenes |
| 173474  | 1.00 | Cliente muy leal |
| 13918   | 1.00 | Siempre pide lo mismo |
| ... | ... | ... |
| 165726  | 0.00 | Nunca ha reordenado (cliente nuevo) |

#### Estadísticas Esperadas

```
count    149626.000000    # ~150k clientes únicos
mean          0.494853    # En promedio, 49% de productos son reordenes
std           0.292685
min           0.000000    # Algunos clientes nunca reordenan
25%           0.272727
50%           0.500000    # Mediana: 50%
75%           0.724138
max           1.000000    # Algunos siempre reordenan
```

#### Conclusión Esperada

> En promedio, los clientes reordenan ~50% de sus productos (mean=0.49). La distribución es bastante simétrica alrededor del 50%:
> - Hay clientes que siempre reordenan (tasa=1.0) - clientes con listas de compras fijas
> - Hay clientes que nunca reordenan (tasa=0.0) - clientes nuevos o experimentales
> - La mayoría está en el rango 30-70%, indicando un balance entre productos habituales y nuevos

---

### [C5] Top 20 productos añadidos primero al carrito

#### Checklist
- [ ] **[OBLIGATORIO]** Filtra productos con add_to_cart_order=1
- [ ] **[OBLIGATORIO]** Combina con products para obtener nombres
- [ ] **[OBLIGATORIO]** Muestra top 20 con ID, nombre y conteo
- [ ] **[OBLIGATORIO]** Crea gráfico

> **Nota para revisores - VERIFICAR FILTRO**:
> - El filtro debe ser `add_to_cart_order == 1` (primer producto añadido)
> - Si el estudiante rellenó NaN con 999 en el Paso 2, este filtro funcionará correctamente
> - Si NO rellenó, habrá NaN en la columna y el filtro los excluirá automáticamente (también es correcto)

---

#### Nota Metodológica: ¿Qué significa "añadido primero"? (Explicado paso a paso)

**Pregunta que queremos responder:** "¿Cuáles son los productos que los clientes añaden PRIMERO a su carrito?"

**¿Qué significa la columna `add_to_cart_order`?**
- Es el ORDEN en que el cliente añadió cada producto al carrito
- `add_to_cart_order = 1`: Fue el PRIMER producto añadido
- `add_to_cart_order = 2`: Fue el SEGUNDO producto añadido
- Y así sucesivamente...

**Ejemplo visual:**
| order_id | product_name | add_to_cart_order | Significado |
|----------|--------------|-------------------|-------------|
| 100 | Banana | 1 | "Lo primero que el cliente añadió" |
| 100 | Leche | 2 | "Lo segundo que añadió" |
| 100 | Pan | 3 | "Lo tercero que añadió" |
| 101 | Organic Milk | 1 | "Otro cliente, también empezó con leche" |

**Paso 1: Filtrar solo los productos con `add_to_cart_order == 1`**
```python
primeros = order_products[order_products['add_to_cart_order'] == 1]
```
Resultado: Solo los productos que fueron añadidos PRIMERO en cada pedido.

**Paso 2: Combinar con `products` para obtener nombres**
```python
primeros_con_nombre = primeros.merge(products, on='product_id')
```

**Paso 3: Contar cuántas veces cada producto fue añadido primero**
```python
conteo = primeros_con_nombre.groupby(['product_id', 'product_name']).size()
```

**Interpretación del resultado:**
- Si Banana tiene 15,562 → significa que en 15,562 pedidos diferentes, Banana fue el PRIMER producto añadido al carrito
- Esto puede indicar:
  - Es el producto que la gente busca primero (prioridad mental)
  - Aparece prominentemente en la interfaz de la app
  - Es un producto "ancla" que inicia la experiencia de compra

**¿Por qué es útil este análisis?**
- Identifica productos "estrella" que inician el comportamiento de compra
- Útil para diseño de UX: ¿qué productos mostrar primero?
- Útil para marketing: ¿qué productos promocionar como "entrada"?

---

#### Código Correcto

```python
# Combinar order_products con products
df_combinado = order_products.merge(products, on='product_id')

# Filtrar productos añadidos primero al carrito
primeros_en_carrito = df_combinado[df_combinado['add_to_cart_order'] == 1]

# Contar y ordenar
conteo_primeros = primeros_en_carrito.groupby(['product_id', 'product_name']).size().sort_values(ascending=False)

# Mostrar top 20
print(conteo_primeros.head(20))

# Crear gráfico
conteo_primeros.head(20).plot.bar()
plt.xlabel('ID y Nombre del Producto')
plt.ylabel('Veces Añadido Primero')
plt.title('Top 20 Productos Añadidos Primero al Carrito')
plt.tight_layout()
plt.show()
```

> **ERROR COMÚN A DETECTAR**: Si el estudiante usa `add_to_cart_order <= 1` o incluye NaN sin darse cuenta, los números serán incorrectos.

#### Tabla de Datos Esperada

| # | product_id | product_name | Veces Primero | % del Top 1 |
|---|------------|--------------|---------------|-------------|
| 1 | 24852 | Banana | **15,562** | 100% |
| 2 | 13176 | Bag of Organic Bananas | **11,026** | 71% |
| 3 | 27845 | Organic Whole Milk | 4,363 | 28% |
| 4 | 21137 | Organic Strawberries | 3,946 | 25% |
| 5 | 47209 | Organic Hass Avocado | 3,390 | 22% |
| 6 | 21903 | Organic Baby Spinach | 3,336 | 21% |
| 7 | 47766 | Organic Avocado | 3,044 | 20% |
| 8 | 19660 | Spring Water | 2,336 | 15% |
| 9 | 16797 | Strawberries | 2,308 | 15% |
| 10 | 27966 | Organic Raspberries | 2,024 | 13% |

#### Gráfico Esperado

<svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="700" height="400" fill="white"/>
  <text x="350" y="25" text-anchor="middle" font-size="14" font-weight="bold">Top 20 Productos Añadidos Primero al Carrito</text>
  <text x="15" y="200" text-anchor="middle" font-size="11" transform="rotate(-90, 15, 200)">Veces Añadido Primero</text>
  <line x1="50" y1="40" x2="50" y2="320" stroke="black" stroke-width="1"/>
  <line x1="50" y1="320" x2="680" y2="320" stroke="black" stroke-width="1"/>
  <text x="45" y="320" text-anchor="end" font-size="9">0</text>
  <text x="45" y="250" text-anchor="end" font-size="9">5k</text>
  <text x="45" y="180" text-anchor="end" font-size="9">10k</text>
  <text x="45" y="110" text-anchor="end" font-size="9">15k</text>
  <rect x="60" y="58" width="28" height="262" fill="#2ca02c"/>
  <rect x="92" y="115" width="28" height="205" fill="#2ca02c"/>
  <rect x="124" y="230" width="28" height="90" fill="#1f77b4"/>
  <rect x="156" y="238" width="28" height="82" fill="#1f77b4"/>
  <rect x="188" y="248" width="28" height="72" fill="#1f77b4"/>
  <rect x="220" y="251" width="28" height="69" fill="#1f77b4"/>
  <rect x="252" y="257" width="28" height="63" fill="#1f77b4"/>
  <rect x="284" y="271" width="28" height="49" fill="#1f77b4"/>
  <rect x="316" y="272" width="28" height="48" fill="#1f77b4"/>
  <rect x="348" y="278" width="28" height="42" fill="#1f77b4"/>
  <text x="74" y="335" text-anchor="start" font-size="7" transform="rotate(45, 74, 335)">Banana</text>
  <text x="106" y="335" text-anchor="start" font-size="7" transform="rotate(45, 106, 335)">Bag Org B...</text>
  <text x="138" y="335" text-anchor="start" font-size="7" transform="rotate(45, 138, 335)">Org Whole...</text>
</svg>

*Nota: Las barras verdes indican productos que dominan significativamente como primera elección.*

#### Conclusión Esperada

> Banana (15,562 veces) y Bag of Organic Bananas (11,026 veces) son los productos que más frecuentemente se añaden primero al carrito. Esto puede indicar:
> 1. Son productos "ancla" que los clientes buscan primero
> 2. Aparecen prominentemente en la interfaz de la app
> 3. Son productos de compra habitual que los clientes añaden inmediatamente
>
> Organic Whole Milk ocupa el tercer lugar, sugiriendo que los lácteos también son productos de alta prioridad.

---

## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS de Paso 1 y Paso 2: 14/14
  - Al menos 3 preguntas de análisis completadas (A o B)

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 14/14
  - Secciones A y B completas (7 preguntas)
  - Al menos 2 preguntas de sección C

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 14/14
  - Secciones A, B y C completas (12 preguntas)
  - Conclusiones bien justificadas en cada sección

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook con celdas sin ejecutar secuencialmente
- No carga los 5 archivos CSV correctamente
- No usa sep=';' al cargar los datos
- No identifica ni elimina duplicados en orders
- No maneja valores ausentes en las 3 columnas requeridas
- No crea ningún gráfico de visualización
- No combina DataFrames (no usa merge) en sección B3 o C
- Código genera errores de sintaxis sin corregir
- Plagio o copia directa sin comprensión

---

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

### Errores en Carga de Datos

1. **No usar sep=';' al cargar CSV:**
   - Incorrecto: `pd.read_csv('file.csv')`
   - Correcto: `pd.read_csv('file.csv', sep=';')`
   - Consecuencia: Una sola columna con todos los datos concatenados

2. **Rutas incorrectas:**
   - Incorrecto: `pd.read_csv('instacart_orders.csv')`
   - Correcto: `pd.read_csv('/datasets/instacart_orders.csv', sep=';')`
   - Consecuencia: FileNotFoundError

### Errores en Duplicados

3. **No verificar duplicados por columna específica:**
   - Incorrecto: Solo usar `df.duplicated()`
   - Correcto: También verificar `df.duplicated(subset='order_id')`
   - Consecuencia: Puede perder duplicados parciales

4. **Eliminar nombres de productos duplicados:**
   - Incorrecto: `products.drop_duplicates(subset='product_name')`
   - Correcto: Mantener porque tienen IDs diferentes y ubicaciones distintas
   - Consecuencia: Pérdida de productos válidos

### Errores en Valores Ausentes

5. **Eliminar filas con days_since_prior_order = NaN:**
   - Incorrecto: `orders.dropna(subset=['days_since_prior_order'])`
   - Correcto: Mantener porque son primeros pedidos (order_number=1)
   - Consecuencia: Pérdida de ~28,817 primeros pedidos

6. **No convertir add_to_cart_order a int después de fillna:**
   - Incorrecto: `order_products['add_to_cart_order'].fillna(999)` (queda como float)
   - Correcto: `order_products['add_to_cart_order'].fillna(999).astype('int')`
   - Consecuencia: Tipo de dato incorrecto

### Errores en Análisis

7. **Confundir value_counts() con groupby():**
   - `value_counts()` cuenta ocurrencias de valores únicos
   - `groupby().count()` cuenta filas por grupo
   - Ambos funcionan pero tienen sintaxis diferente

8. **No ordenar por índice después de value_counts:**
   - Incorrecto: `orders['order_hour_of_day'].value_counts()` (ordenado por frecuencia)
   - Correcto: `orders['order_hour_of_day'].value_counts().sort_index()` (ordenado por hora)
   - Consecuencia: Gráfico con eje X desordenado

9. **Olvidar merge antes de mostrar nombres de productos:**
   - Incorrecto: Mostrar solo product_id sin nombre
   - Correcto: Hacer merge con products antes de agrupar
   - Consecuencia: Resultados difíciles de interpretar

### Errores en Merge (Sección C)

10. **Usar merge incorrecto para tasa de reorden por cliente:**
    - Incorrecto: `order_products.merge(products)` - no tiene user_id
    - Correcto: `order_products.merge(orders)` - tiene user_id
    - Consecuencia: No puede agrupar por cliente

11. **Hacer merge DESPUÉS de filtrar cuando debería ser antes:**
    - El orden depende del ejercicio, pero para mostrar nombres de productos el merge con products debe hacerse antes del groupby

12. **Olvidar especificar columna de merge:**
    - Incorrecto: `df1.merge(df2)` (asume columnas con mismo nombre)
    - Mejor práctica: `df1.merge(df2, on='product_id')` (explícito)
    - Consecuencia: Puede funcionar pero es ambiguo

### Errores en Visualizaciones

13. **Gráficos sin título ni etiquetas:**
    - Incorrecto: `df.plot(kind='bar')`
    - Correcto: Agregar `title=`, `xlabel=`, `ylabel=`
    - Consecuencia: Gráficos sin contexto

14. **No usar figsize para gráficos con muchas barras:**
    - Incorrecto: Gráfico con 30 barras apretadas
    - Correcto: `plt.figure(figsize=[12, 6])` o `figsize=[12, 6]` en plot
    - Consecuencia: Etiquetas ilegibles

### Errores en Interpretación

15. **No explicar el pico en 30 días:**
    - Incorrecto: Ignorar el comportamiento anómalo
    - Correcto: Explicar que es un valor tope del sistema
    - Consecuencia: Conclusión incompleta

16. **Confundir días de la semana:**
    - Incorrecto: Asumir que 0 = lunes
    - Correcto: 0 = domingo (verificar en documentación)
    - Consecuencia: Interpretación errónea de patrones semanales

---

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
