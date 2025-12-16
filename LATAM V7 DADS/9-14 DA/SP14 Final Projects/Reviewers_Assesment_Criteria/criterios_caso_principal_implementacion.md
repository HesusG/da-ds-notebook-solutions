# Criterios de Evaluación: DA_Final - Caso Principal: Implementación (Versión Completa)

## Objetivo

Materializar exhaustivamente el plan definido en la Descomposición de Tareas mediante una implementación analítica completa que dé solución al problema de negocio, aplicando todas las técnicas aprendidas en el bootcamp y generando entregables de calidad profesional.

**Requisitos previos**: Aprobación de la Descomposición de Tareas

**Competencias que desarrollarás**: Limpieza avanzada de datos, análisis estadístico descriptivo e inferencial, visualización profesional, pruebas de hipótesis, storytelling con datos, dashboards interactivos, comunicación ejecutiva

<details>
<summary>Requisitos del Entregable</summary>

## Descripción del Entregable

La Implementación consiste en **3 componentes obligatorios**:

1. **Jupyter Notebook**: Análisis completo con código estructurado
2. **Dashboard**: Tablero interactivo con KPIs principales
3. **Informe Final**: Documento ejecutivo con estructura CAR

</details>

## Glosario de Términos Técnicos

**Estructura CAR**: Challenge (contexto y problema), Action (metodología y acciones), Results (hallazgos, impacto, recomendaciones).

**Inferencia Estadística**: Proceso de extraer conclusiones sobre una población a partir de una muestra usando pruebas de hipótesis.

**p-value**: Probabilidad de obtener resultados tan extremos como los observados si H0 fuera verdadera. p < α → rechazar H0.

**Significancia (α)**: Umbral para rechazar H0. Típicamente 0.05 (5% de probabilidad de error tipo I).

**Dashboard**: Tablero visual que presenta métricas clave de forma interactiva, permitiendo filtros y drill-down.

**Storytelling con datos**: Técnica de comunicación que usa datos y visualizaciones para contar una historia persuasiva.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (12 criterios obligatorios)

**Notebook - Código**
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores en celdas secuenciales
- [ ] **[OBLIGATORIO]** Código estructurado de forma organizada y didáctica
- [ ] **[OBLIGATORIO]** Usa funciones para automatizar procesos repetitivos
- [ ] **[OBLIGATORIO]** Usa bucles y condicionales apropiadamente

**Notebook - Análisis Descriptivo**
- [ ] **[OBLIGATORIO]** Incluye análisis estadístico descriptivo completo
- [ ] **[OBLIGATORIO]** Incluye visualizaciones claras para diagnosticar patrones
- [ ] **[OBLIGATORIO]** Visualizaciones tienen títulos, ejes etiquetados, leyendas

**Notebook - Inferencia**
- [ ] **[OBLIGATORIO]** Realiza pruebas estadísticas para validar hipótesis del plan
- [ ] **[OBLIGATORIO]** Justifica los tipos de pruebas utilizadas
- [ ] **[OBLIGATORIO]** Interpreta correctamente los resultados (p-value, conclusión)

**Entregables Adicionales**
- [ ] **[OBLIGATORIO]** Dashboard presenta KPIs definidos en el plan
- [ ] **[OBLIGATORIO]** Informe sigue estructura CAR

### INTERMEDIO (10 criterios)

**Notebook - Calidad**
- [ ] Buen uso de celdas markdown que explican el "qué" y "por qué"
- [ ] Hilo conductor claro: problema → análisis → conclusiones
- [ ] Código es limpio, legible y comentado donde necesario
- [ ] Coherente con el plan de la Descomposición aprobada

**Dashboard**
- [ ] **[OBLIGATORIO]** Dashboard es claro y entendible para stakeholders no técnicos
- [ ] Permite filtrar o agrupar por variables relevantes
- [ ] Incluye contexto/explicación de cada KPI
- [ ] Es compartible (link público o archivo exportable)

**Informe**
- [ ] **[OBLIGATORIO]** Incluye conclusiones con impacto concreto en el negocio
- [ ] **[OBLIGATORIO]** Incluye recomendaciones accionables

### AVANZADO (8 criterios)

**Calidad Analítica**
- [ ] Verifica supuestos de las pruebas estadísticas (normalidad, varianzas)
- [ ] Usa pruebas alternativas si supuestos no se cumplen
- [ ] Calcula e interpreta tamaño del efecto, no solo significancia
- [ ] Considera múltiples factores/variables en el análisis

