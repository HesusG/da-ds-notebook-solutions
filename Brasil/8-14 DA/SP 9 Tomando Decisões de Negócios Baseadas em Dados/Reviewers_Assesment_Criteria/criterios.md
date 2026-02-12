# Evaluation Criteria: Making Data-Driven Business Decisions (A/B Testing)

## Objective

Students will prioritize business hypotheses using ICE and RICE frameworks, then analyze an A/B test to determine statistical significance of conversion and order size differences. This project tests skills in hypothesis prioritization, cumulative metric analysis, anomaly detection, and statistical hypothesis testing.

## Project Description

<details>
<summary>Task Statement</summary>

This project consists of two parts:

**Part 1: Hypothesis Prioritization**
Using ICE and RICE frameworks to prioritize 9 business hypotheses for an online store.

**Part 2: A/B Test Analysis**
Analyze A/B test results to determine if changes improved key metrics.

**Datasets:**
- `hypotheses_us.csv` - 9 hypotheses with Reach, Impact, Confidence, Effort scores
- `orders_us.csv` - 1,197 orders during A/B test (August 2019)
- `visitors_us.csv` - Daily visitor counts per group

**Hypothesis Columns:**
- Reach: How many users will be affected (1-10)
- Impact: Effect on revenue (1-10)
- Confidence: Certainty in the estimate (1-10)
- Effort: Resources required to implement (1-10)

</details>

## Technical Glossary

