# Criterios de Evaluación: Proyecto Megaline

## Objetivo

Implementar y comparar modelos de machine learning para clasificar usuarios de telecom entre planes Smart y Ultra, seleccionando el modelo con mejor accuracy (≥0.75) mediante evaluación sistemática.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Implementación de ML supervisado, evaluación de modelos, toma de decisiones basada en métricas, interpretación de resultados en contexto de negocio

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

La compañía móvil Megaline no está satisfecha al ver que muchos de sus clientes utilizan planes heredados. Quieren desarrollar un modelo que pueda analizar el comportamiento de los clientes y recomendar uno de los nuevos planes de Megaline: Smart o Ultra.

Tienes acceso a los datos de comportamiento de los suscriptores que ya se han cambiado a los planes nuevos (del proyecto del sprint de Análisis estadístico de datos). Para esta tarea de clasificación debes crear un modelo que escoja el plan correcto. Como ya hiciste el paso de procesar los datos, puedes lanzarte directo a crear el modelo.

Desarrolla un modelo con la mayor exactitud posible. En este proyecto, el umbral de exactitud es 0.75. Usa el dataset para comprobar la exactitud.

## Instrucciones del proyecto

1. Abre y examina el archivo de datos: `/datasets/users_behavior.csv`
2. Descarga el dataset
3. Segmenta los datos fuente en tres conjuntos: entrenamiento, validación y prueba
4. Investiga la calidad de diferentes modelos cambiando los hiperparámetros. Describe brevemente los hallazgos del estudio
5. Comprueba la calidad del modelo usando el conjunto de prueba
6. Tarea adicional: haz una prueba de cordura al modelo

## Descripción de los datos

- `calls` — número de llamadas
- `minutes` — duración total de las llamadas en minutos
- `messages` — número de mensajes de texto
- `mb_used` — tráfico de Internet utilizado en MB
- `is_ultra` — plan para el mes actual (1 = Ultra, 0 = Smart)


</details>


## Glosario de Términos Técnicos

**GridSearchCV**: Herramienta de sklearn que prueba automáticamente diferentes combinaciones de hiperparámetros para encontrar la mejor configuración del modelo.

**random_state**: Parámetro que fija la semilla aleatoria para garantizar reproducibilidad en los resultados.

**Prueba de cordura/Sanity check**: Verificación básica que confirma que el modelo funciona mejor que una predicción aleatoria o muy simple.

**Train/validation/test split**: División del dataset en 3 partes: entrenamiento (60%), validación (20%) para optimizar, y prueba (20%) para evaluación final.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Carga**
- [ ] **[OBLIGATORIO]** Carga users_behavior.csv
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores
- [ ] Reconoce features básicos (calls, minutes, messages, mb_used)

**Modelos**
- [ ] **[OBLIGATORIO]** Al menos 1 modelo implementado
      

### INTERMEDIO
**Dataset y Exploración**
- [ ] info(), describe(), head() implementados
- [ ] Maneja tipos de datos correctamente

**Segmentación**
- [ ] **[OBLIGATORIO]** Train/validation/test split correcto (60/20/20)
- [ ] Usa random_state para reproducibilidad

**Modelos**
- [ ] DecisionTree, RandomForest o LogisticRegression
- [ ] GridSearchCV para optimización


**Evaluación**
- [ ] **[OBLIGATORIO]** Evaluación en conjunto de prueba
- [ ] Comparación entre modelos
- [ ] Selección justificada del mejor modelo
- [ ] Prueba de cordura básica


### AVANZADO

**Exploración Avanzada**
- [ ] Visualizaciones de distribuciones
- [ ] Análisis de correlaciones
- [ ] Comparación Smart vs Ultra
- [ ] Detección de outliers
- [ ] Feature engineering

**Validación Robusta**
- [ ] Cross-validation implementada 
- [ ] Múltiples métricas de evaluación (F1, AUC-ROC)
- [ ] Identifica overfitting/underfitting en sus modelos 

**Interpretación Profunda**
- [ ] Insights de negocio específicos
- [ ] Análisis de errores, identifica los casos mal clásificados y por qué

**Código Profesional**
- [ ] Funciones modulares
- [ ] Documentación detallada
- [ ] Manejo de errores

## Criterios de Aprobación General
**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**: 
  - Todos los criterios OBLIGATORIOS: 5/5
  - Al menos 3 criterios adicionales 


- **SUFICIENTE (Aprobado satisfactorio)**: 
  - Todos los criterios OBLIGATORIOS: 5/5
  - Al menos 6 criterios adicionales


- **EXCELENTE (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 5/5
  - Al menos 12 criterios adicionales
 
  
## Ejemplos de Cumplimiento

**Selección justificada del mejor modelo:**
```
"Selecciono RandomForest (accuracy: 0.78) sobre DecisionTree (0.75)
porque muestra mejor generalización y menor overfitting en validación."
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Dataset incorrecto o no cargado
- Notebook cargado en google colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 8/8)
- Evaluación solo en datos de entrenamiento
- Data leakage evidente entre conjuntos de datos

## Errores Frecuentes

*Esta sección será completada basándose en feedback de revisores y estudiantes.*

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

**📝 Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)

*Nota al equipo: Se propone crear un Google Form para recopilar feedback continuo de coaches y revisores sobre errores frecuentes observados en los proyectos. Esto permitirá actualizar dinámicamente esta sección con insights reales del proceso de evaluación.*
