# Criterios de Evaluación: Proyecto Sure Tomorrow - Protección de Datos por Ofuscación

## Objetivo

Implementar algoritmo de ofuscación de datos mediante multiplicación matricial con matriz invertible, verificar empíricamente que la transformación preserva la calidad del modelo de regresión lineal (R² idéntico), y demostrar que datos se pueden recuperar con la matriz inversa mientras se protege información personal.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Álgebra lineal aplicada (multiplicación matricial, matrices invertibles), implementación de regresión lineal desde cero con NumPy, protección de datos (data masking), privacy-preserving machine learning, verificación empírica de preservación de calidad

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

La compañía de seguros Sure Tomorrow tiene cuatro tareas que requieren machine learning. La Tarea 4 (foco de este proyecto) consiste en proteger los datos personales de los clientes mediante ofuscación de datos, sin afectar la calidad del modelo.

Necesitas desarrollar un método de transformación de datos que dificulte la recuperación de información personal si los datos caen en manos equivocadas. La transformación no debe afectar la calidad de los modelos de machine learning.

No es necesario elegir el mejor modelo, solo debes demostrar que el algoritmo funciona correctamente.

## Instrucciones del proyecto

### Tarea 4: Protección de datos

1. Desarrolla un algoritmo de transformación de datos para ofuscar los datos
2. Proporciona una demostración (puede ser matemática o empírica) de que la ofuscación no afecta la calidad del modelo
3. Programa el algoritmo y demuestra que funciona correctamente:
   - Entrena un modelo con datos originales
   - Transforma los datos con tu algoritmo
   - Entrena un modelo con datos transformados
   - Compara las métricas de calidad (R²) de ambos modelos
   - Demuestra que las métricas son iguales

## Método sugerido de ofuscación

Multiplica las características (features) por una matriz invertible.

**Transformación**: X' = X × P

Donde:
- X: matriz de características originales
- P: matriz invertible aleatoria
- X': matriz de características ofuscadas

## Descripción de los datos

**Archivo**: `/datasets/insurance_us.csv`

**Features**:
- `gender`: Género del cliente (0 o 1)
- `age`: Edad del cliente
- `income`: Salario del cliente
- `family_members`: Número de miembros de la familia

**Target**:
- `insurance_benefits`: Número de beneficios de seguro recibidos en los últimos 5 años

**Tamaño**: 5000 registros

</details>


## Glosario de Términos Técnicos

**Ofuscación/Data Masking**: Técnica de transformación de datos que oculta información sensible haciendo que los datos originales sean irrecuperables sin conocer la clave de transformación, mientras se preserva la utilidad para análisis.

**Matriz Invertible**: Matriz cuadrada que tiene una matriz inversa. Para matriz P, existe P^(-1) tal que P × P^(-1) = I (matriz identidad). Condición: determinante ≠ 0.

**Multiplicación Matricial**: Operación donde elemento (i,j) del resultado es el producto punto de fila i de primera matriz con columna j de segunda matriz. El orden importa (AB ≠ BA).

**Matriz Inversa**: Para matriz P, la inversa P^(-1) cumple: P × P^(-1) = P^(-1) × P = I. Se calcula con np.linalg.inv(P).

**Matriz Identidad (I)**: Matriz cuadrada con 1s en diagonal y 0s en otros lugares. Propiedad: A × I = I × A = A.

**Regresión Lineal en forma matricial**: Modelo donde predicciones son a = Xw, y los pesos se calculan como w = (X^T X)^(-1) X^T y.

**R² (R-squared/Coeficiente de determinación)**: Métrica que mide qué proporción de la varianza en la variable objetivo es explicada por el modelo. Rango [0, 1], donde 1 es perfecto.

**RMSE (Root Mean Squared Error)**: Raíz del error cuadrático medio. Mide la magnitud promedio del error de predicción.

**Bias term/Intercept**: Término independiente en regresión lineal. Se implementa agregando columna de 1s a la matriz de features.

**Privacy-preserving ML**: Técnicas de machine learning que protegen privacidad de datos mientras permiten entrenamiento y predicción de modelos.

