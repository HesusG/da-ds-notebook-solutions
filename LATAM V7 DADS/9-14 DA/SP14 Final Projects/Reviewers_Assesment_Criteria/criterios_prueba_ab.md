# Criterios de Evaluación: DA_Final - Prueba A/B (Versión Completa)

## Objetivo

Validar exhaustivamente el desempeño de un experimento A/B real utilizando conocimientos avanzados sobre embudos de conversión, diseño experimental y pruebas de hipótesis estadísticas, generando un análisis riguroso con conclusiones y recomendaciones de alto valor.

**Requisitos previos**: Haber completado todos los sprints previos del bootcamp de Data Analyst

**Competencias que desarrollarás**: Diseño experimental, análisis de experimentos A/B, embudos de conversión, pruebas de hipótesis, poder estadístico, interpretación crítica, pensamiento analítico

**Nota**: Este caso es **INDEPENDIENTE** del Caso Principal.

<details>
<summary>Requisitos del Entregable</summary>

## Descripción del Entregable

Un **Jupyter Notebook** exhaustivo que contenga:

1. **Objetivo del experimento**: Explicación detallada del propósito
2. **Hipótesis**: Planteamiento formal de H0 y H1
3. **Análisis del diseño**: Limitaciones, sesgos potenciales, poder estadístico
4. **Diagnóstico de datos**: Calidad, limpieza, validación
5. **Análisis del embudo**: Todas las etapas con métricas por grupo
6. **Pruebas A/B**: Validación estadística rigurosa
7. **Análisis de sensibilidad**: Robustez de resultados
8. **Conclusiones**: Al menos 4 conclusiones/recomendaciones fundamentadas

</details>

## Glosario de Términos Técnicos

**Prueba A/B**: Experimento controlado aleatorizado para comparar dos versiones y determinar cuál tiene mejor desempeño.

**Grupo de Control (A)**: Recibe la versión actual/original. Establece la línea base.

**Grupo de Tratamiento (B)**: Recibe la nueva versión que se evalúa.

**Aleatorización**: Asignación aleatoria de usuarios a grupos para eliminar sesgos de selección.

**Poder Estadístico (1-β)**: Probabilidad de detectar un efecto real cuando existe. Típicamente se busca ≥80%.

**MDE (Minimum Detectable Effect)**: Mínimo efecto que el experimento puede detectar con el poder dado.

**Efecto Novelty**: Sesgo donde usuarios reaccionan al cambio por ser nuevo, no por ser mejor.

**Efecto de Múltiples Comparaciones**: Aumenta probabilidad de falsos positivos al hacer muchas pruebas. Requiere corrección (Bonferroni, FDR).

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (12 criterios obligatorios)

**Comprensión del Experimento**
- [ ] **[OBLIGATORIO]** Explica objetivo del experimento con sus propias palabras
- [ ] **[OBLIGATORIO]** Plantea hipótesis formal con estructura H0/H1
- [ ] **[OBLIGATORIO]** Identifica métrica principal del experimento
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores en celdas secuenciales

**Diagnóstico de Datos**
- [ ] **[OBLIGATORIO]** Realiza diagnóstico completo (tipos de datos, valores ausentes, duplicados, outliers)
- [ ] **[OBLIGATORIO]** Establece y ejecuta plan de limpieza documentado

**Análisis del Embudo**
- [ ] **[OBLIGATORIO]** Visualiza embudo completo en todas sus etapas (ej: login → product_page → product_cart → purchase)
- [ ] **[OBLIGATORIO]** Calcula tasas de conversión absolutas y relativas por etapa para cada grupo
- [ ] **[OBLIGATORIO]** Diferencia claramente grupos A (control) y B (tratamiento) con métricas específicas

**Pruebas Estadísticas**
- [ ] **[OBLIGATORIO]** Realiza pruebas A/B para validar hipótesis principal (ej: test Z de proporciones)
- [ ] **[OBLIGATORIO]** Justifica los métodos estadísticos empleados según tipo de variable
- [ ] **[OBLIGATORIO]** Interpreta correctamente resultados (p-value, estadístico de prueba, conclusión sobre H0)

### INTERMEDIO (8 criterios)

**Análisis del Diseño**
- [ ] Describe al menos 3 limitaciones del diseño experimental (ej: duración, tamaño de muestra, efecto novelty)
- [ ] Evalúa calidad de la aleatorización: verifica balance entre grupos (tamaños, distribución de características)
- [ ] Identifica posibles fuentes de sesgo (ej: contaminación entre grupos, eventos externos concurrentes)

