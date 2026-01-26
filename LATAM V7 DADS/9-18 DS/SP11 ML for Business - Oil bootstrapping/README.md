# SP11: Machine Learning for Business

> **Track:** Data Scientist | **Sprint:** 11 de 18

## Resumen del Proyecto

Selección de la mejor región para abrir 200 nuevos pozos petroleros para OilyGiant. Se utilizan modelos de regresión lineal para predecir el volumen de reservas y la técnica de Bootstrapping para analizar riesgos y ganancias potenciales.

## Objetivo de Aprendizaje

- Implementar regresión lineal para predicción de volumen
- Aplicar técnica Bootstrapping para análisis de riesgo
- Calcular intervalos de confianza y probabilidad de pérdidas
- Tomar decisiones de negocio basadas en análisis costo-beneficio

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `geo_data_0.csv` | Datos de pozos de la Región 0 |
| `geo_data_1.csv` | Datos de pozos de la Región 1 |
| `geo_data_2.csv` | Datos de pozos de la Región 2 |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P10.ipynb`](./P%20English%20version/P10.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S10 EN SOLV ML for Business.py`](./P%20English%20version/S10%20EN%20SOLV%20ML%20for%20Business.py) | Script de referencia |
| Español | [`S11 ESP ML negocios - Selección región pozos petróleo.ipynb`](./P%20Spanish%20version/S11%20ESP%20ML%20negocios%20-%20Selección%20región%20pozos%20petróleo.ipynb) | Solución principal |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- scikit-learn (LinearRegression, StandardScaler)
- Técnica de Bootstrapping manual

## Entregables

- [ ] Modelos de regresión lineal para las 3 regiones
- [ ] Cálculo de RMSE y volumen promedio predicho
- [ ] Cálculo de volumen mínimo para cubrir costos
- [ ] Bootstrapping con 1000 iteraciones (500 muestras → mejores 200)
- [ ] Intervalos de confianza del 95% y riesgo de pérdidas
- [ ] Selección de región óptima con justificación