**Floating-point precision**: Limitación numérica de computadoras que causa pequeños errores de redondeo (ej: 1.0000000001 en lugar de 1.0).

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Carga**
- [ ] **[OBLIGATORIO]** Carga insurance_us.csv correctamente (5000 registros, 5 columnas)
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores (todas las celdas ejecutadas secuencialmente)
- [ ] Separa correctamente features (4 columnas) y target (insurance_benefits)

**Ofuscación Básica**
- [ ] **[OBLIGATORIO]** Genera matriz P aleatoria de dimensión 4×4
- [ ] **[OBLIGATORIO]** Ofusca datos multiplicando: X' = X @ P
- [ ] Muestra que datos ofuscados lucen diferentes a datos originales

### INTERMEDIO

**Implementación de Regresión Lineal**
- [ ] **[OBLIGATORIO]** Implementa regresión lineal usando operaciones matriciales NumPy (no sklearn.LinearRegression)
- [ ] Usa np.linalg.inv() para inversión de matrices
- [ ] Implementa métodos fit() y predict()

**Verificación de Invertibilidad**
- [ ] **[OBLIGATORIO]** Verifica que P es invertible calculando P^(-1) con np.linalg.inv()

**Reversibilidad**
- [ ] **[OBLIGATORIO]** Demuestra reversibilidad: X_recovered = X' @ P^(-1)

**Comparación de Modelos**
- [ ] Entrena modelo en datos originales y calcula R² y RMSE
- [ ] **[OBLIGATORIO]** Entrena modelo en datos ofuscados y calcula R² y RMSE
- [ ] **[OBLIGATORIO]** Verifica que R² original ≈ R² ofuscado (diferencia < 0.01)

### AVANZADO

**Verificación Exhaustiva de Predicciones**
- [ ] Compara predicciones individuales: y_pred_original vs y_pred_ofuscado
- [ ] Demuestra que predicciones son idénticas elemento por elemento (diferencia < 1e-10)
- [ ] Calcula y muestra diferencia máxima entre predicciones

**Análisis de Pesos**
- [ ] Muestra que pesos w y w' son diferentes
- [ ] Calcula w' teóricamente: w' = P^(-1) @ w (si se implementa)
- [ ] Explica conceptualmente por qué w ≠ w' pero a = a'


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 3 criterios adicionales de los 20 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 6 criterios adicionales de los 20 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 12 criterios adicionales de los 20 no obligatorios


## Nota Importante sobre Demostración Matemática

**Para Revisores**: La demostración matemática formal que prueba algebraicamente que a' = a requiere conocimientos avanzados de álgebra lineal (propiedades de transposición, inversión de matrices, simplificación de identidades) que están fuera del alcance esperado para este nivel.

**Recomendación**: Se acepta y valora la **verificación empírica** como prueba suficiente. Si el estudiante demuestra que R² original = R² ofuscado mediante experimentación (entrenando ambos modelos y comparando métricas), esto es evidencia sólida de que el algoritmo funciona correctamente.

La demostración matemática formal NO es un criterio obligatorio. Si el estudiante la incluye y es correcta, debe valorarse como criterio AVANZADO adicional, pero su ausencia no debe penalizar el proyecto.


## Ejemplos de Cumplimiento

**Implementación correcta de regresión lineal personalizada:**
```python
class MyLinearRegression:
    def __init__(self):
        self.weights = None

    def fit(self, X, y):
        # Agregar columna de 1s para bias term
        X_bias = np.append(np.ones([len(X), 1]), X, axis=1)

        # Calcular pesos: w = (X^T X)^(-1) X^T y
        self.weights = np.linalg.inv(X_bias.T @ X_bias) @ X_bias.T @ y

    def predict(self, X):
        # Agregar columna de 1s para bias term
        X_bias = np.append(np.ones([len(X), 1]), X, axis=1)

        # Predicciones: a = Xw
        return X_bias @ self.weights
```

