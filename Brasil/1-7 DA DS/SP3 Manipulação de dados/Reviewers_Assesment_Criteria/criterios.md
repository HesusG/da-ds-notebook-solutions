# Evaluation Criteria: Data Wrangling - Instacart

## Objective
Perform exploratory data analysis (EDA) on an Instacart dataset, applying advanced preprocessing and analysis techniques with pandas and matplotlib.

## Project Description
<details>
<summary>Task Statement</summary>

Instacart is a grocery delivery platform. The dataset contains information about orders, products, aisles, and departments.

**Steps:**
1. **Data overview**: Load and examine 5 DataFrames
2. **Data preparation**: Check types, handle missing values, remove duplicates
3. **Data analysis**:
   - **[A] Easy**: Verify values, charts by hour/day
   - **[B] Medium**: Compare days, order distribution, top 20 products
   - **[C] Hard**: Items per order, reordering, first in cart
</details>

## Expected Results - Specific Numbers

### Data Overview (5 DataFrames)

| DataFrame | Rows | Columns | Notes |
|-----------|------|---------|-------|
| `orders` | 478,967 | 6 | days_since_prior_order has missing values |
| `products` | 49,694 | 4 | product_name has missing values |
| `departments` | 21 | 2 | Complete |
| `aisles` | 134 | 2 | Complete |
| `order_products` | 4,545,007 | 4 | add_to_cart_order has missing values |

### Missing Values

| DataFrame | Column | Count | Reason |
|-----------|--------|-------|--------|
| `products` | product_name | 1,258 | All with aisle_id=100, department_id=21 ("missing") |
| `orders` | days_since_prior_order | 28,817 | First order (order_number=1) |
| `order_products` | add_to_cart_order | 836 | Orders with >64 items (system limit) |

### Duplicates

| DataFrame | Type | Count | Pattern |
|-----------|------|-------|---------|
| `orders` | Explicit | 15 | All: order_dow=3, order_hour_of_day=2 (Wednesday 2am) |
| `products` | Implicit (name) | 104 | Same name, different IDs (do not remove) |

### Analysis [A] - Valid Values

| Column | Expected Range | Found Range |
|--------|---------------|-------------|
| order_hour_of_day | 0-23 | 0-23 |
| order_dow | 0-6 | 0-6 |

### Top 20 Most Purchased Products

| # | Product ID | Name | Purchases |
|---|------------|------|-----------|
| 1 | 24852 | Banana | 66,050 |
| 2 | 13176 | Bag of Organic Bananas | 53,297 |
| 3 | 21137 | Organic Strawberries | 37,039 |
| 4 | 21903 | Organic Baby Spinach | 33,971 |
| 5 | 47209 | Organic Hass Avocado | 29,773 |
| 6 | 47766 | Organic Avocado | 24,689 |
| 7 | 47626 | Large Lemon | 21,495 |
| 8 | 16797 | Strawberries | 20,018 |

### Top 20 Reordered Products

| # | Product ID | Name | Reorders |
|---|------------|------|----------|
| 1 | 24852 | Banana | 55,763 |
| 2 | 13176 | Bag of Organic Bananas | 44,450 |
| 3 | 21137 | Organic Strawberries | 28,639 |
| 4 | 21903 | Organic Baby Spinach | 26,233 |
| 5 | 47209 | Organic Hass Avocado | 23,629 |

### First Item in Cart (Top 5)

| # | Product ID | Name | Times First |
|---|------------|------|-------------|
| 1 | 24852 | Banana | 15,562 |
| 2 | 13176 | Bag of Organic Bananas | 11,026 |
| 3 | 27845 | Organic Whole Milk | 4,363 |
| 4 | 21137 | Organic Strawberries | 3,946 |
| 5 | 47209 | Organic Hass Avocado | 3,390 |

### Reordering Statistics

| Metric | Value |
|--------|-------|
| Average reorder rate per customer | 49.5% |
| Median reorder rate | 50.0% |
| Customers with 100% reorder rate | Several (e.g.: user_id 137587) |
| Customers with 0% reorder rate | Several (e.g.: user_id 165726) |

## Evaluation Rubric - Reviewer Checklist

This project is a guided exercise with specific expected outputs at each step. All criteria are required for approval.

