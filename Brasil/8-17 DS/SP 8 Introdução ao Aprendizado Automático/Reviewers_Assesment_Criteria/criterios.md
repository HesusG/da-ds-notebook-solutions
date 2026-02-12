# Evaluation Criteria: Introduction to Machine Learning

## Objective
Develop a classification model to recommend phone plans (Smart or Ultra) based on user behavior, achieving a minimum accuracy of 0.75.

## Project Description
<details>
<summary>Task Statement</summary>

You have access to behavior data from subscribers who have already switched to the new plans. For this classification task, you need to develop a model that selects the right plan.

**Requirements:**
- Develop a model with the highest possible accuracy
- Minimum accuracy threshold: 0.75
- Verify accuracy using a test set
</details>

## Expected Results - Specific Numbers

### Dataset: users_behavior.csv

| Metric | Value |
|--------|-------|
| Total rows | 3,214 |
| Total columns | 5 |
| Missing values | 0 |

### Columns

| Column | Type | Description |
|--------|------|------------|
| calls | float64 | Number of calls |
| minutes | float64 | Total duration in minutes |
| messages | float64 | Number of messages |
| mb_used | float64 | Internet traffic in MB |
| is_ultra | int64 | Target (1=Ultra, 0=Smart) |

### Data Split (60/20/20)

| Set | Rows | Proportion |
|-----|------|-----------|
| Train | 1,928 | 60% |
| Valid | 643 | 20% |
| Test | 643 | 20% |

### Baseline (Sanity Check)

| Class | Proportion |
|-------|-----------|
| 0 (Smart) | 69.35% |
| 1 (Ultra) | 30.65% |

**Note:** A model that always predicts class 0 would have 69.35% accuracy.

### Results by Model

#### Decision Tree (max_depth)
| depth | Train | Valid |
|-------|-------|-------|
| 1 | 76.0% | 73.6% |
| 2 | 79.5% | 74.8% |
| 3 | 81.0% | **76.2%** |
| 4 | 82.1% | **76.4%** |
| 5 | 82.4% | 75.9% |
| 6-10 | >83% | <75.5% |

**Best:** max_depth=4 (valid=76.4%)

#### Random Forest (n_estimators)
| n_est | Train | Valid |
|-------|-------|-------|
| 10 | 98.1% | **78.1%** |
| 20 | 99.5% | 77.9% |
| 30-40 | 99.9% | 76.8-77.0% |
| 50-80 | 100% | 77.4-**78.1%** |
| 90-100 | 100% | 76.8-77.4% |

**Best:** n_estimators=80 (valid=78.1%)

#### Logistic Regression
| Train | Valid |
|-------|-------|
| 75.8% | 72.2% |

**Worst performance, but no overfitting.**

### Final Result on Test

| Model | Config | Test Accuracy |
|-------|--------|--------------|
| Random Forest | n_estimators=80 | **80.6%** |

**Conclusion:** Approved (>75%)

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Loads data (3,214 rows)
- [ ] **[REQUIRED]** Splits into features and target correctly
- [ ] **[REQUIRED]** Splits into train/valid/test (~60/20/20)
- [ ] **[REQUIRED]** Trains at least 2 different models
- [ ] **[REQUIRED]** Tests multiple hyperparameter values (e.g., max_depth, n_estimators)
- [ ] **[REQUIRED]** Evaluates on validation set
- [ ] **[REQUIRED]** Compares train vs valid accuracy (identifies overfitting)
- [ ] **[REQUIRED]** Justifies choice of final model
- [ ] **[REQUIRED]** Evaluates final model on test
- [ ] **[REQUIRED]** Test accuracy >= 0.75

### INTERMEDIATE

- [ ] Decision Tree: tests max_depth from 1 to 10
- [ ] Random Forest: tests n_estimators (10-100)
- [ ] Documents results of each experiment in a table or summary
- [ ] Performs sanity check (baseline ~69.4%)
- [ ] Trains final model with train+valid before testing

### ADVANCED

