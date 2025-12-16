# Criterios de Evaluación: Proyecto Megaline - Análisis de Planes Telefónicos

## Objetivo

Determinar cuál plan telefónico (Surf vs Ultimate) genera más ingresos mediante análisis estadístico, agregación de datos mensuales por usuario, implementación de reglas de negocio para cálculo de ingresos, y pruebas de hipótesis t-test para validar diferencias significativas.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Análisis estadístico con pruebas t-test, agregación de datos relacionales, implementación de reglas de negocio, análisis descriptivo comparativo, visualización de distribuciones, interpretación de p-values, recomendaciones basadas en datos

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Megaline es una empresa de telecomunicaciones que ofrece dos tarifas de prepago: **Surf** y **Ultimate**. El departamento comercial necesita saber cuál plan genera más ingresos para ajustar el presupuesto de publicidad.

Dispones de datos de 500 clientes de Megaline del año 2018 en 5 tablas relacionales: usuarios, llamadas, mensajes, internet y planes. Tu tarea es analizar el comportamiento de los clientes y determinar qué tarifa genera más ingresos mediante análisis estadístico y pruebas de hipótesis.

## Instrucciones del proyecto

1. **Prepara los datos:**
   - Carga 5 archivos CSV: megaline_calls.csv, megaline_internet.csv, megaline_messages.csv, megaline_plans.csv, megaline_users.csv
   - Examina cada tabla y busca problemas (valores ausentes, duplicados, tipos de datos incorrectos)
   - Convierte columnas de fecha a tipo datetime
   - Convierte MB a GB en tabla de planes e internet
   - Aplica reglas de redondeo (np.ceil) para llamadas individuales e internet mensual
   - Elimina llamadas con duración 0
   - Crea columna `month` en tablas de uso
   - Agrega datos por user_id y month para obtener consumos mensuales
   - Implementa función de cálculo de ingresos aplicando reglas de cada plan

2. **Analiza el comportamiento de los clientes:**
   - Calcula estadísticas descriptivas (media, mediana, std) por plan para:
     - Duración de llamadas (minutos)
     - Número de mensajes
     - Volumen de internet (GB)
     - Ingresos mensuales
   - Crea histogramas comparativos por plan
   - Crea diagramas de caja (boxplots) por plan
   - Analiza porcentaje de usuarios que exceden límites del plan
   - Identifica valores atípicos y su impacto
   - Calcula varianza por plan y mes

3. **Prueba las hipótesis:**
   - **Hipótesis 1**: El ingreso promedio de usuarios del plan Surf es diferente al de Ultimate
     - H0: ingresos promedios son iguales
     - H1: ingresos promedios son diferentes
     - Prueba: t-test independiente con α=0.05
   - **Hipótesis 2**: El ingreso promedio de usuarios del área NY-NJ es diferente al de otras regiones
     - H0: ingresos promedios son iguales por región
     - H1: ingresos promedios son diferentes por región
     - Prueba: t-test independiente con α=0.05

4. **Formula conclusiones:**
   - Identifica plan con mayor ingreso promedio por usuario
   - Compara ingresos totales vs número de usuarios
   - Recomienda estrategia para presupuesto publicitario

## Descripción de los datos

**megaline_calls.csv:**
- `id` - identificador único de llamada
- `user_id` - identificador de usuario
- `call_date` - fecha de la llamada
- `duration` - duración en minutos

**megaline_internet.csv:**
- `id` - identificador único de sesión
- `user_id` - identificador de usuario
- `session_date` - fecha de la sesión
- `mb_used` - volumen de datos usado en la sesión (MB)

**megaline_messages.csv:**
- `id` - identificador único de mensaje
- `user_id` - identificador de usuario
- `message_date` - fecha del mensaje

**megaline_plans.csv:**
- `plan_name` - nombre del plan (surf, ultimate)
- `usd_monthly_pay` - pago mensual base
- `minutes_included` - minutos incluidos
- `messages_included` - mensajes incluidos
- `mb_per_month_included` - datos incluidos (MB)
- `usd_per_minute` - costo por minuto adicional
- `usd_per_message` - costo por mensaje adicional
- `usd_per_gb` - costo por GB adicional

**megaline_users.csv:**
- `user_id` - identificador único de usuario
- `first_name` - nombre
- `last_name` - apellido
- `age` - edad
- `city` - ciudad de residencia
- `reg_date` - fecha de registro
- `plan` - nombre del plan (surf, ultimate)
- `churn_date` - fecha de cancelación (NaN si sigue activo)

