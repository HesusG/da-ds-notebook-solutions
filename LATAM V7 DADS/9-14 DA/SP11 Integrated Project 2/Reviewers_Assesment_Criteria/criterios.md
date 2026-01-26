# Criterios de Evaluación: DA_11 - Proyecto Integrado 2 (Comportamiento de Usuarios y Test A/A/B)


## Objetivo

Analizar el comportamiento de los usuarios de una aplicación de entrega de alimentos mediante un embudo de ventas y evaluar los resultados de un test A/A/B (cambio de fuentes en la app) para decidir si implementar el cambio.

**Requisitos previos**: Conocimientos de Python, Pandas, Plotly/Seaborn, Estadística (Z-test para proporciones).

**Competencias que desarrollarás**: Análisis de embudos de conversión (Funnels), diseño y evaluación de experimentos A/A/B, pruebas de hipótesis para proporciones, corrección de significancia estadística.

<details>
<summary>Requisitos del Entregable</summary>

## Contenido esperado del entregable

Para que tu entregable sea aprobado, el mismo deberá ser realizado en **Jupyter Notebook** y contener al menos lo siguiente:

### 1. Preprocesamiento y Exploración
Se espera que seas capaz de:
- **Cargar y limpiar el dataset** (`logs_exp_us.csv`): Renombrar columnas, ajustar tipos de datos (fechas).
- **Filtrar datos incompletos**: Identificar el periodo de tiempo donde los datos son completos y descartar los registros antiguos.
- **Verificar la integridad del experimento**: Asegurar que no haya usuarios en múltiples grupos.

### 2. Embudo de Eventos (Funnel Analysis)
- **Identificar la secuencia de eventos**: ¿Cuál es el camino lógico del usuario? (ej. MainScreen -> Offers -> Cart -> Payment).
- **Calcular la conversión**: Tasa de conversión total y paso a paso.
- **Identificar puntos de fricción**: ¿En qué etapa se pierden más usuarios?

### 3. Análisis del Experimento (Test A/A/B)
- **Evaluar el Test A/A**: Comparar los dos grupos de control (246 y 247) para asegurar que el sistema de división de tráfico funciona correctamente.
- **Evaluar el Test A/B**: Comparar cada grupo de control con el grupo de test (248) y el grupo de control combinado con el de test.
- **Aplicar pruebas estadísticas**: Usar Z-test para diferencia de proporciones.

### 4. Conclusiones
- **Interpretar los resultados**: ¿Hay diferencias significativas?
- **Recomendación de negocio**: ¿Se debe cambiar la fuente de la aplicación?

</details>

## Glosario de Términos Técnicos

**Embudo de Conversión (Funnel)**: Representación de las etapas que recorre un usuario hasta cumplir un objetivo. Permite ver dónde abandonan el proceso.

**Test A/A**: Experimento donde ambos grupos ven la misma versión. Sirve para validar que la herramienta de testing funciona y que no hay sesgos en la división de usuarios.

**Test A/B**: Experimento donde un grupo ve la versión actual (Control) y otro la nueva (Test).

**Z-test para proporciones**: Prueba estadística para determinar si dos proporciones (ej. tasas de conversión) son significativamente diferentes.

**Corrección de Bonferroni/Holm**: Ajuste del nivel de significancia (alpha) cuando se realizan múltiples comparaciones estadísticas para evitar aumentar la probabilidad de error tipo I (falsos positivos).

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**Preprocesamiento**
- [ ] **[OBLIGATORIO]** Renombra columnas a snake_case
- [ ] **[OBLIGATORIO]** Convierte fechas a tipo datetime
- [ ] **[OBLIGATORIO]** Filtra datos antiguos (periodo incompleto)
- [ ] **[OBLIGATORIO]** Verifica usuarios duplicados entre grupos

**Embudo de Eventos**
- [ ] **[OBLIGATORIO]** Identifica secuencia lógica de eventos
- [ ] **[OBLIGATORIO]** Calcula conversión paso a paso
- [ ] **[OBLIGATORIO]** Identifica etapa con mayor pérdida

**Test A/A/B**
- [ ] **[OBLIGATORIO]** Realiza Test A/A (246 vs 247)
- [ ] **[OBLIGATORIO]** Realiza Test A/B (Control vs Test)
- [ ] **[OBLIGATORIO]** Concluye sobre el impacto del cambio

### INTERMEDIO (6 criterios)

**Calidad del Análisis**
- [ ] **[OBLIGATORIO]** Visualiza el embudo (ej. gráfico de barras o funnel chart)
- [ ] **[OBLIGATORIO]** Menciona/Aplica corrección de alpha por comparaciones múltiples
- [ ] **[OBLIGATORIO]** Interpreta correctamente el resultado del Test A/A (no debe haber diferencias)
- [ ] Analiza la cantidad de eventos por usuario

**Profundidad**
- [ ] Compara resultados con el grupo de control combinado (246+247)
- [ ] Documenta la elección del periodo de tiempo filtrado

### AVANZADO (4 criterios)

**Excelencia y Automatización**
- [ ] Crea función reutilizable para pruebas de hipótesis
- [ ] Discute el nivel de significancia y probabilidad de errores (Tipo I/II)
- [ ] Recomendación clara y fundamentada para producto
- [ ] Código eficiente y bien estructurado

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 1 criterio adicional de los 6 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (incluye los 3 obligatorios de Intermedio)
  - Al menos 3 criterios adicionales de los 4 no obligatorios restantes

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (Básico + Intermedio)
  - Al menos 3 criterios de la sección AVANZADO

---

## Aspectos negativos a evitar en el entregable

- **No filtrar datos**: Usar todo el histórico incluyendo días con datos casi nulos, lo que distorsiona el promedio diario.
- **Error en Z-test**: Usar librerías incorrectas o parámetros erróneos (ej. número de eventos en lugar de número de usuarios).
- **Ignorar fallo en A/A**: Si el Test A/A da diferencias significativas, el Test A/B no es válido, pero a veces se ignora esto.
- **Conclusiones ambiguas**: "Parece que hay diferencia" no es suficiente; se requiere "Hay diferencia estadísticamente significativa con p-value X".

---

## Ejemplos de Cumplimiento (Contexto: App Delivery)

**Filtrado de Datos:**
```python
# Determinar fecha de corte visualmente o por percentil
limit_date = pd.to_datetime('2019-08-01')
data_filtered = data[data['event_time'] >= limit_date]
print(f"Datos conservados: {len(data_filtered) / len(data):.1%}")
```

**Función de Test de Hipótesis:**
```python
from statsmodels.stats.proportion import proportions_ztest

def test_hypothesis(group1, group2, event, alpha=0.05):
    # Obtener número de éxitos (usuarios que hicieron el evento) y número de observaciones (total usuarios en el grupo)
    successes = [group1[group1['event'] == event]['user_id'].nunique(), 
                 group2[group2['event'] == event]['user_id'].nunique()]
    nobs = [group1['user_id'].nunique(), group2['user_id'].nunique()]
    
    stat, pval = proportions_ztest(successes, nobs)
    
    print(f"Evento: {event} | p-value: {pval:.4f}")
    if pval < alpha:
        print("Rechazamos H0: Hay diferencia significativa")
    else:
        print("No rechazamos H0: No hay diferencia significativa")
```

**Conclusión:**
```markdown
### Recomendación:
No implementar el cambio de fuentes.
El test A/B no mostró diferencias estadísticamente significativas en la conversión de ninguna etapa del embudo (p-value > 0.05 en todos los casos), incluso comparando con el grupo de control combinado. Dado que el cambio no mejora la conversión, no justifica el esfuerzo de implementación.
```
