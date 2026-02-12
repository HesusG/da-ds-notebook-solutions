# Evaluation Criteria: Statistical Data Analysis (Megaline)

## Objective

Students will perform statistical data analysis to determine which prepaid mobile plan (Surf vs Ultimate) generates more revenue for the telecommunications company Megaline. This project tests skills in data preprocessing, aggregation, descriptive statistics, and hypothesis testing.

## Project Description

<details>
<summary>Task Statement</summary>

You work as an analyst for Megaline, a telecommunications company. The company offers two prepaid plans: Surf and Ultimate. The commercial department wants to know which plan generates more revenue to adjust the advertising budget.

You will analyze data from 500 Megaline customers: who the customers are, where they are from, which plan they use, and the number of calls and messages they made in 2018. Your task is to analyze customer behavior and determine which prepaid plan generates more revenue.

**Datasets:**
- `megaline_calls.csv` - Call records (137,735 entries)
- `megaline_internet.csv` - Internet session data (104,825 entries)
- `megaline_messages.csv` - Message records (76,051 entries)
- `megaline_plans.csv` - Plan details (2 plans)
- `megaline_users.csv` - User information (500 users)

**Plan Details:**
| Feature | Surf | Ultimate |
|---------|------|----------|
| Monthly fee | $20 | $70 |
| Minutes included | 500 | 3000 |
| Messages included | 50 | 1000 |
| Data included | 15 GB | 30 GB |
| Extra minute | $0.03 | $0.01 |
| Extra message | $0.03 | $0.01 |
| Extra GB | $10 | $7 |

</details>

## Technical Glossary