</details>


## Glosario de Términos Técnicos

**T-test (Prueba t de Student)**: Prueba estadística que compara las medias de dos grupos independientes para determinar si la diferencia es estadísticamente significativa. Asume distribuciones aproximadamente normales.

**P-value (Valor p)**: Probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo que la hipótesis nula es verdadera. Si p < α (usualmente 0.05), se rechaza H0.

**Hipótesis nula (H0)**: Afirmación que asume que no hay diferencia o efecto. Se rechaza cuando la evidencia estadística es suficientemente fuerte (p < α).

**Hipótesis alternativa (H1)**: Afirmación que contradice H0, sugiriendo que existe una diferencia o efecto significativo.

**Nivel de significancia (α - alfa)**: Umbral para decidir si rechazar H0, comúnmente α=0.05 (5%). Representa la probabilidad de rechazar H0 cuando es verdadera (error tipo I).

**Agregación de datos**: Proceso de combinar múltiples registros en resúmenes estadísticos, como agrupar llamadas diarias en consumo mensual por usuario.

**np.ceil()**: Función de NumPy que redondea hacia arriba al entero más cercano. Esencial para aplicar reglas de facturación (ej: 8.52 minutos → 9 minutos).

**Boxplot/Diagrama de caja**: Visualización que muestra distribución mediante cuartiles (Q1, mediana, Q3), detectando valores atípicos fuera de 1.5×IQR.

**Varianza**: Medida de dispersión que cuantifica cuán lejos están los valores de la media. Varianza alta indica datos muy dispersos.

**Merge/Join**: Operación para combinar tablas basándose en claves comunes (ej: user_id), similar a SQL JOIN.

**GroupBy**: Operación que agrupa datos por categorías (ej: user_id, month) para calcular estadísticas por grupo.

**Equal_var parameter**: Parámetro de t-test que indica si asumir varianzas iguales. equal_var=False usa corrección de Welch para varianzas desiguales.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Carga**
- [ ] **[OBLIGATORIO]** Carga 5 archivos CSV correctamente (calls, internet, messages, plans, users)
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores (todas las celdas ejecutadas secuencialmente)
- [ ] Examina estructura de cada tabla con info() y describe()
- [ ] Identifica valores ausentes y duplicados por tabla

**Corrección de Tipos de Datos**
- [ ] **[OBLIGATORIO]** Convierte columnas de fecha a datetime (call_date, session_date, message_date, reg_date, churn_date)
- [ ] Verifica que todas las fechas sean del año 2018

### INTERMEDIO

**Transformación de Unidades**
- [ ] **[OBLIGATORIO]** Convierte mb_per_month_included de MB a GB en tabla de planes
- [ ] Convierte mb_used de MB a GB (gb_used) en tabla de internet
- [ ] Renombra columnas apropiadamente después de conversión

**Aplicación de Reglas de Negocio**
- [ ] **[OBLIGATORIO]** Aplica np.ceil() a duración de llamadas individuales (redondeo hacia arriba por llamada)
- [ ] Elimina llamadas con duración 0 (no facturables)
- [ ] Aplica np.ceil() a consumo mensual de internet (redondeo hacia arriba por mes)

**Agregación de Datos**
- [ ] **[OBLIGATORIO]** Crea columna month en tablas de uso (calls, internet, messages)
- [ ] Agrupa llamadas por user_id y month para calcular:
  - Número de llamadas (num_calls)
  - Duración total en minutos (duration)
- [ ] Agrupa mensajes por user_id y month para calcular número de mensajes (num_mess)
- [ ] Agrupa internet por user_id y month para calcular GB consumidos (gb_used con redondeo)
- [ ] Combina tablas agregadas en df_monthly con merge/join
- [ ] Rellena valores ausentes con 0 (usuarios sin actividad en cierta métrica ese mes)
- [ ] Une información de usuarios (city, plan) a df_monthly

**Cálculo de Ingresos**
- [ ] **[OBLIGATORIO]** Implementa función monthly_income() que calcula ingresos por fila
- [ ] Aplica correctamente reglas de plan Surf:
  - Pago base: $20
  - Exceso minutos: (duration - 500) × $0.03
  - Exceso mensajes: (num_mess - 50) × $0.03
  - Exceso internet: (gb_used - 15) × $10
