# Evaluation Criteria: How to Tell a Story Using Data

## Objective
Conduct market research on restaurants in Los Angeles to support the decision to open a robot-operated cafe, presenting insights through visualizations and data analysis.

## Project Description
<details>
<summary>Task Statement</summary>

You decided to open a small robot-operated cafe in Los Angeles. The project is promising but expensive, so you need to attract investors.

**Required analyses:**
1. Proportions of establishment types
2. Proportion of chains vs non-chains
3. Most common type of chain
4. Seat distribution in chains
5. Average seats by type
6. Top 10 streets by number of restaurants
7. Streets with only one restaurant
8. Seat distribution on popular streets
</details>

## Expected Results - Specific Numbers

### Dataset: rest_data_us.csv

| Metric | Value |
|--------|-------|
| Total rows | 9,651 |
| Total columns | 6 |

### Columns

| Column | Type | Missing |
|--------|------|---------|
| id | int64 | 0 |
| object_name | object | 0 |
| address | object | 0 |
| chain | object | 3 |
| object_type | object | 0 |
| number | int64 | 0 |

### Establishment Types

| Type | Count | % |
|------|-------|---|
| Restaurant | 7,255 | 75.2% |
| Fast Food | 1,066 | 11.0% |
| Cafe | 435 | 4.5% |
| Pizza | 320 | 3.3% |
| Bar | 292 | 3.0% |
| Bakery | 283 | 2.9% |

### Chain vs Non-Chain

| Type | Count | % |
|------|-------|---|
| Non-chain (False) | 5,972 | 61.9% |
| Chain (True) | 3,676 | 38.1% |

### Chain Proportion by Type

| Type | % Chain | Note |
|------|---------|------|
| Bakery | 100% | All are chains |
| Cafe | 61.1% | Majority are chains |
| Fast Food | 56.8% | Majority are chains |
| Pizza | 48.0% | Almost half |
| Restaurant | 31.6% | Majority independent |
| Bar | 26.4% | Majority independent |

### Top 5 Chains by Number of Locations

| Chain | Locations |
|-------|----------|
| THE COFFEE BEAN & TEA LEAF | 47 |
| SUBWAY | 31 |
| DOMINO'S PIZZA | 15 |
| KENTUCKY FRIED CHICKEN | 14 |
| WABA GRILL | 14 |

### Average Seats by Type

| Type | Mean | Median |
|------|------|--------|
| Restaurant | 48.0 | 29 |
| Bar | 44.8 | 28.5 |
| Fast Food | 31.8 | 21 |
| Pizza | 28.5 | 18.5 |
| Cafe | 25.0 | 21 |
| Bakery | 21.8 | 18 |

### Top 10 Streets by Number of Restaurants

| Street | Restaurants |
|--------|------------|
| W SUNSET BLVD | 296 |
| W PICO BLVD | 288 |
| HOLLYWOOD BLVD | 167 |
| WILSHIRE BLVD | 161 |
| S VERMONT AVE | 148 |
| SANTA MONICA BLVD | 146 |
| W 3RD ST | 145 |
| BEVERLY BLVD | 135 |
| S FIGUEROA ST | 134 |
| MELROSE AVE | 128 |

### Streets with Only One Restaurant

