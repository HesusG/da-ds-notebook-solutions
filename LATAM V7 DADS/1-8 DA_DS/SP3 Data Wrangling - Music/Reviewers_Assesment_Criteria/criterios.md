# Criterios de Evaluación: Proyecto 3 — Data Wrangling (Música)

## Objetivo

Limpiar y preparar datos de streaming de música para análisis, aplicando técnicas fundamentales de data wrangling con pandas: exploración de datos, renombrado de columnas, manejo de valores ausentes, eliminación de duplicados explícitos e implícitos, y análisis básico con groupby.

**Requisitos previos**: Completar SP1 y SP2 (Python básico, funciones, bucles, condicionales).

**Competencias que desarrollarás**: Importación de pandas, lectura de CSV, exploración de datos (info, head, columns), preprocesamiento (renombrado, NaN, duplicados), análisis con groupby, filtrado de DataFrames, creación de funciones de análisis

> **NOTA IMPORTANTE**: Este sprint está estructurado en **etapas secuenciales** (este proyecto usa "Etapa" en lugar de "Paso"). Cada etapa tiene sub-pasos numerados (1.1, 1.2, etc.) que deben completarse correctamente. La evaluación se basa en la correcta ejecución de cada etapa con su salida esperada.

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Los datos contienen información de reproducción de música de dos ciudades: Springfield y Shelbyville. Tu tarea es limpiar los datos y analizar si el comportamiento de los usuarios (en cuanto a la música que escuchan) varía según la ciudad y el día de la semana.

## Instrucciones del proyecto

1. **Descripción de los datos:**
   - Importar pandas y leer el archivo CSV
   - Explorar estructura con info(), head(), columns
   - Identificar problemas en los datos

2. **Preprocesamiento:**
   - Corregir nombres de columnas (minúsculas, sin espacios, snake_case)
   - Identificar y reemplazar valores ausentes
   - Eliminar duplicados explícitos
   - Identificar y corregir duplicados implícitos

3. **Análisis:**
   - Comparar reproducción de canciones por ciudad
   - Comparar reproducción por día de la semana
   - Crear función para analizar combinaciones ciudad/día

## Descripción de los datos

- `userID`: identificador del usuario
- `Track`: título de la canción
- `artist`: nombre del artista
- `genre`: género de la canción
- `City`: ciudad del usuario
- `time`: hora de reproducción
- `Day`: día de la semana

</details>

## Glosario de Términos Técnicos

**pandas**: Biblioteca de Python para manipulación y análisis de datos estructurados en DataFrames.

**DataFrame**: Estructura de datos bidimensional (tabla) con filas y columnas etiquetadas.

**read_csv()**: Función de pandas para leer archivos CSV y convertirlos en DataFrame.

**info()**: Método que muestra información sobre el DataFrame: tipos de datos, valores no nulos, uso de memoria.

**head(n)**: Método que muestra las primeras n filas del DataFrame (por defecto 5).

**columns**: Atributo que devuelve los nombres de las columnas como un Index.

**isna()**: Método que detecta valores ausentes (NaN) devolviendo True/False por cada celda.

**fillna(value)**: Método que reemplaza valores NaN con el valor especificado.

**duplicated()**: Método que identifica filas duplicadas devolviendo True para duplicados.

**drop_duplicates()**: Método que elimina filas duplicadas del DataFrame.

**unique()**: Método que devuelve los valores únicos de una columna.

**nunique()**: Método que cuenta el número de valores únicos en una columna.

**replace(old, new)**: Método que reemplaza valores específicos por otros.

**groupby()**: Método que agrupa datos por una o más columnas para aplicar funciones de agregación.

**count()**: Función de agregación que cuenta el número de valores no nulos.

**Duplicados explícitos**: Filas completamente idénticas en todas sus columnas.

**Duplicados implícitos**: Valores que representan lo mismo pero escritos de forma diferente (ej: "hip-hop", "hip", "hop").