- [ ] Aplica correctamente reglas de plan Ultimate:
  - Pago base: $70
  - Exceso minutos: (duration - 3000) × $0.01
  - Exceso mensajes: (num_mess - 1000) × $0.01
  - Exceso internet: (gb_used - 30) × $7
- [ ] Prueba función con casos de ejemplo antes de aplicar
- [ ] Crea columna income en df_monthly

**Análisis Descriptivo**
- [ ] **[OBLIGATORIO]** Separa datos por plan (df_monthly_s para Surf, df_monthly_u para Ultimate)
- [ ] Calcula estadísticas descriptivas por plan (mean, median, std) para:
  - duration
  - num_mess
  - gb_used
  - income
- [ ] Calcula porcentaje de usuarios que exceden límites por plan

**Visualizaciones**
- [ ] **[OBLIGATORIO]** Crea histogramas comparativos por plan para al menos 2 métricas
- [ ] Crea boxplots comparativos por plan para al menos 2 métricas
- [ ] Gráficos tienen títulos descriptivos

### AVANZADO

**Análisis Estadístico Profundo**
- [ ] Calcula estadísticas descriptivas por plan Y mes (groupby(['plan', 'month']))
- [ ] Calcula varianza por plan y mes
- [ ] Analiza evolución mensual con gráficos de barras
- [ ] Identifica y analiza valores atípicos con porcentajes

**Pruebas de Hipótesis**
- [ ] **[OBLIGATORIO]** Implementa prueba t-test para comparar ingresos entre planes
- [ ] Usa st.ttest_ind() con equal_var=False (corrección de Welch)
- [ ] Define α=0.05 explícitamente
- [ ] Interpreta p-value correctamente (rechaza H0 si p < α)
- [ ] **[OBLIGATORIO]** Implementa prueba t-test para comparar ingresos NY-NJ vs otras regiones
- [ ] Interpreta resultados de ambas pruebas en contexto de negocio

**Análisis de Ingresos**
- [ ] Calcula ingreso promedio mensual por usuario para cada plan
- [ ] Calcula ingresos totales 2018 por plan
- [ ] Cuenta número total de usuarios por plan
- [ ] Analiza relación entre ingresos totales, promedios y número de usuarios

**Conclusiones y Recomendaciones**
- [ ] **[OBLIGATORIO]** Identifica plan con mayor ingreso promedio por usuario
- [ ] Compara ingresos totales vs número de usuarios
- [ ] Formula recomendación específica para presupuesto publicitario
- [ ] Justifica recomendación con datos cuantitativos

**Análisis de Comportamiento**
- [ ] Analiza por qué usuarios Surf generan más ingresos totales (exceden límites)
- [ ] Analiza por qué usuarios Ultimate se mantienen dentro del plan
- [ ] Documenta diferencias de comportamiento entre planes


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 3 criterios adicionales de los 26 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 8 criterios adicionales de los 26 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 16 criterios adicionales de los 26 no obligatorios


## Ejemplos de Cumplimiento

**Conversión de MB a GB:**
```python
# En tabla de planes
df_plans['mb_per_month_included'] = df_plans['mb_per_month_included'] / 1024
df_plans = df_plans.rename(columns={'mb_per_month_included': 'gb_per_month'})

# En tabla de internet
df_int['mb_used'] = df_int['mb_used'] / 1024
df_int = df_int.rename(columns={'mb_used': 'gb_used'})
```

**Aplicación de redondeo hacia arriba:**
```python
# Redondeo por llamada individual (antes de agregar)
df_calls = df_calls[df_calls['duration'] != 0]  # Eliminar llamadas de 0 min
df_calls['duration'] = np.ceil(df_calls['duration'])

# Redondeo mensual de internet (después de agregar)
df_nint = df_int.groupby(['user_id', 'month'])['gb_used'].sum().reset_index()
df_nint['gb_used'] = df_nint['gb_used'].apply(np.ceil)  # Redondear total mensual
```

