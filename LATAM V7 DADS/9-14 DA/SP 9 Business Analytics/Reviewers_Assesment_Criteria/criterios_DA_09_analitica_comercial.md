# Criterios de Evaluación: DA_9 - Analítica Comercial (Yandex.Afisha)



## Objetivo

Ayudar al departamento de marketing de Yandex.Afisha a optimizar sus gastos de marketing analizando cómo los usuarios utilizan el producto, cuándo empiezan a comprar, cuánto dinero aporta cada cliente (LTV) y cuándo se recuperan los gastos de captación (ROI/ROMI).

**Requisitos previos**: Conocimientos de Python, Pandas, Matplotlib/Seaborn y métricas de negocio (LTV, CAC, ROMI).

**Competencias que desarrollarás**: Preprocesamiento de datos, análisis de cohortes, cálculo de métricas de negocio, visualización de datos, interpretación de resultados para toma de decisiones.

<details>
<summary>Requisitos del Entregable</summary>

## Contenido esperado del entregable

Para que tu entregable sea aprobado, el mismo deberá ser realizado en **Jupyter Notebook** y contener al menos lo siguiente:

### 1. Preprocesamiento de datos
Se espera que seas capaz de:
- **Cargar los datasets** correctamente (`visits_log.csv`, `orders_log.csv`, `costs.csv`).
- **Convertir tipos de datos**, especialmente las fechas a `datetime`.
- **Identificar y tratar duplicados** y valores ausentes si los hubiera.

### 2. Análisis de Producto (Métricas de Uso)
- **Calcular métricas de usuario**: DAU (Daily Active Users), WAU (Weekly Active Users) y MAU (Monthly Active Users).
- **Analizar la frecuencia de visitas** y la duración promedio de la sesión (ASL).
- **Calcular la tasa de retención** (Retention Rate) utilizando análisis de cohortes.

### 3. Análisis de Ventas (Métricas de Negocio)
- **Analizar el tiempo hasta la primera compra**: ¿Cuánto tardan los usuarios en convertirse en clientes?
- **Calcular el número de compras** por cliente y el ticket promedio.
- **Calcular el LTV (Lifetime Value)**: Valor de vida del cliente, desglosado por cohortes mensuales.

### 4. Análisis de Marketing (Métricas de Costos y Retorno)
- **Calcular el CAC (Coste de Adquisición de Clientes)**: Desglosado por fuente de tráfico.
- **Calcular el ROMI (Return on Marketing Investment)**: Retorno de la inversión, desglosado por cohortes y fuentes.

### 5. Conclusiones y Recomendaciones
- **Sintetizar los hallazgos**: ¿Qué fuentes son rentables? ¿Cuándo se recupera la inversión?
- **Dar recomendaciones accionables**: Sugerencias para redistribuir el presupuesto de marketing.

</details>

## Glosario de Términos Técnicos

**LTV (Lifetime Value)**: Ingresos totales esperados de un cliente durante toda su relación con la empresa. En este proyecto se calcula acumulativamente por cohortes.

**CAC (Customer Acquisition Cost)**: Costo total de marketing dividido por el número de clientes adquiridos.

**ROMI (Return on Marketing Investment)**: (Ingresos - Costos) / Costos. Indica la rentabilidad de la inversión. A veces se simplifica como LTV / CAC.

**Cohorte**: Grupo de usuarios que comparten una característica común en un periodo de tiempo (ej. usuarios que hicieron su primera visita en enero).

**DAU/WAU/MAU**: Usuarios activos diarios, semanales y mensuales. Métricas clave de "stickiness" o adherencia.

**Retention Rate**: Porcentaje de usuarios de una cohorte que regresan en periodos subsiguientes.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**Carga y Preprocesamiento**
- [ ] **[OBLIGATORIO]** Carga correctamente los 3 archivos de datos
- [ ] **[OBLIGATORIO]** Convierte columnas de fecha a tipo `datetime`
- [ ] **[OBLIGATORIO]** Verifica y maneja duplicados/nulos

**Métricas de Producto**
- [ ] **[OBLIGATORIO]** Calcula y visualiza DAU, WAU y MAU
- [ ] **[OBLIGATORIO]** Calcula la duración promedio de sesión (ASL)
- [ ] **[OBLIGATORIO]** Calcula y visualiza la Tasa de Retención (Retention Rate)