- [ ] Identifies overfitting vs accuracy trade-off with clear explanation
- [ ] Random Forest ~78-80% on test
- [ ] Well-organized code with clear sections
- [ ] Detailed conclusions about performance and model comparison

## General Approval Criteria

| Level | Requirements |
|-------|------------|
| **Basic** | All 10 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 3 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Split data (60/20/20):
```python
# First: 80% train+valid, 20% test
train_valid, test = train_test_split(df, test_size=0.2, random_state=12345)

# Then: 60% train, 20% valid (0.25 of 80% = 20%)
train, valid = train_test_split(train_valid, test_size=0.25, random_state=12345)

# Separate features and target
features_train = train.drop(['is_ultra'], axis=1)
target_train = train['is_ultra']
# ... same for valid and test

print(features_train.shape)  # (1928, 4)
print(features_valid.shape)  # (643, 4)
print(features_test.shape)   # (643, 4)
```

### Test Decision Tree:
```python
print("Decision Tree")
for depth in range(1, 11):
    model = DecisionTreeClassifier(max_depth=depth, random_state=12345)
    model.fit(features_train, target_train)
    print(f"max_depth = {depth}")
    print(f"Train: {model.score(features_train, target_train)}")
    print(f"Valid: {model.score(features_valid, target_valid)}")
```

### Sanity check:
```python
# Class distribution
baseline = df['is_ultra'].value_counts() / df.shape[0]
print(f"Baseline (majority class): {baseline[0]:.2%}")
# Output: ~69.35% - model that always predicts 0
```

### Final model:
```python
# Train with train + valid
features_full_train = train_valid.drop(['is_ultra'], axis=1)
target_full_train = train_valid['is_ultra']

model = RandomForestClassifier(n_estimators=80, random_state=12345)
model.fit(features_full_train, target_full_train)

# Evaluate on test
test_accuracy = model.score(features_test, target_test)
print(f"Test Accuracy: {test_accuracy}")  # ~80.6%
```

## Disqualification Criteria

- [ ] Test accuracy < 0.75
- [ ] Does not split into train/valid/test
- [ ] Uses test data to tune hyperparameters
- [ ] Evaluates final model only on train (not on test)
- [ ] Does not train any classification model

## Common Conceptual Errors

### 1. Using test to tune model
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| Choose hyperparameters by looking at test | Use ONLY validation for tuning | Data leakage - inflated accuracy |

**Correct concept:** The test set is SACRED. Only use it ONCE, at the end, to report real performance.

### 2. Wrong proportions in split
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| 50/25/25 | 60/20/20 | Training needs more data |
| Only train/test | train/valid/test | Validation needed for tuning |

### 3. Forgetting random_state
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `train_test_split(df, test_size=0.2)` | `..., random_state=12345)` | Non-reproducible results |

### 4. Ignoring overfitting
| Overfitting signal | Example in project |
|-------------------|-------------------|
| Train much higher than valid | Random Forest: Train=100%, Valid=78% |
| Gap increases with complexity | Decision Tree depth=10: Train=88%, Valid=75% |

**Correct concept:** Overfitting occurs when the model memorizes training data but doesn't generalize. Prefer models with smaller train/valid gap.

### 5. Not combining train+valid for final model
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| Use only train | Use train+valid | More data = better model |

### 6. Not doing sanity check
| Problem | Solution |
|---------|---------|
| Model with 71% seems good | Baseline is 69.4%, model learned little |

**Correct concept:** ALWAYS compare with baseline. If accuracy is close to the majority class, the model hasn't learned much.

## Project Pitfalls

1. **Logistic Regression is weak here**: With 72% on valid, it doesn't reach the 75% threshold. This is expected - data is not linearly separable.

2. **Random Forest has severe overfitting**: Train=100%, Valid=78%. This is expected with forests without regularization.

3. **Best model is Random Forest with n_estimators=80**: Achieves ~80.6% on test, well above the threshold.

4. **Sanity check is crucial**: Baseline of 69.4% means we only improved ~11 percentage points. Seems small, but it's significant.

5. **Training with train+valid improves results**: More training data = more robust final model.