| Term | Definition |
|------|------------|
| **ICE Score** | Impact × Confidence / Effort - prioritization without reach |
| **RICE Score** | Reach × Impact × Confidence / Effort - prioritization with reach |
| **A/B Test** | Controlled experiment comparing two versions (A = control, B = treatment) |
| **Conversion Rate** | Percentage of visitors who make a purchase |
| **Statistical Significance** | Probability that observed difference is not due to chance |
| **p-value** | Probability of seeing results as extreme as observed if null hypothesis is true |
| **Mann-Whitney U Test** | Non-parametric test for comparing two independent samples |
| **Cumulative Metrics** | Running total of metrics over time to observe trends |
| **Anomaly** | Data point that significantly deviates from expected pattern |
| **Percentile** | Value below which a percentage of data falls |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** ICE score calculated correctly: `Impact × Confidence / Effort`
- [ ] **[REQUIRED]** RICE score calculated correctly: `Reach × Impact × Confidence / Effort`
- [ ] **[REQUIRED]** Hypotheses sorted by both ICE and RICE scores
- [ ] **[REQUIRED]** Observation that rankings differ between frameworks (ICE top: #8=16.20, RICE top: #7=112.0)
- [ ] **[REQUIRED]** All 3 datasets loaded correctly (hypotheses, orders, visitors)
- [ ] **[REQUIRED]** Date columns converted to datetime
- [ ] **[REQUIRED]** Test date range verified (August 1-31, 2019) with ~1,197 total orders
- [ ] **[REQUIRED]** Cumulative revenue graph by group created
- [ ] **[REQUIRED]** Cumulative average order size graph by group created
- [ ] **[REQUIRED]** Cumulative conversion graph by group created
- [ ] **[REQUIRED]** Relative difference graphs created (B/A - 1)
- [ ] **[REQUIRED]** Percentiles calculated for orders per user (95th=2, 99th=4), anomalous users defined as 3+ orders
- [ ] **[REQUIRED]** Percentiles calculated for order revenue (95th≈$435.54), anomalous orders defined as >$430
- [ ] **[REQUIRED]** Scatter plots created to visualize anomalies
- [ ] **[REQUIRED]** Mann-Whitney U test used (appropriate for non-normal distributions)
- [ ] **[REQUIRED]** Raw conversion test: p-value ~0.01679 (significant at α=0.05), difference ~13.8% (B > A)
- [ ] **[REQUIRED]** Raw order size test: p-value ~0.692 (not significant), difference ~25.2%
- [ ] **[REQUIRED]** Anomalous users identified and removed for filtered analysis
- [ ] **[REQUIRED]** Filtered conversion test: p-value ~0.01418 (significant), difference ~17.1% (B > A)
- [ ] **[REQUIRED]** Filtered order size test: p-value ~0.750 (not significant), difference ~-2.7%
- [ ] **[REQUIRED]** Clear statement: conversion is significantly different, order size is NOT
- [ ] **[REQUIRED]** Recommendation to implement Group B (stop test)
- [ ] **[REQUIRED]** Justification based on both raw and filtered results

### INTERMEDIATE

- [ ] Observation that Group B shows higher cumulative revenue
- [ ] Recognition of potential anomaly causing revenue spike in B
- [ ] Note that conversion shows B leading throughout test
- [ ] Discussion of trend convergence/divergence
- [ ] Justifies the choice of limits for anomalies
- [ ] Documents data preprocessing (duplicates, types)

### ADVANCED

- [ ] Analyzes the impact of anomalies on test results (raw vs filtered comparison)
- [ ] Analyzes stability of cumulative graphs over time
- [ ] Professional presentation of findings
- [ ] Well-commented code with clear narrative

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All 23 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 4 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct ICE/RICE Calculation
```python
hypothesis['ICE'] = hypothesis['Impact'] * hypothesis['Confidence'] / hypothesis['Effort']
hypothesis['RICE'] = hypothesis['Reach'] * hypothesis['Impact'] * hypothesis['Confidence'] / hypothesis['Effort']

print(hypothesis.sort_values(by='ICE', ascending=False))
print(hypothesis.sort_values(by='RICE', ascending=False))
```

### Correct Cumulative Data Aggregation
```python
datesGroups = orders[['date','group']].drop_duplicates()

ordersAggregated = datesGroups.apply(
    lambda x: orders[
        np.logical_and(orders['date'] <= x['date'], orders['group'] == x['group'])
    ].agg({
        'transactionId': pd.Series.nunique,
        'visitorId': pd.Series.nunique,
        'revenue': 'sum'
    }), axis=1
).sort_values(by=['date','group'])
```

### Correct Anomaly Detection
```python
# Orders per user percentiles
ordersByUsers = orders.groupby('visitorId', as_index=False).agg({
    'transactionId': pd.Series.nunique
})
ordersByUsers.columns = ['userId', 'orders']
np.percentile(ordersByUsers['orders'], [90, 95, 99])  # [1., 2., 4.]

# Revenue percentiles
np.percentile(orders['revenue'], [90, 95, 99])  # [282.48, 435.54, 900.904]

# Define anomalous users
usersWithManyOrders = ordersByUsers[ordersByUsers['orders'] > 2]['userId']
usersWithExpensiveOrders = orders[orders['revenue'] > 430]['visitorId']
abnormalUsers = pd.concat([usersWithManyOrders, usersWithExpensiveOrders]).drop_duplicates()
```

### Correct Statistical Testing
```python
from scipy import stats

# Conversion test (using Mann-Whitney)
sampleA = pd.concat([
    ordersByUsersA['orders'],
    pd.Series(0, index=np.arange(visitorsA - len(ordersByUsersA)))
])
sampleB = pd.concat([
    ordersByUsersB['orders'],
    pd.Series(0, index=np.arange(visitorsB - len(ordersByUsersB)))
])

p_value = stats.mannwhitneyu(sampleA, sampleB)[1]
print(f"p-value: {p_value:.5f}")  # 0.01679

relative_diff = sampleB.mean() / sampleA.mean() - 1
print(f"Difference: {relative_diff:.3f}")  # 0.138
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **Wrong ICE/RICE formula** - Incorrect operators or missing components
2. **Using t-test without checking normality** - Should use Mann-Whitney for non-normal data
3. **Not filtering anomalies** - Analyzing only raw data without considering outliers
4. **Misinterpreting p-value** - Claiming significance when p > 0.05 or vice versa
5. **No final decision** - Failing to make a recommendation based on analysis

## Common Errors

### Error 1: Using Wrong Test Statistic
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `stats.ttest_ind(sampleA, sampleB)` without normality check |
| **Correct** | `stats.mannwhitneyu(sampleA, sampleB)` for non-normal data |
| **Consequence** | May produce incorrect p-values for skewed distributions |

### Error 2: Incorrect Conversion Sample Construction
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Only including buyers in the sample |
| **Correct** | Including zeros for non-converting visitors: `pd.concat([orders, pd.Series(0, index=non_buyers)])` |
| **Consequence** | Conversion rates will be inflated and test will be invalid |

### Error 3: Not Using Cumulative Metrics
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Plotting daily metrics without accumulation |
| **Correct** | Accumulating metrics over time to show trends |
| **Consequence** | Cannot observe how metrics stabilize over time |

### Error 4: Ignoring Anomaly Impact
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Reporting only raw data results |
| **Correct** | Analyzing both raw and filtered data, comparing results |
| **Consequence** | Outliers may skew conclusions, especially for order size |

### Error 5: Conflicting Decision
| Aspect | Description |
|--------|-------------|
| **Incorrect** | "Stop test, no difference" when p < 0.05 for conversion |
| **Correct** | "Stop test, implement B - conversion is significantly higher" |
| **Consequence** | Business decision contradicts statistical evidence |

### Error 6: Users in Multiple Groups
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Ignoring users who appear in both groups |
| **Correct** | Identifying and discussing users in multiple groups (~58 users, 5.63%) |
| **Consequence** | May affect validity of independent samples assumption |

## Expected Key Results Summary

### Part 1: Hypothesis Prioritization

| Hypothesis | Reach | Impact | Confidence | Effort | ICE | RICE |
|------------|-------|--------|------------|--------|-----|------|
| #8 | 1 | 9 | 9 | 5 | 16.20 | 16.2 |
| #0 | 3 | 10 | 8 | 6 | 13.33 | 40.0 |
| #7 | 10 | 7 | 8 | 5 | 11.20 | 112.0 |
| #6 | 5 | 3 | 8 | 3 | 8.00 | 40.0 |
| #2 | 8 | 3 | 7 | 3 | 7.00 | 56.0 |

### Part 2: A/B Test Results

| Metric | Value |
|--------|-------|
| Test Duration | August 1-31, 2019 |
| Total Orders | 1,197 |
| Users in Both Groups | 58 (5.63%) |
| 95th percentile (orders) | 2 orders |
| 95th percentile (revenue) | $435.54 |

### Statistical Tests

| Test | Raw Data | Filtered Data |
|------|----------|---------------|
| Conversion p-value | 0.01679 | 0.01418 |
| Conversion difference | +13.8% (B > A) | +17.1% (B > A) |
| Order size p-value | 0.692 | 0.750 |
| Order size difference | +25.2% | -2.7% |

### Final Decision
- **Conversion**: Statistically significant (p < 0.05), Group B is better
- **Order Size**: Not statistically significant (p > 0.05), no real difference
- **Recommendation**: Stop test, implement Group B
