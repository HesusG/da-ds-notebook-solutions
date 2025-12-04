# Criterios de Evaluación: DA_Final - Caso Principal: Descomposición de Tareas (Versión Completa)

## Objetivo

Construir un documento exhaustivo de planificación que establezca todos los pasos necesarios para resolver el problema de negocio, demostrando profundo entendimiento del contexto empresarial, análisis riguroso de los datos disponibles, y una estrategia detallada de análisis.

**Requisitos previos**: Haber completado todos los sprints previos del bootcamp de Data Analyst

**Competencias que desarrollarás**: Planificación de proyectos analíticos, entendimiento de problemas de negocio, formulación de hipótesis estadísticas, definición de KPIs, diagnóstico de datos, identificación de stakeholders

<details>
<summary>Requisitos del Entregable</summary>

## Descripción del Entregable

La Descomposición de Tareas debe ser un **Jupyter Notebook** con las siguientes 6 secciones obligatorias:

1. **Identificación del problema de negocio**
   - Reformulación del problema
   - Valor/importancia del análisis
   - Investigación del sector

2. **Descripción de los datos**
   - Volumen (filas, columnas, tablas)
   - Calidad (NaN, duplicados, tipos)
   - Resumen estadístico completo
   - Variables de mayor interés

3. **Hipótesis a validar**
   - Estructura H0/H1
   - Medibles y verificables
   - Métodos de comprobación

4. **Indicadores clave (KPIs)**
   - Definición con fórmulas
   - Vinculados a hipótesis

5. **Acciones a ejecutar**
   - ≥4 actividades de limpieza
   - ≥4 actividades de análisis
   - ≥2 actividades de comunicación
   - Tiempos estimados

6. **Stakeholders impactados**
   - Roles/áreas identificados
   - Justificación de selección

</details>

## Glosario de Términos Técnicos

**KPI (Key Performance Indicator)**: Indicador clave de rendimiento. Métrica cuantificable que permite evaluar el éxito. Debe ser específico, medible y vinculado a objetivos de negocio.

**Hipótesis Nula (H0)**: Afirmación inicial que asume que no hay efecto o diferencia. Se busca rechazarla mediante evidencia estadística con p < α.

**Hipótesis Alternativa (H1)**: Afirmación opuesta a H0. Puede ser de una cola (mayor que / menor que) o dos colas (diferente de).

**Stakeholder**: Persona, grupo o área interesada en los resultados del análisis. Se clasifican en directos (usuarios) e indirectos (afectados).

**EDA (Exploratory Data Analysis)**: Análisis exploratorio para entender estructura, calidad y patrones antes del análisis formal.

**Descomposición de tareas**: Técnica de planificación que divide un proyecto en actividades específicas, estimables y asignables.

**Valor de negocio**: Beneficio cuantificable (ingresos, ahorro, eficiencia) que genera el análisis para la organización.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**Identificación del Problema**
- [ ] **[OBLIGATORIO]** Identifica problema de negocio concreto (no copia literal)
- [ ] **[OBLIGATORIO]** Explica el valor/importancia de resolver el problema
- [ ] **[OBLIGATORIO]** Reformula el problema demostrando comprensión propia

**Descripción de Datos**
- [ ] **[OBLIGATORIO]** Describe volumen de datos (filas, columnas, tablas)
- [ ] **[OBLIGATORIO]** Identifica calidad de datos (NaN, duplicados, tipos incorrectos)
- [ ] **[OBLIGATORIO]** Incluye resumen estadístico de variables principales

**Código**
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores en celdas secuenciales

**Hipótesis**
- [ ] **[OBLIGATORIO]** Plantea al menos 3 hipótesis relacionadas al problema
- [ ] **[OBLIGATORIO]** Hipótesis usan estructura H0/H1
- [ ] **[OBLIGATORIO]** Hipótesis son medibles con los datos disponibles

### INTERMEDIO (10 criterios)

**Análisis de Datos Profundo**
- [ ] Identifica variables de mayor interés (métricas vs dimensiones)
- [ ] Incluye visualizaciones exploratorias iniciales
- [ ] Analiza distribuciones de variables clave

**KPIs y Métricas**
- [ ] **[OBLIGATORIO]** Define KPIs específicos con fórmulas matemáticas
- [ ] **[OBLIGATORIO]** KPIs están vinculados a las hipótesis planteadas
- [ ] Establece umbrales o valores esperados para los KPIs

**Plan de Acción**
- [ ] Lista al menos 4 actividades de limpieza/procesamiento
- [ ] Lista al menos 4 actividades de análisis de datos
- [ ] Lista al menos 2 actividades de comunicación de resultados
- [ ] Describe métodos estadísticos a utilizar para cada hipótesis

### AVANZADO (8 criterios)

