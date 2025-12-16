# Criterios de Evaluación: Proyecto Film Junky Union - Análisis de Sentimiento

## Objetivo

Desarrollar sistema de clasificación binaria de sentimientos en reseñas de películas usando procesamiento de lenguaje natural (NLP), aplicando normalización de texto, lemmatización (NLTK o spaCy), vectorización TF-IDF, y alcanzando F1 score ≥ 0.85 en conjunto de prueba.

**Requisitos previos**: TBD

**Competencias que desarrollarás**: NLP (procesamiento de lenguaje natural), clasificación de texto, lemmatización, TF-IDF, análisis de sentimientos, comparación de bibliotecas NLP (NLTK vs spaCy), evaluación con F1 score

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

Film Junky Union, una nueva comunidad edgy para aficionados de las películas clásicas, está desarrollando un sistema para filtrar y categorizar reseñas de películas. Tu objetivo es entrenar un modelo para detectar automáticamente las críticas negativas.

Utilizarás un conjunto de datos de reseñas de películas de IMDB con etiquetado para construir un modelo que clasifique reseñas como positivas o negativas.

## Instrucciones del proyecto

1. Carga los datos
2. Lleva a cabo el EDA y haz conclusiones sobre la proporción de clases
3. Preprocesa los datos para el modelado
4. Entrena al menos tres modelos diferentes para el conjunto de datos de entrenamiento
5. Prueba los modelos para el conjunto de datos de prueba
6. Compón tus propios reviews e introdúcelos en los modelos para ver si identifican correctamente los sentimientos

**Objetivo**: Alcanzar un valor F1 de al menos 0.85 en el conjunto de prueba

## Descripción de los datos

**Archivo:** `/datasets/imdb_reviews.tsv`

Los datos fueron provistos por Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, y Christopher Potts. (2011). Learning Word Vectors for Sentiment Analysis. La reunión anual número 49 de la Asociación de Lingüística Computacional (ACL 2011).

**Columnas:**
- `review`: Texto de la reseña
- `pos`: Target (0 = negativo, 1 = positivo)
- `ds_part`: Indica si pertenece al conjunto 'train' o 'test'

Los archivos seleccionados están equilibrados entre críticas positivas y negativas.

</details>


## Glosario de Términos Técnicos

**Análisis de Sentimientos**: Tarea de NLP que clasifica texto según su polaridad emocional (positivo/negativo/neutral).

**Lemmatización**: Proceso que reduce palabras a su forma base/raíz (lema). Ejemplo: "running", "ran", "runs" → "run". Más preciso que stemming.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Técnica de vectorización que convierte texto en números ponderando palabras por importancia. Palabras comunes tienen menor peso.

**NLTK (Natural Language Toolkit)**: Biblioteca Python para NLP que incluye tokenización, lemmatización, stopwords.

**spaCy**: Biblioteca Python moderna para NLP, más rápida que NLTK, con modelos pre-entrenados para lemmatización.

**Stopwords**: Palabras comunes sin valor semántico (the, and, is, etc.) que se eliminan del texto para reducir ruido.

**F1 Score**: Métrica que balancea precisión y recall. Ideal para clasificación binaria. Rango [0,1], donde 1 es perfecto.

**Normalización de Texto**: Limpiar texto eliminando caracteres especiales, números, convertir a minúsculas, etc.

**Vectorización**: Convertir texto (strings) en representación numérica que modelos ML puedan procesar.

**DummyClassifier**: Modelo baseline que hace predicciones simples (aleatorias, constantes) para establecer punto de referencia.

**ROC AUC**: Área bajo curva ROC. Mide capacidad del modelo de distinguir entre clases.

**BERT (Bidirectional Encoder Representations from Transformers)**: Modelo avanzado de NLP basado en transformers. Opcional en este proyecto.

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**Dataset y Exploración**
- [ ] **[OBLIGATORIO]** Carga imdb_reviews.tsv correctamente
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores
- [ ] Analiza distribución de clases (pos: 0 vs 1)
- [ ] Verifica proporción train/test usando columna ds_part

**Preprocesamiento de Texto**
- [ ] **[OBLIGATORIO]** Normaliza texto (lowercase, elimina caracteres especiales/números)
- [ ] **[OBLIGATORIO]** Aplica lemmatización (NLTK o spaCy)
- [ ] Elimina stopwords


### INTERMEDIO

