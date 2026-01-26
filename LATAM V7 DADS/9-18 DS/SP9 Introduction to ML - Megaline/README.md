# SP9: Introduction to Machine Learning

> **Track:** Data Scientist | **Sprint:** 9 de 18

## Resumen del Proyecto

Desarrollo de un modelo de clasificación para recomendar planes de telefonía móvil (Smart o Ultra) a clientes de Megaline. El objetivo es alcanzar una accuracy de al menos 0.75 mediante la comparación de diferentes algoritmos de ML.

## Objetivo de Aprendizaje

- Implementar modelos de clasificación supervisada (DecisionTree, RandomForest, LogisticRegression)
- Dividir datos en conjuntos de entrenamiento, validación y prueba
- Evaluar modelos con métricas de clasificación (accuracy)
- Realizar pruebas de cordura (sanity checks)

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `users_behavior.csv` | Comportamiento de suscriptores (llamadas, mensajes, MB, plan actual) |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P8.ipynb`](./P%20English%20version/P8.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S8 EN SOL ntro to ML.py`](./P%20English%20version/S8%20EN%20SOL%20ntro%20to%20ML.py) | Script de referencia |
| Español | [`S9 ESP SOL - suscriptores megaline.ipynb`](./P%20Spanish%20version/S9%20ESP%20SOL%20-%20suscriptores%20megaline.ipynb) | Solución principal |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- scikit-learn (DecisionTreeClassifier, RandomForestClassifier, LogisticRegression)

## Entregables

- [ ] Carga y exploración del dataset
- [ ] División de datos (60/20/20 train/valid/test)
- [ ] Entrenamiento de al menos un modelo de clasificación
- [ ] Optimización de hiperparámetros
- [ ] Evaluación en conjunto de prueba (accuracy ≥ 0.75)
- [ ] Prueba de cordura del modelo