**snake_case**: Convención de nombrado que usa guiones bajos entre palabras (ej: user_id).

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO - Etapa 1: Descripción de los datos (Etapas 1.1-1.4)

#### Etapa 1.1: Importar pandas
- [ ] **[OBLIGATORIO]** Importa pandas correctamente con `import pandas as pd`

**Código correcto:**
```python
import pandas as pd
```

---

#### Etapa 1.2: Leer archivo CSV
- [ ] **[OBLIGATORIO]** Lee el archivo CSV con `pd.read_csv()`
- [ ] **[OBLIGATORIO]** Guarda el resultado en la variable `df`

**Código correcto:**
```python
df = pd.read_csv('/datasets/music_project_en.csv')
```

---

#### Etapa 1.3: Mostrar primeras filas
- [ ] **[OBLIGATORIO]** Usa `head(10)` para ver las primeras 10 filas
- [ ] **[OBLIGATORIO]** La salida muestra una tabla con 7 columnas

**Código correcto:**
```python
df.head(10)
```

**Salida esperada (primeras filas):**
```
     userID                        Track            artist   genre        City        time        Day
0  FFB692EC            Kamigata To Boots  The Mass Missile    rock  Shelbyville  20:28:33  Wednesday
1  55204538  Delayed Because of Accident  Andreas Rönnberg    rock  Springfield  14:07:09     Friday
...
```

---

#### Etapa 1.4: Obtener información general
- [ ] **[OBLIGATORIO]** Usa `info()` para ver estructura de datos
- [ ] **[OBLIGATORIO]** Identifica que hay 65079 filas y 7 columnas
- [ ] **[OBLIGATORIO]** Identifica columnas con valores nulos (Track, artist, genre)

**Código correcto:**
```python
df.info()
```

**Salida esperada:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 65079 entries, 0 to 65078
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0     userID  65079 non-null  object
 1   Track     63736 non-null  object
 2   artist    57512 non-null  object
 3   genre     63881 non-null  object
 4     City    65079 non-null  object
 5   time      65079 non-null  object
 6   Day       65079 non-null  object
```

> **Nota para revisores**: Verificar que el estudiante identifica los dos problemas en los encabezados:
> 1. Algunos en mayúsculas, otros en minúsculas
> 2. Espacios en los nombres de columnas (`  userID`, `  City  `)

---

#### Estructura General del Código (Etapa 1)
- [ ] **[OBLIGATORIO]** El código ejecuta sin errores de sintaxis
- [ ] **[OBLIGATORIO]** Todas las celdas están ejecutadas secuencialmente

---

### INTERMEDIO - Etapa 2: Preprocesamiento de los datos (Etapas 2.1-2.14)

#### Etapa 2.1: Mostrar nombres de columnas
- [ ] **[OBLIGATORIO]** Usa `df.columns` para ver los nombres

**Código correcto:**
```python
df.columns
```

**Salida esperada:**
```
Index(['  userID', 'Track', 'artist', 'genre', '  City  ', 'time', 'Day'], dtype='object')
```

> **Nota para revisores**: Los espacios en `  userID` y `  City  ` son intencionales y deben ser limpiados.

---

#### Etapa 2.2: Convertir a minúsculas con bucle for
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre `df.columns`
- [ ] **[OBLIGATORIO]** Usa `lower()` para convertir a minúsculas
- [ ] **[OBLIGATORIO]** Usa `append()` para agregar a nueva lista
- [ ] **[OBLIGATORIO]** Reasigna `df.columns = new_names`

**Código correcto:**
```python
new_names = []

for old_name in df.columns:
    lowercase_name = old_name.lower()
    new_names.append(lowercase_name)