- [ ] **[REQUIRED]** Code runs without errors
- [ ] **[REQUIRED]** Loads 5 DataFrames with `sep=';'`
- [ ] **[REQUIRED]** Uses `info()` and identifies correct sizes for all DataFrames
- [ ] **[REQUIRED]** Identifies 15 explicit duplicates in orders
- [ ] **[REQUIRED]** Identifies pattern in duplicates (Wednesday 2am)
- [ ] **[REQUIRED]** Removes duplicates and verifies 0 remaining
- [ ] **[REQUIRED]** Explains missing values in days_since_prior_order (first order)
- [ ] **[REQUIRED]** Explains missing values in add_to_cart_order (64-item limit)
- [ ] **[REQUIRED]** Fills product_name with 'Unknown' and add_to_cart_order with 999
- [ ] **[REQUIRED]** Verifies valid ranges (order_hour_of_day: 0-23, order_dow: 0-6)
- [ ] **[REQUIRED]** Creates bar charts for orders by hour and by day
- [ ] **[REQUIRED]** Uses `merge()` to combine order_products with products
- [ ] **[REQUIRED]** Compares Wednesday vs Saturday order patterns
- [ ] **[REQUIRED]** Order distribution per customer (histogram)
- [ ] **[REQUIRED]** Identifies top 20 most purchased products (Banana #1 with 66,050)
- [ ] **[REQUIRED]** Calculates items per order distribution
- [ ] **[REQUIRED]** Calculates reorder proportion per product
- [ ] **[REQUIRED]** Calculates reorder proportion per customer (average ~49.5%)
- [ ] **[REQUIRED]** Identifies top 20 first items added to cart

## General Approval Criteria

| Requirement | Details |
|-------------|---------|
| **Approved** | All 19 criteria above met. Each step has a specific expected output — partial completion is not sufficient. |
| **Needs revision** | Any required criterion not met. Student must fix and resubmit. |

## Disqualification Criteria

- [ ] Does not load all 5 DataFrames
- [ ] Does not use `sep=';'` (data becomes incorrect)
- [ ] Does not complete section [A]
- [ ] Top 20 products completely different from expected
- [ ] Removes data without justification (e.g.: deleting valid missing values)

## Common Conceptual Errors

### 1. Not using correct separator
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `pd.read_csv('file.csv')` | `pd.read_csv('file.csv', sep=';')` | Data ends up in a single column |

**Correct concept:** CSV files can use different separators (`,`, `;`, `\t`). ALWAYS check the file before assuming comma.

### 2. Confusing explicit vs implicit duplicates
| Type | Definition | Action |
|------|-----------|--------|
| Explicit | 100% identical rows | Remove |
| Implicit | Same value in key column, others different | Investigate before removing |

**In SP3:** Products with the same name but different IDs are NOT duplicates - they may be different products or different locations.

### 3. Removing missing values that are valid
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| Delete rows with days_since_prior_order=NaN | Keep them | These are first orders, NaN is expected |

**Correct concept:** NaN doesn't always mean an error. For `days_since_prior_order`, NaN on the first order is CORRECT (there is no prior order).

### 4. Confusing count() vs size() in groupby
| Method | What it does | Example |
|--------|-------------|---------|
| `size()` | Counts ALL rows | `groupby('col').size()` |
| `count()` | Counts NON-null values | `groupby('col')['other'].count()` |

### 5. Not investigating duplicate patterns
| Poor approach | Correct approach |
|--------------|-----------------|
| `df.drop_duplicates()` directly | Investigate what duplicates have in common BEFORE removing |

**In SP3:** The 15 duplicates in orders all occur at 2am on Wednesday - this suggests a system error, not duplicate manual entry.

### 6. Calculating proportion incorrectly
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| `sum(reordered) / len(df)` | `mean(reordered)` | mean() already does sum/count automatically |

**Correct concept:** When a column is binary (0/1), the mean IS the proportion. `mean([0,1,1,0,1]) = 3/5 = 0.6 = 60%`

## Project Pitfalls

1. **64-item cart limit**: The system only records the position of the first 64 items. Orders with more items will have NaN in `add_to_cart_order` for items beyond the 64th. Filling with 999 differentiates "unknown" from real positions.

2. **"Missing" products**: Products with aisle_id=100 and department_id=21 are in categories called "missing" - these are products without a defined category, not data errors.

3. **Wednesday vs Saturday comparison**: The shopping pattern is similar, with a peak between 10am-3pm. The difference is that Saturday has more orders late at night.

4. **Banana is king**: The most purchased, most reordered, and most frequently first-in-cart product is ALWAYS Banana (product_id 24852). If the student finds another product at the top, something is wrong.