**Vectorización**
- [ ] **[OBLIGATORIO]** Aplica TF-IDF vectorization a textos preprocesados
- [ ] Usa TfidfVectorizer de sklearn correctamente
- [ ] **[OBLIGATORIO]** Vectoriza features ANTES de entrenar modelos (incluido DummyClassifier si se usa)

**Comparación de Modelos**
- [ ] Implementa al menos 3 modelos diferentes
- [ ] Incluye modelo baseline (DummyClassifier) para comparación
- [ ] Prueba LogisticRegression como uno de los modelos
- [ ] Calcula múltiples métricas (F1, Accuracy, ROC AUC)
- [ ] Crea tabla comparativa de resultados

**Evaluación**
- [ ] **[OBLIGATORIO]** Usa el split train/test proporcionado en ds_part (no crea split adicional)
- [ ] Compara modelos y selecciona el mejor justificando con F1

### AVANZADO

**Comparación de Bibliotecas NLP**
- [ ] Compara NLTK vs spaCy para lemmatización
- [ ] Analiza diferencias en performance entre bibliotecas
- [ ] Documenta ventajas/desventajas de cada enfoque

**Optimización de Modelos**
- [ ] Optimiza hiperparámetros con GridSearchCV
- [ ] Prueba modelos avanzados (LightGBM, XGBoost, Random Forest)
- [ ] Experimenta con diferentes configuraciones de TF-IDF

**Visualización y Análisis**
- [ ] Crea curvas ROC para comparar modelos
- [ ] Crea curvas Precision-Recall
- [ ] Visualiza distribución de longitud de reseñas
- [ ] Analiza palabras más importantes (feature importance o TF-IDF scores)


## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 2 criterios adicionales de los 17 no obligatorios


- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 4 criterios adicionales de los 17 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 8 criterios adicionales de los 17 no obligatorios



## Nota Importante sobre BERT

**Para Revisores**: El uso de BERT (Bidirectional Encoder Representations from Transformers) es **OPCIONAL** en este proyecto. BERT es un modelo avanzado que requiere recursos computacionales significativos y conocimientos avanzados de deep learning.

**Recomendación**: Se valora si el estudiante implementa BERT correctamente, pero **NO es obligatorio**. Modelos tradicionales (LogisticRegression, LightGBM) con TF-IDF son suficientes para alcanzar F1 ≥ 0.85.

Si el estudiante no implementa BERT, esto **NO debe penalizar** el proyecto.


## Ejemplos de Cumplimiento

**Normalización de texto:**
```python
import re

def normalize_text(text):
    """Normaliza texto: lowercase y solo letras"""
    # Eliminar números, caracteres especiales, mantener solo letras y espacios
    text = re.sub("[^a-zA-Z]", " ", text)
    # Convertir a minúsculas y eliminar espacios extras
    text = text.strip().lower()
    return text

# Aplicar normalización
df_reviews['review_norm'] = df_reviews['review'].apply(normalize_text)
```

**Lemmatización con NLTK:**
```python
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Descargar recursos (solo una vez)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Inicializar
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def lemmatize_nltk(text):
    """Tokeniza, lemmatiza y elimina stopwords"""
    # Tokenizar
    tokens = word_tokenize(text)
    # Lemmatizar y filtrar stopwords
    lemmas = [lemmatizer.lemmatize(token) for token in tokens
              if token not in stop_words]
    return ' '.join(lemmas)

# Aplicar
df_reviews['review_lemm'] = df_reviews['review_norm'].apply(lemmatize_nltk)
```

**Lemmatización con spaCy (alternativa):**
```python
import spacy

# Cargar modelo (descarga con: python -m spacy download en_core_web_sm)
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

def lemmatize_spacy(text):
    """Lemmatiza con spaCy y elimina stopwords"""
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc
              if not token.is_stop and not token.is_punct]
    return ' '.join(lemmas)

# Aplicar
df_reviews['review_lemm'] = df_reviews['review_norm'].apply(lemmatize_spacy)
```

**Vectorización TF-IDF:**
```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Separar train/test usando columna ds_part
train_reviews = df_reviews[df_reviews['ds_part'] == 'train']
test_reviews = df_reviews[df_reviews['ds_part'] == 'test']

# Features y target
X_train = train_reviews['review_lemm']
y_train = train_reviews['pos']
X_test = test_reviews['review_lemm']
y_test = test_reviews['pos']

# Vectorizar con TF-IDF
tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

print(f"Train shape: {X_train_tfidf.shape}")
print(f"Test shape: {X_test_tfidf.shape}")
```

**Entrenamiento y evaluación de modelos:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score

results = []