**Calidad del Análisis**
- [ ] Verifica supuestos de las pruebas estadísticas (ej: tamaño de muestra suficiente para aproximación normal)
- [ ] Usa pruebas apropiadas según tipo de variable (proporciones vs medias, test Z vs t-test)
- [ ] Considera corrección por múltiples comparaciones si realiza varias pruebas simultáneas

**Documentación**
- [ ] Markdown cells contextualizan cada sección con explicaciones claras
- [ ] Código es limpio, comentado y sigue buenas prácticas (funciones reutilizables, nombres descriptivos)

### AVANZADO (8 criterios)

**Análisis Avanzado**
- [ ] Calcula o estima poder estadístico del experimento (1-β) y efecto mínimo detectable (MDE)
- [ ] Calcula intervalo de confianza del efecto observado (ej: IC 95% para diferencia de proporciones)
- [ ] Realiza análisis de sensibilidad o robustez (ej: análisis por semana, verificación de estabilidad temporal)
- [ ] Analiza subgrupos relevantes si aplica (ej: por dispositivo, región) con precaución sobre p-hacking

**Conclusiones**
- [ ] Incluye al menos 4 conclusiones/recomendaciones fundamentadas con evidencia cuantitativa
- [ ] Conclusiones consideran limitaciones identificadas y contextualizan resultados
- [ ] Recomendaciones son específicas y accionables (qué hacer, cuándo, cómo medir éxito)
- [ ] Discute implicancias para futuros experimentos (duración, tamaño de muestra, métricas)

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 13/13
  - Al menos 2 criterios adicionales de los 15 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 13/13
  - Al menos 6 criterios adicionales de los 15 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 12/12 (Básico + Intermedio)
  - Al menos 5 criterios de la sección AVANZADO

---

## Ejemplos de Cumplimiento

**Análisis de limitaciones del diseño:**
```markdown
## 3. Análisis del Diseño Experimental

### 3.1 Limitaciones Identificadas

#### Limitación 1: Duración del Experimento
- **Problema**: El experimento duró solo 14 días
- **Riesgo**: No captura ciclos semanales completos ni efectos estacionales
- **Impacto**: Resultados pueden no ser estables a largo plazo
- **Mitigación sugerida**: Extender a 4 semanas mínimo en futuros experimentos

#### Limitación 2: Efecto Novelty
- **Problema**: Usuarios del grupo B experimentan el nuevo diseño por primera vez
- **Riesgo**: Engagement inicial puede ser artificialmente alto
- **Impacto**: Sobreestimación del efecto real del cambio
- **Cómo detectar**: Analizar si el efecto se mantiene semana a semana

#### Limitación 3: Tamaño de Muestra
- **Problema**: n_control=5,000, n_tratamiento=4,800
- **Análisis de poder**: Con α=0.05 y conversión base=3.2%,
  podemos detectar efectos ≥0.8pp (MDE=25% relativo)
- **Riesgo**: Efectos menores pueden no ser detectados
- **Impacto**: Podríamos concluir "no hay efecto" cuando existe uno pequeño

#### Limitación 4: Posible Contaminación
- **Problema**: No hay información sobre cookies/sesiones cruzadas
- **Riesgo**: Un usuario podría estar en ambos grupos
- **Impacto**: Diluye el efecto real
- **Verificación**: Revisar si hay user_ids duplicados entre grupos

### 3.2 Evaluación de Aleatorización

Verificamos que los grupos sean comparables en características base:
```

```python
# Verificar balance entre grupos
def verificar_balance(df, grupo_col, caracteristicas):
    """
    Verifica si los grupos están balanceados en características base.
    """
    resultados = []

    for col in caracteristicas:
        grupo_a = df[df[grupo_col] == 'A'][col]
        grupo_b = df[df[grupo_col] == 'B'][col]

        if df[col].dtype in ['int64', 'float64']:
            # Variable numérica: t-test
            stat, p = stats.ttest_ind(grupo_a.dropna(), grupo_b.dropna())
            test = 't-test'
            media_a = grupo_a.mean()
            media_b = grupo_b.mean()
        else:
            # Variable categórica: chi-cuadrado
            tabla = pd.crosstab(df[grupo_col], df[col])
            stat, p, dof, expected = stats.chi2_contingency(tabla)
            test = 'chi2'
            media_a = grupo_a.mode()[0] if len(grupo_a.mode()) > 0 else 'N/A'
            media_b = grupo_b.mode()[0] if len(grupo_b.mode()) > 0 else 'N/A'

        balance = '✓ Balanceado' if p > 0.05 else '✗ Desbalanceado'

        resultados.append({
            'Variable': col,
            'Grupo A': media_a,
            'Grupo B': media_b,
            'Test': test,
            'p-value': p,
            'Balance': balance
        })

    return pd.DataFrame(resultados)

# Verificar
caracteristicas_base = ['edad', 'genero', 'antiguedad_dias', 'dispositivo']
balance_df = verificar_balance(df, 'group', caracteristicas_base)
print(balance_df.to_string(index=False))
```

