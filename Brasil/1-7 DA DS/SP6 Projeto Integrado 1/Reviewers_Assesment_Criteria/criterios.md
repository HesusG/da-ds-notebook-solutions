# Evaluation Criteria: Integrated Project 1 - Game Analysis

## Objective
Perform a complete analysis of video game sales data to identify success patterns, create user profiles by region, and test statistical hypotheses.

## Project Description
<details>
<summary>Task Statement</summary>

The online store Ice sells video games worldwide. Data on user and expert reviews, genres, platforms, and historical sales are available.

**Objective:** Identify patterns that determine the success of a game to plan advertising campaigns.

**Steps:**
1. Prepare the data (missing values, data types, total sales calculation)
2. Analyze data: releases per year, sales by platform, lifespan, correlations
3. Create user profile by region (NA, EU, JP)
4. Test statistical hypotheses
</details>

## Expected Results - Specific Numbers

### Data Overview

| Metric | Value |
|--------|-------|
| Total rows | 16,715 |
| Total columns | 11 (+ 1 created: total_sales) |
| Duplicates | 0 |

### Missing Values

| Column | Missing | % of Total |
|--------|---------|-----------|
| critic_score | 8,578 | 51% |
| user_score | 6,701 (+ 2,424 'tbd') | 40% + 14% |
| rating | 6,766 | 40% |
| year_of_release | 269 | 2% |
| name | 2 | ~0% |
| genre | 2 | ~0% |

### Top 5 Games by Total Sales

| # | Name | Platform | Sales (millions) |
|---|------|----------|-----------------|
| 1 | Wii Sports | Wii | 82.54 |
| 2 | Super Mario Bros. | NES | 40.24 |
| 3 | Mario Kart Wii | Wii | 35.52 |
| 4 | Wii Sports Resort | Wii | 32.77 |
| 5 | Pokemon Red/Pokemon Blue | GB | 31.38 |

### Platforms with Positive Z-score (Dominant)

| Platform | Total Sales | Z-score |
|----------|------------|---------|
| PS2 | 1,255.77 | 2.78 |
| X360 | 971.42 | 1.96 |
| PS3 | 939.65 | 1.87 |
| Wii | 907.51 | 1.78 |
| DS | 806.12 | 1.49 |
| PS | 730.86 | 1.27 |

### Correlations (PS4 Platform, 2013-2016 period)

| Relationship | Correlation | Interpretation |
|-------------|------------|---------------|
| Critic Score vs Sales | 0.41 | Moderate positive |
| User Score vs Sales | -0.03 | Virtually zero |

### Profile by Region - Top 5 Platforms

| NA | EU | JP |
|----|----|----|
| PS4 (108.74) | PS4 (141.09) | 3DS (67.81) |
| XOne (93.12) | PS3 (67.81) | PS3 (23.35) |
| X360 (81.66) | XOne (51.59) | PSV (18.59) |
| PS3 (63.50) | X360 (42.52) | PS4 (15.96) |
| 3DS (38.20) | 3DS (30.96) | WiiU (10.88) |

### Profile by Region - Top 5 Genres

| NA | EU | JP |
|----|----|----|
| Action | Action | Role-Playing |
| Shooter | Shooter | Action |
| Sports | Sports | Misc |
| Role-Playing | Role-Playing | Fighting |
| Misc | Racing | Shooter |

### Hypothesis Test 1: XOne vs PC (User Score)

| Metric | Value |
|--------|-------|
| XOne Mean | 6.52 |
| PC Mean | 6.27 |
| Levene Test | Different variances |
| p-value (t-test) | 0.148 |
| Decision | Do not reject H0 (no significant difference) |

### Hypothesis Test 2: Action vs Sports (User Score)

| Metric | Value |
|--------|-------|
| Action Mean | 6.84 |
| Sports Mean | 5.24 |
| Levene Test | Different variances |
| p-value (t-test) | 1.45e-20 |
| Decision | Reject H0 (significant difference exists) |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Loads data and identifies 16,715 rows
- [ ] **[REQUIRED]** Calculates `total_sales` column correctly
- [ ] **[REQUIRED]** Handles 'tbd' in user_score (convert to NaN)
- [ ] **[REQUIRED]** Creates at least 3 different visualizations
- [ ] **[REQUIRED]** Identifies dominant platforms
- [ ] **[REQUIRED]** Documents conclusions in markdown