**Agregación de datos mensuales:**
```python
# Agregar llamadas por usuario por mes
df_ncalls = df_calls.groupby(['user_id', 'month'])['id'].count().reset_index()
df_ncalls = df_ncalls.rename(columns={'id': 'num_calls'})

df_mcalls = df_calls.groupby(['user_id', 'month'])['duration'].sum().reset_index()

# Agregar mensajes
df_nmess = df_mess.groupby(['user_id', 'month'])['id'].count().reset_index()
df_nmess = df_nmess.rename(columns={'id': 'num_mess'})

# Agregar internet (ya con redondeo)
df_nint = df_int.groupby(['user_id', 'month'])['gb_used'].sum().reset_index()
df_nint['gb_used'] = df_nint['gb_used'].apply(np.ceil)

# Combinar todo
df_monthly = df_nint.merge(df_nmess, on=['user_id', 'month'], how='outer')
df_monthly = df_monthly.merge(df_ncalls, on=['user_id', 'month'], how='outer')
df_monthly = df_monthly.merge(df_mcalls, on=['user_id', 'month'], how='outer')
df_monthly = df_monthly.fillna(0)  # Rellenar meses sin actividad
```

**Función de cálculo de ingresos:**
```python
def monthly_income(row):
    if row['plan'] == 'ultimate':
        income = 70  # Pago base
        if row['num_mess'] > 1000:
            income += (row['num_mess'] - 1000) * 0.01
        if row['gb_used'] > 30:
            income += (row['gb_used'] - 30) * 7
        if row['duration'] > 3000:
            income += (row['duration'] - 3000) * 0.01
        row['income'] = income
    else:  # surf
        income = 20  # Pago base
        if row['num_mess'] > 50:
            income += (row['num_mess'] - 50) * 0.03
        if row['gb_used'] > 15:
            income += (row['gb_used'] - 15) * 10
        if row['duration'] > 500:
            income += (row['duration'] - 500) * 0.03
        row['income'] = income
    return row

# Probar función con casos de ejemplo
row_test = pd.Series({'plan': 'surf', 'num_mess': 51, 'gb_used': 20,
                      'duration': 510, 'income': 0})
result = monthly_income(row_test)
print(result['income'])  # Esperado: 20 + 0.03 + 50 + 0.30 = 70.33

# Aplicar a todo el dataset
df_monthly = df_monthly.apply(monthly_income, axis=1)
```

**Prueba de hipótesis t-test:**
```python
from scipy import stats as st

alpha = 0.05

# Hipótesis 1: Comparar ingresos entre planes
h1 = st.ttest_ind(df_monthly_s['income'], df_monthly_u['income'], equal_var=False)
print(f'p-value: {h1.pvalue}')

if h1.pvalue < alpha:
    print("Se rechaza la hipótesis nula: hay diferencia significativa en ingresos")
else:
    print("No se rechaza la hipótesis nula: no hay evidencia de diferencia")

# Hipótesis 2: Comparar ingresos NY-NJ vs otras regiones
ny_nj_income = df_monthly.query('city == "New York-Newark-Jersey City, NY-NJ-PA MSA"')['income']
other_income = df_monthly.query('city != "New York-Newark-Jersey City, NY-NJ-PA MSA"')['income']

h2 = st.ttest_ind(ny_nj_income, other_income, equal_var=False)
print(f'p-value: {h2.pvalue}')

if h2.pvalue < alpha:
    print("Se rechaza H0: ingresos de NY-NJ son diferentes a otras regiones")
else:
    print("No se rechaza H0: no hay evidencia de diferencia por región")
```

**Análisis de porcentajes de exceso:**
```python
# Porcentaje de usuarios Surf que exceden límites
surf_exceed_minutes = (df_monthly_s.query('duration > 500').shape[0]
                       / df_monthly_s.shape[0] * 100)
surf_exceed_messages = (df_monthly_s.query('num_mess > 50').shape[0]
                        / df_monthly_s.shape[0] * 100)
surf_exceed_internet = (df_monthly_s.query('gb_used > 15').shape[0]
                        / df_monthly_s.shape[0] * 100)

print(f"Usuarios Surf que exceden límite de minutos: {surf_exceed_minutes:.2f}%")  # ~36%
print(f"Usuarios Surf que exceden límite de mensajes: {surf_exceed_messages:.2f}%")  # ~22%
print(f"Usuarios Surf que exceden límite de internet: {surf_exceed_internet:.2f}%")  # ~58%

# Porcentaje de usuarios Ultimate que exceden límites
ultimate_exceed_minutes = (df_monthly_u.query('duration > 3000').shape[0]
                           / df_monthly_u.shape[0] * 100)
ultimate_exceed_internet = (df_monthly_u.query('gb_used > 30').shape[0]
                            / df_monthly_u.shape[0] * 100)

print(f"Usuarios Ultimate que exceden límite de minutos: {ultimate_exceed_minutes:.2f}%")  # 0%
print(f"Usuarios Ultimate que exceden límite de internet: {ultimate_exceed_internet:.2f}%")  # ~6%
```

