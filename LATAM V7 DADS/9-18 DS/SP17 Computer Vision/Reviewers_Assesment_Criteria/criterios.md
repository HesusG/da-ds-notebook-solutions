# Criterios de Evaluación: Proyecto Good Seed - Detección de Edad con Visión Artificial

## Objetivo

Desarrollar modelo de visión artificial (computer vision) para predecir edad de personas en fotografías usando redes neuronales convolucionales (CNN) o transfer learning, procesando imágenes correctamente, y alcanzando MAE < 8 años en conjunto de validación.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: Computer vision, procesamiento de imágenes, redes neuronales convolucionales (CNN), transfer learning, ImageDataGenerator, evaluación con MAE en regresión de imágenes

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

La cadena de supermercados Good Seed quiere explorar si la inteligencia artificial puede ayudar a cumplir las leyes sobre venta de alcohol, asegurándose de no vender alcohol a menores de edad.

Te piden que evalúes la viabilidad de usar visión artificial para verificar la edad de las personas. Tu tarea es construir un modelo que pueda verificar la edad de una persona a partir de una fotografía.

## Instrucciones del proyecto

1. Realiza un análisis exploratorio de datos para obtener una comprensión general del conjunto de datos
2. Entrena y evalúa el modelo (en una plataforma con GPU)
3. Combina tu código, resultados y hallazgos en un reporte final
4. Para aprobar la revisión de código, debes alcanzar al menos un valor MAE de 8 en el conjunto de prueba

## Descripción de los datos

**Imágenes:** `/datasets/faces/final_files/`
- Conjunto de fotografías de rostros
- 7,591 imágenes

**Labels:** `/datasets/faces/labels.csv`
- `file_name`: Nombre del archivo de imagen
- `real_age`: Edad real de la persona

</details>


## Nota Importante sobre la Dificultad de este Proyecto

**Para Revisores**: Este es uno de los proyectos MÁS DIFÍCILES del bootcamp porque:
- Requiere GPU para entrenamiento (plataforma separada)
- Introduce computer vision y CNNs (temas avanzados)
- Procesamiento de imágenes es diferente a datos tabulares
- Tiempos de entrenamiento largos
- Dataset limitado para clase minoritaria (menores de 18)

**Recomendación**: Ser MUY LAXOS con los criterios. Si el estudiante logra cargar imágenes, entrenar CUALQUIER red neuronal, y obtener MAE < 8, debe APROBAR. No exigir perfección en arquitectura, hiperparámetros, o código.

**Enfoque**: Evaluar esfuerzo y comprensión básica, NO perfección técnica.


## Glosario de Términos Técnicos

**Computer Vision**: Área de IA que permite a las computadoras "ver" y entender imágenes.

**CNN (Convolutional Neural Network)**: Red neuronal especializada en procesar imágenes usando capas convolucionales que detectan patrones visuales.

**Transfer Learning**: Técnica de reutilizar un modelo pre-entrenado (como ResNet50 en ImageNet) y adaptarlo a nueva tarea. Más efectivo que entrenar desde cero.

**ImageDataGenerator**: Herramienta de Keras para cargar y preprocesar imágenes automáticamente desde directorios.

**MAE (Mean Absolute Error)**: Error absoluto promedio entre edad predicha y edad real. En años. Valores bajos son mejores.

**Rescaling/Normalización**: Dividir píxeles por 255 para convertir rango [0, 255] a [0, 1]. Mejora entrenamiento de redes neuronales.

**ResNet50**: Arquitectura de CNN pre-entrenada con 50 capas. Muy efectiva para visión artificial.

**GlobalAveragePooling2D**: Capa que reduce dimensiones de salida de CNN promediando.

**Batch Size**: Número de imágenes procesadas simultáneamente en cada paso de entrenamiento.

**Epoch**: Una pasada completa sobre todo el conjunto de entrenamiento.

**GPU (Graphics Processing Unit)**: Hardware necesario para entrenar redes neuronales grandes en tiempos razonables.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Carga de Datos**
- [ ] **[OBLIGATORIO]** Carga imágenes desde `/datasets/faces/final_files/`
- [ ] **[OBLIGATORIO]** Carga labels desde labels.csv
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores graves

