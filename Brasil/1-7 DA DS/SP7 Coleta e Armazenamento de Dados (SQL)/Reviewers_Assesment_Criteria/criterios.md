# Evaluation Criteria: Data Collection and Storage (SQL) - Taxis

## Objective
Analyze Chicago taxi trip data to understand passenger preferences and the impact of weather on rides, combining SQL queries with Python analysis.

## Project Description
<details>
<summary>Task Statement</summary>

You work as an analyst for Zuber, a new ride-sharing company in Chicago.

**Steps:**
1. **Web Scraping**: Extract Chicago weather data for November 2017
2. **Exploratory Analysis (SQL)**: Trips by company, popular neighborhoods
3. **Hypothesis Test**: Trip duration Loop->O'Hare on rainy Saturdays
4. **Python Analysis**: Charts and interpretations
</details>

## Expected Results - Specific Numbers

### Company Data (Nov 15-16, 2017)

| Metric | Value |
|--------|-------|
| Total companies | 64 |
| Average trips per company | 2,145 |
| Maximum trips | 19,558 (Flash Cab) |
| Minimum trips | 2 |

### Top 10 Taxi Companies

| # | Company | Trips |
|---|---------|-------|
| 1 | Flash Cab | 19,558 |
| 2 | Taxi Affiliation Services | 11,422 |
| 3 | Medallion Leasing | 10,367 |
| 4 | Yellow Cab | 9,888 |
| 5 | Taxi Affiliation Service Yellow | 9,299 |
| 6 | Chicago Carriage Cab Corp | 9,181 |
| 7 | City Service | 8,448 |
| 8 | Sun Taxi | 7,701 |
| 9 | Star North Management LLC | 7,455 |
| 10 | Blue Ribbon Taxi Association Inc. | 5,953 |

### Top 10 Drop-off Locations

| # | Neighborhood | Average Trips |
|---|-------------|---------------|
| 1 | Loop | 10,727 |
| 2 | River North | 9,523 |
| 3 | Streeterville | 6,664 |
| 4 | West Loop | 5,163 |
| 5 | O'Hare | 2,546 |
| 6 | Lake View | 2,420 |
| 7 | Grant Park | 2,068 |
| 8 | Museum Campus | 1,510 |
| 9 | Gold Coast | 1,364 |
| 10 | Sheffield & DePaul | 1,259 |

### Loop -> O'Hare Trips

| Metric | Value |
|--------|-------|
| Total trips | 1,068 |
| Average duration | 2,071 seconds |
| Standard deviation | 769 seconds |
| Minimum | 0 seconds |
| Maximum | 7,440 seconds |

### Outlier Removal (IQR)

| Metric | Value |
|--------|-------|
| Q1 | 1,438.25 |
| Q3 | 2,580.00 |
| IQR | 1,141.75 |
| Lower cutoff | 0 (cannot be negative) |
| Upper cutoff | 4,292.625 |

### Hypothesis Test: Loop -> O'Hare

| Metric | Value |
|--------|-------|
| Alpha | 0.05 |
| p-value | 1.24e-13 |
| Decision | Reject H0 |
| Conclusion | Duration CHANGES on rainy days |

## Note for Reviewers: Credentials and Security

> If the student uses database credentials (host, username, password) in their notebook, remind them:
> - **Never hardcode credentials** in source code. Use environment variables or `.env` files instead (e.g., `os.getenv('DB_PASSWORD')`).
> - **Never push credentials to git.** Add `.env` to `.gitignore`. Pushing secrets to a repository — even a private one — is a serious security risk.
> - In this educational context, hardcoded credentials are acceptable for submission, but students should understand this is **not acceptable in real-world applications**.

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Loads all 3 DataFrames correctly
- [ ] **[REQUIRED]** Uses `info()` and `describe()` to examine data
- [ ] **[REQUIRED]** Converts average_trips to int
- [ ] **[REQUIRED]** Identifies Flash Cab as company #1 (19,558 trips)
- [ ] **[REQUIRED]** Identifies Loop as location #1 (10,727 trips)
- [ ] **[REQUIRED]** Sorts data correctly before creating charts
- [ ] **[REQUIRED]** Creates at least 2 bar charts (companies + locations)
- [ ] **[REQUIRED]** Formulates H0 and H1 hypotheses correctly
- [ ] **[REQUIRED]** Identifies outliers using boxplot or IQR method
- [ ] **[REQUIRED]** Calculates IQR correctly (Q1=1438.25, Q3=2580, IQR=1141.75)
- [ ] **[REQUIRED]** Removes outliers BEFORE the statistical test
- [ ] **[REQUIRED]** Implements t-test: `st.ttest_ind(good, bad)`
- [ ] **[REQUIRED]** p-value ~1.24e-13 -> rejects H0
- [ ] **[REQUIRED]** Correct conclusion: duration CHANGES significantly on rainy days