**Generación de matriz invertible:**
```python
def generate_invertible_matrix(n_features, seed=42):
    """Genera matriz invertible aleatoria"""
    rng = np.random.default_rng(seed=seed)
    P = rng.random(size=(n_features, n_features))

    try:
        P_inv = np.linalg.inv(P)
        det_P = np.linalg.det(P)
        print(f"Matriz P es invertible. Determinante: {det_P:.4f}")
        return P, P_inv
    except np.linalg.LinAlgError:
        print("Matriz no invertible. Generando nueva...")
        return generate_invertible_matrix(n_features, seed=seed+1)
```

**Ofuscación y reversibilidad:**
```python
# Ofuscar datos
X_obfuscated = X @ P
print("Primeras 3 filas de datos originales:")
print(X[:3])
print("\nPrimeras 3 filas de datos ofuscados:")
print(X_obfuscated[:3])

# Recuperar datos originales
X_recovered = X_obfuscated @ P_inv
print("\nPrimeras 3 filas de datos recuperados:")
print(X_recovered[:3])

# Verificar recuperación
difference = np.abs(X - X_recovered)
max_diff = difference.max()
print(f"\nDiferencia máxima: {max_diff:.2e}")
print(f"Recuperación exitosa: {max_diff < 1e-10}")
```

**Comparación de resultados:**
```python
# Modelo con datos originales
model_original = MyLinearRegression()
model_original.fit(X_train, y_train)
y_pred_original = model_original.predict(X_test)
r2_original = r2_score(y_test, y_pred_original)
rmse_original = mean_squared_error(y_test, y_pred_original, squared=False)

# Modelo con datos ofuscados
X_train_obf = X_train @ P
X_test_obf = X_test @ P
model_obfuscated = MyLinearRegression()
model_obfuscated.fit(X_train_obf, y_train)
y_pred_obfuscated = model_obfuscated.predict(X_test_obf)
r2_obfuscated = r2_score(y_test, y_pred_obfuscated)
rmse_obfuscated = mean_squared_error(y_test, y_pred_obfuscated, squared=False)

# Comparar
print("="*50)
print("COMPARACIÓN DE RESULTADOS")
print("="*50)
print(f"R² Original:     {r2_original:.6f}")
print(f"R² Ofuscado:     {r2_obfuscated:.6f}")
print(f"Diferencia R²:   {abs(r2_original - r2_obfuscated):.2e}")
print(f"\nRMSE Original:   {rmse_original:.6f}")
print(f"RMSE Ofuscado:   {rmse_obfuscated:.6f}")
print(f"Diferencia RMSE: {abs(rmse_original - rmse_obfuscated):.2e}")

# Verificar predicciones idénticas
pred_diff = np.abs(y_pred_original - y_pred_obfuscated)
print(f"\nDiferencia máxima en predicciones: {pred_diff.max():.2e}")
print(f"✓ Ofuscación preserva calidad del modelo" if pred_diff.max() < 1e-10 else "✗ Error en implementación")
```

**Salida esperada:**
```
==================================================
COMPARACIÓN DE RESULTADOS
==================================================
R² Original:     0.660000
R² Ofuscado:     0.660000
Diferencia R²:   0.00e+00

RMSE Original:   0.340000
RMSE Ofuscado:   0.340000
Diferencia RMSE: 0.00e+00

Diferencia máxima en predicciones: 1.42e-14
✓ Ofuscación preserva calidad del modelo
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 10/10)
- **Usa sklearn.LinearRegression en lugar de implementación propia**
- **R² original ≠ R² ofuscado** (diferencia > 0.01) indica implementación incorrecta
- **No demuestra reversibilidad** de la transformación (no calcula X_recovered)
- **Matriz P no es invertible** (determinante = 0 o no verifica invertibilidad)
- **Dimensiones incorrectas**: P no es 4×4 (debe coincidir con número de features)

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Errores en Implementación

1. **Usar sklearn.LinearRegression (ERROR MÁS COMÚN)**:
   - Incorrecto: `from sklearn.linear_model import LinearRegression`
   - Correcto: Implementar clase propia con operaciones matriciales NumPy
   - Consecuencia: No cumple objetivo de demostrar comprensión de álgebra lineal





**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