**Preprocesamiento de Imágenes**
- [ ] **[OBLIGATORIO]** Redimensiona imágenes a tamaño consistente (cualquier tamaño entre 128x128 y 224x224 aceptable)
- [ ] **[OBLIGATORIO]** Normaliza/rescala píxeles (divide por 255 o usa rescale=1./255)
- [ ] Divide datos en train/validation (cualquier split aceptable: 70/30, 75/25, 80/20)

### INTERMEDIO

**Preprocesamiento Avanzado**
- [ ] Usa ImageDataGenerator con flow_from_dataframe
- [ ] Configura validation_split correctamente

**Arquitectura de Modelo**
- [ ] Usa transfer learning (ResNet50, VGG, MobileNet, etc.)
- [ ] Configura capas de salida apropiadas para regresión (Dense con 1 neurona)
- [ ] Usa optimizador apropiado (Adam, SGD, etc.)

**Entrenamiento**
- [ ] Entrena al menos 10 epochs
- [ ] MAE < 7 en conjunto de validación

### AVANZADO

**Optimización**
- [ ] Experimenta con múltiples arquitecturas o hiperparámetros
- [ ] Implementa data augmentation
- [ ] MAE < 6.5 en conjunto de validación
- [ ] Usa callbacks (EarlyStopping, ReduceLROnPlateau, etc.)


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 1 criterio adicional de los 7 no obligatorios
  - **Total: 11/17 criterios**

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 3 criterios adicionales de los 7 no obligatorios
  - **Total: 13/17 criterios**

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 5 criterios adicionales de los 7 no obligatorios
  - **Total: 15/17 criterios**


## Ejemplos de Cumplimiento

**Carga de imágenes con ImageDataGenerator:**
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd

# Cargar labels
labels = pd.read_csv('/datasets/faces/labels.csv')
labels['file_name'] = labels['file_name'].apply(lambda x: f'/datasets/faces/final_files/{x}')

# ImageDataGenerator con normalización
datagen = ImageDataGenerator(
    rescale=1./255,  # Normalizar píxeles
    validation_split=0.25  # 75% train, 25% validation
)

# Generadores
train_gen = datagen.flow_from_dataframe(
    dataframe=labels,
    x_col='file_name',
    y_col='real_age',
    target_size=(224, 224),  # Redimensionar a 224x224
    batch_size=32,
    class_mode='raw',  # Para regresión
    subset='training'
)

val_gen = datagen.flow_from_dataframe(
    dataframe=labels,
    x_col='file_name',
    y_col='real_age',
    target_size=(224, 224),
    batch_size=32,
    class_mode='raw',
    subset='validation'
)
```

**Modelo simple con CNN desde cero:**
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Arquitectura simple
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='relu')  # Salida: 1 valor (edad)
])

model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# Entrenar
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=10
)
```

**Modelo con Transfer Learning (ResNet50) - MÁS RECOMENDADO:**
```python
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.optimizers import Adam

# Cargar ResNet50 pre-entrenado (sin top layer)
backbone = ResNet50(
    include_top=False,
    input_shape=(224, 224, 3),
    weights='imagenet'
)

# Congelar capas del backbone (opcional)
backbone.trainable = False

# Construir modelo
model = Sequential([
    backbone,
    GlobalAveragePooling2D(),
    Dense(1, activation='relu')  # Salida: edad
])

model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='mse',
    metrics=['mae']
)

# Entrenar
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=20
)

# Evaluar
val_mae = history.history['val_mae'][-1]
print(f"MAE en validación: {val_mae:.2f} años")
print(f"Cumple umbral (< 8): {val_mae < 8}")
```