### INTERMEDIATE

- [ ] Uses `set_index()` to improve visualizations
- [ ] All charts have appropriate titles and labels
- [ ] Well-organized code with markdown sections
- [ ] Discusses practical significance (~8 min difference between good and bad weather)

### ADVANCED

- [ ] Multiple chart types used (bar + boxplot + histogram)
- [ ] Business recommendations based on findings
- [ ] Identifies that outlier removal changes the test outcome
- [ ] Code well-commented with clear narrative

## General Approval Criteria

| Level | Requirements |
|-------|------------|
| **Basic** | All 14 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 3 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Load and examine data:
```python
company_df = pd.read_csv('project_sql_result_01.csv')
trips_df = pd.read_csv('project_sql_result_04.csv')

company_df.info()  # 64 entries, 2 columns
trips_df.info()    # 94 entries, 2 columns
```

### Top 10 companies with chart:
```python
top_10_companies = company_df.sort_values('trips_amount', ascending=False).head(10)
top_10_companies = top_10_companies.set_index('company_name')
top_10_companies.plot(kind='barh')
plt.title('Number of Trips per Taxi Company')
plt.show()
```

### Identify and remove outliers:
```python
Q1 = loop_ohare['duration_seconds'].quantile(0.25)  # 1438.25
Q3 = loop_ohare['duration_seconds'].quantile(0.75)  # 2580.0
IQR = Q3 - Q1  # 1141.75

top_cutoff = Q3 + 1.5 * IQR  # 4292.625

loop_ohare_clean = loop_ohare.query('duration_seconds <= @top_cutoff')
```

### Hypothesis test:
```python
alpha = 0.05

good_weather = loop_ohare_clean.query('weather_conditions == "Good"')
bad_weather = loop_ohare_clean.query('weather_conditions == "Bad"')

results = st.ttest_ind(good_weather['duration_seconds'],
                       bad_weather['duration_seconds'])

print('p-value:', results.pvalue)  # 1.24e-13

if results.pvalue < alpha:
    print("We reject H0: duration CHANGES on rainy days")
else:
    print("We do not reject H0")
```

## Disqualification Criteria

- [ ] Does not load SQL data
- [ ] Does not create any charts
- [ ] Hypothesis test absent
- [ ] Inverted conclusion (says does NOT reject H0 with p < 0.05)
- [ ] Does not remove outliers before the test

## Common Conceptual Errors

### 1. Not sorting data before chart
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `df.plot(kind='bar')` | `df.sort_values('col').plot(kind='bar')` | Chart without logical order |

### 2. Not removing outliers
| Incorrect | Correct | Impact |
|-----------|---------|--------|
| Test with all data | Remove outliers first | Result may be distorted |

**Correct concept:** Outliers can distort statistical tests. In the project, trips with 0 seconds or >4292 seconds are anomalous.

### 3. Formulating hypotheses incorrectly
| Incorrect | Correct |
|-----------|---------|
| H0: "Duration changes" | H0: "Duration does NOT change" |
| H1: "There is no difference" | H1: "Duration changes" |

**Correct concept:** H0 (null) ALWAYS states "there is no difference" or "they are equal." H1 (alternative) states the opposite.

### 4. Interpreting p-value incorrectly
| Error | Correct |
|-------|---------|
| "p=1.24e-13 means 99.99% certainty" | "p=1.24e-13 means very low probability of seeing this if H0 were true" |

### 5. Not converting average_trips to int
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| Keep as float64 | `astype(int)` | Trips are integer counts |

### 6. Using vertical chart with many categories
| Problem | Solution |
|---------|---------|
| Overlapping labels | Use `kind='barh'` (horizontal) |

## Project Pitfalls

1. **Flash Cab dominates**: With 19,558 trips, it's almost double the second place. This is expected.

2. **Loop is the center**: As Chicago's central neighborhood, it's the most popular destination. O'Hare (airport) is in 5th place.

3. **Outliers are critical**: Before removing outliers, it may seem like there's no difference. After removing:
   - Good Weather average: ~1,900s
   - Bad Weather average: ~2,400s
   - Difference of ~500 seconds (~8 minutes)

4. **Extremely low p-value**: 1.24e-13 is much lower than 0.05, so we reject H0 with high confidence.

5. **Practical interpretation**: Rain adds ~8 minutes to Loop->O'Hare trips. This is significant for planning.