**Calidad de Comunicación**
- [ ] Conclusiones son implicancias, no descripciones de resultados
- [ ] Informe es conciso (no replica todo el notebook)
- [ ] Formato profesional (PDF/Word/Slides/Quarto)
- [ ] Visualizaciones profesionales y autoexplicativas

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 16/16
  - Al menos 3 criterios adicionales de los 14 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 16/16
  - Al menos 7 criterios adicionales de los 14 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 15/15 (Básico + Intermedio)
  - Al menos 5 criterios de la sección AVANZADO

---

## Ejemplos de Cumplimiento

**Función documentada para automatizar:**
```python
def analizar_variacion_yoy(df, columna_fecha, columna_valor, columna_grupo=None):
    """
    Calcula la variación Year-over-Year de una métrica.

    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con los datos
    columna_fecha : str
        Nombre de la columna con fechas
    columna_valor : str
        Nombre de la columna con la métrica a analizar
    columna_grupo : str, opcional
        Columna para agrupar (ej: 'category')

    Retorna:
    --------
    pd.DataFrame
        DataFrame con período, valor actual, valor anterior y variación %

    Ejemplo:
    --------
    >>> variacion = analizar_variacion_yoy(df, 'date', 'revenue', 'category')
    """
    df = df.copy()
    df['year'] = df[columna_fecha].dt.year
    df['week'] = df[columna_fecha].dt.isocalendar().week

    if columna_grupo:
        grouped = df.groupby(['year', 'week', columna_grupo])[columna_valor].sum().unstack(0)
    else:
        grouped = df.groupby(['year', 'week'])[columna_valor].sum().unstack()

    # Obtener años disponibles
    years = sorted(grouped.columns)
    if len(years) < 2:
        raise ValueError("Se necesitan al menos 2 años de datos")

    current_year = years[-1]
    previous_year = years[-2]

    result = pd.DataFrame({
        'actual': grouped[current_year],
        'anterior': grouped[previous_year]
    })
    result['variacion_pct'] = ((result['actual'] - result['anterior'])
                                / result['anterior'] * 100).round(2)

    return result
```

**Prueba estadística con verificación de supuestos:**
```python
from scipy import stats
import numpy as np

def prueba_hipotesis_variacion_categoria(df, categoria_interes, alpha=0.05):
    """
    Prueba si una categoría tiene variación significativamente diferente al resto.

    H0: La variación de la categoría es igual al promedio de las demás
    H1: La variación de la categoría es diferente (dos colas)
    """

    # Datos
    cat_interes = df[df['category'] == categoria_interes]['variacion_pct']
    otras = df[df['category'] != categoria_interes]['variacion_pct']

    print(f"="*60)
    print(f"PRUEBA DE HIPÓTESIS: {categoria_interes} vs Otras categorías")
    print(f"="*60)

    print(f"\nDatos:")
    print(f"  {categoria_interes}: n={len(cat_interes)}, media={cat_interes.mean():.2f}%")
    print(f"  Otras: n={len(otras)}, media={otras.mean():.2f}%")

    # 1. VERIFICAR SUPUESTOS
    print(f"\n--- Verificación de Supuestos ---")

    # Normalidad (Shapiro-Wilk para n < 50, o evaluación visual)
    if len(cat_interes) >= 3:
        stat_cat, p_cat = stats.shapiro(cat_interes)
        print(f"Normalidad {categoria_interes}: p={p_cat:.4f} {'✓' if p_cat > 0.05 else '✗'}")
    if len(otras) >= 3:
        stat_otras, p_otras = stats.shapiro(otras)
        print(f"Normalidad Otras: p={p_otras:.4f} {'✓' if p_otras > 0.05 else '✗'}")

    # Homocedasticidad (Levene)
    stat_lev, p_lev = stats.levene(cat_interes, otras)
    print(f"Homogeneidad varianzas (Levene): p={p_lev:.4f} {'✓' if p_lev > 0.05 else '✗'}")

    # 2. SELECCIONAR PRUEBA APROPIADA
    print(f"\n--- Selección de Prueba ---")

    normalidad_ok = (p_cat > 0.05) and (p_otras > 0.05)
    varianzas_ok = p_lev > 0.05

    if normalidad_ok and varianzas_ok:
        # Datos normales, varianzas iguales: t-test clásico
        stat, p_value = stats.ttest_ind(cat_interes, otras)
        prueba_usada = "t-test (Student)"
    elif normalidad_ok and not varianzas_ok:
        # Datos normales, varianzas diferentes: Welch t-test
        stat, p_value = stats.ttest_ind(cat_interes, otras, equal_var=False)
        prueba_usada = "t-test (Welch)"
    else:
        # Datos no normales: Mann-Whitney U
        stat, p_value = stats.mannwhitneyu(cat_interes, otras, alternative='two-sided')
        prueba_usada = "Mann-Whitney U"

    print(f"Prueba seleccionada: {prueba_usada}")

    # 3. RESULTADOS
    print(f"\n--- Resultados ---")
    print(f"Estadístico: {stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    print(f"Nivel de significancia (α): {alpha}")

    # 4. CONCLUSIÓN
    print(f"\n--- Conclusión ---")
    if p_value < alpha:
        print(f"✅ Rechazamos H0 (p={p_value:.4f} < α={alpha})")
        print(f"   La variación de {categoria_interes} ({cat_interes.mean():.2f}%)")
        print(f"   es SIGNIFICATIVAMENTE DIFERENTE al resto ({otras.mean():.2f}%)")

        # Tamaño del efecto (Cohen's d)
        pooled_std = np.sqrt(((len(cat_interes)-1)*cat_interes.std()**2 +
                              (len(otras)-1)*otras.std()**2) /
                             (len(cat_interes)+len(otras)-2))
        cohens_d = (cat_interes.mean() - otras.mean()) / pooled_std
        print(f"   Tamaño del efecto (Cohen's d): {cohens_d:.2f}", end=" ")
        if abs(cohens_d) < 0.2:
            print("(pequeño)")
        elif abs(cohens_d) < 0.8:
            print("(mediano)")
        else:
            print("(grande)")
    else:
        print(f"❌ No rechazamos H0 (p={p_value:.4f} >= α={alpha})")
        print(f"   No hay evidencia suficiente de que {categoria_interes}")
        print(f"   tenga variación diferente al resto")

    return {'prueba': prueba_usada, 'estadistico': stat, 'p_value': p_value}
```

