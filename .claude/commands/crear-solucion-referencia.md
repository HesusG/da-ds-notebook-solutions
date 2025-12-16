# Crear Solución de Referencia

Genera un notebook Jupyter (.ipynb) de solución de referencia para el sprint especificado.

## Instrucciones

1. **Identifica el sprint** a partir del argumento proporcionado: $ARGUMENTS

2. **Lee todos los notebooks de solución (SOL/SOLV)** del sprint:
   - Identifica las mejores prácticas de cada uno
   - Nota las diferencias en enfoques
   - Detecta errores conceptuales a evitar

3. **Si hay múltiples soluciones (SP5, SP6, SP8):**
   - Combina las mejores prácticas de ambas
   - Usa el enfoque más claro y pedagógico
   - Documenta cuando hay alternativas válidas

4. **Crea el notebook de referencia** con esta estructura:

```
# [Nombre del Proyecto] - Solución de Referencia

## Introducción
[Contexto del proyecto y objetivos]

## Configuración
[Imports y configuración inicial]

## Paso 1: Carga y Exploración de Datos
[Código con explicaciones detalladas]

## Paso 2: Limpieza de Datos
[Manejo de NaN, duplicados, tipos]

## Paso 3: Análisis Exploratorio
[EDA con visualizaciones]

## Paso 4: [Análisis Específico del Sprint]
[Estadística, SQL, etc.]

## Conclusiones
[Resumen de hallazgos]

## Notas para Revisores
[Puntos clave a evaluar]
```

5. **Características del notebook de referencia:**

### Código
- Bien comentado y explicado
- Sigue PEP 8
- Usa nombres de variables descriptivos
- Evita código duplicado
- Maneja errores apropiadamente

### Markdown
- Explica el "por qué" de cada decisión
- Documenta suposiciones
- Incluye interpretación de resultados
- Menciona alternativas cuando aplica

### Visualizaciones
- Títulos descriptivos
- Etiquetas de ejes
- Leyendas cuando necesario
- Colores accesibles

### Metodología
- Justifica selección de técnicas
- Documenta parámetros elegidos
- Valida resultados
- Reconoce limitaciones

6. **Guarda el notebook** en:
   `{Sprint}/local-assets/solucion-referencia.ipynb`

## Formato del Notebook

El notebook debe ser un archivo JSON válido con estructura ipynb:

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": ["# Título"]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": ["import pandas as pd"]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}
```

## Notas Importantes

- La solución debe ser ejecutable de principio a fin
- Incluir todos los pasos, incluso los "obvios"
- Priorizar claridad sobre elegancia
- Este notebook es para referencia interna, no para estudiantes
