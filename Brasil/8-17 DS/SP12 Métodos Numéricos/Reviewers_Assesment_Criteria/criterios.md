# Evaluation Criteria: Numerical Methods (Car Price Prediction)

## Objective

Students will build regression models to predict used car prices, comparing multiple algorithms (Linear Regression, Decision Tree, Random Forest, LightGBM, CatBoost, XGBoost) based on prediction quality (RMSE), training speed, and prediction speed. This project emphasizes gradient boosting methods and model comparison.

## Project Description

<details>
<summary>Task Statement</summary>

Rusty Bargain used car sales service is developing an app to attract new customers. In that app, you can quickly find out the market value of your car.

You need to build a model to determine car value. Rusty Bargain is interested in:
- The quality of the prediction (RMSE)
- The speed of the prediction
- The time required for training

**Dataset:**
- `car_data.csv` - 354,369 used car listings
- Features: technical specifications, trim versions, registration info
- Target: Price

**Required Models:**
- Linear Regression (baseline)
- Decision Tree
- Random Forest
- At least one gradient boosting model (LightGBM, CatBoost, or XGBoost)

</details>

## Technical Glossary

| Term | Definition |
|------|------------|
| **RMSE** | Root Mean Square Error - prediction quality metric |
| **Gradient Boosting** | Ensemble technique building trees sequentially to correct errors |
| **LightGBM** | Light Gradient Boosting Machine - fast gradient boosting framework |
| **CatBoost** | Categorical Boosting - handles categorical features natively |
| **XGBoost** | Extreme Gradient Boosting - regularized gradient boosting |
| **One-Hot Encoding (OHE)** | Converting categorical variables to binary columns |
| **Hyperparameter Tuning** | Optimizing model parameters (max_depth, n_estimators, etc.) |
| **GridSearchCV** | Exhaustive search over parameter grid with cross-validation |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Dataset loaded correctly (354,369 records)
- [ ] **[REQUIRED]** Data types checked and converted appropriately
- [ ] **[REQUIRED]** Missing values identified and quantified
- [ ] **[REQUIRED]** Date columns converted to datetime or year extracted
- [ ] **[REQUIRED]** Missing values handled appropriately (VehicleType, FuelType, NotRepaired, Gearbox/Model)
- [ ] **[REQUIRED]** Outliers identified and handled (Price=0, Power=0, invalid years)
- [ ] **[REQUIRED]** ~80% of original data preserved after cleaning
- [ ] **[REQUIRED]** Irrelevant columns dropped (DateCrawled, DateCreated, LastSeen, etc.)
- [ ] **[REQUIRED]** Categorical variables encoded (OHE or native handling)
- [ ] **[REQUIRED]** Data split correctly (75-25 or 80-20) with random state
- [ ] **[REQUIRED]** Linear Regression implemented as baseline
- [ ] **[REQUIRED]** Decision Tree Regressor implemented
- [ ] **[REQUIRED]** Random Forest Regressor implemented
- [ ] **[REQUIRED]** Hyperparameter tuning performed (at least max_depth)
- [ ] **[REQUIRED]** At least one gradient boosting model (LightGBM, CatBoost, or XGBoost) implemented
- [ ] **[REQUIRED]** Multiple hyperparameter configurations tested for boosting model
- [ ] **[REQUIRED]** Training time measured for each model
- [ ] **[REQUIRED]** Prediction time measured for each model
- [ ] **[REQUIRED]** All models compared on RMSE, training time, and prediction time
- [ ] **[REQUIRED]** Comparison table or visualization created
- [ ] **[REQUIRED]** Trade-offs discussed (quality vs speed)
- [ ] **[REQUIRED]** Best model identified with justification

### INTERMEDIATE

- [ ] High-cardinality categories grouped (e.g., rare brands → "other")
- [ ] Correlation analysis performed
- [ ] GridSearchCV used for systematic tuning
- [ ] Cross-validation results documented

### ADVANCED

- [ ] CatBoost used with native categorical feature handling (Pool)
- [ ] Multiple gradient boosting models compared
- [ ] Business-oriented recommendation (balancing accuracy vs deployment speed)
- [ ] Clean, well-commented code

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All 22 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 3 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct Data Preprocessing
```python
# Handle missing values
df['VehicleType'] = df['VehicleType'].fillna(
    df.groupby('Model')['VehicleType'].transform(lambda x: x.mode()[0] if len(x.mode()) > 0 else 'other')
)
df['FuelType'] = df['FuelType'].fillna('unknown')
df['NotRepaired'] = df['NotRepaired'].fillna('no')

# Remove outliers
df = df.loc[(df['Price'] > 60) & (df['Power'] > 30)]
df = df.loc[(df['RegistrationYear'] > 1909) & (df['RegistrationYear'] < 2020)]
```