**Markdown cell explicativo:**
```markdown
## 4. Análisis de Variación por Categoría

### 4.1 Contexto
En la descomposición planteamos la **Hipótesis 1**: que alguna categoría
tiene una caída significativamente mayor al promedio. Para validarla,
compararemos la variación de cada categoría contra las demás.

### 4.2 Metodología
1. Calcular variación YoY por categoría
2. Identificar categorías con mayor caída visual
3. Realizar prueba estadística para confirmar significancia

### 4.3 Resultado Visual
[Gráfico de barras mostrando variación por categoría]

### 4.4 Prueba Estadística
Realizamos un t-test (o Mann-Whitney si no hay normalidad) para comparar
la categoría "Electrónica" (mayor caída observada) contra el resto.

### 4.5 Interpretación
La categoría Electrónica tiene una caída de -28%, significativamente
mayor (p < 0.001) que el promedio de -12% del resto de categorías.
El tamaño del efecto es grande (d = 1.2), indicando una diferencia
sustancial, no solo estadísticamente significativa.

**Implicancia para el negocio**: Electrónica representa 35% de ingresos
pero 52% de la caída total. Requiere atención prioritaria.
```

**Estructura del Informe Final completo:**
```markdown
# Informe Ejecutivo: Diagnóstico de Caída de Ventas Q3 2024
## ShopMax - Análisis para Gerencia Comercial

**Fecha**: [Fecha]
**Analista**: [Nombre]
**Período analizado**: Q3 2024 vs Q3 2023

---

## RESUMEN EJECUTIVO

ShopMax experimentó una caída del 15% en ingresos durante Q3 2024.
Este análisis identifica las causas principales y proporciona
recomendaciones accionables con impacto proyectado de +$1.8M en Q4.

**Hallazgos Clave**:
1. Electrónica: -28% (causa 52% de la caída total)
2. Segmento "Nuevos": conversión 40% menor que recurrentes
3. Abandono en checkout aumentó de 30% a 42%

---

## 1. CHALLENGE: El Problema

### Contexto
- Caída de 15% en ingresos Q3 2024 vs Q3 2023
- $4.2M menos en el trimestre
- Presupuesto Q4 en riesgo si no se corrige

### Preguntas de Negocio
1. ¿Qué categorías están más afectadas?
2. ¿Qué segmentos de clientes han reducido compras?
3. ¿Dónde se produce la pérdida en el funnel?

---

## 2. ACTION: Metodología

### Datos Analizados
| Fuente | Registros | Período |
|--------|-----------|---------|
| Transacciones | 450,000 | Q3 2023-2024 |
| Usuarios | 180,000 | Activos en período |
| Sesiones | 2.1M | Q3 2024 |

### Análisis Realizados
1. **Variación por categoría**: ANOVA + comparaciones múltiples
2. **Segmentación de clientes**: Análisis de cohortes + z-test
3. **Funnel de conversión**: Análisis de embudo por etapa
4. **Correlaciones**: Factores asociados a baja conversión

---

## 3. RESULTS: Hallazgos

### Hallazgo 1: Electrónica Lidera la Caída
| Categoría | Variación YoY | % del Total Caída |
|-----------|---------------|-------------------|
| Electrónica | -28% | 52% |
| Hogar | -12% | 18% |
| Moda | -8% | 15% |
| Otros | -5% | 15% |

**Estadísticamente significativo**: p < 0.001, efecto grande (d=1.2)

**Causa probable**: Análisis de precios muestra que competidores
redujeron precios 15% en productos clave.

### Hallazgo 2: Clientes Nuevos en Crisis
| Segmento | Conversión 2023 | Conversión 2024 | Cambio |
|----------|-----------------|-----------------|--------|
| Nuevos | 2.8% | 1.7% | -39% |
| Recurrentes | 4.5% | 4.2% | -7% |

**Estadísticamente significativo**: p < 0.001

**Causa probable**: CAC aumentó 25%, calidad de leads disminuyó.

### Hallazgo 3: Abandono en Checkout Disparado
| Etapa | Abandono 2023 | Abandono 2024 | Cambio |
|-------|---------------|---------------|--------|
| Cart→Checkout | 30% | 32% | +2pp |
| Checkout→Payment | 20% | 35% | +15pp |
| Payment→Complete | 8% | 10% | +2pp |

**Causa probable**: Nuevo checkout implementado en julio
introdujo fricción adicional (3 pasos más).

---

## 4. RECOMENDACIONES

### Corto Plazo (Q4 2024)

| # | Acción | Responsable | Impacto Est. |
|---|--------|-------------|--------------|
| 1 | Ajustar precios en Electrónica (-10%) | Comercial | +$800K |
| 2 | Simplificar checkout (volver a versión anterior) | Producto | +$600K |
| 3 | Campaña de reactivación para nuevos abandonadores | Marketing | +$400K |

**Impacto total estimado: +$1.8M**

### Mediano Plazo (2025)

1. Revisar estrategia de adquisición de clientes nuevos
2. Implementar A/B testing antes de cambios en checkout
3. Desarrollar programa de fidelización para nuevos clientes

---

## ANEXOS

- A1: Detalle metodológico de pruebas estadísticas
- A2: Dashboard interactivo [Link]
- A3: Datos crudos utilizados

---

**Contacto**: [email] | **Dashboard**: [link]
```

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**

