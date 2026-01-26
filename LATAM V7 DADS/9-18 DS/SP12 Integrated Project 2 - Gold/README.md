# SP12: Integrated Project 2 - Gold Recovery

> **Track:** Data Scientist | **Sprint:** 12 de 18

## Resumen del Proyecto

Desarrollo de un modelo de machine learning para Zyfra que predice la cantidad de oro extraído del mineral. El modelo optimiza la producción eliminando parámetros no rentables en el proceso de extracción y purificación de oro.

## Objetivo de Aprendizaje

- Analizar datos de procesos industriales (múltiples etapas de extracción)
- Desarrollar métricas de evaluación personalizadas (sMAPE)
- Entrenar modelos de regresión para optimización de producción
- Integrar análisis de datos con desarrollo de modelos

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `gold_recovery_train.csv` | Datos de entrenamiento del proceso de extracción |
| `gold_recovery_test.csv` | Datos de prueba del proceso |
| `gold_recovery_full.csv` | Dataset completo para análisis |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P11.ipynb`](./P%20English%20version/P11.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S11 EN SOL Integrated Project 2.py`](./P%20English%20version/S11%20EN%20SOL%20Integrated%20Project%202.py) | Script de referencia |
| Español | [`S12 ESP Proyecto integrado 2 - Extracción oro.ipynb`](./P%20Spanish%20version/S12%20ESP%20Proyecto%20integrado%202%20-%20Extracción%20oro.ipynb) | Solución principal |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn (modelos de regresión, cross-validation)

## Entregables

- [ ] Preparación y limpieza de datos
- [ ] Análisis exploratorio del proceso de extracción
- [ ] Implementación de métrica sMAPE personalizada
- [ ] Entrenamiento y comparación de modelos
- [ ] Evaluación final en conjunto de prueba
