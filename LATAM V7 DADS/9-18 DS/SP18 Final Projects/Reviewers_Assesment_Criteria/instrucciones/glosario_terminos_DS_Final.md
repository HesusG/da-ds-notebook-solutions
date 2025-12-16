# Glosario de Términos Técnicos - DS_Final

Este glosario contiene definiciones de los términos técnicos utilizados en las tres etapas del proyecto final de Data Science.

---

## A

### Accuracy (Exactitud)
Proporción de predicciones correctas sobre el total. `Accuracy = (TP + TN) / (TP + TN + FP + FN)`. Útil cuando las clases están balanceadas; engañosa cuando hay desbalanceo significativo.

### AUC-ROC (Area Under the ROC Curve)
Área bajo la curva ROC. Mide la capacidad del modelo de discriminar entre clases. Rango [0, 1], donde 0.5 es aleatorio y 1.0 es perfecto. Independiente del umbral de decisión.

---

## B

### Baseline (Modelo Base)
Modelo de referencia simple que establece el rendimiento mínimo a superar. En scikit-learn: `DummyClassifier` (clasificación) o `DummyRegressor` (regresión). Un modelo útil debe superar significativamente al baseline.

### Balanceo de Clases
Técnicas para manejar datasets donde una clase tiene muchas más muestras que otra. Incluye: upsampling (aumentar minoritaria), downsampling (reducir mayoritaria), SMOTE (generar sintéticos), class_weight (penalizar errores en minoritaria).

---

## C

### CAR (Challenge-Action-Results)
Estructura de comunicación ejecutiva para presentar proyectos:
- **Challenge**: El problema y su contexto
- **Action**: Lo que se hizo para resolverlo
- **Results**: Los resultados e impacto logrado

### class_weight='balanced'
Parámetro de scikit-learn que ajusta pesos inversamente proporcionales a la frecuencia de clases. Penaliza más los errores en la clase minoritaria.

### Confusion Matrix (Matriz de Confusión)
Tabla que muestra las predicciones vs valores reales:
```
              Predicho
              Neg   Pos
Real  Neg     TN    FP
      Pos     FN    TP
```

### Cross-Validation (Validación Cruzada)
Técnica que divide datos en K particiones. Entrena en K-1, valida en 1, repite K veces. Produce estimación más robusta del rendimiento. `StratifiedKFold` mantiene proporción de clases.

---

## D

### Data Leakage (Filtración de Datos)
Error donde información del conjunto de prueba contamina el entrenamiento. Ejemplos:
- Escalar/codificar antes del split
- Usar features que no existirían en producción
- Incluir información del futuro

### DummyClassifier
Clasificador de scikit-learn que hace predicciones simples ignorando features. Strategies:
- `stratified`: Proporcional a distribución de clases
- `most_frequent`: Siempre predice clase mayoritaria
- `uniform`: Aleatorio uniforme

### DummyRegressor
Regresor de scikit-learn para baseline. Strategies:
- `mean`: Siempre predice la media
- `median`: Siempre predice la mediana

---

## E

### EDA (Exploratory Data Analysis)
Análisis exploratorio de datos. Incluye:
- Estadísticas descriptivas (describe())
- Distribuciones (histogramas)
- Correlaciones
- Detección de outliers
- Calidad de datos (NaN, duplicados)

---

## F

### F1-Score
Media armónica de precision y recall. `F1 = 2 × (Precision × Recall) / (Precision + Recall)`. Útil cuando se necesita balance entre precision y recall.

### False Negative (FN)
Caso positivo real predicho como negativo. En churn: cliente que canceló pero el modelo predijo que no.

### False Positive (FP)
Caso negativo real predicho como positivo. En churn: cliente que no canceló pero el modelo predijo que sí.

### Feature Importance (Importancia de Variables)
Medida de cuánto contribuye cada variable a las predicciones. En árboles: basada en ganancia de información. En modelos lineales: coeficientes.

### Feature Engineering
Proceso de crear nuevas variables a partir de las existentes. Ejemplo: crear "tenure_months" a partir de fecha de inicio.

---

## G

### GridSearchCV
Búsqueda exhaustiva de hiperparámetros. Prueba todas las combinaciones del grid definido con validación cruzada. Computacionalmente costosa pero completa.

---

## H

### Hiperparámetros
Parámetros del modelo que no se aprenden de los datos. Se definen antes del entrenamiento. Ejemplos: n_estimators, max_depth, learning_rate.

---

## I

### Imputación
Técnica para manejar valores ausentes reemplazándolos con valores estimados. Estrategias:
- Media/Mediana: Para numéricas
- Moda: Para categóricas
- KNN: Basado en vecinos similares

