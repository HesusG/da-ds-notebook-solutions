# SP17: Computer Vision

> **Track:** Data Scientist | **Sprint:** 17 de 18 | **PROYECTO OPCIONAL**

## Resumen del Proyecto

Desarrollo de un modelo de visión artificial para la cadena de supermercados Good Seed que determina la edad de una persona a partir de una fotografía. El objetivo es ayudar a cumplir con las leyes de venta de alcohol verificando si el cliente es mayor de edad.

## Objetivo de Aprendizaje

- Implementar redes neuronales convolucionales (CNN) para clasificación de imágenes
- Utilizar transfer learning con modelos pre-entrenados (ResNet)
- Trabajar con datasets de imágenes de rostros
- Evaluar modelos de regresión de edad (MAE)

## Dataset

| Archivo | Descripción |
|---------|-------------|
| `faces_dataset/` | Conjunto de fotografías de personas con su edad etiquetada |

> Los datasets están en `.gitignore`. Obtenerlos del LMS.

## Estructura del Proyecto

### Proyecto del Estudiante

| Idioma | Archivo |
|--------|---------|
| English | [`P16_3.ipynb`](./P%20English%20version/P16_3.ipynb) |
| Español | [`S17 ESP - Vision artificial Fotos.ipynb`](./P%20Spanish%20version/S17%20ESP%20-%20Vision%20artificial%20Fotos.ipynb) |

### Soluciones

| Idioma | Archivo | Notas |
|--------|---------|-------|
| Español | [`S17 ESP SOL vision artificial.ipynb`](./P%20Spanish%20version/S17%20ESP%20SOL%20vision%20artificial.ipynb) | Solución principal |
| Español | [`S17 ESP SOL2 Vision artificial.ipynb`](./P%20Spanish%20version/S17%20ESP%20SOL2%20Vision%20artificial.ipynb) | Solución alternativa |
| Español | [`S17 ESP SOL3 Vision artificial - Colab GPU.ipynb`](./P%20Spanish%20version/S17%20ESP%20SOL3%20Vision%20artificial%20-%20Colab%20GPU.ipynb) | Solución para Colab con GPU |

### Recursos Adicionales

Los diagramas explicativos del proyecto se encuentran en:
- [`local-assets/generated_images/`](./local-assets/generated_images/)

### Criterios de Evaluación

[**criterios.md**](./Reviewers_Assesment_Criteria/criterios.md)

---

## Requisitos Técnicos

- Python 3.x
- TensorFlow/Keras o PyTorch
- pandas, numpy
- matplotlib
- **GPU recomendada** (Google Colab con GPU es una opción)

## Notas Importantes

> **Este proyecto se clasifica como OPCIONAL** hasta nuevo aviso ya que la plataforma no provee un espacio adecuado para realizarlo.
>
> - El proyecto es aceptado tras realizar un análisis exploratorio básico
> - Se recomienda usar Google Colab con GPU para el entrenamiento

## Entregables

- [ ] Análisis exploratorio de las imágenes y distribución de edades
- [ ] Preprocesamiento de imágenes (redimensionamiento, normalización)
- [ ] Implementación de CNN o transfer learning (ResNet)
- [ ] Entrenamiento del modelo (preferiblemente con GPU)
- [ ] Evaluación con MAE (Mean Absolute Error)