df.columns = new_names
df.columns
```

**Salida esperada:**
```
Index(['  userid', 'track', 'artist', 'genre', '  city  ', 'time', 'day'], dtype='object')
```

---

#### Etapa 2.3: Eliminar espacios con strip()
- [ ] **[OBLIGATORIO]** Usa bucle `for` similar al anterior
- [ ] **[OBLIGATORIO]** Usa `strip()` para eliminar espacios
- [ ] **[OBLIGATORIO]** Reasigna `df.columns = new_names`

**Código correcto:**
```python
new_names = []

for old_name in df.columns:
    clean_name = old_name.strip()
    new_names.append(clean_name)

df.columns = new_names
df.columns
```

**Salida esperada:**
```
Index(['userid', 'track', 'artist', 'genre', 'city', 'time', 'day'], dtype='object')
```

---

#### Etapa 2.4: Renombrar userid a user_id (snake_case)
- [ ] **[OBLIGATORIO]** Usa `df.rename(columns={'userid': 'user_id'})`
- [ ] **[OBLIGATORIO]** Reasigna a `df` o usa `inplace=True`

**Código correcto:**
```python
df = df.rename(columns={'userid': 'user_id'})
df.columns
```

**Salida esperada:**
```
Index(['user_id', 'track', 'artist', 'genre', 'city', 'time', 'day'], dtype='object')
```

---

#### Etapa 2.5: Verificar encabezados / Contar valores ausentes
- [ ] **[OBLIGATORIO]** Usa `isna().sum()` para contar valores nulos por columna

**Código correcto:**
```python
df.isna().sum()
```

**Salida esperada:**
```
user_id       0
track      1343
artist     7567
genre      1198
city          0
time          0
day           0
dtype: int64
```

> **Nota para revisores**: Verificar que track tiene 1343, artist tiene 7567, y genre tiene 1198 valores nulos.

---

#### Etapa 2.6: Reemplazar valores ausentes con fillna()
- [ ] **[OBLIGATORIO]** Crea lista `columns_to_replace = ['track', 'artist', 'genre']`
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre las columnas
- [ ] **[OBLIGATORIO]** Usa `fillna('unknown')` para reemplazar NaN

**Código correcto:**
```python
columns_to_replace = ['track', 'artist', 'genre']

for col in columns_to_replace:
    df[col] = df[col].fillna('unknown')
```

> **ADVERTENCIA**: NO usar `df[col].fillna('unknown', inplace=True)` ya que genera FutureWarning en pandas moderno.

---

#### Etapa 2.7: Verificar que no hay valores ausentes
- [ ] **[OBLIGATORIO]** Usa `isna().sum()` nuevamente
- [ ] **[OBLIGATORIO]** Todos los valores deben ser 0

**Código correcto:**
```python
df.isna().sum()
```

**Salida esperada:**
```
user_id    0
track      0
artist     0
genre      0
city       0
time       0
day        0
dtype: int64
```

---

#### Etapa 2.8: Contar duplicados explícitos
- [ ] **[OBLIGATORIO]** Usa `duplicated().sum()` para contar duplicados
- [ ] **[OBLIGATORIO]** El resultado es 3826

**Código correcto:**
```python
df.duplicated().sum()
```

**Salida esperada:**
```
3826
```

---

#### Etapa 2.9: Eliminar duplicados explícitos
- [ ] **[OBLIGATORIO]** Usa `drop_duplicates()`
- [ ] **[OBLIGATORIO]** Usa `inplace=True` o reasigna a `df`

**Código correcto:**
```python
df.drop_duplicates(inplace=True)
```

---

#### Etapa 2.10: Verificar eliminación de duplicados
- [ ] **[OBLIGATORIO]** Usa `duplicated().sum()` nuevamente
- [ ] **[OBLIGATORIO]** El resultado es 0

**Código correcto:**
```python
df.duplicated().sum()
```

**Salida esperada:**
```
0
```

---

#### Etapa 2.11: Mostrar géneros únicos
- [ ] **[OBLIGATORIO]** Usa `unique()` o `sort_values().unique()` en la columna genre
- [ ] **[OBLIGATORIO]** Identifica 269 géneros únicos (antes de limpiar)

**Código correcto:**
```python
print(df['genre'].nunique())
df['genre'].sort_values().unique()
```

**Salida esperada:**
```
269
array(['acid', 'acoustic', ... 'hip', 'hip-hop', 'hiphop', ... 'hop', ...], dtype=object)
```

> **Nota para revisores**: Verificar que el estudiante identifica los duplicados implícitos de hiphop: `hip`, `hop`, `hip-hop`

---

#### Etapa 2.12: Crear función replace_wrong_genres()
- [ ] **[OBLIGATORIO]** Define función con parámetros: `df`, `column`, `wrong_values`, `correct_value`
- [ ] **[OBLIGATORIO]** Usa bucle `for` para iterar sobre `wrong_values`
- [ ] **[OBLIGATORIO]** Usa `replace()` (NO `str.replace()`)

**Código correcto:**
```python
def replace_wrong_genres(df, column, wrong_values, correct_value):
    for g in wrong_values:
        df[column] = df[column].replace(g, correct_value)
