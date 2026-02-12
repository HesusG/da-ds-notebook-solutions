# Evaluation Criteria: Computer Vision (Age Verification)

## Objective

Students will build a computer vision model to estimate a person's age from a photograph for alcohol sales verification at supermarkets. This project uses transfer learning with ResNet50 and requires achieving MAE ≤ 8 on the validation set.

## Project Description

<details>
<summary>Task Statement</summary>

The Good Seed supermarket chain wants to explore whether Data Science can help them comply with alcohol laws by not selling alcohol to minors. Stores are equipped with cameras at checkout that trigger when someone is purchasing alcohol.

**Requirements:**
- Build and evaluate a model to verify people's age
- Use computer vision methods to determine age from photos
- MAE must be ≤ 8 years

**Dataset:**
- `faces/` folder containing:
  - `final_files/` - 7,591 photographs
  - `labels.csv` - file_name and real_age columns

**Execution:**
- Model must be trained on GPU platform
- Create a script with required functions for GPU execution

</details>

## Google Colab GPU Version

> **Reviewer Note:** A Google Colab GPU-compatible solution notebook is available in this sprint folder:
> `S17 ESP SOL3 Vision artificial - Colab GPU.ipynb`
> This notebook is configured to run on Google Colab with GPU acceleration and can be used as a reference when reviewing student submissions that were executed on Colab.

## Technical Glossary

| Term | Definition |
|------|------------|
| **CNN** | Convolutional Neural Network - architecture for image processing |
| **Transfer Learning** | Using pre-trained model weights as starting point |
| **ResNet50** | Residual Network with 50 layers, pre-trained on ImageNet |
| **ImageDataGenerator** | Keras utility for loading and augmenting images in batches |
| **MAE** | Mean Absolute Error - average of absolute differences between predictions and true values |
| **MSE** | Mean Squared Error - loss function for regression |
| **GlobalAveragePooling2D** | Pooling layer that reduces spatial dimensions to single values |
| **Backbone** | Pre-trained base model used for feature extraction |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Labels loaded from CSV file (7,591 entries)
- [ ] **[REQUIRED]** ImageDataGenerator used for image loading
- [ ] **[REQUIRED]** Images rescaled to 0-1 range (`rescale=1./255`)
- [ ] **[REQUIRED]** Target size defined (typically 224x224), batch size ~32
- [ ] **[REQUIRED]** Age distribution visualized
- [ ] **[REQUIRED]** Statistics calculated (mean ~31, median ~29)
- [ ] **[REQUIRED]** Age range identified (1-100 years)
- [ ] **[REQUIRED]** Sample images displayed with ages
- [ ] **[REQUIRED]** Class imbalance discussed (few minors/elderly)
- [ ] **[REQUIRED]** Data split using `validation_split` (training ~75%, validation ~25%)
- [ ] **[REQUIRED]** `subset='training'` and `subset='validation'` used
- [ ] **[REQUIRED]** `load_train(path)` function defined
- [ ] **[REQUIRED]** `load_test(path)` function defined
- [ ] **[REQUIRED]** `create_model(input_shape)` function defined
- [ ] **[REQUIRED]** `train_model()` function defined
- [ ] **[REQUIRED]** ResNet50 backbone with ImageNet weights, `include_top=False`
- [ ] **[REQUIRED]** GlobalAveragePooling2D added after backbone
- [ ] **[REQUIRED]** Dense(1) output layer with ReLU activation
- [ ] **[REQUIRED]** Optimizer: Adam (lr ~0.0001), Loss: MSE, Metric: MAE
- [ ] **[REQUIRED]** Model trained for sufficient epochs (~20)
- [ ] **[REQUIRED]** Validation MAE ≤ 8 achieved
- [ ] **[REQUIRED]** GPU script created with all imports and functions

### INTERMEDIATE

- [ ] Training progress visualized (loss curves)
- [ ] Discussion of overfitting (train MAE << val MAE)
- [ ] Analysis of model performance by age group
- [ ] Conclusions about model performance

### ADVANCED

- [ ] Data augmentation techniques discussed or applied
- [ ] Learning rate scheduling considered
- [ ] Recommendations for improving model (more data for underrepresented ages)
- [ ] Clean code with comprehensive documentation

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All 22 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 3 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct Image Data Generator
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.25)

