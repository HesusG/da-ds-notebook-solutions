# DA_Final - Resumen de Criterios de Evaluación (Propuesta B: Exhaustiva)

## Estructura del Proyecto Final

El DA_Final se compone de **3 casos de uso INDEPENDIENTES**, con un total de **4 entregables**:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           DA_FINAL                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  CASO PRINCIPAL (2 entregables secuenciales)                           │
│  ├── 1. Descomposición de Tareas  →  Requiere aprobación               │
│  └── 2. Implementación            →  (Notebook + Dashboard + Informe)  │
│                                                                         │
│  PRUEBA A/B (1 entregable independiente)                               │
│  └── Jupyter Notebook con análisis completo del experimento            │
│                                                                         │
│  MANEJO SQL (1 entregable independiente)                               │
│  └── Jupyter Notebook con consultas SQL avanzadas                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Nota**: Los 3 casos usan datos diferentes y NO están relacionados entre sí.

---

## Resumen por Entregable

### 1. Caso Principal - Descomposición de Tareas

| Nivel | Criterios Totales | Obligatorios | Adicionales Requeridos |
|-------|-------------------|--------------|------------------------|
| BÁSICO | 28 | 16 | +3 |
| INTERMEDIO | 28 | 16 | +6 |
| AVANZADO | 28 | 16 | +10 |

**Criterios OBLIGATORIOS (16):**

*Comprensión del Problema (4):*
1. Identifica problema de negocio concreto con propias palabras
2. Reformula problema sin copiar literal del enunciado
3. Explica valor/importancia del análisis para stakeholders
4. Identifica stakeholders que se beneficiarán

*Datos (4):*
5. Código ejecuta sin errores
6. Describe volumen de datos (filas, columnas, tamaño)
7. Identifica calidad de datos (NaN, duplicados, tipos)
8. Documenta hallazgos relevantes de la exploración

*Hipótesis (4):*
9. Plantea al menos 2 hipótesis relevantes
10. Cada hipótesis incluye estructura H0/H1
11. Hipótesis son medibles y verificables con los datos
12. Hipótesis conectan con el problema de negocio

*Plan (4):*
13. Define al menos 3 KPIs específicos
14. KPIs incluyen fórmula matemática
15. Incluye al menos 4 actividades de análisis
16. Incluye estimación de tiempos por actividad

**Archivo detallado:** `criterios_caso_principal_descomposicion.md`

---

### 2. Caso Principal - Implementación

| Nivel | Criterios Totales | Obligatorios | Adicionales Requeridos |
|-------|-------------------|--------------|------------------------|
| BÁSICO | 30 | 16 | +3 |
| INTERMEDIO | 30 | 16 | +7 |
| AVANZADO | 30 | 16 | +12 |

**Criterios OBLIGATORIOS (16):**

*Notebook - Código (4):*
1. Código ejecuta sin errores en celdas secuenciales
2. Código estructurado de forma organizada y didáctica
3. Usa funciones para automatizar procesos repetitivos
4. Usa bucles y condicionales apropiadamente

*Notebook - Análisis Descriptivo (3):*
5. Incluye análisis estadístico descriptivo completo
6. Incluye visualizaciones claras para diagnosticar patrones
7. Visualizaciones tienen títulos, ejes etiquetados, leyendas

*Notebook - Inferencia (3):*
8. Realiza pruebas estadísticas para validar hipótesis del plan
9. Justifica los tipos de pruebas utilizadas
10. Interpreta correctamente los resultados (p-value, conclusión)

*Dashboard (3):*
11. Dashboard presenta KPIs definidos en el plan
12. Dashboard es claro y entendible para stakeholders no técnicos
13. Dashboard es compartible (link público o archivo exportable)

*Informe (3):*
14. Informe sigue estructura CAR (Challenge-Action-Results)
15. Incluye conclusiones con impacto concreto en el negocio
16. Incluye recomendaciones accionables

**Archivo detallado:** `criterios_caso_principal_implementacion.md`

---

### 3. Prueba A/B

| Nivel | Criterios Totales | Obligatorios | Adicionales Requeridos |
|-------|-------------------|--------------|------------------------|
| BÁSICO | 28 | 13 | +3 |
| INTERMEDIO | 28 | 13 | +7 |
| AVANZADO | 28 | 13 | +13 |

**Criterios OBLIGATORIOS (13):**

*Comprensión del Experimento (4):*
1. Explica objetivo del experimento con propias palabras
2. Plantea hipótesis formal con estructura H0/H1
3. Identifica métrica principal del experimento
4. Código ejecuta sin errores en celdas secuenciales

*Diagnóstico de Datos (2):*
5. Realiza diagnóstico completo (tipos, NaN, duplicados, outliers)
6. Establece y ejecuta plan de limpieza

*Análisis del Embudo (3):*
7. Visualiza embudo completo en todas sus etapas
8. Calcula tasas de conversión por etapa
9. Diferencia claramente grupos A (control) y B (tratamiento)

*Pruebas Estadísticas (3):*
10. Realiza pruebas A/B para validar hipótesis principal
11. Justifica los métodos estadísticos empleados
12. Interpreta correctamente resultados (p-value, conclusión)

*Conclusiones (1):*
13. Incluye al menos 4 conclusiones/recomendaciones fundamentadas

**Archivo detallado:** `criterios_prueba_ab.md`

---

### 4. Manejo de SQL

| Nivel | Criterios Totales | Obligatorios | Adicionales Requeridos |
|-------|-------------------|--------------|------------------------|
| BÁSICO | 28 | 10 | +2 |
| INTERMEDIO | 28 | 10 | +6 |
| AVANZADO | 28 | 10 | +12 |

