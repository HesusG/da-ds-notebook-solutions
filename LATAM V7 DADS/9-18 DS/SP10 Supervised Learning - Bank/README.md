# SP10: Supervised Learning

> **Track:** Data Scientist | **Sprint:** 10 de 18

## Resumen del Proyecto

Predicción de abandono de clientes (churn) para Beta Bank. El modelo debe manejar datos desbalanceados y alcanzar un F1-score de al menos 0.59, utilizando técnicas de balanceo como upsampling o class_weight.

## Objetivo de Aprendizaje

- Manejar clases desbalanceadas en problemas de clasificación
- Aplicar técnicas de balanceo (upsampling, class_weight)
- Optimizar modelos con GridSearchCV
- Evaluar con métricas apropiadas para datos desbalanceados (F1-score, ROC-AUC)

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `Churn.csv` | Datos históricos de clientes bancarios con variable de abandono |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P9 Customer churn Bank loyalty.ipynb`](./P%20English%20version/P9%20Customer%20churn%20Bank%20loyalty.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S9 EN SOL Supervised Learning.py`](./P%20English%20version/S9%20EN%20SOL%20Supervised%20Learning.py) | Script de referencia |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- scikit-learn (clasificadores, StandardScaler, train_test_split, GridSearchCV)
- Métricas: f1_score, roc_auc_score

## Entregables

- [ ] Preprocesamiento (manejo de nulos, encoding, escalado)
- [ ] Modelo baseline sin balanceo
- [ ] Al menos dos técnicas de balanceo implementadas
- [ ] Comparación de modelos con métricas apropiadas
- [ ] Evaluación final con F1-score ≥ 0.59 y ROC-AUC