**Cálculo de poder estadístico:**
```python
from statsmodels.stats.power import NormalIndPower, tt_ind_solve_power
from statsmodels.stats.proportion import proportion_effectsize

def calcular_poder_experimento(n_control, n_tratamiento, conversion_base, alpha=0.05):
    """
    Calcula el poder estadístico y MDE del experimento.
    """
    # Tamaño de muestra efectivo (promedio armónico para muestras desiguales)
    n_effective = 2 * n_control * n_tratamiento / (n_control + n_tratamiento)

    # Calcular MDE para poder de 80%
    # effect_size = h (Cohen's h para proporciones)
    power_analysis = NormalIndPower()

    # MDE en términos de Cohen's h
    mde_h = power_analysis.solve_power(
        effect_size=None,
        nobs1=n_effective/2,
        alpha=alpha,
        power=0.8,
        ratio=1.0,
        alternative='two-sided'
    )

    # Convertir h a diferencia de proporciones
    # h = 2 * (arcsin(sqrt(p2)) - arcsin(sqrt(p1)))
    # Aproximación: para p pequeños, delta ≈ h * sqrt(p*(1-p))
    mde_absoluto = mde_h * np.sqrt(conversion_base * (1 - conversion_base)) * 2
    mde_relativo = mde_absoluto / conversion_base * 100

    print(f"="*60)
    print(f"ANÁLISIS DE PODER ESTADÍSTICO")
    print(f"="*60)
    print(f"\nParámetros:")
    print(f"  n_control: {n_control:,}")
    print(f"  n_tratamiento: {n_tratamiento:,}")
    print(f"  Conversión base: {conversion_base*100:.2f}%")
    print(f"  Alpha: {alpha}")
    print(f"\nResultados:")
    print(f"  MDE (efecto mínimo detectable):")
    print(f"    Absoluto: {mde_absoluto*100:.2f} puntos porcentuales")
    print(f"    Relativo: {mde_relativo:.1f}%")
    print(f"\n  Interpretación:")
    print(f"    Con el tamaño de muestra actual, podemos detectar")
    print(f"    diferencias de al menos {mde_relativo:.1f}% con 80% de poder.")
    print(f"    Efectos menores podrían no ser detectados.")

    return {'mde_absoluto': mde_absoluto, 'mde_relativo': mde_relativo}

# Ejecutar
poder = calcular_poder_experimento(
    n_control=5000,
    n_tratamiento=4800,
    conversion_base=0.032
)
```