# Modelo 1: Baseline (DummyClassifier)
# IMPORTANTE: DummyClassifier también necesita features vectorizadas
dummy = DummyClassifier(strategy='uniform', random_state=12345)
dummy.fit(X_train_tfidf, y_train)
y_pred = dummy.predict(X_test_tfidf)
y_proba = dummy.predict_proba(X_test_tfidf)[:, 1]
results.append({
    'Model': 'DummyClassifier',
    'F1': f1_score(y_test, y_pred),
    'Accuracy': accuracy_score(y_test, y_pred),
    'ROC AUC': roc_auc_score(y_test, y_proba)
})

# Modelo 2: Logistic Regression
lr = LogisticRegression(random_state=12345, max_iter=1000)
lr.fit(X_train_tfidf, y_train)
y_pred = lr.predict(X_test_tfidf)
y_proba = lr.predict_proba(X_test_tfidf)[:, 1]
results.append({
    'Model': 'LogisticRegression',
    'F1': f1_score(y_test, y_pred),
    'Accuracy': accuracy_score(y_test, y_pred),
    'ROC AUC': roc_auc_score(y_test, y_proba)
})

# Modelo 3: Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=12345)
rf.fit(X_train_tfidf, y_train)
y_pred = rf.predict(X_test_tfidf)
y_proba = rf.predict_proba(X_test_tfidf)[:, 1]
results.append({
    'Model': 'RandomForest',
    'F1': f1_score(y_test, y_pred),
    'Accuracy': accuracy_score(y_test, y_pred),
    'ROC AUC': roc_auc_score(y_test, y_proba)
})

# Mostrar resultados
results_df = pd.DataFrame(results)
results_df['Cumple F1≥0.85'] = results_df['F1'] >= 0.85
print(results_df)
```

**Salida esperada:**
```
            Model        F1  Accuracy   ROC AUC  Cumple F1≥0.85
  DummyClassifier  0.499823  0.500085  0.500034           False
LogisticRegression  0.879345  0.880012  0.951234            True
      RandomForest  0.865432  0.867890  0.938765            True

✓ LogisticRegression y RandomForest cumplen umbral F1 ≥ 0.85
Mejor modelo: LogisticRegression (F1 = 0.879)
```

**Prueba con reseñas propias:**
```python
# Reseñas de ejemplo
custom_reviews = [
    "This movie was absolutely terrible. Waste of time and money!",
    "Amazing film! Best movie I've seen this year. Highly recommend!",
    "Boring and predictable. I fell asleep halfway through."
]

# Preprocesar
custom_norm = [normalize_text(r) for r in custom_reviews]
custom_lemm = [lemmatize_nltk(r) for r in custom_norm]

# Vectorizar
custom_tfidf = tfidf.transform(custom_lemm)

# Predecir con mejor modelo
predictions = lr.predict(custom_tfidf)
sentiments = ['Negative' if p == 0 else 'Positive' for p in predictions]

for review, sentiment in zip(custom_reviews, sentiments):
    print(f"Review: {review[:50]}...")
    print(f"Sentiment: {sentiment}\n")
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- Notebook cargado en Google Colab y pegado como una liga
- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 10/10)
- **F1 score < 0.85 en test set** (no cumple umbral requerido)
- **No vectoriza texto antes de entrenar modelos** (pasa strings directamente a clasificadores)
- **Bug de accuracy NaN**: Pasa listas de texto a DummyClassifier sin vectorizar
- **Crea split adicional ignorando ds_part** (rompe separación train/test original)
- **No aplica lemmatización** (solo usa texto raw o normalizado)

## Errores Frecuentes

**¿Has identificado errores comunes en este proyecto?**
Ayúdanos a mejorar estos criterios reportando errores frecuentes que observes:

### Error Crítico: Bug de Accuracy NaN

1. **No vectorizar features para DummyClassifier (ERROR MÁS COMÚN QUE CAUSA NaN)**:
   - Incorrecto:
   ```python
   train_features = lemmatize_nltk(train_reviews['review_norm'])  # Lista de strings
   model_0 = DummyClassifier().fit(train_features, train_target)  # ERROR!
   ```
   - Correcto:
   ```python
   train_features = lemmatize_nltk(train_reviews['review_norm'])
   # AGREGAR VECTORIZACIÓN
   tfidf = TfidfVectorizer()
   train_features_vec = tfidf.fit_transform(train_features)
   model_0 = DummyClassifier().fit(train_features_vec, train_target)
   ```
   - Consecuencia: DummyClassifier recibe strings en lugar de matrices numéricas, causando predicciones inválidas y accuracy = NaN