**Planificación Detallada**
- [ ] Incluye estimación de tiempos para cada actividad
- [ ] Tiempos se ajustan al límite de 2 semanas
- [ ] Incluye dependencias entre actividades

**Stakeholders y Contexto**
- [ ] Identifica stakeholders impactados
- [ ] Justifica por qué cada stakeholder es relevante
- [ ] Investiga contexto del sector donde opera la empresa

**Calidad del Documento**
- [ ] Markdown cells contextualizan cada sección adecuadamente
- [ ] Documento cuenta una historia coherente del problema a la solución

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 16/16
  - Al menos 3 criterios adicionales de los 12 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 16/16
  - Al menos 6 criterios adicionales de los 12 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 12/12 (Básico + Intermedio)
  - Al menos 5 criterios de la sección AVANZADO

---

## Ejemplos de Cumplimiento (Contexto: CallMeMaybe)

**Identificación completa del problema:**
```markdown
## 1. Identificación del Problema de Negocio

### 1.1 Contexto del Sector
Los centros de llamadas (Call Centers) son críticos para la experiencia del cliente.
La ineficiencia operativa (llamadas perdidas, esperas largas) impacta directamente
en la satisfacción (NPS) y aumenta costos operativos.

### 1.2 El Problema Específico
CallMeMaybe necesita identificar operadores ineficaces. Se considera ineficaz si:
- Tiene muchas llamadas entrantes perdidas.
- Tiene tiempos de espera prolongados.
- Realiza pocas llamadas salientes (si aplica).

### 1.3 Mi Reformulación del Problema
El objetivo es desarrollar un sistema de detección de ineficiencia que permita:
1. **Cuantificar el desempeño** de cada operador.
2. **Segmentar** a los operadores en eficaces/ineficaces.
3. **Probar estadísticamente** si las diferencias son significativas.

### 1.4 Valor del Análisis
Identificar estos patrones permitirá:
- Mejorar la asignación de turnos y capacitación.
- Reducir la tasa de abandono de llamadas.
- **Impacto potencial**: Aumentar la tasa de atención en un 15%, mejorando la retención de clientes.
```

**Descripción exhaustiva de datos:**
```python
# 1. VOLUMEN DE DATOS
print("="*60)
print("1. VOLUMEN DE DATOS")
print("="*60)

tablas = {
    'telecom_dataset': df_dataset,
    'telecom_clients': df_clients
}

for nombre, df in tablas.items():
    print(f"\n{nombre}:")
    print(f"  Filas: {df.shape[0]:,}")
    print(f"  Columnas: {df.shape[1]}")

# 2. CALIDAD DE DATOS
print("\n" + "="*60)
print("2. CALIDAD DE DATOS")
print("="*60)

# Análisis de nulos y duplicados
# ...

# 3. VARIABLES DE INTERÉS
print("\n" + "="*60)
print("3. VARIABLES DE MAYOR INTERÉS")
print("="*60)
```

```markdown
### Variables de Mayor Interés

| Variable | Tabla | Tipo | Uso |
|----------|-------|------|-----|
| operator_id | telecom_dataset | Dimensión | Identificador clave para agrupar |
| is_missed_call | telecom_dataset | Métrica | Indicador de ineficacia (True/False) |
| call_duration | telecom_dataset | Métrica | Tiempo de conversación |
| total_call_duration | telecom_dataset | Métrica | Incluye tiempo de espera |
| direction | telecom_dataset | Dimensión | Segmentación (in/out) |
```

**Hipótesis con estructura formal:**
```markdown
## 3. Hipótesis a Validar

### Hipótesis 1: Diferencia en Tiempos de Espera
- **H0**: El tiempo de espera promedio es igual para todos los operadores.
- **H1**: Existen operadores con tiempos de espera significativamente mayores.
- **Prueba**: ANOVA o Kruskal-Wallis (si no es normal).
- **KPI asociado**: Tiempo de espera promedio por operador.

### Hipótesis 2: Tasa de Llamadas Perdidas
- **H0**: La proporción de llamadas perdidas es independiente del operador.
- **H1**: Algunos operadores tienen una tasa de llamadas perdidas mayor al promedio.
- **Prueba**: Chi-cuadrado de independencia.
- **KPI asociado**: Tasa de llamadas perdidas (%).

### Hipótesis 3: Eficiencia en Llamadas Salientes
- **H0**: El número de llamadas salientes promedio es igual entre operadores.
- **H1**: Hay operadores con un volumen de llamadas salientes significativamente menor.
- **Prueba**: T-test de una cola (vs media del grupo).
- **KPI asociado**: Promedio de llamadas salientes diarias.
```