```

> **ADVERTENCIA**: NO usar `str.replace()` ya que reemplaza subcadenas, no valores exactos. Esto causaría que "hiphop" se convierta en "hiphophop".

---

#### Etapa 2.13: Usar función para unificar hiphop
- [ ] **[OBLIGATORIO]** Llama a la función con los valores correctos
- [ ] **[OBLIGATORIO]** wrong_values = `['hip', 'hop', 'hip-hop']`
- [ ] **[OBLIGATORIO]** correct_value = `'hiphop'`

**Código correcto:**
```python
wrong_genres = ['hip', 'hop', 'hip-hop']
replace_wrong_genres(df, 'genre', wrong_genres, 'hiphop')
```

---

#### Etapa 2.14: Verificar géneros únicos después de limpieza
- [ ] **[OBLIGATORIO]** Usa `nunique()` o `unique()` nuevamente
- [ ] **[OBLIGATORIO]** Ahora hay 266 géneros únicos (3 menos que antes)

**Código correcto:**
```python
print(df['genre'].nunique())
df['genre'].sort_values().unique()
```

**Salida esperada:**
```
266
```

> **Nota para revisores**: Verificar que `hip`, `hop`, `hip-hop` ya NO aparecen en la lista, solo `hiphop`.

---

### AVANZADO - Etapa 3: Análisis (Etapas 3.1-3.6)

#### Etapa 3.1: Contar canciones por ciudad con groupby
- [ ] **[OBLIGATORIO]** Usa `groupby('city')['track'].count()`
- [ ] **[OBLIGATORIO]** Springfield tiene más canciones que Shelbyville

**Código correcto:**
```python
df.groupby('city')['track'].count()
```

**Salida esperada:**
```
city
Shelbyville    18512
Springfield    42741
Name: track, dtype: int64
```

---

#### Etapa 3.2: Observaciones sobre ciudades
- [ ] Documenta que Springfield tiene ~2.3x más reproducciones que Shelbyville

---

#### Etapa 3.3: Contar canciones por día
- [ ] **[OBLIGATORIO]** Agrupa por día y cuenta canciones
- [ ] **[OBLIGATORIO]** Filtra solo Monday y Friday

**Código correcto:**
```python
df.groupby('day')['track'].count().loc[['Monday', 'Friday']]
```

**Salida esperada:**
```
day
Friday    21840
Monday    21354
Name: track, dtype: int64
```

---

#### Etapa 3.4: Observaciones sobre días
- [ ] Documenta que viernes tiene ligeramente más reproducciones que lunes

---

#### Etapa 3.5: Crear función number_tracks()
- [ ] **[OBLIGATORIO]** Define función `number_tracks(day, city)` con 2 parámetros
- [ ] **[OBLIGATORIO]** Filtra por día Y por ciudad
- [ ] **[OBLIGATORIO]** Cuenta user_id y retorna el resultado

**Código correcto (solución básica - filtrado secuencial):**
```python
def number_tracks(day, city):
    # Filtra por día
    track_list = df[df['day'] == day]
    # Filtra por ciudad
    track_list = track_list[track_list['city'] == city]
    # Cuenta y retorna
    track_list_count = track_list['user_id'].count()
    return track_list_count
