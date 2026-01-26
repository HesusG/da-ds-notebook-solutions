# SP14: Numerical Methods

> **Track:** Data Scientist | **Sprint:** 14 de 18

## Resumen del Proyecto

Desarrollo de un modelo para determinar el valor de mercado de coches usados para Rusty Bargain. El modelo debe equilibrar calidad de predicción, velocidad de predicción y tiempo de entrenamiento, comparando diferentes algoritmos incluyendo Gradient Boosting.

## Objetivo de Aprendizaje

- Comparar algoritmos de ML por calidad, velocidad y tiempo de entrenamiento
- Implementar modelos de Gradient Boosting (XGBoost, LightGBM, CatBoost)
- Optimizar hiperparámetros para balance rendimiento/velocidad
- Evaluar modelos con RMSE

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `car_data.csv` | Historial de coches, especificaciones técnicas y precios |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P13.ipynb`](./P%20English%20version/P13.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S13 EN SOL Numerical Methods.py`](./P%20English%20version/S13%20EN%20SOL%20Numerical%20Methods.py) | Script de referencia |
| Español | [`S14 Métodos numéricos - Precio autos.ipynb`](./P%20Spanish%20version/S14%20Métodos%20numéricos%20-%20Precio%20autos.ipynb) | Proyecto estudiante |
| Español | [`S14 ESP SOL2 Métodos numéricos - Precio autos.ipynb`](./P%20Spanish%20version/S14%20ESP%20SOL2%20Métodos%20numéricos%20-%20Precio%20autos.ipynb) | Solución alternativa |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- scikit-learn
- XGBoost, LightGBM, CatBoost (Gradient Boosting libraries)

## Entregables

- [ ] Preprocesamiento de datos de coches usados
- [ ] Comparación de múltiples modelos (incluyendo Gradient Boosting)
- [ ] Medición de tiempo de entrenamiento y predicción
- [ ] Análisis de trade-off calidad vs velocidad
- [ ] Selección del modelo óptimo con justificación