**Conclusión y recomendación:**
```
"Análisis de ingresos:
- Ingreso promedio mensual por usuario:
  - Surf: $60.71
  - Ultimate: $72.31 (19% mayor)

- Ingresos totales 2018:
  - Surf: $95,491.18 (333 usuarios)
  - Ultimate: $52,066.00 (157 usuarios)

- Comportamiento:
  - 58% de usuarios Surf exceden límite de internet
  - 36% de usuarios Surf exceden límite de minutos
  - Solo 6% de usuarios Ultimate exceden algún límite

**Recomendación: Aumentar presupuesto publicitario del plan Ultimate**

Razones:
1. Ingreso promedio 19% mayor ($72.31 vs $60.71)
2. Plan Ultimate tiene la mitad de usuarios pero genera ingresos consistentes
3. Si duplicamos usuarios Ultimate (157→314), ingresos proyectados: $104,132 vs $95,491
4. Usuarios Ultimate son más predecibles (no exceden límites)
5. Mayor satisfacción del cliente (no sorpresas en facturación)"
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 10/10)
- **No carga las 5 tablas** o falta alguna tabla
- **No convierte fechas a datetime** (call_date, session_date, message_date)
- **No convierte MB a GB** en planes e internet
- **No agrega datos por user_id y month** (trabaja con datos sin agregar)
- **No implementa función de cálculo de ingresos** o implementación incorrecta
- **No aplica reglas de redondeo** con np.ceil()
- **No realiza pruebas de hipótesis** o no usa t-test
- **No presenta conclusión** sobre cuál plan recomendar
- Data leakage: usa datos globales para imputar valores antes de segmentar

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Errores Críticos en Reglas de Negocio

1. **Redondear después de agregar llamadas (ERROR MÁS COMÚN)**:
   - Incorrecto: Agrupar llamadas por mes, LUEGO aplicar np.ceil() al total
   - Correcto: Aplicar np.ceil() a CADA llamada individual, LUEGO agrupar
   - Consecuencia: Cálculo incorrecto de minutos facturables, ingresos subestimados
   - Ejemplo incorrecto: 3 llamadas de 1.2 min → sum=3.6 → ceil=4 minutos
   - Ejemplo correcto: 3 llamadas de 1.2 min → ceil(1.2)×3 = 2×3 = 6 minutos

2. **Redondear antes de agregar internet (ERROR COMÚN)**:
   - Incorrecto: Aplicar np.ceil() a cada sesión de internet individual
   - Correcto: Sumar GB por mes, LUEGO aplicar np.ceil() al total mensual
   - Consecuencia: Sobrefacturación masiva de internet
   - Ejemplo incorrecto: 3 sesiones de 0.5 GB → ceil×3 = 1×3 = 3 GB
   - Ejemplo correcto: 3 sesiones de 0.5 GB → sum=1.5 → ceil=2 GB

3. **No eliminar llamadas de duración 0**:
   - Incorrecto: Incluir llamadas de 0 min en agregación
   - Correcto: Eliminar antes de agregar (`df_calls = df_calls[df_calls['duration'] != 0]`)
   - Consecuencia: Inflación artificial del número de llamadas

4. **Calcular ingresos sin aplicar límites de plan**:
   - Incorrecto: `income = duration * 0.03 + gb_used * 10`
   - Correcto: `if duration > 500: income += (duration - 500) * 0.03`
   - Consecuencia: Sobrefacturación, ingresos completamente erróneos

### Errores en Agregación de Datos

5. **No rellenar valores ausentes con 0**:
   - Incorrecto: Dejar NaN después de merge de tablas agregadas
   - Correcto: `df_monthly = df_monthly.fillna(0)`
   - Consecuencia: Usuarios sin actividad en una métrica aparecen como NaN, cálculos incorrectos

6. **Agregar por user_id sin month**:
   - Incorrecto: `df_calls.groupby('user_id')['duration'].sum()` (anual)
   - Correcto: `df_calls.groupby(['user_id', 'month'])['duration'].sum()` (mensual)
   - Consecuencia: Pierde granularidad mensual, no puede analizar evolución temporal

7. **Usar merge con how='inner' en lugar de 'outer'**:
   - Incorrecto: `df_monthly.merge(..., how='inner')` elimina usuarios sin actividad
   - Correcto: `df_monthly.merge(..., how='outer')` retiene todos los usuarios
   - Consecuencia: Pierde usuarios que no usaron cierto servicio ese mes

### Errores en Pruebas de Hipótesis

8. **Usar equal_var=True sin justificación**:
   - Incorrecto: `st.ttest_ind(a, b, equal_var=True)` asume varianzas iguales
   - Correcto: `st.ttest_ind(a, b, equal_var=False)` usa corrección de Welch
   - Consecuencia: Resultados incorrectos si varianzas son muy diferentes

9. **No definir nivel de significancia α**:
   - Incorrecto: Comparar p-value sin definir α
   - Correcto: Definir `alpha = 0.05` explícitamente antes de pruebas
   - Consecuencia: Interpretación ambigua de resultados

10. **Interpretar p-value incorrectamente**:
    - Incorrecto: "p=0.03 significa 3% de probabilidad de que H0 sea verdadera"
    - Correcto: "p=0.03 < α=0.05, por tanto se rechaza H0: hay evidencia de diferencia significativa"
    - Consecuencia: Conclusiones estadísticas erróneas

11. **Usar prueba equivocada (t-test pareado en lugar de independiente)**:
    - Incorrecto: Usar st.ttest_rel() para comparar Surf vs Ultimate
    - Correcto: Usar st.ttest_ind() porque son grupos independientes
    - Consecuencia: Prueba estadística inapropiada, resultados inválidos

### Errores en Análisis Descriptivo

12. **No separar datos por plan antes de análisis**:
    - Incorrecto: Analizar df_monthly completo sin filtrar por plan
    - Correcto: Crear df_monthly_s (Surf) y df_monthly_u (Ultimate)
    - Consecuencia: Estadísticas globales ocultan diferencias entre planes

13. **Calcular porcentajes con denominador incorrecto**:
    - Incorrecto: `df_monthly_s.query('duration > 500').shape[0] / df_monthly.shape[0]` (usa todos los usuarios)
    - Correcto: `df_monthly_s.query('duration > 500').shape[0] / df_monthly_s.shape[0]` (solo Surf)
    - Consecuencia: Porcentajes subestimados

14. **No analizar valores atípicos**:
    - Incorrecto: Ignorar outliers en boxplots sin comentar
    - Correcto: Identificar, cuantificar (%) y explicar impacto de outliers
    - Consecuencia: Análisis superficial, pierde insights importantes

### Errores en Conversión de Unidades

15. **Dividir entre 1000 en lugar de 1024**:
    - Incorrecto: `mb_used / 1000` para convertir a GB
    - Correcto: `mb_used / 1024` (1 GB = 1024 MB en computación)
    - Consecuencia: Conversión incorrecta, ingresos de internet erróneos

16. **No renombrar columnas después de conversión**:
    - Incorrecto: Convertir mb_used a GB pero dejar nombre "mb_used"
    - Correcto: Renombrar a "gb_used" después de conversión
    - Consecuencia: Confusión, código poco legible

### Errores en Conclusiones

17. **No cuantificar recomendaciones**:
    - Incorrecto: "Recomiendorecomendaría plan Ultimate porque es mejor"
    - Correcto: "Recomiendorecomendaría aumentar publicidad de Ultimate: ingreso promedio 19% mayor ($72 vs $61)"
    - Consecuencia: Recomendación vaga sin justificación cuantitativa

18. **Confundir ingresos totales con promedios**:
    - Incorrecto: "Surf es mejor porque ingresos totales son $95k vs $52k Ultimate"
    - Correcto: "Surf tiene más ingresos totales por tener más usuarios (333 vs 157), pero Ultimate tiene mayor ingreso promedio ($72 vs $61)"
    - Consecuencia: Conclusión incorrecta, no normaliza por número de usuarios

19. **No documentar por qué usuarios exceden límites**:
    - Incorrecto: Solo reportar que 58% excede límite de internet
    - Correcto: Analizar que límite Surf (15GB) es bajo vs consumo típico (~17GB promedio)
    - Consecuencia: No genera insights sobre adecuación de planes

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