### INTERMEDIATE

- [ ] Uses z-score to identify dominant platforms
- [ ] Selects relevant period (2013-2016 or similar)
- [ ] Analyzes platform lifecycle (~10 years)
- [ ] Calculates correlations between reviews and sales
- [ ] Creates regional profiles (NA, EU, JP) with correct differences
- [ ] Identifies that Xbox is not popular in Japan

### ADVANCED

- [ ] Implements Levene test before t-test
- [ ] Uses `equal_var=False` when variances are different
- [ ] Hypothesis 1: p-value ~0.15, does not reject H0
- [ ] Hypothesis 2: p-value ~1e-20, rejects H0
- [ ] Interprets results considering practical impact
- [ ] Well-founded conclusions about marketing strategy

## General Approval Criteria

| Level | Requirements |
|-------|------------|
| **Basic** | All BASIC criteria + complete exploratory analysis |
| **Intermediate** | Basic + regional profiles + correlations |
| **Advanced** | Intermediate + both hypotheses tested correctly |

## Compliance Examples

### Calculate total_sales:
```python
data['total_sales'] = data[['na_sales','eu_sales','jp_sales','other_sales']].sum(axis=1)
```

### Z-score for platforms:
```python
df_sales = data.groupby('platform')['total_sales'].sum().reset_index()
df_sales['z_score'] = (df_sales['total_sales'] - df_sales['total_sales'].mean()) / df_sales['total_sales'].std()
# Platforms with z_score > 0 are dominant
```

### Handle 'tbd' in user_score:
```python
data.loc[data['user_score'] == 'tbd', 'user_score'] = np.nan
data['user_score'] = data['user_score'].astype('float')
```

### Complete hypothesis test:
```python
alpha = 0.05

# Levene test (variances)
p_value_levene = stats.levene(sample1, sample2).pvalue
equal_var = p_value_levene >= alpha

# T-test with correct variances
p_value = stats.ttest_ind(sample1, sample2, nan_policy='omit', equal_var=equal_var).pvalue

if p_value < alpha:
    print("We reject H0")
else:
    print("We do not reject H0")
```

## Disqualification Criteria

- [ ] Does not calculate total_sales
- [ ] Does not test any hypothesis
- [ ] Hypothesis tests with inverted interpretation
- [ ] Does not create regional profiles
- [ ] Conclusions contradictory to the data

## Common Conceptual Errors

### 1. Not handling 'tbd' in user_score
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| Convert directly to float | Replace 'tbd' with NaN first | Conversion error |

### 2. Interpreting correlation as causation
| Incorrect | Correct |
|-----------|---------|
| "High review CAUSES more sales" | "There is a positive correlation between review and sales" |

### 3. Not using relevant period
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| Analyze since 1980 | Focus on 2013-2016 | Old platforms are irrelevant |

### 4. Using t-test without checking variances
| Incorrect | Correct | Impact |
|-----------|---------|--------|
| `ttest_ind(a, b)` default | Test Levene first, use `equal_var=False` if needed | Result may be invalid |

### 5. Confusing statistical significance with practical significance
| Error | Reality |
|-------|---------|
| "p < 0.05 = large difference" | p < 0.05 only means statistically significant |
| Action vs Sports: 1.6 point difference | Statistically significant, but evaluate real impact |

### 6. Formulating hypotheses incorrectly
| Incorrect | Correct |
|-----------|---------|
| H0: "They are different" | H0: "There is no difference" (always negative) |

## Project Pitfalls

1. **Platform lifecycle**: It's ~10 years. If the student finds another value, review the analysis.

2. **Japan is different**: Xbox practically doesn't exist. Top platforms are Sony (PS) and Nintendo (3DS, WiiU). Role-Playing is the #1 genre.

3. **Critic vs User Score correlation**:
   - Critic Score vs Sales: ~0.4 (moderate positive correlation)
   - User Score vs Sales: ~0 (virtually no correlation)

   **Correct conclusion**: Critics influence more than users.

4. **XOne vs PC hypothesis**: The p-value is 0.15 > 0.05, so we do NOT reject H0. The means are similar (6.52 vs 6.27).

5. **Action vs Sports hypothesis**: The p-value is ~0 (1.45e-20), so we reject H0. The means are different (6.84 vs 5.24).