```

**Código correcto (solución avanzada - filtrado combinado):**
```python
def number_tracks(day, city):
    track_list = df[(df['day'] == day) & (df['city'] == city)]
    return track_list['user_id'].count()
```

**Código correcto (solución con query):**
```python
def number_tracks(day, city):
    return df.query("city == @city and day == @day")['user_id'].count()
```

> **Nota para revisores**: Las tres soluciones son válidas y producen el mismo resultado.

---

#### Etapa 3.6: Llamar función 4 veces
- [ ] **[OBLIGATORIO]** Llama la función para las 4 combinaciones
- [ ] **[OBLIGATORIO]** Los resultados son correctos

**Código correcto:**
```python
print(number_tracks('Monday', 'Springfield'))   # 15740
print(number_tracks('Monday', 'Shelbyville'))   # 5614
print(number_tracks('Friday', 'Springfield'))   # 15945
print(number_tracks('Friday', 'Shelbyville'))   # 5895
```

**Salidas esperadas:**
| Día | Ciudad | Resultado |
|-----|--------|-----------|
| Monday | Springfield | 15740 |
| Monday | Shelbyville | 5614 |
| Friday | Springfield | 15945 |
| Friday | Shelbyville | 5895 |

---

#### Conclusiones
- [ ] **[OBLIGATORIO]** Escribe conclusiones basadas en los datos
- [ ] Menciona patrones observados (Springfield > Shelbyville, Friday ≈ Monday)
- [ ] Responde a la pregunta: ¿varía el comportamiento según ciudad y día?

---

## Criterios de Aprobación General

**Niveles de aprobación:**

- **APROBADO**:
  - Todas las etapas completadas correctamente con las salidas esperadas
  - El código ejecuta sin errores
  - Todas las celdas ejecutadas secuencialmente

- **APROBADO CON DISTINCIÓN**:
  - Todos los criterios de APROBADO
  - Usa solución avanzada en función number_tracks() (filtrado combinado o query)
  - Documenta observaciones detalladas en cada etapa
  - Conclusiones bien fundamentadas con datos específicos

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook con celdas sin ejecutar
- No importa pandas
- No lee el archivo CSV correctamente
- No identifica ni trata valores ausentes
- No elimina duplicados explícitos
- No crea función replace_wrong_genres()
- No realiza ningún análisis con groupby
- No crea función number_tracks()
- Código genera errores de sintaxis sin corregir
- Plagio o copia directa sin comprensión

---

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

### Errores en Lectura de Datos

1. **Ruta incorrecta al archivo CSV**:
   - Incorrecto: `pd.read_csv('music_project_en.csv')` sin ruta completa
   - Correcto: `pd.read_csv('/datasets/music_project_en.csv')`
   - Consecuencia: FileNotFoundError

2. **Olvidar asignar el resultado de read_csv**:
   - Incorrecto: `pd.read_csv('/datasets/music_project_en.csv')`
   - Correcto: `df = pd.read_csv('/datasets/music_project_en.csv')`
   - Consecuencia: Los datos no se guardan para uso posterior

### Errores en Renombrado de Columnas

3. **No reasignar df.columns después del bucle**:
   - Incorrecto: Solo crear `new_names` sin asignar
   - Correcto: `df.columns = new_names`
   - Consecuencia: Las columnas mantienen nombres originales

4. **Usar rename() incorrectamente**:
   - Incorrecto: `df.rename({'userid': 'user_id'})` sin `columns=`
   - Correcto: `df.rename(columns={'userid': 'user_id'})`
   - Consecuencia: No se renombra nada

5. **Olvidar inplace=True o reasignar**:
   - Incorrecto: `df.rename(columns={'userid': 'user_id'})` sin guardar
   - Correcto: `df = df.rename(columns={'userid': 'user_id'})` o `inplace=True`
   - Consecuencia: El cambio no se aplica

### Errores en Valores Ausentes

6. **Usar dropna() en lugar de fillna()**:
   - Incorrecto: `df.dropna()` elimina filas con datos valiosos
   - Correcto: `df['col'] = df['col'].fillna('unknown')`
   - Consecuencia: Pérdida de datos

7. **Aplicar fillna a todo el DataFrame**:
   - Incorrecto: `df.fillna('unknown')` afecta todas las columnas
   - Correcto: Aplicar solo a columnas específicas
   - Consecuencia: Puede introducir valores incorrectos en columnas numéricas

8. **Usar inplace con vista temporal (FutureWarning)**:
   - Incorrecto: `df[col].fillna('unknown', inplace=True)`
   - Correcto: `df[col] = df[col].fillna('unknown')`
   - Consecuencia: Warning y posible comportamiento inesperado en pandas futuro

### Errores en Duplicados

9. **Confundir duplicated() con drop_duplicates()**:
   - `duplicated()` identifica duplicados (retorna True/False)
   - `drop_duplicates()` elimina duplicados
   - Consecuencia: Usar el método incorrecto

10. **Usar str.replace() para duplicados implícitos**:
    - Incorrecto: `df['genre'].str.replace('hip', 'hiphop')` reemplaza subcadenas
    - Correcto: `df['genre'].replace('hip', 'hiphop')` reemplaza valores exactos
    - Consecuencia: Reemplaza parcialmente valores como "hiphop" → "hiphophop"

### Errores en Groupby

11. **Olvidar especificar columna después de groupby**:
    - Incorrecto: `df.groupby('city').count()` cuenta todas las columnas
    - Correcto: `df.groupby('city')['track'].count()`
    - Consecuencia: Resultados confusos con múltiples columnas

12. **No usar operador & correctamente en filtros**:
    - Incorrecto: `df[df['day'] == 'Monday' and df['city'] == 'Springfield']`
    - Correcto: `df[(df['day'] == 'Monday') & (df['city'] == 'Springfield')]`
    - Consecuencia: ValueError por ambigüedad

### Errores en Funciones

13. **Función que modifica variable global**:
    - Incorrecto: Función que depende de `df` global sin parámetro
    - Correcto: Pasar df como parámetro o documentar dependencia clara
    - Consecuencia: Función no reutilizable en otros contextos

14. **No retornar valor de la función**:
    - Incorrecto: `def number_tracks(day, city): df[...].count()` sin return
    - Correcto: `return df[...].count()`
    - Consecuencia: La función retorna None

---

## Resumen de Salidas Esperadas por Etapa

| Etapa | Verificación | Valor Esperado |
|-------|--------------|----------------|
| 1.4 | Filas totales | 65079 |
| 2.5 | NaN en track | 1343 |
| 2.5 | NaN en artist | 7567 |
| 2.5 | NaN en genre | 1198 |
| 2.7 | NaN total | 0 (todas las columnas) |
| 2.8 | Duplicados | 3826 |
| 2.10 | Duplicados después | 0 |
| 2.11 | Géneros únicos | 269 |
| 2.14 | Géneros únicos después | 266 |
| 3.1 | Springfield tracks | 42741 |
| 3.1 | Shelbyville tracks | 18512 |
| 3.6 | Monday Springfield | 15740 |
| 3.6 | Monday Shelbyville | 5614 |
| 3.6 | Friday Springfield | 15945 |
| 3.6 | Friday Shelbyville | 5895 |

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
