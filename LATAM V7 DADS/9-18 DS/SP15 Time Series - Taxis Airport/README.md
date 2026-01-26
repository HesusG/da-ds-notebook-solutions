# SP15: Time Series

> **Track:** Data Scientist | **Sprint:** 15 de 18

## Resumen del Proyecto

Predicción de demanda de taxis en aeropuertos para Sweet Lift Taxi. El modelo debe predecir la cantidad de pedidos de taxis para la próxima hora, ayudando a atraer más conductores durante las horas pico. La métrica RMSE en el conjunto de prueba no debe ser superior a 48.

## Objetivo de Aprendizaje

- Analizar y preprocesar series temporales
- Crear features de calendario y lag features
- Implementar modelos para predicción de series temporales
- Evaluar modelos con RMSE en horizonte de predicción

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `taxi.csv` | Datos históricos de pedidos de taxis por hora |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| Español | [`S15 ESP Series temporales Taxis.ipynb`](./P%20Spanish%20version/S15%20ESP%20Series%20temporales%20Taxis.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S14 EN SOL Time Series.ipynb`](./P%20English%20version/S14%20EN%20SOL%20Time%20Series.ipynb) | Solución principal |
| Español | [`S15 ESP SOL pedidos de taxis.ipynb`](./P%20Spanish%20version/S15%20ESP%20SOL%20pedidos%20de%20taxis.ipynb) | Solución principal |
| Español | [`S15 ESP SOL2 Series temporales - Pedidos taxis.ipynb`](./P%20Spanish%20version/S15%20ESP%20SOL2%20Series%20temporales%20-%20Pedidos%20taxis.ipynb) | Solución alternativa |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- statsmodels (opcional, para análisis de series temporales)

## Entregables

- [ ] Análisis exploratorio de la serie temporal
- [ ] Remuestreo de datos a frecuencia horaria
- [ ] Creación de features (lag, rolling, calendario)
- [ ] Entrenamiento y comparación de modelos
- [ ] Evaluación final con RMSE ≤ 48
