# Evaluation Criteria: Machine Learning for Texts (Movie Review Classification)

## Objective

Students will build a text classification model to automatically detect negative movie reviews. This project covers text preprocessing, vectorization (TF-IDF), and classification using various models. The goal is to achieve F1 score ≥ 0.85 on the test set.

## Project Description

<details>
<summary>Task Statement</summary>

The Film Junky Union, a community for classic movie enthusiasts, is developing a system for filtering and categorizing movie reviews. The goal is to train a model to automatically detect negative reviews.

**Requirements:**
- F1 score must be at least 0.85 on test set
- Use IMDB movie reviews dataset with polarity labeling

**Dataset:**
- `imdb_reviews.tsv` - 47,331 movie reviews
- Key columns: `review` (text), `pos` (target: 1=positive, 0=negative), `ds_part` (train/test split)

**Tasks:**
1. Load and preprocess text data
2. Explore class distribution
3. Transform text to vectors
4. Train and evaluate classification models
5. Test on custom reviews

</details>

## Google Colab Version

> **Reviewer Note:** A Google Colab-compatible solution notebook is available in this sprint folder:
> `S16 ESP SOL3 Aprendizaje textos - Análisis sentimiento-COLAB.ipynb`
> This notebook is configured to run on Google Colab and can be used as a reference when reviewing student submissions that were executed on Colab.

## Technical Glossary

| Term | Definition |
|------|------------|
| **TF-IDF** | Term Frequency-Inverse Document Frequency - text vectorization method |
| **Tokenization** | Splitting text into individual words/tokens |
| **Lemmatization** | Reducing words to their base/dictionary form |
| **Stop Words** | Common words (the, is, at) filtered out before processing |
| **Bag of Words** | Text representation as word frequency counts |
| **NLTK** | Natural Language Toolkit - Python library for NLP |
| **spaCy** | Industrial-strength NLP library with pre-trained models |
| **BERT** | Bidirectional Encoder Representations from Transformers - deep learning model |
| **F1 Score** | Harmonic mean of precision and recall |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Data loaded correctly (47,331 reviews)
- [ ] **[REQUIRED]** Train/test split identified via `ds_part` column
- [ ] **[REQUIRED]** Target balance checked (~50/50 positive/negative)
- [ ] **[REQUIRED]** Rating distribution visualized
- [ ] **[REQUIRED]** Text converted to lowercase
- [ ] **[REQUIRED]** Non-alphabetic characters removed
- [ ] **[REQUIRED]** Normalized review column created
- [ ] **[REQUIRED]** TF-IDF vectorizer applied
- [ ] **[REQUIRED]** Stop words handled (NLTK or built-in)
- [ ] **[REQUIRED]** Feature matrix created (~60,000-73,000 features)
- [ ] **[REQUIRED]** Constant/Dummy classifier as baseline (F1 ~0.67)
- [ ] **[REQUIRED]** Logistic Regression trained
- [ ] **[REQUIRED]** At least one other model (LightGBM, SVM, etc.)
- [ ] **[REQUIRED]** Model evaluation with multiple metrics (F1, Accuracy, ROC AUC)
- [ ] **[REQUIRED]** F1 ≥ 0.85 achieved on test set

### INTERMEDIATE

- [ ] NLTK or spaCy used for lemmatization
- [ ] Processing with progress bar (tqdm)
- [ ] Comparison of lemmatized vs non-lemmatized performance

### ADVANCED

- [ ] F1 scores at different thresholds visualized
- [ ] ROC curve and Precision-Recall curve plotted
- [ ] Train vs Test comparison to detect overfitting
- [ ] Model tested on custom reviews with correct interpretation

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All 15 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 2 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct Text Normalization
```python
# Convert to lowercase and remove non-alphabetic characters
df['review_norm'] = df['review'].str.lower().str.replace('[^a-zA-Z]', ' ', regex=True)
```

### Correct TF-IDF Vectorization
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

# Download stopwords
import nltk
nltk.download('stopwords')

# Create vectorizer with stopwords
tfidf = TfidfVectorizer(stop_words=stopwords.words('english'), lowercase=True)