train_gen = train_datagen.flow_from_dataframe(
    dataframe=labels,
    directory=path + 'final_files/',
    x_col='file_name',
    y_col='real_age',
    target_size=(224, 224),
    batch_size=32,
    class_mode='raw',
    subset='training',
    seed=12345
)
```

### Correct Model Architecture
```python
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.optimizers import Adam

def create_model(input_shape):
    backbone = ResNet50(
        input_shape=input_shape,
        weights='imagenet',
        include_top=False
    )

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1, activation='relu'))

    model.compile(
        optimizer=Adam(learning_rate=0.0001),
        loss='mean_squared_error',
        metrics=['mae']
    )

    return model
```

### Correct Training Function
```python
def train_model(model, train_data, test_data, epochs=20,
                steps_per_epoch=None, validation_steps=None):
    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)
    if validation_steps is None:
        validation_steps = len(test_data)

    model.fit(
        train_data,
        validation_data=test_data,
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2
    )

    return model
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **MAE > 8** - Must achieve MAE ≤ 8 on validation set
2. **No transfer learning** - Must use pre-trained ResNet50
3. **Missing GPU script** - Must provide executable script
4. **Wrong class_mode** - Must use `class_mode='raw'` for regression
5. **No validation split** - Must evaluate on separate validation set

## Common Errors

### Error 1: Using class_mode='categorical'
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `class_mode='categorical'` (for classification) |
| **Correct** | `class_mode='raw'` (for regression - continuous age) |
| **Consequence** | Model will try to classify instead of predict age |

### Error 2: Not Freezing Backbone Initially
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Training all layers from start |
| **Correct** | Consider `backbone.trainable = False` initially, then fine-tune |
| **Consequence** | May lead to slower convergence or overfitting |

### Error 3: Wrong Output Activation
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `Dense(1, activation='sigmoid')` or `'softmax'` |
| **Correct** | `Dense(1, activation='relu')` or `'linear'` |
| **Consequence** | Sigmoid limits output to 0-1, not age range |

### Error 4: Using Wrong Loss Function
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `loss='categorical_crossentropy'` |
| **Correct** | `loss='mean_squared_error'` or `'mae'` |
| **Consequence** | Classification loss doesn't work for regression |

### Error 5: Not Rescaling Images
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using raw pixel values (0-255) |
| **Correct** | `rescale=1./255` to normalize to 0-1 |
| **Consequence** | Model may not converge properly |

### Error 6: Inconsistent Train/Test Generators
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Different seeds or settings for train and test generators |
| **Correct** | Same `validation_split`, same `seed` for both |
| **Consequence** | Data leakage or inconsistent splits |

## Expected Key Results Summary

### Dataset Overview
| Metric | Value |
|--------|-------|
| Total images | 7,591 |
| Training images | ~5,694 (75%) |
| Validation images | ~1,897 (25%) |
| Age range | 1-100 years |
| Mean age | ~31.2 |
| Median age | 29 |
| 25th percentile | 20 years |
| 75th percentile | 41 years |

### Age Distribution Concerns
| Group | Count | Percentage |
|-------|-------|------------|
| Under 18 (target) | ~795 | ~10% |
| 18-40 | ~5,000 | ~66% |
| Over 40 | ~1,800 | ~24% |

### Model Architecture
| Layer | Output Shape |
|-------|--------------|
| ResNet50 backbone | (7, 7, 2048) |
| GlobalAveragePooling2D | (2048,) |
| Dense(1) | (1,) |

### Training Progress (Approximate)
| Epoch | Train MAE | Val MAE |
|-------|-----------|---------|
| 1 | ~11.2 | ~25.1 |
| 5 | ~3.0 | ~6.9 |
| 10 | ~2.0 | ~6.2 |
| 15 | ~1.7 | ~6.1 |
| 20 | ~1.8 | **~6.1** |

### Final Results
| Metric | Value | Requirement |
|--------|-------|-------------|
| Training MAE | ~1.8 | - |
| Validation MAE | **~6.1** | ≤ 8 |

### Conclusions
- Model achieves MAE ≤ 8 requirement
- Limited data for minors (target group) may affect accuracy for that age range
- Overfitting observed (train MAE << val MAE)
- Recommend collecting more photos of people under 18
- ResNet50 with transfer learning is effective for age estimation
