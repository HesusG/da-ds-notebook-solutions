# Criterios de Evaluación: DS_Final - Etapa 3: Informe de Solución (Versión Completa)

## Objetivo

Elaborar un informe ejecutivo completo que comunique efectivamente los resultados del proyecto de ciencia de datos a stakeholders de diferentes niveles, vinculando los hallazgos técnicos con el impacto estratégico en el negocio y proporcionando recomendaciones accionables y cuantificadas.

**Requisitos previos**: Aprobación de la Etapa 2 (Código de Solución)

**Competencias que desarrollarás**: Comunicación ejecutiva, storytelling con datos, estimación de impacto financiero, redacción de recomendaciones accionables, visualización para stakeholders no técnicos

<details>
<summary>Requisitos del Entregable</summary>

## Descripción del Entregable

El Informe de Solución debe ser un documento que contenga:

1. **Problema de Negocio**
   - Descripción del reto abordado
   - Importancia del problema para la organización
   - Contexto del sector/industria

2. **Datos Utilizados**
   - Fuentes de datos
   - Volumen y calidad
   - Período de análisis

3. **Solución Técnica**
   - Algoritmo seleccionado y configuración
   - Calibraciones/optimizaciones realizadas
   - Métricas logradas vs objetivos
   - Comparación con otros modelos probados

4. **Impacto en el Negocio**
   - Estimación cualitativa del valor
   - Estimación cuantitativa (ingresos/costos/ROI)
   - Supuestos utilizados

5. **Limitaciones**
   - De los datos
   - Del modelo
   - Factores externos

6. **Conclusiones y Recomendaciones**
   - Hallazgos principales
   - Recomendaciones accionables específicas
   - Próximos pasos sugeridos

**Estructura recomendada**: CAR (Challenge - Action - Results)
**Extensión**: 4-6 páginas ejecutivas (excluyendo anexos técnicos opcionales)

</details>

## Glosario de Términos Técnicos

**Estructura CAR**: Framework de comunicación ejecutiva: Challenge (el problema y su contexto), Action (lo que se hizo para resolverlo), Results (los resultados obtenidos y su impacto).

**Informe Ejecutivo**: Documento conciso orientado a tomadores de decisiones. Prioriza insights accionables sobre detalles técnicos. Usa lenguaje de negocio.

**ROI (Return on Investment)**: Retorno sobre inversión. ROI = (Beneficio - Costo) / Costo × 100%. Métrica clave para justificar proyectos.

**LTV (Lifetime Value)**: Valor de por vida del cliente. Ingresos totales esperados de un cliente durante su relación con la empresa.

**Stakeholder**: Persona o grupo con interés en el proyecto. Incluye usuarios directos, tomadores de decisiones, equipos impactados.

**Recomendación Accionable**: Sugerencia específica, medible y ejecutable. "Contactar semanalmente clientes con score >0.7 y tenure <12 meses" vs "Mejorar retención".

**Trade-off**: Compromiso entre objetivos contrapuestos. Ejemplo: precision vs recall, velocidad vs precisión.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (6 criterios obligatorios)

**Contenido Mínimo**
- [ ] **[OBLIGATORIO]** Describe el problema de negocio abordado claramente
- [ ] **[OBLIGATORIO]** Explica la importancia de resolver el problema
- [ ] **[OBLIGATORIO]** Describe los datos utilizados (fuentes, volumen, período)
- [ ] **[OBLIGATORIO]** Menciona las métricas/KPIs utilizados para evaluar el modelo
- [ ] **[OBLIGATORIO]** Presenta los resultados del mejor modelo seleccionado
- [ ] **[OBLIGATORIO]** Incluye conclusiones principales del proyecto


### INTERMEDIO (10 criterios)

**Detalle de la Solución**
- [ ] **[OBLIGATORIO]** Detalla el algoritmo del mejor modelo (nombre, configuración clave)
- [ ] **[OBLIGATORIO]** Describe calibraciones/optimizaciones realizadas
- [ ] Compara rendimiento del modelo final con otros modelos probados
- [ ] Presenta tabla comparativa clara de modelos

**Visualización y Estructura**
- [ ] Incluye visualizaciones de resultados clave (métricas, importancia features)
- [ ] Sigue estructura CAR (Challenge-Action-Results) o equivalente

**Análisis Crítico**
- [ ] Describe limitaciones de los datos utilizados
- [ ] Describe limitaciones del modelo desarrollado
- [ ] Vincula aspectos técnicos con impacto en decisiones de negocio
- [ ] No replica información innecesaria de etapas anteriores (síntesis)

### AVANZADO (8 criterios)

**Impacto de Negocio**
- [ ] Estima impacto en negocio (cualitativo o cuantitativo)
- [ ] Incluye estimación cuantitativa con números específicos (ingresos, costos, clientes)
- [ ] Recomendaciones específicas, medibles y accionables
- [ ] Identifica próximos pasos concretos para implementación

