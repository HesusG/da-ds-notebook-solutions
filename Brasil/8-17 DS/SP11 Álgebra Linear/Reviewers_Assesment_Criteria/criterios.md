# Evaluation Criteria: Linear Algebra (Data Obfuscation)

## Objective

Students will apply linear algebra concepts to machine learning tasks: finding similar customers using kNN, classification, linear regression, and data obfuscation. The final task requires proving analytically and computationally that multiplying features by an invertible matrix does not affect linear regression predictions.

## Project Description

<details>
<summary>Task Statement</summary>

The Sure Tomorrow insurance company wants to solve several tasks with ML:

**Task 1:** Find similar customers for a given customer (marketing use case)
**Task 2:** Predict whether a customer is likely to receive insurance benefits (classification)
**Task 3:** Predict the number of insurance benefits (linear regression)
**Task 4:** Protect clients' personal data without breaking the model (data obfuscation)

**Dataset:**
- `insurance_us.csv` - 5,000 customer records
- Features: gender, age, income, family_members
- Target: insurance_benefits (0-5)

**Key Requirement for Task 4:**
Develop a data transformation algorithm (X' = X × P) that:
- Makes it hard to recover personal information
- Does not affect model quality

</details>

## Technical Glossary

| Term | Definition |
|------|------------|
| **k-Nearest Neighbors (kNN)** | Algorithm that finds k most similar objects based on distance |
| **Euclidean Distance** | Straight-line distance between two points |
| **Manhattan Distance** | Sum of absolute differences between coordinates |
| **Feature Scaling** | Normalizing features to comparable ranges |
| **MaxAbsScaler** | Scales each feature by its maximum absolute value |
| **Invertible Matrix** | A square matrix with non-zero determinant that has an inverse |
| **Matrix Multiplication** | Operation where columns of first matrix match rows of second |
| **Linear Regression** | Model: y = Xw, where w = (X^T X)^(-1) X^T y |
| **Data Obfuscation** | Transforming data to hide original values while preserving utility |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Dataset loaded correctly (5,000 records)
- [ ] **[REQUIRED]** Column names standardized, data types appropriate (age as int, income as float)
- [ ] **[REQUIRED]** No missing values confirmed, basic statistics reviewed
- [ ] **[REQUIRED]** kNN implemented with 4 combinations (unscaled/scaled × Euclidean/Manhattan)
- [ ] **[REQUIRED]** MaxAbsScaler used for scaling
- [ ] **[REQUIRED]** Key insight: unscaled data returns similar income values (income dominates distance)
- [ ] **[REQUIRED]** Key insight: scaled data returns more balanced similarity
- [ ] **[REQUIRED]** Binary target created (insurance_benefits > 0), class imbalance noted (564 positive / 4,436 negative)
- [ ] **[REQUIRED]** Dummy model tested with P = [0, 0.11, 0.5, 1]
- [ ] **[REQUIRED]** kNN classifier tested for k = 1 to 10, results compared scaled vs unscaled
- [ ] **[REQUIRED]** F1 metric used for evaluation (kNN k=1 scaled F1 ~0.97)
- [ ] **[REQUIRED]** Custom linear regression implemented using matrix formula: w = (X^T X)^(-1) X^T y
- [ ] **[REQUIRED]** Unity column added: X2 = [1, X]
- [ ] **[REQUIRED]** RMSE ~0.34, R² ~0.66
- [ ] **[REQUIRED]** Random matrix P generated (n_features × n_features), invertibility verified (determinant ≠ 0)
- [ ] **[REQUIRED]** Data transformed: X' = X × P, original values not recognizable
- [ ] **[REQUIRED]** Recovery demonstrated: X = X' × P^(-1)
- [ ] **[REQUIRED]** Analytical proof: step-by-step derivation shows w_P = P^(-1) w
- [ ] **[REQUIRED]** Conclusion: ŷ = X' w_P = XP P^(-1) w = Xw = original predictions
- [ ] **[REQUIRED]** Computational proof: RMSE on original vs obfuscated data are equal (~0.34)

### INTERMEDIATE

- [ ] Same RMSE results verified for scaled/unscaled data in Task 3
- [ ] Visualization of kNN results across different k values
- [ ] Clear documentation of each task with markdown sections
- [ ] Comparison table summarizing all model results

### ADVANCED

- [ ] Discussion of why scaling matters for distance-based algorithms
- [ ] Explanation of why linear regression is invariant to invertible transformation
- [ ] Business context for data obfuscation (privacy implications)
- [ ] Clean, well-commented code with clear variable names

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All 20 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 3 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct kNN Implementation
```python
def get_knn(df, n, k, metric):
    feature_names = ['gender', 'age', 'income', 'family_members']
    nbrs = sklearn.neighbors.NearestNeighbors(
        n_neighbors=k,
        algorithm='brute',
        metric=metric
    ).fit(df[feature_names])

    distances, indices = nbrs.kneighbors(
        [df.iloc[n][feature_names]], k, return_distance=True
    )
    return df.iloc[indices[0]]
```

### Correct Custom Linear Regression
```python
class MyLinearRegression:
    def __init__(self):
        self.weights = None

    def fit(self, X, y):
        # Add column of ones for intercept
        X2 = np.append(np.ones([len(X), 1]), X, axis=1)
        # Analytical solution: w = (X^T X)^(-1) X^T y
        self.weights = np.linalg.inv(X2.T @ X2) @ X2.T @ y

    def predict(self, X):
        X2 = np.append(np.ones([len(X), 1]), X, axis=1)
        return X2 @ self.weights
```

### Correct Data Obfuscation
```python
# Generate random invertible matrix
rng = np.random.default_rng(seed=42)
P = rng.random(size=(X.shape[1], X.shape[1]))

# Verify invertibility
det = np.linalg.det(P)
assert abs(det) > 1e-5, "Matrix not invertible"

# Transform data
X_transformed = X @ P

# Recover original data
P_inv = np.linalg.inv(P)
X_recovered = X_transformed @ P_inv
```

### Correct Analytical Proof Structure
```
w_P = [(XP)^T XP]^(-1) (XP)^T y
    = [P^T X^T X P]^(-1) P^T X^T y           # (AB)^T = B^T A^T
    = P^(-1) (X^T X)^(-1) (P^T)^(-1) P^T X^T y   # (AB)^(-1) = B^(-1) A^(-1)
    = P^(-1) (X^T X)^(-1) I X^T y            # A^(-1) A = I
    = P^(-1) (X^T X)^(-1) X^T y
    = P^(-1) w

Therefore: ŷ = X' w_P = XP(P^(-1) w) = X(PP^(-1))w = XIw = Xw
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **Missing invertibility check** - Using matrix P without verifying determinant ≠ 0
2. **Wrong matrix dimensions** - P must be square (n_features × n_features)
3. **Missing analytical proof** - Only computational proof is not sufficient
4. **Wrong proof conclusion** - Not showing that predictions remain unchanged
5. **Using sklearn for Task 3** - Custom implementation required to demonstrate LA

## Common Errors

### Error 1: Forgetting Unity Column in Linear Regression
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `self.weights = np.linalg.inv(X.T @ X) @ X.T @ y` |
| **Correct** | `X2 = np.append(np.ones([len(X), 1]), X, axis=1)` then use X2 |
| **Consequence** | Missing intercept term, poor model fit |

### Error 2: Wrong Matrix for Obfuscation
| Aspect | Description |
|--------|-------------|
| **Incorrect** | P with shape (n_samples, n_samples) |
| **Correct** | P with shape (n_features, n_features) |
| **Consequence** | Matrix multiplication X @ P will fail or give wrong dimensions |

### Error 3: Not Checking Invertibility
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using any random matrix |
| **Correct** | Checking `np.linalg.det(P) != 0` before using |
| **Consequence** | Cannot recover data if matrix is singular |

### Error 4: Incomplete Analytical Proof
| Aspect | Description |
|--------|-------------|
| **Incorrect** | "The RMSE is the same so transformation works" |
| **Correct** | Step-by-step algebraic derivation showing w_P = P^(-1) w |
| **Consequence** | Does not demonstrate understanding of why transformation preserves quality |

### Error 5: Not Comparing Scaled vs Unscaled for kNN
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Only testing one scaling condition |
| **Correct** | Testing all 4 combinations and discussing differences |
| **Consequence** | Missing key insight about feature scaling importance |

### Error 6: Using Wrong Metrics
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using accuracy for imbalanced classification |
| **Correct** | Using F1 score for imbalanced data |
| **Consequence** | Misleading evaluation of classifier performance |

## Expected Key Results Summary

### Dataset
| Metric | Value |
|--------|-------|
| Total records | 5,000 |
| Features | gender, age, income, family_members |
| Target range | 0-5 insurance benefits |
| Positive class (>0) | 564 (11.28%) |

### Task 2: Classification
| Model | Configuration | F1 Score |
|-------|---------------|----------|
| Dummy | P=0.0 | 0.00 |
| Dummy | P=0.11 | 0.12 |
| Dummy | P=0.5 | 0.20 |
| kNN | k=1, unscaled | 0.60 |
| kNN | k=1, scaled | 0.97 |

### Task 3: Linear Regression
| Metric | Value |
|--------|-------|
| RMSE | 0.34 |
| R² | 0.66 |

### Task 4: Data Obfuscation
| Condition | RMSE |
|-----------|------|
| Original data | 0.34 |
| Obfuscated data (X' = XP) | 0.34 |

### Key Matrix Properties Used in Proof
| Property | Formula |
|----------|---------|
| Transpose of product | (AB)^T = B^T A^T |
| Inverse of product | (AB)^(-1) = B^(-1) A^(-1) |
| Inverse identity | A^(-1) A = AA^(-1) = I |
| Identity property | IA = AI = A |
