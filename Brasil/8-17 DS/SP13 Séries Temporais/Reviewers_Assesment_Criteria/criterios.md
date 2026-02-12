# Evaluation Criteria: Time Series (Taxi Orders Prediction)

## Objective

Students will build models to predict hourly taxi orders at airports, using time series analysis techniques including resampling, seasonal decomposition, and feature engineering with lag/rolling features. The goal is to achieve RMSE ≤ 48 on the test set.

## Project Description

<details>
<summary>Task Statement</summary>

Sweet Lift Taxi company has collected historical data on taxi orders at airports. To attract more drivers during peak hours, we need to predict the amount of taxi orders for the next hour.

**Requirements:**
- RMSE on test set must not exceed 48
- Test sample should be 10% of the dataset

**Dataset:**
- `taxi.csv` - 26,496 records at 10-minute intervals
- Period: March 1, 2018 to August 31, 2018
- Column: `num_orders` - number of taxi orders

**Tasks:**
1. Download the data and resample by one hour
2. Analyze the data (trend, seasonality)
3. Train different models with different hyperparameters
4. Test using the test sample and provide conclusions

</details>

## Technical Glossary

| Term | Definition |
|------|------------|
| **Resampling** | Changing the frequency of time series data (e.g., 10min → 1hour) |
| **Lag Features** | Previous values used as predictors (e.g., lag_1 = value 1 hour ago) |
| **Rolling Mean** | Moving average over a sliding window |
| **Seasonal Decomposition** | Splitting time series into trend, seasonal, and residual components |
| **TimeSeriesSplit** | Cross-validation strategy respecting temporal order |
| **RMSE** | Root Mean Square Error - prediction quality metric |
| **Trend** | Long-term increase or decrease in the series |
| **Seasonality** | Repeating patterns at fixed intervals |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Data loaded with datetime index
- [ ] **[REQUIRED]** Resampled to hourly frequency using `.resample('1h').sum()`
- [ ] **[REQUIRED]** Original: 26,496 records (10-min intervals), after resampling: ~4,416 (hourly)
- [ ] **[REQUIRED]** Date range identified (2018-03-01 to 2018-08-31)
- [ ] **[REQUIRED]** No missing values confirmed, basic time series plot created
- [ ] **[REQUIRED]** Seasonal decomposition performed (`seasonal_decompose`)
- [ ] **[REQUIRED]** Trend, seasonality, and residual components analyzed
- [ ] **[REQUIRED]** Calendar features created (month, day, dayofweek, hour)
- [ ] **[REQUIRED]** Lag features created (at least lag_1 to lag_5)
- [ ] **[REQUIRED]** Rolling mean feature created
- [ ] **[REQUIRED]** NaN values from lag/rolling features handled (dropped)
- [ ] **[REQUIRED]** Test set is 10% of data, `shuffle=False` to preserve temporal order
- [ ] **[REQUIRED]** Baseline model (constant/median) implemented
- [ ] **[REQUIRED]** Linear Regression implemented
- [ ] **[REQUIRED]** Decision Tree with hyperparameter tuning
- [ ] **[REQUIRED]** Random Forest with hyperparameter tuning
- [ ] **[REQUIRED]** At least one gradient boosting model (CatBoost or LightGBM)
- [ ] **[REQUIRED]** `TimeSeriesSplit` used for cross-validation
- [ ] **[REQUIRED]** RMSE calculated for all models, comparison table created
- [ ] **[REQUIRED]** At least one model achieves RMSE ≤ 48 on test set
- [ ] **[REQUIRED]** Best model identified and justified

### INTERMEDIATE

- [ ] Daily pattern identified (lowest 6-7 AM, peak 11PM-3AM and 4PM)
- [ ] Monthly trend: orders increase each month
- [ ] August has ~2x orders compared to March
- [ ] Multiple lag window sizes tested

### ADVANCED

- [ ] Multiple gradient boosting models compared
- [ ] Feature importance analysis performed
- [ ] Visualization of predictions vs actual values
- [ ] Clean, well-documented code with clear narrative

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All 21 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 3 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct Resampling
```python
df = pd.read_csv('taxi.csv', index_col=[0], parse_dates=[0])
df = df.resample('1h').sum()  # Sum orders per hour
```

### Correct Feature Engineering
```python
# Calendar features
df['month'] = df.index.month
df['day'] = df.index.day
df['dayofweek'] = df.index.dayofweek
df['hour'] = df.index.hour

# Lag features
max_lag = 5
for lag in range(1, max_lag + 1):
    df[f'lag_{lag}'] = df['num_orders'].shift(lag)

# Rolling mean
df['rolling_mean_6'] = df['num_orders'].shift().rolling(6).mean()

# Drop NaN rows created by lag/rolling
df = df.dropna()
```