### Errores en Preprocesamiento

2. **No normalizar texto**:
   - Incorrecto: Aplicar lemmatización directamente al texto raw
   - Correcto: Normalizar primero (lowercase, remover especiales), luego lemmatizar
   - Consecuencia: Ruido en texto afecta calidad del modelo

3. **No aplicar lemmatización**:
   - Incorrecto: Solo normalizar y vectorizar sin lemmatizar
   - Correcto: Normalizar → Tokenizar → Lemmatizar → Vectorizar
   - Consecuencia: F1 más bajo, no cumple objetivo de aprendizaje

4. **Confundir stemming con lemmatización**:
   - Incorrecto: Usar PorterStemmer o SnowballStemmer
   - Correcto: Usar WordNetLemmatizer (NLTK) o spaCy
   - Consecuencia: Stemming es más agresivo y menos preciso

5. **No eliminar stopwords**:
   - Incorrecto: Mantener palabras comunes (the, and, is)
   - Correcto: Filtrar stopwords durante lemmatización
   - Consecuencia: Features ruidosas, TF-IDF menos efectivo

### Errores en Vectorización

6. **No aplicar TF-IDF**:
   - Incorrecto: Pasar texto como strings directamente a modelos
   - Correcto: Usar TfidfVectorizer para convertir texto a matriz numérica
   - Consecuencia: Modelos sklearn no pueden procesar strings

7. **Aplicar fit_transform en test set**:
   - Incorrecto: `tfidf.fit_transform(X_test)` (data leakage)
   - Correcto: `tfidf.fit_transform(X_train)`, luego `tfidf.transform(X_test)`
   - Consecuencia: Información de test contamina vectorizador

8. **Vectorizar antes de lemmatizar**:
   - Incorrecto: TF-IDF en texto raw, luego lemmatizar
   - Correcto: Lemmatizar texto, luego TF-IDF
   - Consecuencia: Orden incorrecto, TF-IDF pierde beneficios de lemmatización

### Errores en Modelado

9. **Crear split adicional en lugar de usar ds_part**:
   - Incorrecto: `train_test_split(df_reviews)` ignorando columna ds_part
   - Correcto: Filtrar con `df[df['ds_part'] == 'train']` y `df[df['ds_part'] == 'test']`
   - Consecuencia: No usa el split oficial, resultados no comparables

10. **No implementar modelo baseline**:
    - Incorrecto: Solo modelos complejos (LogisticRegression, LGBM)
    - Correcto: Incluir DummyClassifier para punto de referencia
    - Consecuencia: No tiene baseline para comparar mejora

11. **Comparar menos de 3 modelos**:
    - Incorrecto: Solo entrenar 1-2 modelos
    - Correcto: Implementar al menos 3 modelos diferentes
    - Consecuencia: No cumple requisito de exploración

### Errores en Evaluación

12. **Usar accuracy en lugar de F1 como métrica principal**:
    - Incorrecto: Optimizar/seleccionar modelo por accuracy
    - Correcto: F1 es la métrica objetivo (F1 ≥ 0.85)
    - Consecuencia: No cumple objetivo del proyecto

13. **No calcular ROC AUC**:
    - Incorrecto: Solo reportar F1 y accuracy
    - Correcto: Calcular F1, accuracy, ROC AUC, Average Precision
    - Consecuencia: Evaluación incompleta, no muestra capacidad de discriminación

14. **Evaluar solo en train set**:
    - Incorrecto: No calcular métricas en test set
    - Correcto: Evaluar en test set (donde se verifica F1 ≥ 0.85)
    - Consecuencia: No demuestra generalización, no cumple requisito

### Errores Conceptuales

15. **Creer que BERT es obligatorio**:
    - Incorrecto: Pensar que necesita implementar BERT para aprobar
    - Correcto: BERT es opcional, modelos tradicionales son suficientes
    - Consecuencia: Invierte tiempo innecesario, se complica sin necesidad

16. **No entender diferencia entre tokens y lemmas**:
    - Incorrecto: Confundir tokenización con lemmatización
    - Correcto: Tokenización = dividir en palabras, Lemmatización = convertir a forma base
    - Consecuencia: Implementación incorrecta del preprocesamiento

17. **Pensar que dataset desbalanceado**:
    - Incorrecto: Aplicar técnicas de balanceo (SMOTE, class_weight)
    - Correcto: Dataset ya está balanceado 50/50, no necesita balanceo
    - Consecuencia: Complejidad innecesaria

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