**Calidad Profesional**
- [ ] Lenguaje ejecutivo (evita jerga técnica innecesaria)
- [ ] Visualizaciones profesionales y autoexplicativas
- [ ] Coherencia con hallazgos documentados en Etapa 2
- [ ] Interpretaciones estadísticas correctas y contextualizadas

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 3 criterios adicionales de los 17 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 8/8
  - Al menos 7 criterios adicionales de los 17 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 8/8 (Básico + Intermedio)
  - Al menos 5 criterios de la sección AVANZADO

---

## Ejemplos de Cumplimiento

### Ejemplo de Informe Ejecutivo Completo (Estructura CAR)

```markdown
# Informe Ejecutivo: CallMeMaybe - Proyecto de Retención de Clientes

**Fecha**: [Fecha]
**Autor**: [Nombre]
**Versión**: 1.0

---

## RESUMEN EJECUTIVO

CallMeMaybe enfrenta pérdidas anuales de $5M por cancelaciones de clientes.
Desarrollamos un modelo de machine learning que identifica el 78% de los
clientes en riesgo antes de que cancelen, permitiendo intervenciones proactivas
que podrían recuperar $3.6M anuales.

---

## 1. CHALLENGE: El Problema de Negocio

### 1.1 Contexto
La industria de telecomunicaciones en América Latina experimenta tasas de
churn del 20-30% anual. Estudios de McKinsey indican que adquirir un cliente
nuevo cuesta 5-7 veces más que retener uno existente.

### 1.2 El Reto Específico
CallMeMaybe reporta una tasa de cancelación del 25% mensual, lo que representa:

| Métrica | Valor Anual |
|---------|-------------|
| Clientes perdidos | 12,500 |
| Costo de adquisición unitario | $400 |
| **Costo total de reemplazo** | **$5,000,000** |
| LTV promedio por cliente | $1,200 |
| **Ingresos perdidos** | **$15,000,000** |

### 1.3 Objetivo del Proyecto
Desarrollar un sistema predictivo que permita al equipo de retención:
1. Identificar clientes con alta probabilidad de cancelar
2. Priorizar intervenciones basadas en riesgo
3. Reducir la tasa de churn mediante acciones proactivas

---

## 2. ACTION: La Solución Desarrollada

### 2.1 Datos Analizados

| Fuente | Registros | Variables | Período |
|--------|-----------|-----------|---------|
| Contratos | 50,000 | 5 | 2020-2023 |
| Información Personal | 50,000 | 3 | - |
| Servicios Internet | 45,000 | 4 | - |
| Servicios Teléfono | 48,000 | 3 | - |

**Calidad de datos**: 97% completos. Valores ausentes imputados con
estrategias específicas por tipo de variable.

### 2.2 Algoritmo Seleccionado

**Modelo Final**: LightGBM (Light Gradient Boosting Machine) con optimización
de hiperparámetros.

**Configuración óptima**:
- n_estimators: 200
- max_depth: 7
- learning_rate: 0.05
- class_weight: balanced

**Calibraciones realizadas**:
1. Optimización de hiperparámetros con RandomizedSearchCV (20 iteraciones)
2. Ajuste de umbral de decisión a 0.35 para maximizar recall
3. Balanceo de clases con class_weight='balanced'

### 2.3 Rendimiento del Modelo

**Comparación con objetivos definidos**:

| Métrica | Objetivo | Logrado | Estado |
|---------|----------|---------|--------|
| AUC-ROC | ≥ 0.75 | **0.88** | ✅ Superado |
| Recall | ≥ 0.70 | **0.78** | ✅ Superado |
| Precision | ≥ 0.60 | **0.71** | ✅ Superado |
| F1-Score | ≥ 0.65 | **0.74** | ✅ Superado |

**Comparación con otros modelos probados**:

| Modelo | AUC | Recall | F1 | Comentario |
|--------|-----|--------|-----|------------|
| Baseline (Random) | 0.50 | 0.25 | 0.25 | Referencia |
| Logistic Regression | 0.81 | 0.68 | 0.62 | No cumple recall |
| Random Forest | 0.85 | 0.72 | 0.69 | Cumple, overfitting |
| **LightGBM** | **0.88** | **0.78** | **0.74** | **Mejor opción** |

### 2.4 Factores Predictivos Principales

Los 5 factores más importantes para predecir churn son:

1. **Tipo de contrato** (32%): Contratos mes a mes tienen 3x más riesgo
2. **Antigüedad** (24%): Clientes nuevos (<12 meses) son más propensos
3. **Monto mensual** (18%): Montos muy altos o muy bajos indican riesgo
4. **Servicios contratados** (15%): Menos servicios = mayor riesgo
5. **Método de pago** (11%): Pago manual tiene mayor churn

---

## 3. RESULTS: Impacto y Recomendaciones

### 3.1 Impacto Proyectado

Con recall del 78%, el modelo identificaría correctamente:

**Escenario Conservador** (20% efectividad de retención):
| Métrica | Cálculo | Valor |
|---------|---------|-------|
| Clientes en riesgo identificados | 12,500 × 78% | 9,750 |
| Retenidos con intervención | 9,750 × 20% | 1,950 |
| Valor preservado (LTV) | 1,950 × $1,200 | **$2,340,000** |
| Ahorro en adquisición | 1,950 × $400 | **$780,000** |
| **Beneficio total anual** | | **$3,120,000** |

**Escenario Optimista** (35% efectividad de retención):
| Métrica | Cálculo | Valor |
|---------|---------|-------|
| Clientes retenidos | 9,750 × 35% | 3,413 |
| Valor preservado | 3,413 × $1,200 | **$4,095,600** |
| Ahorro en adquisición | 3,413 × $400 | **$1,365,200** |
| **Beneficio total anual** | | **$5,460,800** |

### 3.2 ROI del Proyecto

| Concepto | Valor |
|----------|-------|
| Inversión estimada (desarrollo) | $80,000 |
| Beneficio anual (conservador) | $3,120,000 |
| **ROI** | **3,800%** |
| Payback | **< 1 mes** |

### 3.3 Limitaciones

**De los datos**:
- No incluyen datos de satisfacción (NPS, encuestas)
- No incluyen interacciones con servicio al cliente
- Período de análisis limitado a 3 años

**Del modelo**:
- Asume patrones históricos se mantendrán
- No captura factores externos (competencia, economía)
- Requiere actualización periódica con nuevos datos

**De implementación**:
- Requiere integración con CRM existente
- Equipo de retención necesita capacitación
- Capacidad de contacto puede ser limitante

### 3.4 Recomendaciones

**Inmediatas (Semana 1-2)**:
1. Generar lista priorizada de los 500 clientes con mayor riesgo
2. Asignar al equipo de retención para contacto inmediato
3. Ofrecer incentivos predefinidos (descuentos, upgrades)

**Corto plazo (Mes 1-3)**:
1. Implementar scoring semanal automatizado
2. Integrar scores en dashboard de retención
3. Definir scripts de retención basados en factores de riesgo

**Mediano plazo (Trimestre 1-2)**:
1. Incorporar datos de satisfacción al modelo (NPS, quejas)
2. Desarrollar modelos segmentados por tipo de cliente
3. Implementar A/B testing de estrategias de retención

### 3.5 Próximos Pasos

| Paso | Responsable | Fecha Target |
|------|-------------|--------------|
| Validar lista inicial con negocio | Gerente Retención | Semana 1 |
| Piloto con 100 clientes | Equipo Retención | Semana 2-4 |
| Medir efectividad piloto | Analytics | Semana 5 |
| Escalar a producción | TI + Analytics | Mes 2 |
| Re-entrenar modelo | Data Science | Trimestre 2 |

---

## 4. CONCLUSIONES

1. **El modelo funciona**: Supera todos los objetivos definidos, identificando
   78% de los clientes en riesgo con 71% de precisión.

2. **El impacto es significativo**: Potencial de $3-5M anuales en valor
   recuperado, con ROI superior al 3,800%.

3. **Los factores son accionables**: Los principales predictores (tipo de
   contrato, antigüedad, servicios) permiten diseñar intervenciones específicas.

4. **Hay espacio para mejorar**: Incorporar datos de satisfacción y
   comportamiento podría aumentar aún más la precisión.

**El proyecto demuestra que la ciencia de datos puede generar valor tangible
y medible cuando se aplica a problemas de negocio bien definidos.**

---

## ANEXO: Contacto y Recursos

- **Código fuente**: [Repositorio interno]
- **Dashboard de monitoreo**: [Link]
- **Contacto técnico**: [Email]
```

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**