| Term | Definition |
|------|------------|
| **Hypothesis Testing** | Statistical method to determine if there is enough evidence to reject a null hypothesis |
| **p-value** | Probability of obtaining results at least as extreme as observed, assuming null hypothesis is true |
| **Significance Level (α)** | Threshold for rejecting the null hypothesis (typically 0.05) |
| **t-test** | Statistical test comparing means of two groups |
| **Variance** | Measure of dispersion around the mean |
| **Aggregation** | Combining multiple records into summary statistics |
| **Revenue** | Income generated from plan fees plus charges for exceeding plan limits |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** All 5 datasets loaded correctly (calls, internet, messages, plans, users)
- [ ] **[REQUIRED]** `.info()` and `.head()` used to explore each dataset
- [ ] **[REQUIRED]** Date columns converted to datetime format (`pd.to_datetime()`)
- [ ] **[REQUIRED]** Call duration rounded UP to whole minutes (ceiling function)
- [ ] **[REQUIRED]** Zero-duration calls handled (removed or explained)
- [ ] **[REQUIRED]** Internet data converted from MB to GB
- [ ] **[REQUIRED]** Monthly usage calculated per user (minutes, messages, GB)
- [ ] **[REQUIRED]** Aggregated data merged correctly using `merge()` with appropriate join type
- [ ] **[REQUIRED]** Monthly revenue calculated per user
- [ ] **[REQUIRED]** Extra charges applied only when usage exceeds plan limits
- [ ] **[REQUIRED]** Base monthly fee added to extra charges
- [ ] **[REQUIRED]** Hypothesis test 1: Surf vs Ultimate revenue (p-value ~3.17e-15 → reject H0)
- [ ] **[REQUIRED]** Hypothesis test 2: NY-NJ vs other regions (p-value ~0.044 → reject H0)
- [ ] **[REQUIRED]** `equal_var=False` used (Welch's t-test) due to unequal variances
- [ ] **[REQUIRED]** Correct interpretation of p-values (reject H0 when p < α)

### INTERMEDIATE

- [ ] Mean and standard deviation calculated for each plan (Minutes ~429/430, Messages ~31/38, GB ~17/17, Revenue ~$61/$72)
- [ ] Histograms comparing distributions between plans
- [ ] Box plots showing monthly distributions
- [ ] Bar charts comparing monthly averages by plan
- [ ] Appropriate labels and titles on all graphs
- [ ] Variance calculated for revenue by plan (Surf ~3066 vs Ultimate ~130)

### ADVANCED

- [ ] Levene's test for equality of variances before t-test
- [ ] Month-by-month variance analysis
- [ ] Clear written conclusions about user behavior differences
- [ ] Business context in conclusions (Ultimate = predictable revenue, Surf = variable extra charges)

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All BASIC [REQUIRED] items completed correctly |
| **Intermediate** | Basic + at least 4 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct Revenue Calculation
```python
def monthly_income(row):
    income = row["usd_monthly_pay"]

    if row['num_mess'] > row["messages_included"]:
        income += (row['num_mess'] - row["messages_included"]) * row["usd_per_message"]
    if row['gb_used'] > row["gb_per_month"]:
        income += (row['gb_used'] - row["gb_per_month"]) * row["usd_per_gb"]
    if row['minutes_used'] > row["minutes_included"]:
        income += (row['minutes_used'] - row["minutes_included"]) * row["usd_per_minute"]

    row['income'] = income
    return row
```

### Correct Hypothesis Test
```python
alpha = 0.05

# Separate by plan
df_surf = df_monthly.query('plan == "surf"')
df_ultimate = df_monthly.query('plan == "ultimate"')

# Welch's t-test (unequal variances)
result = st.ttest_ind(df_surf['income'], df_ultimate['income'], equal_var=False)
print('p-value:', result.pvalue)

if result.pvalue < alpha:
    print("Reject null hypothesis: revenues differ significantly")
```

### Correct Data Aggregation
```python
# Round minutes UP before aggregating
calls['duration'] = np.ceil(calls['duration'])

# Monthly aggregation
month_calls = calls.groupby(['user_id', 'month_year']).agg(
    minutes_used=('duration', 'sum'),
    calls_made=('duration', 'count')
).reset_index()
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **Hypothesis test conclusion reversed** - Rejecting H0 when p > α or failing to reject when p < α
2. **Revenue calculation before plan limits** - Charging for all usage instead of only excess
3. **Wrong rounding direction** - Rounding minutes DOWN instead of UP (contractual requirement)
4. **Incorrect merge type** - Using inner join and losing users who don't use all services
5. **Hardcoded plan values** - Using magic numbers instead of referencing plan data

## Common Errors

### Error 1: Rounding Minutes Down
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `calls['duration'] = calls['duration'].round()` or `math.floor()` |
| **Correct** | `calls['duration'] = np.ceil(calls['duration'])` |
| **Consequence** | Underestimates revenue - telecom companies bill partial minutes as full minutes |

### Error 2: Calculating Extra Charges Incorrectly
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Charging for ALL usage: `income = minutes × rate` |
| **Correct** | Charging only for EXCESS: `income = max(0, minutes - included) × rate` |
| **Consequence** | Overestimates revenue by including charges for included usage |

### Error 3: Using Wrong Merge Type
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `df.merge(..., how='inner')` |
| **Correct** | `df.merge(..., how='outer')` then fill NaN with 0 |
| **Consequence** | Loses records for users who don't use all services (no calls, no messages, etc.) |

### Error 4: Using Regular t-test with Unequal Variances
| Aspect | Description |
|--------|-------------|
| **Incorrect** | `st.ttest_ind(a, b)` or `st.ttest_ind(a, b, equal_var=True)` |
| **Correct** | `st.ttest_ind(a, b, equal_var=False)` |
| **Consequence** | May produce incorrect p-value when variances differ significantly |

### Error 5: Confusing Statistical and Practical Significance
| Aspect | Description |
|--------|-------------|
| **Incorrect** | "Surf is better because p < 0.05" |
| **Correct** | "The revenue difference is statistically significant, with Ultimate generating higher average revenue ($72 vs $61), but Surf users contribute more variable extra charges" |
| **Consequence** | Missing business context - Ultimate has predictable revenue while Surf has high-revenue outliers |

### Error 6: Not Handling Zero-Duration Calls
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Including calls with duration=0 in analysis |
| **Correct** | Filtering out or investigating zero-duration calls: `calls = calls[calls['duration'] != 0]` |
| **Consequence** | May skew averages and count statistics |

## Expected Key Results Summary

| Metric | Expected Value |
|--------|----------------|
| Number of users | 500 |
| Number of churned users | 34 |
| Total call records | 137,735 (110,901 after removing zeros) |
| Surf mean revenue | ~$35-61 (varies by methodology) |
| Ultimate mean revenue | ~$70-72 |
| Surf revenue variance | ~1500-3100 (varies by methodology) |
| Ultimate revenue variance | ~50-130 |
| Plan comparison p-value | <0.001 (highly significant) |
| Regional comparison p-value | ~0.03-0.05 (significant at α=0.05) |

### Methodology Notes

**Revenue values may vary based on:**
1. Whether all 12 months are included vs only months with activity
2. Whether churned users' months after churn are excluded
3. How "no usage" months are handled (included as base fee or excluded)

**What matters for evaluation:**
- Hypothesis test conclusions are correct (plans have different revenue)
- Welch's t-test is used (unequal variances)
- p-value interpretation is correct
- Business context is provided in conclusions