# Fit on train, transform both
train_features = tfidf.fit_transform(df_train['review_norm'])
test_features = tfidf.transform(df_test['review_norm'])
```

### Correct Lemmatization with spaCy
```python
import spacy
from tqdm import tqdm
tqdm.pandas()

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

def lemmatize_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return ' '.join(tokens)

df['review_lemma'] = df['review_norm'].progress_apply(lemmatize_text)
```

### Correct Model Evaluation
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score

model = LogisticRegression()
model.fit(train_features, train_target)

pred = model.predict(test_features)
pred_proba = model.predict_proba(test_features)[:, 1]

print(f"F1: {f1_score(test_target, pred):.2f}")
print(f"Accuracy: {accuracy_score(test_target, pred):.2f}")
print(f"ROC AUC: {roc_auc_score(test_target, pred_proba):.2f}")
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **Data leakage** - Fitting TF-IDF on test data
2. **No F1 ≥ 0.85** - Must achieve threshold on test set
3. **Wrong split** - Not using provided train/test split
4. **No text preprocessing** - Raw text without normalization
5. **Ignoring target balance** - Not checking class distribution

## Common Errors

### Error 1: Fitting TF-IDF on Full Dataset
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `tfidf.fit_transform(all_reviews)` then splitting |
| **Correct** | `tfidf.fit_transform(train)` then `tfidf.transform(test)` |
| **Consequence** | Data leakage - test set vocabulary affects training |

### Error 2: Not Removing Non-Alphabetic Characters
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using raw text with punctuation and numbers |
| **Correct** | `text.str.replace('[^a-zA-Z]', ' ', regex=True)` |
| **Consequence** | Noise in features, potential lower performance |

### Error 3: Using Accuracy Instead of F1
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Reporting only accuracy for balanced dataset |
| **Correct** | Using F1 as primary metric (project requirement) |
| **Consequence** | Wrong metric for evaluation |

### Error 4: Not Using Pre-defined Split
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `train_test_split(df, test_size=0.3)` |
| **Correct** | `df_train = df.query('ds_part == "train"')` |
| **Consequence** | Different split from expected, incomparable results |

### Error 5: Lemmatizing Test Data Separately
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Different lemmatization settings for train and test |
| **Correct** | Same preprocessing pipeline for both |
| **Consequence** | Inconsistent feature representation |

### Error 6: Not Including Probabilities in Evaluation
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Only using binary predictions for ROC/PRC |
| **Correct** | Using `predict_proba()[:, 1]` for probability scores |
| **Consequence** | Cannot calculate ROC AUC or vary thresholds |

## Expected Key Results Summary

### Dataset Overview
| Metric | Value |
|--------|-------|
| Total reviews | 47,331 |
| Train set | ~23,796 |
| Test set | ~23,535 |
| Positive reviews | ~23,616 (50%) |
| Negative reviews | ~23,715 (50%) |
| TF-IDF features | ~60,000-73,000 |

### Model Comparison
| Model | Train F1 | Test F1 | Meets Requirement |
|-------|----------|---------|-------------------|
| Constant (baseline) | 0.67 | 0.66 | No |
| TF-IDF + LogReg (NLTK) | 0.95 | **0.88** | Yes |
| TF-IDF + LogReg (spaCy) | 0.95 | **0.88** | Yes |
| TF-IDF + LightGBM | 0.92 | **0.85** | Yes |
| BERT + LogReg | ~0.84 | ~0.78-0.85 | Depends |

### Additional Metrics (Best Model)
| Metric | Train | Test |
|--------|-------|------|
| Accuracy | ~0.93 | ~0.88 |
| F1 | ~0.95 | ~0.88 |
| ROC AUC | ~0.98 | ~0.95 |
| Average Precision | ~0.98 | ~0.95 |

### Key Observations
- Simple TF-IDF + Logistic Regression achieves F1 ≥ 0.85
- Lemmatization with spaCy provides marginal improvement
- BERT requires GPU for practical runtime
- Dataset is balanced (50/50), so accuracy ≈ F1
- Some overfitting observed (train F1 higher than test F1)