**Criterios OBLIGATORIOS (10):**

*Conexión y Exploración (4):*
1. Conexión correcta a la base de datos
2. Explora TODAS las tablas existentes
3. Describe estructura de cada tabla (columnas, tipos)
4. Código ejecuta sin errores en celdas secuenciales

*Modelo de Datos (3):*
5. Explica la relación entre las tablas
6. Identifica claves primarias de cada tabla
7. Identifica claves foráneas y cómo conectan las tablas

*Consultas y Conclusiones (3):*
8. Resuelve TODAS las consultas usando SQL (no Pandas)
9. Consultas ejecutan correctamente sin errores
10. Cada resultado tiene una conclusión relevante

**Archivo detallado:** `criterios_manejo_sql.md`

---

## Totales del Proyecto (Propuesta B)

| Métrica | Valor |
|---------|-------|
| **Total de criterios** | 114 |
| **Criterios obligatorios** | 55 |
| **Criterios opcionales** | 59 |
| **Entregables** | 4 |

---

## Comparativa: Propuesta A vs Propuesta B

| Aspecto | Propuesta A (Simplificada) | Propuesta B (Exhaustiva) |
|---------|---------------------------|--------------------------|
| **Criterios totales** | 66 | 114 |
| **Criterios obligatorios** | 39 | 55 |
| **Criterios opcionales** | 27 | 59 |
| **Enfoque** | Esencial | Completo |
| **Técnicas avanzadas** | Mencionadas | Evaluadas explícitamente |

---

## Criterios de Descalificación Generales

### Todos los Entregables
- Notebook cargado como link de Google Colab (no como archivo .ipynb)
- Celdas sin ejecutar secuencialmente
- No cumple criterios OBLIGATORIOS mínimos
- Código copiado de IA sin comprensión demostrada
- Código con errores de ejecución no corregidos

### Caso Principal - Descomposición
- Copiado literal del enunciado sin reformulación personal
- Hipótesis genéricas o no verificables con los datos disponibles
- Actividades genéricas sin relación específica al caso
- KPIs sin fórmula matemática
- No referencia métricas o variables específicas del dataset

### Caso Principal - Implementación
- Interpretaciones equivocadas de estadísticas (ej: p-value)
- Falta de celdas markdown que contextualicen
- No incluye Dashboard
- No incluye Informe Final
- Análisis no coherente con la Descomposición aprobada

### Prueba A/B
- Interpretaciones equivocadas de p-value o significancia
- Conclusiones contradictorias con resultados estadísticos
- No diferenciar claramente grupos A y B
- No calcular tasas de conversión

### Manejo SQL
- Usar Pandas en lugar de SQL para resolver consultas
- No explicar relaciones entre tablas
- Resultados sin conclusiones interpretativas
- Consultas con errores de sintaxis no corregidos

---

## Flujo Recomendado

```
                    ┌────────────────────────┐
                    │    INICIO PROYECTO     │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │ Descomposición Tareas  │
                    │   (Caso Principal)     │
                    └───────────┬────────────┘
                                │
                        Enviar para revisión
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ▼                   ▼                   ▼
   ┌─────────────────┐ ┌─────────────────┐ Esperar
   │   Prueba A/B    │ │  Manejo SQL     │ aprobación
   │ (Independiente) │ │ (Independiente) │
   └────────┬────────┘ └────────┬────────┘
            │                   │
            ▼                   ▼
   Enviar para revisión   Enviar para revisión
            │                   │
            └───────────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │  Aprobada Descomp.?    │
                    └───────────┬────────────┘
                                │ SÍ
                                ▼
                    ┌────────────────────────┐
                    │   Implementación       │
                    │ (Notebook+Dashboard+   │
                    │      Informe)          │
                    └───────────┬────────────┘
                                │
                        Enviar para revisión
                                │
                                ▼
                    ┌────────────────────────┐
                    │  PROYECTO COMPLETADO   │
                    │  (4 entregables OK)    │
                    └────────────────────────┘
```

---

## Niveles de Aprobación - Resumen

| Nivel | Descripción | Requisitos |
|-------|-------------|------------|
| **BÁSICO** | Aprobado mínimo | Todos los obligatorios + mínimo adicionales |
| **INTERMEDIO** | Aprobado satisfactorio | Todos los obligatorios + adicionales moderados |
| **AVANZADO** | Aprobado con distinción | Todos los obligatorios + mayoría de adicionales |

---

## Archivos de Referencia

1. `criterios_caso_principal_descomposicion.md` - Planificación (28 criterios)
2. `criterios_caso_principal_implementacion.md` - Implementación (30 criterios)
3. `criterios_prueba_ab.md` - Experimento A/B (28 criterios)
4. `criterios_manejo_sql.md` - Consultas SQL (28 criterios)

---

## Notas para Revisores

1. **Los 3 casos son independientes**: Pueden revisarse en cualquier orden
2. **Descomposición antes de Implementación**: No aprobar Implementación sin Descomposición aprobada
3. **SQL solo en plataforma**: Este caso no se trabaja localmente
4. **Verificar coherencia**: En Implementación, verificar que sigue el plan de Descomposición
5. **Dashboard e Informe**: En Implementación, verificar que incluye los 3 componentes
6. **Técnicas avanzadas**: En Propuesta B, evaluar explícitamente uso de técnicas avanzadas (CTEs, window functions, poder estadístico, etc.)
7. **Calidad de conclusiones**: Dar peso a conclusiones accionables y con impacto de negocio