**Prueba con intervalo de confianza:**
```python
from statsmodels.stats.proportion import confint_proportions_2indep

def prueba_ab_completa(conversiones_a, n_a, conversiones_b, n_b, alpha=0.05):
    """
    Realiza prueba A/B completa con intervalo de confianza.
    """
    p_a = conversiones_a / n_a
    p_b = conversiones_b / n_b
    diferencia = p_b - p_a
    diferencia_relativa = (p_b - p_a) / p_a * 100

    # Z-test de proporciones
    count = np.array([conversiones_b, conversiones_a])
    nobs = np.array([n_b, n_a])
    stat, p_value = proportions_ztest(count, nobs, alternative='two-sided')

    # Intervalo de confianza para la diferencia
    ci_low, ci_high = confint_proportions_2indep(
        conversiones_b, n_b, conversiones_a, n_a,
        method='wald', compare='diff', alpha=alpha
    )

    print(f"="*60)
    print(f"PRUEBA A/B - CONVERSIÓN TOTAL")
    print(f"="*60)

    print(f"\nConversiones:")
    print(f"  Control (A): {p_a*100:.2f}% ({conversiones_a:,}/{n_a:,})")
    print(f"  Tratamiento (B): {p_b*100:.2f}% ({conversiones_b:,}/{n_b:,})")

    print(f"\nDiferencia observada:")
    print(f"  Absoluta: {diferencia*100:+.2f} puntos porcentuales")
    print(f"  Relativa: {diferencia_relativa:+.1f}%")

    print(f"\nPrueba estadística (z-test de proporciones):")
    print(f"  Estadístico Z: {stat:.4f}")
    print(f"  P-value (dos colas): {p_value:.4f}")

    print(f"\nIntervalo de confianza ({(1-alpha)*100:.0f}%) para la diferencia:")
    print(f"  [{ci_low*100:.2f}%, {ci_high*100:.2f}%]")

    print(f"\n--- CONCLUSIÓN ---")
    if p_value < alpha:
        print(f"✅ SIGNIFICATIVO (p={p_value:.4f} < α={alpha})")
        if diferencia > 0:
            print(f"   El tratamiento (B) tiene conversión MAYOR que control (A)")
        else:
            print(f"   El tratamiento (B) tiene conversión MENOR que control (A)")
        print(f"   Con {(1-alpha)*100:.0f}% de confianza, la diferencia real está")
        print(f"   entre {ci_low*100:.2f}% y {ci_high*100:.2f}%")
    else:
        print(f"❌ NO SIGNIFICATIVO (p={p_value:.4f} >= α={alpha})")
        print(f"   No hay evidencia suficiente de diferencia entre grupos")
        if 0 >= ci_low and 0 <= ci_high:
            print(f"   El intervalo de confianza incluye 0, consistente con H0")

    return {
        'p_a': p_a, 'p_b': p_b,
        'diferencia': diferencia, 'diferencia_relativa': diferencia_relativa,
        'stat': stat, 'p_value': p_value,
        'ci': (ci_low, ci_high)
    }

# Ejecutar
resultado = prueba_ab_completa(
    conversiones_a=160,
    n_a=5000,
    conversiones_b=197,
    n_b=4800
)
```

**Conclusiones fundamentadas:**
```markdown
## 8. Conclusiones y Recomendaciones

### Conclusión 1: El nuevo checkout mejora conversión significativamente
**Evidencia**: La conversión pasó de 3.2% (control) a 4.1% (tratamiento),
una mejora de +28% relativo (p < 0.001).

**Contexto**: El intervalo de confianza 95% [+0.5%, +1.4%] excluye 0,
y el efecto mínimo es +0.5pp, superior al MDE de 0.25pp.

**Recomendación**: Implementar el nuevo checkout para todos los usuarios.

### Conclusión 2: Mayor impacto en etapa checkout → payment
**Evidencia**: La tasa de conversión en esta etapa mejoró de 45% a 58%
(+29% relativo), mientras otras etapas permanecieron estables.

**Contexto**: Esto sugiere que el checkout simplificado reduce fricción
específicamente en el momento de pago, no en todo el funnel.

**Recomendación**: Estudiar qué elementos del nuevo checkout causan
la mejora para replicar principios en otras etapas.

### Conclusión 3: Posible efecto novelty requiere monitoreo
**Evidencia**: El efecto fue más pronunciado en semana 1 (+32%) que
en semana 2 (+24%), aunque ambos significativos.

**Contexto**: Esta tendencia podría indicar efecto novelty decreciente.

**Recomendación**: Monitorear métricas post-implementación durante
8 semanas para confirmar que el efecto se estabiliza.

### Conclusión 4: Segmentos responden diferente (exploración)
**Evidencia**: Usuarios móviles mostraron mejora de +35% vs +18% en desktop.

**Contexto**: Análisis exploratorio, no pre-registrado. Requiere
confirmación con experimento dedicado.

**Recomendación**: Diseñar experimento específico para evaluar
diferencias por dispositivo con poder estadístico adecuado.

### Implicancias para Futuros Experimentos
1. **Duración**: Extender a 4 semanas mínimo para detectar efecto novelty
2. **Poder**: Calcular tamaño de muestra antes de iniciar
3. **Segmentos**: Pre-registrar análisis de subgrupos para evitar p-hacking
4. **Métricas**: Definir métricas secundarias con corrección por múltiples pruebas
```

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**

- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 13/13)
- **Código copiado de IA** sin comprensión
- **Interpretaciones equivocadas** de p-value o intervalos de confianza
- **Conclusiones contradictorias** con resultados estadísticos
- Menos de 4 conclusiones/recomendaciones

---

## Notas Importantes

- Este caso es **INDEPENDIENTE** del Caso Principal
- Se recomienda realizarlo mientras esperas aprobación de la Descomposición
- El análisis debe ser **estadísticamente riguroso**
- Las conclusiones deben **considerar las limitaciones** identificadas