---

## K

### KPI (Key Performance Indicator)
Métrica clave para evaluar el éxito. En ML típicamente: Accuracy, F1, AUC-ROC, RMSE. Debe tener umbral de aceptación definido.

---

## L

### Label Encoding
Convierte categorías en enteros (0, 1, 2...). Útil para modelos basados en árboles. Problema: implica orden que puede no existir.

### LightGBM
Implementación eficiente de gradient boosting. Características: leaf-wise growth, histogram-based, manejo nativo de categóricas.

### LTV (Lifetime Value)
Valor de por vida del cliente. Ingresos totales esperados durante la relación. Usado para cuantificar impacto de retención.

---

## M

### MAE (Mean Absolute Error)
Error absoluto medio. `MAE = mean(|y_real - y_pred|)`. Menos sensible a outliers que RMSE.

### MinMaxScaler
Escala features al rango [0, 1]. `X_scaled = (X - X_min) / (X_max - X_min)`. Útil cuando se necesitan valores positivos.

### Multicolinealidad
Correlación alta entre variables predictoras. Puede causar inestabilidad en modelos lineales. Se mitiga con `drop='first'` en OHE.

---

## O

### One-Hot Encoding (OHE)
Convierte categóricas en columnas binarias (0/1). Cada categoría única se convierte en una columna. `drop='first'` evita multicolinealidad.

### Overfitting (Sobreajuste)
Modelo memoriza training pero no generaliza a datos nuevos. Se detecta cuando `train_score >> test_score`. Se mitiga con regularización, validación cruzada, más datos.

---

## P

### Precision (Precisión)
Proporción de predicciones positivas que son correctas. `Precision = TP / (TP + FP)`. Alta precision = pocos falsos positivos.

---

## R

### Random Forest
Ensemble de árboles de decisión entrenados con diferentes subconjuntos de datos y features. Robusto a overfitting, maneja no-linealidades.

### RandomizedSearchCV
Búsqueda aleatoria de hiperparámetros. Muestrea n combinaciones del espacio definido. Más eficiente que GridSearch para espacios grandes.

### Recall (Sensibilidad)
Proporción de casos positivos reales capturados. `Recall = TP / (TP + FN)`. Alto recall = pocos falsos negativos.

### RMSE (Root Mean Squared Error)
Raíz del error cuadrático medio. `RMSE = sqrt(mean((y_real - y_pred)^2))`. Penaliza errores grandes, en mismas unidades que target.

### ROC Curve (Curva ROC)
Gráfico de True Positive Rate vs False Positive Rate a diferentes umbrales. Permite visualizar trade-off entre sensitivity y specificity.

### ROI (Return on Investment)
Retorno sobre inversión. `ROI = (Beneficio - Costo) / Costo × 100%`. Métrica clave para justificar proyectos.

---

## S

### SMOTE (Synthetic Minority Over-sampling)
Técnica de oversampling que genera ejemplos sintéticos de clase minoritaria interpolando entre ejemplos existentes y sus vecinos.

### Stakeholder
Persona o grupo interesado/afectado por el proyecto. Pueden ser:
- Directos: Usuarios del modelo, tomadores de decisiones
- Indirectos: Clientes, otros equipos

### StandardScaler
Normalización que transforma a media=0, std=1. `X_scaled = (X - mean) / std`. Esencial para modelos sensibles a escala (Logistic Regression, SVM, KNN).

### Stratified Split
División de datos que mantiene la proporción de clases en train y test. Crítico para datasets desbalanceados.

---

## T

### Target (Variable Objetivo)
La variable que el modelo intentará predecir. Definir claramente: nombre de columna, tipo (categórica/numérica), distribución.

### Train/Test Split
División de datos en conjuntos de entrenamiento (para ajustar modelo) y prueba (para evaluar generalización). Típicamente 75/25 o 80/20.

### True Negative (TN)
Caso negativo real predicho correctamente como negativo.

### True Positive (TP)
Caso positivo real predicho correctamente como positivo.

---

## U

### Umbral de Decisión
En clasificación, punto de corte para convertir probabilidad en clase. Default: 0.5. Puede ajustarse para optimizar precision vs recall.

### Underfitting (Subajuste)
Modelo demasiado simple que no captura patrones en los datos. Se detecta cuando tanto train como test scores son bajos.

---

## V

### Validación
Proceso de evaluar rendimiento del modelo en datos no vistos durante entrenamiento. Incluye: holdout (test set), cross-validation.

---

## X

### XGBoost
Implementación de gradient boosting extremadamente eficiente. Características: regularización L1/L2, manejo de missing values, parallel processing.

---

## Referencias

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