**KPIs con fórmulas:**
```markdown
## 4. Indicadores Clave (KPIs)

### KPI 1: Tasa de Llamadas Perdidas (Missed Call Rate)
$$\text{MCR}_op = \frac{\text{Llamadas Perdidas}_op}{\text{Total Llamadas Entrantes}_op} \times 100$$

**Umbral de alerta**: MCR > 10%

### KPI 2: Tiempo de Espera Promedio (Average Wait Time)
$$\text{AWT}_op = \frac{\sum (\text{Total Duration} - \text{Call Duration})_op}{\text{Total Llamadas con Espera}_op}$$

**Umbral de alerta**: AWT > 30 segundos

### KPI 3: Cantidad de Llamadas Salientes
$$\text{OutCalls}_op = \text{Conteo de llamadas con direction='out'}$$

**Umbral de alerta**: OutCalls < Promedio - 1 Desviación Estándar
```

**Plan de acción detallado:**
```markdown
## 5. Acciones a Ejecutar

### 5.1 Procesamiento y Limpieza de Datos (3 días)

| # | Actividad | Descripción | Tiempo |
|---|-----------|-------------|--------|
| 1 | Tratamiento de nulos | Analizar nulos en `operator_id`. Decidir si imputar o eliminar. | 4h |
| 2 | Conversión de tipos | `date` a datetime, `is_missed_call` a booleano/int. | 2h |
| 3 | Limpieza de duplicados | Verificar duplicados exactos en registros de llamadas. | 2h |
| 4 | Validación lógica | Filtrar llamadas con duración negativa o inconsistente. | 2h |

### 5.2 Análisis de Datos (5 días)

| # | Actividad | Hipótesis | Método | Tiempo |
|---|-----------|-----------|--------|--------|
| 5 | EDA Univariado | - | Distribución de llamadas por operador. | 4h |
| 6 | Análisis de Espera | H1 | Calcular AWT y test estadístico. | 6h |
| 7 | Análisis de Perdidas | H2 | Calcular MCR y test Chi2. | 6h |
| 8 | Análisis Salientes | H3 | Comparar volumen saliente vs media. | 4h |
| 9 | Segmentación | - | Clasificar operadores (Eficaz/Ineficaz). | 6h |

### 5.3 Comunicación de Resultados (2 días)

| # | Actividad | Descripción | Tiempo |
|---|-----------|-------------|--------|
| 10 | Visualización | Gráficos de barras comparativos por operador. | 6h |
| 11 | Informe Final | Resumen ejecutivo y recomendaciones. | 6h |

**Total estimado**: 10 días (2 semanas)
```

**Stakeholders identificados:**
```markdown
## 6. Stakeholders Impactados

### Stakeholders Directos

| Rol | Área | Interés |
|-----|------|---------|
| **Supervisor de Call Center** | Operaciones | Identificar quién necesita capacitación o feedback inmediato. |
| **Gerente de RRHH** | Recursos Humanos | Evaluar desempeño para planes de carrera o despidos. |

### Justificación
- **Supervisor**: Es el usuario final del reporte. Necesita saber *qué* operadores son ineficaces para actuar.
- **RRHH**: Necesita métricas objetivas para evaluaciones de desempeño semestrales.
```

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**

- Notebook cargado como link de Google Colab
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 16/16)
- **Copiado literal del enunciado** sin reformulación
- **Hipótesis genéricas** o inalcanzables con los datos
- **Actividades genéricas** sin relación al caso específico
- **No referencia métricas** o variables de interés
- Enfoque exclusivo técnico sin contexto de negocio
- **No incluye estimación de tiempos**
- **No identifica stakeholders**

---

## Errores Frecuentes

### En Identificación del Problema

1. **No investigar el sector**:
   - Incorrecto: Ir directo a los datos sin contexto
   - Correcto: Investigar benchmarks de Call Centers (ej: nivel de servicio estándar)
   - Consecuencia: Análisis descontextualizado

### En Hipótesis

2. **Hipótesis sin estructura estadística**:
   - Incorrecto: "Creo que el operador X es malo"
   - Correcto: H0: Tasa_perdidas_X = Tasa_promedio, H1: Tasa_perdidas_X > Tasa_promedio
   - Consecuencia: No permite prueba formal

### En KPIs

3. **KPIs sin fórmulas**:
   - Incorrecto: "Usaré la eficiencia"
   - Correcto: Eficiencia = (Llamadas Atendidas / Total Entrantes) * 100
   - Consecuencia: Ambigüedad en cálculo

### En Plan de Acción

4. **Menos actividades de las requeridas**:
   - Incorrecto: 2 de limpieza, 2 de análisis
   - Correcto: ≥4 limpieza, ≥4 análisis, ≥2 comunicación
   - Consecuencia: Plan incompleto

---

## Notas Importantes

- Este es el **primer entregable del Caso Principal**
- **Requiere aprobación** antes de continuar con la Implementación
- El plan definido aquí **guiará todo el trabajo posterior**
