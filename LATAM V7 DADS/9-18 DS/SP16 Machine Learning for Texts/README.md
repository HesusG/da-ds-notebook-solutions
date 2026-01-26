# SP16: Machine Learning for Texts

> **Track:** Data Scientist | **Sprint:** 16 de 18

## Resumen del Proyecto

Desarrollo de un sistema de clasificación de reseñas de películas para Film Junky Union. El modelo detecta automáticamente críticas negativas, clasificando reseñas de IMDB como positivas o negativas. El objetivo es alcanzar un F1-score de al menos 0.85.

## Objetivo de Aprendizaje

- Preprocesar texto para machine learning (tokenización, lematización)
- Vectorizar texto usando TF-IDF y/o word embeddings
- Entrenar modelos de clasificación de texto
- Evaluar modelos con métricas apropiadas para NLP (F1-score)

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `imdb_reviews.csv` | Reseñas de películas de IMDB con etiquetas de sentimiento |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P15.ipynb`](./P%20English%20version/P15.ipynb) |
| Español | [`S16 Aprendizaje textos peliculas.ipynb`](./P%20Spanish%20version/S16%20Aprendizaje%20textos%20peliculas.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| English | [`S15 EN SOL Machine Learning for Texts.py`](./P%20English%20version/S15%20EN%20SOL%20Machine%20Learning%20for%20Texts.py) | Script de referencia |
| Español | [`S16 ESP SOL2 Aprendizaje textos - Análisis sentimiento.ipynb`](./P%20Spanish%20version/S16%20ESP%20SOL2%20Aprendizaje%20textos%20-%20Análisis%20sentimiento.ipynb) | Solución principal |
| Español | [`S16 ESP SOL3 Aprendizaje textos - Análisis sentimiento-COLAB.ipynb`](./P%20Spanish%20version/S16%20ESP%20SOL3%20Aprendizaje%20textos%20-%20Análisis%20sentimiento-COLAB.ipynb) | Solución para Colab |

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- pandas, numpy
- NLTK o spaCy (para preprocesamiento de texto)
- scikit-learn (TfidfVectorizer, clasificadores)
- (Opcional) transformers, torch para modelos avanzados

## Entregables

- [ ] Preprocesamiento de texto (limpieza, tokenización, lematización)
- [ ] Vectorización de texto (TF-IDF, Word2Vec, o embeddings)
- [ ] Entrenamiento de modelos de clasificación de texto
- [ ] Evaluación con F1-score ≥ 0.85
- [ ] Análisis de resultados y errores del modelo