**Evaluación y selección de modelo:**
```python
# Obtener MAE del mejor epoch
best_mae = min(history.history['val_mae'])
print(f"\nMejor MAE alcanzado: {best_mae:.2f} años")

if best_mae < 8:
    print("✓ Modelo APROBADO - Cumple umbral MAE < 8")
elif best_mae < 7:
    print("✓✓ Modelo EXCELENTE - MAE < 7")
elif best_mae < 6.5:
    print("✓✓✓ Modelo SOBRESALIENTE - MAE < 6.5")
else:
    print("✗ Modelo NO cumple umbral - Necesita mejorar")
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar o con errores graves
- No cumple criterios OBLIGATORIOS (menos de 10/10)
- **MAE > 8 en conjunto de validación** (no cumple umbral mínimo)
- **No carga imágenes correctamente** (no pueden entrenarse modelos)
- **No normaliza píxeles** (modelo no converge apropiadamente)
- **No entrena modelo** (solo carga datos sin entrenar)
- **No es un problema de regresión** (trata edad como clasificación multi-clase)

## Errores Frecuentes

**¿Has identificado errores comunes en este proyecto?**

### Errores en Carga de Datos

1. **No especificar class_mode='raw' para regresión**:
   - Incorrecto: `class_mode='categorical'` o `class_mode='binary'`
   - Correcto: `class_mode='raw'` (para valores continuos/regresión)
   - Consecuencia: Modelo trata edad como clasificación, no regresión

2. **No construir rutas completas de archivos**:
   - Incorrecto: Usar solo nombres de archivos del CSV
   - Correcto: Agregar prefijo `/datasets/faces/final_files/` a file_name
   - Consecuencia: Imágenes no se encuentran, error de lectura

3. **Tamaños de imagen inconsistentes**:
   - Incorrecto: No especificar target_size en flow_from_dataframe
   - Correcto: target_size=(224, 224) o similar
   - Consecuencia: Error por dimensiones variables de entrada

### Errores en Preprocesamiento

4. **No normalizar píxeles**:
   - Incorrecto: Usar valores [0, 255] directamente
   - Correcto: rescale=1./255 en ImageDataGenerator
   - Consecuencia: Convergencia lenta o modelo no aprende

5. **Olvidar validation_split**:
   - Incorrecto: No dividir datos, entrenar en todo el dataset
   - Correcto: validation_split=0.25 y subset='training'/'validation'
   - Consecuencia: No puede evaluar generalización, overfitting

### Errores en Arquitectura

6. **Función de activación incorrecta en salida**:
   - Incorrecto: Dense(1, activation='sigmoid') para edad
   - Correcto: Dense(1, activation='relu') o sin activación
   - Consecuencia: Predicciones limitadas a [0,1], no representa edades

7. **No usar transfer learning cuando es posible**:
   - Incorrecto: Solo intentar CNN desde cero con dataset pequeño
   - Correcto: Usar ResNet50, VGG, MobileNet pre-entrenados
   - Consecuencia: MAE alto, no alcanza umbral de 8

### Errores en Entrenamiento

8. **Muy pocas epochs**:
   - Incorrecto: Entrenar solo 2-3 epochs
   - Correcto: Al menos 10-20 epochs
   - Consecuencia: Modelo no converge, MAE alto

9. **Batch size muy grande o muy pequeño**:
   - Incorrecto: batch_size=1 o batch_size=256
   - Correcto: batch_size=16, 32, 64 (típico)
   - Consecuencia: Inestabilidad o lentitud excesiva

10. **Usar accuracy en lugar de MAE**:
    - Incorrecto: metrics=['accuracy'] (para clasificación)
    - Correcto: metrics=['mae'] (para regresión)
    - Consecuencia: Métrica incorrecta, no evalúa regresión

### Errores Conceptuales

11. **Tratar edad como clasificación multi-clase**:
    - Incorrecto: 100 clases (una por edad 1-100)
    - Correcto: Regresión con salida continua
    - Consecuencia: Arquitectura incorrecta, no es el objetivo

12. **No entender que MAE está en años**:
    - Incorrecto: Pensar que MAE de 6 es malo
    - Correcto: MAE de 6 años es excelente (predice edad ±6 años)
    - Consecuencia: Interpretación incorrecta de resultados

13. **Intentar entrenar sin GPU**:
    - Incorrecto: Correr en CPU local (muy lento)
    - Correcto: Usar plataforma con GPU (Google Colab, Kaggle, etc.)
    - Consecuencia: Entrenamiento toma horas/días en lugar de minutos

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
