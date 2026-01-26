# SP10: Making Business Decisions Based on Data

> **Track:** Data Analyst | **Sprint:** 10 de 14

## Resumen del Proyecto

Priorización de hipótesis para aumentar ingresos de una tienda online y análisis de resultados de un test A/B. Se utilizan frameworks ICE/RICE para priorización y pruebas estadísticas para evaluar la significancia de las diferencias entre grupos.

## Objetivo de Aprendizaje

- Aplicar frameworks de priorización (ICE/RICE) para backlog de hipótesis
- Analizar tests A/B con métricas acumuladas
- Identificar y manejar anomalías (outliers) en datos de e-commerce
- Tomar decisiones basadas en pruebas estadísticas (Mann-Whitney)

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `hypotheses_us.csv` | Lista de hipótesis con parámetros para ICE/RICE |
| `orders_us.csv` | Registro de pedidos del test A/B |
| `visits_us.csv` | Registro de visitas por grupo del test |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

Este proyecto no tiene plantilla inicial para el estudiante.

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`P9 EN SOL .ipynb`](./P%20English%20version/P9%20EN%20SOL%20.ipynb) | Solución principal |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scipy.stats (Mann-Whitney U)

## Entregables

- [ ] Priorización de hipótesis con ICE y RICE
- [ ] Gráficos de métricas acumuladas por grupo (ingresos, conversión, ticket)
- [ ] Análisis de anomalías y filtrado de datos
- [ ] Pruebas estadísticas con datos crudos y filtrados
- [ ] Decisión final sobre el test A/B (parar/continuar)