| Metric | Value |
|--------|-------|
| Total streets with 1 restaurant | 2,481 |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Loads data (9,651 rows)
- [ ] **[REQUIRED]** Analyzes type proportions (Restaurant = 75%)
- [ ] **[REQUIRED]** Analyzes chain proportion (~38% are chains)
- [ ] **[REQUIRED]** Creates at least 4 different charts
- [ ] **[REQUIRED]** Identifies top 10 streets (W Sunset Blvd = #1)
- [ ] **[REQUIRED]** All charts have titles and labels
- [ ] **[REQUIRED]** Documents conclusions in markdown

### INTERMEDIATE

- [ ] Calculates chain ratio by type (Bakery=100%, Cafe=61%)
- [ ] Analyzes seat distribution in chains (histogram)
- [ ] Calculates mean AND median seats by type
- [ ] Extracts street name from address correctly
- [ ] Counts streets with only 1 restaurant (2,481)
- [ ] Analyzes seat distribution on W Sunset Blvd
- [ ] Uses pivot_table for cross-analyses

### ADVANCED

- [ ] Uses multiple libraries (matplotlib, seaborn, plotly)
- [ ] Presents actionable insights for investors
- [ ] Identifies trends and patterns in the market
- [ ] Clear conclusions answering business questions
- [ ] Well-organized and documented code
- [ ] Interactive visualizations with plotly

## General Approval Criteria

| Level | Requirements |
|-------|------------|
| **Basic** | All BASIC criteria met |
| **Intermediate** | Basic + at least 5 INTERMEDIATE criteria |
| **Advanced** | Intermediate + investor insights + advanced visualizations |

## Compliance Examples

### Type proportions:
```python
grouped_rest = rest.groupby('object_type').count()
# Restaurant: 7255, Fast Food: 1066, Cafe: 435, Pizza: 320, Bar: 292, Bakery: 283

ax = sns.barplot(x=grouped_rest.index, y=grouped_rest['id'])
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.show()
```

### Chain ratio by type:
```python
grouped_chain_object = pd.pivot_table(
    rest,
    values='object_name',
    index='object_type',
    columns=['chain'],
    aggfunc='count'
)

grouped_chain_object['ratio'] = (
    grouped_chain_object[True] /
    (grouped_chain_object[True] + grouped_chain_object[False])
)
# Bakery: NaN (100% True), Cafe: 0.61, Fast Food: 0.57, etc.
```

### Extract street name:
```python
# Remove number and keep street name
rest_address = rest['address'].apply(lambda x: ' '.join(x.split(' ')[1:]))
# "3708 N EAGLE ROCK BLVD" -> "N EAGLE ROCK BLVD"
```

### Top 10 streets:
```python
rest_address_top = (
    rest_address
    .to_frame()
    .groupby('address')
    .size()
    .sort_values(ascending=False)
    .head(10)
)
# W SUNSET BLVD: 296, W PICO BLVD: 288, ...
```

### Streets with only 1 restaurant:
```python
single_restaurant_streets = (
    rest_address
    .to_frame()
    .groupby('address')
    .size()
    .loc[lambda x: x == 1]
    .shape[0]
)
# Result: 2481
```

## Disqualification Criteria

- [ ] Does not perform any exploratory analysis
- [ ] Fewer than 3 visualizations created
- [ ] Charts without titles or completely illegible
- [ ] Does not answer the project's main questions
- [ ] Conclusions not based on data

## Common Conceptual Errors

### 1. Not extracting street name correctly
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `address.split()[0]` | `' '.join(address.split()[1:])` | Gets number instead of street |

**Correct concept:** The first "word" in the address is the NUMBER. The street name starts at the second word.

### 2. Confusing count vs sum
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| `groupby().sum()` for counting | `groupby().count()` or `.size()` | sum() adds numeric values |

### 3. Not handling NaN in chain column
| Problem | Solution |
|---------|---------|
| 3 missing values | `rest['chain'].fillna(False)` or check beforehand |

### 4. Calculating proportion incorrectly
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| `True / total` with NaN | Handle NaN first | Bakery has no False, so division fails |

**Correct concept:** Bakery has 100% True and 0 False. The calculation `True/(True+False)` returns NaN because False=NaN. Handle beforehand.

### 5. Charts with overlapping labels
| Problem | Solution |
|---------|---------|
| Illegible labels | `rotation=90` or `kind='barh'` |

### 6. Not using mean AND median
| Problem | Solution |
|---------|---------|
| Mean distorted by outliers | Calculate both and compare |

**Correct concept:** Restaurant has mean=48 but median=29. This indicates large outliers (restaurants with many seats pulling the mean up).

## Project Pitfalls

1. **Bakery is 100% chain**: All 283 Bakery establishments are chains. This may seem like an error, but it's correct in the dataset.

2. **Restaurant dominates**: With 75% of establishments, Restaurant distorts general analyses. Consider separate analyses.

3. **W Sunset Blvd vs Hollywood Blvd**: Sunset has 296 restaurants, Hollywood has 167. But Hollywood is more famous for tourism.

4. **Mean vs Median in seats**: The difference indicates asymmetric distribution:
   - Restaurant: mean=48, median=29 (large outliers)
   - Bar: mean=45, median=28.5 (also asymmetric)

5. **2,481 streets with 1 restaurant**: Does this represent market opportunities or less commercial areas?

6. **Coffee Bean is the largest chain**: With 47 locations, it surpasses Subway (31). This reflects the coffee culture in LA.