### Correct Time Measurement
```python
import time

def train_and_measure(model, X_train, y_train, X_valid):
    # Training time
    start_train = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - start_train

    # Prediction time
    start_pred = time.time()
    predictions = model.predict(X_valid)
    pred_time = time.time() - start_pred

    return train_time, pred_time, predictions
```

### Correct Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [5, 10, 15, 20],
    'n_estimators': [50, 100, 200]
}

grid_search = GridSearchCV(
    estimator=RandomForestRegressor(random_state=12345),
    param_grid=param_grid,
    cv=5,
    scoring='neg_mean_squared_error'
)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
```

### Correct CatBoost with Categorical Features
```python
from catboost import CatBoostRegressor, Pool

categorical_features = [0, 2, 5, 6, 7]  # indices of categorical columns
train_pool = Pool(data=X_train, label=y_train, cat_features=categorical_features)

model = CatBoostRegressor(iterations=100, random_seed=12345, verbose=False)
model.fit(train_pool)
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **No gradient boosting model** - At least one (LightGBM, CatBoost, or XGBoost) required
2. **No time measurements** - Training and prediction times must be compared
3. **No model comparison** - All models must be compared on same metrics
4. **Using MSE instead of RMSE** - Must report RMSE (or take sqrt of MSE)
5. **Data leakage** - Target included in features or validation used for training

## Common Errors

### Error 1: Not Converting MSE to RMSE
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Reporting MSE values in millions |
| **Correct** | `rmse = np.sqrt(mean_squared_error(y_true, y_pred))` |
| **Consequence** | Misleading comparison; RMSE is in same units as target |

### Error 2: Forgetting OHE for Non-CatBoost Models
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Passing categorical strings to sklearn models |
| **Correct** | `pd.get_dummies(features, drop_first=True)` or `OneHotEncoder` |
| **Consequence** | Model will fail or perform poorly |

### Error 3: Not Handling CatBoost Categoricals Properly
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using OHE with CatBoost |
| **Correct** | Use `Pool` with `cat_features` parameter |
| **Consequence** | Loses CatBoost's main advantage |

### Error 4: Measuring Time Incorrectly
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using `%time` without storing values, or measuring single prediction |
| **Correct** | Using `time.time()` around full fit/predict operations |
| **Consequence** | Inconsistent or incomparable time measurements |

### Error 5: Not Preserving Enough Data
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Dropping all rows with any missing value (~50% data loss) |
| **Correct** | Strategic imputation to preserve ~80% of data |
| **Consequence** | Model trained on too little data, poor generalization |

### Error 6: Ignoring Trade-offs in Conclusion
| Aspect | Description |
|--------|-------------|
| **Incorrect** | "CatBoost is best because lowest RMSE" |
| **Correct** | "CatBoost has lowest RMSE but 10x training time; Decision Tree offers good balance" |
| **Consequence** | Missing the point of comparing multiple criteria |

## Expected Key Results Summary

### Dataset After Preprocessing
| Metric | Value |
|--------|-------|
| Original records | 354,369 |
| After cleaning | ~288,000 |
| Data preserved | ~81% |
| Features used | 8 |
| Target | Price |

### Model Comparison (Approximate Values)
| Model | Training Time | Pred Time | Validation RMSE |
|-------|--------------|-----------|-----------------|
| Linear Regression | ~0.25s | ~0.03s | ~10,500,000 |
| Decision Tree | ~1.4s | ~0.02s | ~3,700,000 |
| Random Forest | ~2.0s | ~0.10s | ~4,800,000 |
| LightGBM | ~4.0s | ~0.31s | ~3,500,000 |
| CatBoost | ~10.0s | ~0.32s | ~3,400,000 |
| XGBoost | ~7.0s | ~0.07s | ~12,400,000 |

### Key Hyperparameters to Tune
| Model | Key Parameters |
|-------|----------------|
| Decision Tree | max_depth (optimal ~15) |
| Random Forest | max_depth, n_estimators, max_features |
| LightGBM | num_leaves, max_depth, learning_rate, n_estimators |
| CatBoost | iterations, learning_rate, depth |
| XGBoost | booster, n_estimators, max_depth |

### Expected Conclusions
- Linear Regression: fastest training but worst RMSE (baseline)
- CatBoost: best RMSE but longest training time
- LightGBM: good RMSE, moderate training time
- Decision Tree: good balance of all metrics (often recommended)
- Trade-off between quality and speed must be acknowledged
