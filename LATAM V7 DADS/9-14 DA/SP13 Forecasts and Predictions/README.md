# SP13: Forecasts and Predictions

> **Track:** Data Analyst | **Sprint:** 13 de 14

## Resumen del Proyecto

Análisis de pérdida de clientes (churn) para la cadena de gimnasios Model Fitness. Desarrollo de modelos de clasificación para predecir la probabilidad de abandono y segmentación de usuarios mediante clustering para proponer estrategias de retención personalizadas.

## Objetivo de Aprendizaje

- Entrenar modelos de clasificación supervisada (Regresión Logística, Random Forest)
- Evaluar modelos con métricas de clasificación (Accuracy, Precision, Recall)
- Aplicar clustering no supervisado (K-Means, Dendrogramas)
- Interpretar resultados para estrategias de negocio

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `gym_churn_us.csv` | Perfiles de clientes del gimnasio con variable de churn |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P12.ipynb`](./P%20English%20version/P12.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`P12 EN SOL Forecasts and Predictions.py`](./P%20English%20version/P12%20EN%20SOL%20Forecasts%20and%20Predictions.py) | Script de referencia |
| Español | [`S13 SOL - Pronósticos y predicciones.ipynb`](./P%20Spanish%20Version/S13%20SOL%20-%20Pronósticos%20y%20predicciones.ipynb) | Solución principal |

### Criterios de Evaluación

[**criterios_DA_13_pronosticos_predicciones.md**](./Reviewers_Assesment_Criteria/criterios_DA_13_pronosticos_predicciones.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn (LogisticRegression, RandomForestClassifier, KMeans, StandardScaler)
- scipy (dendrograma)

## Entregables

- [ ] EDA con comparación de características por grupo de churn
- [ ] Modelos de clasificación (Regresión Logística + Random Forest)
- [ ] Evaluación con métricas de clasificación
- [ ] Clustering con K-Means (datos estandarizados)
- [ ] Perfilado de clusters y tasa de churn por grupo
- [ ] Recomendaciones de marketing por segmento