**Métricas de Ventas y Marketing**
- [ ] **[OBLIGATORIO]** Calcula el tiempo promedio a la primera compra
- [ ] **[OBLIGATORIO]** Calcula el LTV por cohortes
- [ ] **[OBLIGATORIO]** Calcula el CAC por fuente
- [ ] **[OBLIGATORIO]** Calcula el ROMI por cohortes y fuente

### INTERMEDIO (8 criterios)

**Calidad del Análisis y Visualización**
- [ ] **[OBLIGATORIO]** Usa gráficos adecuados (líneas para tendencias, mapas de calor para cohortes)
- [ ] **[OBLIGATORIO]** Implementa correctamente el análisis de cohortes (separando por mes de inicio)
- [ ] **[OBLIGATORIO]** Interpreta textualmente cada gráfico/cálculo (no solo código)
- [ ] Analiza métricas por dispositivo (Desktop vs Touch)

**Profundidad**
- [ ] Identifica el punto de equilibrio (Payback Period) en el análisis de ROMI
- [ ] Compara el CAC entre diferentes fuentes de tráfico
- [ ] Analiza la estacionalidad en las métricas de uso (si aplica)
- [ ] Documenta decisiones de análisis con celdas markdown

### AVANZADO (5 criterios)

**Excelencia y Valor de Negocio**
- [ ] Conclusiones accionables: recomienda qué fuentes potenciar/reducir
- [ ] Identifica fuentes con alto volumen pero bajo retorno (o viceversa)
- [ ] Propone una redistribución del presupuesto basada en datos
- [ ] Presentación ejecutiva: introducción clara, estructura navegable, conclusión final sólida
- [ ] Código optimizado y limpio (uso de funciones, comentarios claros)

---
                                zzz
## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 2 criterios adicionales de los 9 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (incluye los 3 obligatorios de Intermedio)
  - Al menos 4 criterios adicionales de los 6 no obligatorios restantes

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (Básico + Intermedio)
  - Al menos 3 criterios de la sección AVANZADO

---

## Aspectos negativos a evitar en el entregable

- **Cálculo incorrecto de LTV**: Sumar ingresos totales sin dividir por el tamaño de la cohorte inicial, o no hacerlo acumulativo.
- **Confusión en ROMI**: No considerar el factor tiempo (cuándo se recupera la inversión).
- **Gráficos ilegibles**: Mapas de calor sin etiquetas de tiempo, ejes sin nombre, o escalas que distorsionan los datos.
- **Falta de conclusiones**: Entregar solo código y gráficos sin explicar qué significan para el negocio.
- **Código repetitivo**: No usar funciones para cálculos repetitivos (ej. para diferentes fuentes).

---

## Ejemplos de Cumplimiento (Contexto: Yandex.Afisha)

**Cálculo de LTV (Cohortes):**
```python
# Agrupar por cohorte (mes de primera compra) y mes del pedido
cohorts = orders.groupby(['first_order_month', 'order_month']).agg({'revenue': 'sum', 'uid': 'nunique'})
# Calcular ingreso acumulado
cohorts['revenue_cumsum'] = cohorts.groupby(level=0)['revenue'].cumsum()
# Calcular LTV (Ingreso acumulado / Usuarios iniciales de la cohorte)
# Nota: Se requiere tener el tamaño de la cohorte inicial (n_buyers) previamente calculado
cohorts['ltv'] = cohorts['revenue_cumsum'] / cohorts['n_buyers']
```

**Visualización de Retención (Heatmap):**
```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(13, 9))
plt.title('Retention Rate')
sns.heatmap(retention_pivot, annot=True, fmt='.1%', linewidths=1, linecolor='gray')
plt.show()
```

**Conclusión de Negocio:**
```markdown
### Conclusión:
La fuente de tráfico 3 tiene el CAC más alto (15.0) y un ROMI que no llega a 1.0 incluso después de 6 meses.
Recomendación: Reducir la inversión en la fuente 3 y redistribuir el presupuesto a la fuente 4, que tiene un CAC bajo y recupera la inversión en el segundo mes.
```