### Correct Time Series Split
```python
from sklearn.model_selection import train_test_split, TimeSeriesSplit

# Test set is 10%, no shuffling
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.1, shuffle=False
)

# For cross-validation
cv = TimeSeriesSplit(n_splits=3)
grid_search = GridSearchCV(model, param_grid, cv=cv, scoring='neg_root_mean_squared_error')
```

### Correct Seasonal Decomposition
```python
from statsmodels.tsa.seasonal import seasonal_decompose

decomposed = seasonal_decompose(df['num_orders'])

# Plot components
decomposed.trend.plot()
decomposed.seasonal.plot()
decomposed.resid.plot()
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **Using `shuffle=True`** - Time series must maintain order
2. **No resampling** - Must convert from 10-min to hourly
3. **Using future data** - Lag features must not use future values
4. **No RMSE ≤ 48** - At least one model must meet the requirement
5. **Regular K-fold CV** - Must use TimeSeriesSplit for time series

## Common Errors

### Error 1: Shuffling Time Series Data
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `train_test_split(X, y, test_size=0.1)` (default shuffle=True) |
| **Correct** | `train_test_split(X, y, test_size=0.1, shuffle=False)` |
| **Consequence** | Data leakage - model sees future values during training |

### Error 2: Not Shifting Before Rolling
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `df['rolling'] = df['num_orders'].rolling(6).mean()` |
| **Correct** | `df['rolling'] = df['num_orders'].shift().rolling(6).mean()` |
| **Consequence** | Data leakage - rolling mean includes current value |

### Error 3: Using Regular K-Fold
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `GridSearchCV(model, params, cv=5)` |
| **Correct** | `GridSearchCV(model, params, cv=TimeSeriesSplit(n_splits=3))` |
| **Consequence** | Training on future data during cross-validation |

### Error 4: Wrong Resampling Aggregation
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `df.resample('1h').mean()` (averages orders) |
| **Correct** | `df.resample('1h').sum()` (total orders per hour) |
| **Consequence** | Predicting wrong metric (average vs total) |

### Error 5: Not Handling NaN from Lag Features
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Training with NaN values in lag columns |
| **Correct** | `df = df.dropna()` after creating lag features |
| **Consequence** | Model errors or incorrect predictions |

### Error 6: Forgetting Baseline Model
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Only testing ML models |
| **Correct** | Include constant model (median) as baseline for comparison |
| **Consequence** | Can't assess if ML models add value over simple prediction |

## Expected Key Results Summary

### Dataset Overview
| Metric | Value |
|--------|-------|
| Original records | 26,496 (10-min intervals) |
| After resampling | 4,416 (hourly) |
| After feature engineering | ~4,410 (after dropping NaN) |
| Period | 2018-03-01 to 2018-08-31 |
| Train set | ~3,969 records |
| Test set | ~441 records (10%) |

### Daily Pattern
| Time | Orders |
|------|--------|
| 6-7 AM | Lowest (~25-30 median) |
| 11 PM - 3 AM | Peak (~100-145 median) |
| 4 PM | Secondary peak (~110) |

### Monthly Trend
| Month | Total Orders |
|-------|--------------|
| March | ~42,768 |
| April | ~45,939 |
| May | ~54,820 |
| June | ~59,906 |
| July | ~74,405 |
| August | ~94,973 |

### Model Comparison (Verified)
| Model | Train RMSE | Test RMSE | Meets Requirement |
|-------|-----------|----------|-------------------|
| CatBoost | ~17 | **~45** | Yes |
| LightGBM | ~18 | **~48** | Yes |
| Random Forest | ~19 | ~50 | No (close) |
| Linear Regression | ~30 | ~53 | No |
| Decision Tree | ~20 | ~58 | No |
| Constant (median) | ~87 | ~87 | No |

**Note:** Random Forest with good tuning can get close (~50) but typically doesn't meet threshold.
Gradient boosting (CatBoost or LightGBM) is required to reliably achieve RMSE ≤ 48.

### Key Hyperparameters Found
| Model | Parameters |
|-------|------------|
| Decision Tree | max_depth=8 |
| Random Forest | max_depth=8, n_estimators=10, max_features='sqrt' |
| CatBoost | depth=4, iterations=100, learning_rate=0.5 |
| LightGBM | num_leaves=15, n_estimators=20, learning_rate=0.5 |

### Conclusions
- Gradient boosting models (CatBoost, LightGBM) achieve the RMSE ≤ 48 requirement
- Traditional models (Linear, Trees, Forest) do not meet the requirement
- Time series features (lags, rolling means) are essential for prediction
- Peak hours identified for driver allocation optimization
