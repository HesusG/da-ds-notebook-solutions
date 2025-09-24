# Criterios de Evaluación: Proyecto Megaline

## Objetivos de Aprendizaje

### Objetivo General
Aplicar algoritmos de machine learning supervisado para resolver un problema de clasificación binaria en el dominio de telecomunicaciones.

### Objetivos Específicos (Taxonomía de Bloom)

**Recordar (Conocimiento)**
- Identificar algoritmos apropiados para clasificación binaria
- Reconocer métricas de evaluación para problemas de clasificación

**Comprender (Comprensión)**
- Explicar diferencias entre modelos de clasificación
- Interpretar métricas de accuracy en contexto de negocio

**Aplicar (Aplicación)**
- Implementar train/validation/test split correctamente
- Ejecutar múltiples algoritmos ML en mismo dataset

**Analizar (Análisis)**
- Comparar rendimiento entre diferentes modelos
- Evaluar trade-offs de accuracy vs complejidad

**Evaluar (Evaluación)**
- Justificar selección del modelo final
- Validar resultados mediante prueba de cordura

**Crear (Síntesis)**
- Generar recomendaciones de negocio basadas en resultados

### Condiciones de Aprendizaje
- Requisitos previos: Python básico, conceptos ML fundamentales (necesitaria detallarlo con el conocimiento previo de los sprints)

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

## Evaluación del proyecto original

Los revisores evalúan: lectura de datos, segmentación correcta, tamaño de conjuntos, evaluación de calidad, modelos e hiperparámetros, hallazgos, pruebas correctas, puntuación de exactitud, estructura del proyecto y código limpio.

</details>

## Análisis de la Solución Actual

### Fortalezas Identificadas

**Cumplimiento Técnico**

- Accuracy logrado: 0.79 (DecisionTree), 0.78 (RandomForest)
- Segmentación apropiada: 60/20/20
- Tres modelos implementados: DecisionTree, RandomForest, LogisticRegression
- GridSearchCV implementado (nota: conceptos avanzados no cubiertos aún en el curso)
- Reproducibilidad con random_state

### Limitaciones Detectadas

**Exploración Limitada**
- EDA muy básico: solo info(), describe(), head()
- No hay visualizaciones
- No analiza distribuciones Smart vs Ultra

**Validación Básica**
- Prueba de cordura muy simple

---

## Rúbrica de Evaluación - Checklist para Revisores

| Categoría | BÁSICO | SUFICIENTE | EXCELENTE |
|-----------|--------|------------|-----------|
| **Dataset y Exploración** | - [ ] Carga `users_behavior.csv` <br> - [ ] Código ejecuta sin errores <br> - [ ] Reconoce features básicos | - [ ] Carga dataset correcto <br> - [ ] `info()`, `describe()`, `head()` <br> - [ ] Manejo correcto de tipos de datos <br> - [ ] (No tiene) Visualizaciones <br> - [ ] (No tiene) Análisis por clases | - [ ] Visualizaciones de distribuciones <br> - [ ] Análisis de correlaciones <br> - [ ] Comparación Smart vs Ultra <br> - [ ] Detección de outliers <br> - [ ] Feature engineering |
| **Segmentación / Validación** | - [ ] Usa `train_test_split` básico | - [ ] Split 60/20/20 correcto <br> - [ ] Usa `random_state` <br> - [ ] (No tiene) Cross-validation | - [ ] Cross-validation (StratifiedKFold) <br> - [ ] Learning/validation curves <br> - [ ] Múltiples métricas <br> - [ ] Análisis overfitting/underfitting |
| **Modelos** | - [ ] ≥1 modelo implementado <br> - [ ] Accuracy > 0.60 | - [ ] DecisionTree <br> - [ ] RandomForest <br> - [ ] LogisticRegression <br> - [ ] GridSearchCV <br> - [ ] Accuracy ≥ 0.75 | - [ ] Ensemble methods <br> - [ ] Feature scaling (LogisticRegression) <br> - [ ] Optimización hiperparámetros <br> - [ ] Pipeline sklearn |
| **Evaluación / Interpretación** | - [ ] *(No requiere EDA, CV, GridSearch, Sanity check)* | - [ ] Evaluación en test set <br> - [ ] Comparación entre modelos <br> - [ ] Selección justificada <br> - [ ] Prueba de cordura básica | - [ ] Matriz de confusión <br> - [ ] ROC curves <br> - [ ] Insights de negocio <br> - [ ] Análisis de errores <br> - [ ] Comparación con modelo aleatorio <br> - [ ] Distribución de predicciones |
| **Código / Documentación** | - [ ] *(No requiere extra)* | - [ ] Notebook claro <br> - [ ] Comentarios explicativos <br> - [ ] Flujo lógico | - [ ] Funciones modulares <br> - [ ] Documentación detallada <br> - [ ] Manejo de errores |

## Criterios de Descalificación

**Errores Críticos:**
- Dataset incorrecto o no cargado
- Notebook cargado en google colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- Accuracy < 0.75 en conjunto de prueba
- Evaluación solo en datos de entrenamiento
- Data leakage evidente

---

## ANÁLISIS DE LA SOLUCIÓN ACTUAL

### SUFICIENTE (Solución Actual)

**Dataset y Exploración**
- [x] Carga dataset correcto
- [x] info(), describe(), head() implementados
- [x] Maneja tipos de datos correctamente
- [ ] Visualizaciones (no tiene)
- [ ] Análisis por clases (no tiene)

**Segmentación**
- [x] Train/validation/test split correcto (60/20/20)
- [x] Usa random_state para reproducibilidad
- [ ] Cross-validation (no tiene)

**Modelos**
- [x] Mínimo 2 modelos diferentes
- [x] DecisionTree implementado
- [x] RandomForest implementado
- [x] LogisticRegression implementado
- [x] GridSearchCV para optimización
- [x] Accuracy >= 0.75 alcanzado

**Evaluación**
- [x] Evaluación en conjunto de prueba
- [x] Comparación sistemática entre modelos
- [x] Selección justificada del mejor modelo
- [x] Prueba de cordura implementada (básica)
- [ ] Feature importance (no tiene)

**Código**
- [x] Estructura clara del notebook
- [x] Comentarios explicativos
- [x] Flujo lógico



## Recomendaciones para Pasar de Suficiente a Excelente

La solución actual necesita:

1. **EDA Visual**: Histogramas, boxplots, correlaciones
2. **Cross-Validation**: Verificar la implementación del cross validation según el feedback recibido
3. **Business Insights**: Interpretar qué caracteriza cada plan


## Alineación Pedagógica


| Categoría               | Objetivo de Aprendizaje      | Checklist de Evaluación                |
| ----------------------- | ---------------------------- | -------------------------------------- |
| **Recordar/Comprender** | Identifica algoritmos ML     | “Al menos 1 modelo implementado”       |
|                         | Reconoce métricas            | “Accuracy > 0.60”                      |
| **Aplicar**             | Implementa train/test split  | “Train/validation/test split correcto” |
|                         | Ejecuta múltiples algoritmos | “Mínimo 2 modelos diferentes”          |
| **Analizar/Evaluar**    | Compara modelos              | “Múltiples métricas de evaluación”     |
|                         | Justifica selección          | “Insights de negocio específicos”      |
| **Crear**               | Recomendaciones de negocio   | “Análisis de errores”                  |