- Documento no compartible (notebook .ipynb sin convertir a PDF/Word/Slides)
- No cumple criterios OBLIGATORIOS (menos de 8/8)
- **Enfoque exclusivamente técnico** sin conexión con negocio
- **Conclusiones genéricas** sin valor específico ("el modelo funciona bien")
- **No estima impacto en negocio** (ni cualitativo ni cuantitativo)
- **Interpretaciones estadísticas incorrectas** (confundir precision/recall, malinterpretar AUC)
- **Replica todo el notebook** sin síntesis ejecutiva
- **Incoherencia** con resultados documentados en Etapa 2

---

## Errores Frecuentes

### En Contenido

1. **Exportar notebook como informe**:
   - Incorrecto: Convertir .ipynb a PDF con todo el código
   - Correcto: Crear documento ejecutivo separado, conciso
   - Consecuencia: Documento ilegible para stakeholders de negocio

2. **Métricas sin contexto**:
   - Incorrecto: "El AUC es 0.88"
   - Correcto: "El AUC de 0.88 supera el objetivo de 0.75, lo que significa que el modelo distingue correctamente entre clientes que cancelarán y los que no en el 88% de los casos"
   - Consecuencia: Audiencia no entiende el valor

3. **No describir limitaciones**:
   - Incorrecto: Presentar modelo como solución perfecta
   - Correcto: Documentar limitaciones conocidas y cómo mitigarlas
   - Consecuencia: Pérdida de credibilidad cuando surjan problemas

