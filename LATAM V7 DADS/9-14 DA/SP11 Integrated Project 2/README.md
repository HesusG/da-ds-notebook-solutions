# SP11: Integrated Project 2

> **Track:** Data Analyst | **Sprint:** 11 de 14

## Resumen del Proyecto

Análisis del comportamiento de usuarios en una app de delivery de alimentos. Estudio del embudo de ventas para identificar puntos de fricción y evaluación de un test A/A/B para determinar si un cambio de fuentes en la aplicación afecta la conversión.

## Objetivo de Aprendizaje

- Construir y analizar embudos de conversión (funnel analysis)
- Diseñar y evaluar experimentos A/A/B
- Aplicar pruebas de hipótesis para proporciones (Z-test)
- Implementar corrección de significancia por comparaciones múltiples

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `logs_exp_us.csv` | Logs de eventos de usuarios (con grupo experimental) |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P10 EN.ipynb`](./P%20English%20version/P10%20EN.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S10 EN SOL Integrated Project 2.ipynb`](./P%20English%20version/S10%20EN%20SOL%20Integrated%20Project%202.ipynb) | Solución principal |
| Español | [`S11 ESP SOL Proyecto Integrado 2.ipynb`](./P%20Spanish%20version/S11%20ESP%20SOL%20Proyecto%20Integrado%202.ipynb) | Solución principal |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- matplotlib, seaborn, plotly
- statsmodels (proportions_ztest)

## Entregables

- [ ] Preprocesamiento y filtrado de datos (periodo válido)
- [ ] Análisis de embudo de eventos con visualización
- [ ] Evaluación del Test A/A (validación del sistema)
- [ ] Evaluación del Test A/B (control vs test)
- [ ] Conclusiones y recomendación de negocio
