# Criterios de Evaluación: DA_10 - Priorización de Hipótesis y Test A/B



## Objetivo

Priorizar una lista de hipótesis para aumentar los ingresos de una tienda en línea y analizar los resultados de un test A/B para tomar decisiones fundamentadas basadas en datos y pruebas estadísticas.

**Requisitos previos**: Conocimientos de Python, Pandas, Matplotlib/Seaborn, Estadística (pruebas de hipótesis, Mann-Whitney).

**Competencias que desarrollarás**: Priorización de backlog (ICE/RICE), análisis de test A/B, detección de anomalías, pruebas de significancia estadística, toma de decisiones basada en datos.

<details>
<summary>Requisitos del Entregable</summary>

## Contenido esperado del entregable

Para que tu entregable sea aprobado, el mismo deberá ser realizado en **Jupyter Notebook** y contener al menos lo siguiente:

### 1. Priorización de Hipótesis
Se espera que seas capaz de:
- **Cargar el dataset de hipótesis** (`hypotheses_us.csv`).
- **Calcular el framework ICE** (Impact, Confidence, Effort).
- **Calcular el framework RICE** (Reach, Impact, Confidence, Effort).
- **Comparar y explicar** los cambios en la priorización entre ambos métodos.

### 2. Análisis de Test A/B (Gráficos Acumulados)
- **Cargar los datos del test** (`orders_us.csv`, `visits_us.csv`) y verificar su integridad.
- **Calcular y graficar métricas acumuladas** por grupo:
    - Ingresos acumulados.
    - Tamaño de pedido promedio acumulado.
    - Tasa de conversión acumulada.
- **Analizar la estabilidad** de las métricas a lo largo del tiempo.

### 3. Análisis de Anomalías
- **Identificar valores atípicos** en el valor de los pedidos y el número de pedidos por usuario.
- **Definir límites** para filtrar estos datos anómalos (ej. percentiles 95 o 99).

### 4. Pruebas Estadísticas
- **Calcular la significancia estadística** de la diferencia en conversión y pedido promedio entre los grupos.
- **Realizar las pruebas con datos crudos** y con **datos filtrados** (sin anomalías).
- **Usar la prueba de Mann-Whitney** debido a la naturaleza no normal de los datos (típicamente).

### 5. Decisión Final
- **Tomar una decisión** basada en los resultados: Parar el test (éxito/fracaso) o continuarlo.

</details>

## Glosario de Términos Técnicos

**ICE/RICE**: Frameworks de priorización. ICE = (Impact * Confidence) / Effort. RICE añade Reach (Alcance) al numerador.

**Métricas Acumuladas**: Suma progresiva de una métrica a lo largo del tiempo. Ayuda a visualizar la estabilización de los datos en un test A/B.

**Mann-Whitney U Test**: Prueba estadística no paramétrica utilizada para comparar diferencias entre dos grupos independientes cuando la variable dependiente no se distribuye normalmente.

**P-value**: Probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo que la hipótesis nula es cierta. Si p-value < alpha, se rechaza la nula.

**Anomalías (Outliers)**: Datos que se desvían significativamente del resto. En e-commerce, suelen ser pedidos de valor muy alto o usuarios con un número inusual de pedidos.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**Priorización**
- [ ] **[OBLIGATORIO]** Calcula correctamente ICE
- [ ] **[OBLIGATORIO]** Calcula correctamente RICE
- [ ] **[OBLIGATORIO]** Explica el cambio de priorización (RICE vs ICE)

**Análisis Gráfico**
- [ ] **[OBLIGATORIO]** Grafica ingresos acumulados por grupo
- [ ] **[OBLIGATORIO]** Grafica pedido promedio acumulado por grupo
- [ ] **[OBLIGATORIO]** Grafica tasa de conversión acumulada por grupo

**Pruebas Estadísticas (Datos Crudos)**
- [ ] **[OBLIGATORIO]** Calcula significancia estadística de conversión (Mann-Whitney)
- [ ] **[OBLIGATORIO]** Calcula significancia estadística de pedido promedio (Mann-Whitney)
- [ ] **[OBLIGATORIO]** Interpreta los p-values correctamente

### INTERMEDIO (8 criterios)

**Calidad del Análisis**
- [ ] **[OBLIGATORIO]** Grafica la diferencia relativa acumulada (Grupo B vs A)
- [ ] **[OBLIGATORIO]** Identifica anomalías usando percentiles (95/99)
- [ ] **[OBLIGATORIO]** Crea dataset filtrado sin anomalías
- [ ] **[OBLIGATORIO]** Compara resultados estadísticos (Crudos vs Filtrados)

**Profundidad**
- [ ] Analiza la estabilidad de los gráficos acumulados
- [ ] Justifica la elección de los límites para anomalías
- [ ] Documenta el preprocesamiento de datos (duplicados, tipos)
- [ ] Código limpio y comentado

### AVANZADO (4 criterios)

**Toma de Decisiones**
- [ ] Toma una decisión clara (Parar/Continuar)
- [ ] Justifica la decisión basándose en gráficos, p-values y diferencias relativas
- [ ] Analiza el impacto de las anomalías en los resultados del test
- [ ] Presentación profesional de hallazgos

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 9/9
  - Al menos 2 criterios adicionales de los 8 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (incluye los 4 obligatorios de Intermedio)
  - Al menos 4 criterios adicionales de los 5 no obligatorios restantes

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (Básico + Intermedio)
  - Al menos 3 criterios de la sección AVANZADO

---

## Aspectos negativos a evitar en el entregable

- **Confusión en RICE/ICE**: Usar fórmulas incorrectas (ej. sumar en lugar de multiplicar componentes).
- **Datos Acumulados Incorrectos**: Graficar datos diarios en lugar de acumulados, lo que hace imposible ver la estabilización.
- **Interpretación errónea de P-value**: Concluir que hay diferencias cuando p > alpha, o viceversa.
- **Falta de Decisión**: Terminar el análisis con "aquí están los números" sin decir qué hacer con el test.
- **No filtrar anomalías**: Ignorar el impacto de los outliers en el ticket promedio (que suele ser muy sensible).

---

## Ejemplos de Cumplimiento (Contexto: Tienda en Línea)

**Cálculo de RICE:**
```python
# RICE = (Reach * Impact * Confidence) / Effort
hypotheses['RICE'] = (hypotheses['Reach'] * hypotheses['Impact'] * hypotheses['Confidence']) / hypotheses['Effort']
print(hypotheses[['hypothesis', 'RICE']].sort_values(by='RICE', ascending=False))
```

**Prueba de Mann-Whitney:**
```python
from scipy import stats

# Comparar conversión Grupo A vs Grupo B
results = stats.mannwhitneyu(ordersByUsersA['orders'], ordersByUsersB['orders'])

print('P-value: {0:.3f}'.format(results.pvalue))
if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula: hay diferencia significativa")
else:
    print("No podemos rechazar la hipótesis nula: no hay diferencia significativa")
```

**Decisión Final:**
```markdown
### Decisión: Parar la prueba y declarar victoria para el Grupo B.
Justificación:
1. La tasa de conversión del Grupo B es significativamente mayor que la del Grupo A (p-value < 0.05 tanto en datos crudos como filtrados).
2. La diferencia relativa en conversión se ha estabilizado alrededor del 15% a favor del Grupo B.
3. Aunque el ticket promedio no muestra diferencias significativas, el aumento en conversión genera más ingresos totales.
```