- Notebook cargado como link de Google Colab
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 16/16)
- **Código copiado de IA** sin comprensión demostrada
- **Código con errores** o interrupciones inesperadas
- **Interpretaciones equivocadas** de inferencias estadísticas
- **Falta de celdas markdown** que contextualicen el análisis
- **No incluye Dashboard** o **no incluye Informe Final**
- **Incoherencia** con el plan de Descomposición aprobado

---

## Errores Frecuentes

[Similar a Propuesta A, con errores adicionales para versión completa]

### Errores Adicionales en Versión Completa

1. **No verificar supuestos de pruebas**:
   - Incorrecto: Usar t-test sin verificar normalidad
   - Correcto: Verificar supuestos, usar alternativa si no se cumplen

2. **Solo reportar significancia, no efecto**:
   - Incorrecto: "p < 0.05, hay diferencia"
   - Correcto: "p < 0.05, diferencia de 16pp con efecto grande (d=1.2)"

3. **Dashboard no compartible**:
   - Incorrecto: Solo funciona localmente
   - Correcto: Link público o archivo exportable

4. **Informe demasiado técnico**:
   - Incorrecto: Incluir código, p-values sin contexto
   - Correcto: Lenguaje ejecutivo, implicancias de negocio

---

## Notas Importantes

- Incluye **3 componentes**: Notebook, Dashboard, Informe Final
- El análisis debe ser **coherente con la Descomposición aprobada**
- Puedes ampliar más allá del plan si consultas con tu tutor
- El Informe es para **stakeholders no técnicos**
