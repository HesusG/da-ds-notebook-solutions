# SP13: Linear Algebra

> **Track:** Data Scientist | **Sprint:** 13 de 18

## Resumen del Proyecto

Resolución de múltiples tareas de machine learning para la compañía de seguros Sure Tomorrow: encontrar clientes similares, predecir beneficios de seguro, y desarrollar un algoritmo de ofuscación de datos que proteja la información personal sin afectar la calidad del modelo.

## Objetivo de Aprendizaje

- Implementar búsqueda de vecinos más cercanos (KNN) para similitud de clientes
- Evaluar modelos de predicción vs modelos dummy
- Aplicar regresión lineal para predicción de beneficios
- Desarrollar algoritmo de enmascaramiento/ofuscación de datos con álgebra lineal

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `insurance_us.csv` | Datos de clientes de la compañía de seguros |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P12.ipynb`](./P%20English%20version/P12.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S12 EN SOL Linear Algebra.py`](./P%20English%20version/S12%20EN%20SOL%20Linear%20Algebra.py) | Script de referencia |
| Español | [`S13 ESP Algebra lineal - Ofuscación compañia de seguros.ipynb`](./P%20Spanish%20version/S13%20ESP%20Algebra%20lineal%20-%20Ofuscación%20compañia%20de%20seguros.ipynb) | Proyecto estudiante |
| Español | [`S13 ESP SOL2 Algebra lineal - Ofuscación datos seguros.ipynb`](./P%20Spanish%20version/S13%20ESP%20SOL2%20Algebra%20lineal%20-%20Ofuscación%20datos%20seguros.ipynb) | Solución alternativa |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- scikit-learn (KNeighborsClassifier, LinearRegression, DummyClassifier)
- Conocimientos de álgebra lineal (matrices, inversas)

## Entregables

- [ ] **Tarea 1:** Encontrar clientes similares usando distancias
- [ ] **Tarea 2:** Comparar modelo de predicción vs modelo dummy
- [ ] **Tarea 3:** Regresión lineal para predecir beneficios
- [ ] **Tarea 4:** Algoritmo de ofuscación de datos que preserve calidad del modelo