4. **Incoherencia con Etapa 2**:
   - Incorrecto: Reportar métricas diferentes a las del código
   - Correcto: Verificar que números coincidan exactamente
   - Consecuencia: Desconfianza en el análisis

### En Impacto de Negocio

5. **No cuantificar impacto**:
   - Incorrecto: "El modelo ayudará a retener clientes"
   - Correcto: "Estimamos retención de 1,950-3,413 clientes adicionales, generando $3.1-5.5M anuales"
   - Consecuencia: No demuestra valor concreto del proyecto

6. **Estimaciones sin supuestos**:
   - Incorrecto: "Ahorraremos $3M"
   - Correcto: "Asumiendo 20-35% de efectividad en retención, el ahorro sería $3.1-5.5M"
   - Consecuencia: Estimaciones no verificables

7. **No calcular ROI**:
   - Incorrecto: Solo mencionar beneficios
   - Correcto: Comparar beneficios vs inversión (tiempo, recursos)
   - Consecuencia: No justifica inversión en el proyecto

### En Comunicación

8. **Demasiado técnico**:
   - Incorrecto: "Usamos GridSearchCV con cv=5 para optimizar max_depth y n_estimators"
   - Correcto: "Optimizamos el modelo probando múltiples configuraciones para encontrar la más efectiva"
   - Consecuencia: Ejecutivos no comprenden

9. **Recomendaciones vagas**:
   - Incorrecto: "Se recomienda mejorar la retención"
   - Correcto: "Contactar semanalmente a clientes con score >0.7 y antigüedad <12 meses, ofreciendo contrato anual con 15% descuento"
   - Consecuencia: No son implementables

10. **Sin estructura clara**:
    - Incorrecto: Texto corrido sin secciones
    - Correcto: CAR o estructura clara con headers, tablas, bullets
    - Consecuencia: Difícil de navegar y entender

### En Formato

11. **Documento muy extenso**:
    - Incorrecto: Informe de 15+ páginas con todo el detalle
    - Correcto: 4-6 páginas ejecutivas con anexos técnicos opcionales
    - Consecuencia: Nadie lo lee completo

12. **Sin visualizaciones**:
    - Incorrecto: Solo texto y tablas numéricas
    - Correcto: Gráficos de impacto, comparación de modelos, tendencias
    - Consecuencia: Menos impactante y memorable

13. **Visualizaciones confusas**:
    - Incorrecto: Gráficos sin títulos, ejes sin labels, colores inconsistentes
    - Correcto: Visualizaciones autoexplicativas con contexto
    - Consecuencia: Confunde en lugar de clarificar

14. **No incluir próximos pasos**:
    - Incorrecto: Terminar con conclusiones
    - Correcto: Incluir plan de acción con responsables y fechas
    - Consecuencia: No hay camino claro para implementación

### Errores Conceptuales

15. **Confundir precision y recall**:
    - Incorrecto: Usar precision cuando se refiere a recall
    - Correcto: Precision = qué tan preciso cuando predice positivo; Recall = qué proporción de positivos reales captura
    - Consecuencia: Interpretaciones incorrectas

16. **Malinterpretar AUC**:
    - Incorrecto: "AUC de 0.88 significa 88% de accuracy"
    - Correcto: "AUC de 0.88 significa que el modelo rankea correctamente a un positivo sobre un negativo aleatorio el 88% del tiempo"
    - Consecuencia: Comunicación incorrecta a stakeholders

---

## Notas Importantes

- Esta es la **Etapa 3 de 3** del proyecto final (última etapa)
- El informe es el **entregable principal** para stakeholders de negocio
- **No es un reporte técnico**: debe ser comprensible para no-técnicos
- La audiencia principal son **tomadores de decisiones** del negocio
- Debe demostrar **valor generado** y **retorno de inversión** del proyecto
- Extensión recomendada: **4-6 páginas ejecutivas** (anexos técnicos opcionales)
- **Coherencia es crítica**: números deben coincidir con Etapa 2
- El éxito del proyecto se mide por la **adopción de las recomendaciones**
