# Evaluation Criteria: Integrated Project 2 (A/A/B Test - Font Change)

## Objective

Students will analyze event logs from an A/A/B test to evaluate whether changing fonts in a mobile app affects user behavior. This project combines funnel analysis with statistical hypothesis testing to make data-driven product decisions.

## Project Description

<details>
<summary>Task Statement</summary>

You work at a food products startup. You need to investigate user behavior in the company's app. First, study the sales funnel and determine how users reach the purchase stage. Then analyze the results of an A/A/B test where designers wanted to change the fonts throughout the app.

The users were split into three groups:
- Group 246 (Control A): Old fonts
- Group 247 (Control B): Old fonts
- Group 248 (Treatment): New fonts

**Dataset:**
- `logs_exp.csv` - 244,126 event records with columns:
  - EventName: Type of event
  - DeviceIDHash: Unique user identifier
  - EventTimestamp: Unix timestamp
  - ExpId: Experiment group (246, 247, or 248)

**Tasks:**
1. Study the sales funnel: how users proceed to purchase
2. Analyze A/A test results to verify proper group splitting
3. Analyze A/B test results to determine font change impact

</details>

## Technical Glossary

| Term | Definition |
|------|------------|
| **Sales Funnel** | Visualization of user journey from first contact to conversion |
| **A/A Test** | Experiment with identical treatment for both groups to validate testing methodology |
| **A/B Test** | Experiment comparing control group to treatment group |
| **Event Log** | Record of user actions with timestamps |
| **Conversion Rate** | Percentage of users completing a desired action |
| **Z-test for Proportions** | Statistical test comparing proportions between two groups |
| **Bonferroni Correction** | Method to adjust significance level for multiple comparisons |
| **Unix Timestamp** | Seconds since January 1, 1970 |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** Dataset loaded correctly (244,126 events)
- [ ] **[REQUIRED]** Column names renamed for clarity
- [ ] **[REQUIRED]** Unix timestamp converted to datetime, date column extracted
- [ ] **[REQUIRED]** Total events ~244,126, unique users ~7,551, events per user ~32.3
- [ ] **[REQUIRED]** Date range identified (2019-07-25 to 2019-08-07)
- [ ] **[REQUIRED]** Incomplete early data identified via histogram
- [ ] **[REQUIRED]** Data filtered to complete period (2019-08-01 onwards), <1% data loss
- [ ] **[REQUIRED]** All three experiment groups confirmed (246, 247, 248)
- [ ] **[REQUIRED]** Event types and frequencies identified (MainScreenAppear ~118K, OffersScreenAppear ~46.5K, CartScreenAppear ~42.4K, PaymentScreenSuccessful ~34.1K, Tutorial ~1K)
- [ ] **[REQUIRED]** Users per event calculated (MainScreen 7,423, Offers 4,597, Cart 3,736, Payment 3,540)
- [ ] **[REQUIRED]** Funnel conversion rates calculated (Main→Offers ~62%, Offers→Cart ~81%, Cart→Payment ~95%)
- [ ] **[REQUIRED]** Biggest drop identified: Main → Offers (~38% loss)
- [ ] **[REQUIRED]** End-to-end conversion: ~47.7% (Main to Payment)
- [ ] **[REQUIRED]** Tutorial excluded from funnel (not sequential)
- [ ] **[REQUIRED]** Users per group calculated (246: ~2,484, 247: ~2,517, 248: ~2,537)
- [ ] **[REQUIRED]** A/A test: z-test for proportions applied, all p-values > α, groups properly split
- [ ] **[REQUIRED]** A/B test: Group 246 vs 248, 247 vs 248, and combined control (246+247) vs 248 compared
- [ ] **[REQUIRED]** All A/B p-values > α — no significant differences found
- [ ] **[REQUIRED]** Conclusion: font change has no statistically significant impact on user behavior

### INTERMEDIATE

- [ ] Bonferroni correction mentioned or applied
- [ ] Adjusted α for multiple tests (e.g., α/n)
- [ ] Funnel visualization created (e.g., plotly funnel chart)
- [ ] Well-organized code with markdown sections

### ADVANCED

- [ ] Business interpretation of font change results
- [ ] Recommendations for future experiments
- [ ] Professional presentation of findings
- [ ] Well-commented code with clear narrative

## General Approval Criteria

| Level | Requirements |
|-------|--------------|
| **Basic** | All 19 BASIC [REQUIRED] criteria met |
| **Intermediate** | Basic + at least 3 INTERMEDIATE criteria |
| **Advanced** | Intermediate + at least 3 ADVANCED criteria |

## Compliance Examples

### Correct Timestamp Conversion
```python
data['date_time'] = pd.to_datetime(data['timestamp'], unit='s')
data['date'] = data['date_time'].dt.floor('1D')
```

### Correct Funnel Calculation
```python
# Users per event
users_per_event = (data
    .pivot_table(index='event', values='user', aggfunc=lambda x: x.nunique())
    .sort_values('user', ascending=False)
)

# Conversion between stages
users_funnel = users_per_event[:-1]  # Exclude Tutorial
users_funnel = (users_funnel / users_funnel.shift())[1:]
```

### Correct Z-test for Proportions
```python
import math
from scipy import stats

def check_hypothesis(successes1, successes2, trials1, trials2, alpha=0.05):
    p1 = successes1 / trials1
    p2 = successes2 / trials2
    p_combined = (successes1 + successes2) / (trials1 + trials2)

    difference = p1 - p2
    z_value = difference / math.sqrt(p_combined * (1 - p_combined) * (1/trials1 + 1/trials2))

    distr = stats.norm(0, 1)
    p_value = (1 - distr.cdf(abs(z_value))) * 2

    return p_value
```

### Correct Combined Control Group
```python
# Combine control groups 246 and 247
users_per_group_control = users_per_group.copy()
users_per_group_control.loc[247] += users_per_group_control.loc[246]
users_per_group_control.drop(246, inplace=True)
```

## Disqualification Criteria

The following errors result in automatic failure:

1. **Wrong timestamp conversion** - Using wrong unit (ms instead of s) or wrong method
2. **Including incomplete data** - Not filtering pre-August data
3. **Wrong funnel order** - Not ordering events by user count or including Tutorial
4. **Misinterpreting A/A test** - Expecting significant differences in A/A test
5. **Wrong test statistic** - Using t-test instead of z-test for proportions
6. **Wrong conclusion** - Claiming font change has significant effect when p > α

## Common Errors

### Error 1: Not Filtering Incomplete Data
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using all data from July 25 onwards |
| **Correct** | Filtering to complete period: `data.query('date_time > "2019-07-31 21:00"')` |
| **Consequence** | Skewed daily metrics due to incomplete early data |

### Error 2: Including Tutorial in Funnel
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Including Tutorial as a funnel stage |
| **Correct** | Excluding Tutorial as it's not part of the purchase sequence |
| **Consequence** | Incorrect funnel progression and conversion rates |

### Error 3: Wrong Proportion Test
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using chi-square or t-test for proportion comparison |
| **Correct** | Using z-test for proportions (two-proportion z-test) |
| **Consequence** | May produce inaccurate p-values |

### Error 4: Forgetting to Combine Control Groups
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Only comparing treatment to one control group |
| **Correct** | Also comparing treatment to combined control (246+247) for higher power |
| **Consequence** | Missing the most powerful comparison |

### Error 5: Expecting A/A Test to Show Differences
| Aspect | Description |
|--------|-------------|
| **Incorrect** | "The A/A test shows different user behavior between groups" |
| **Correct** | A/A test should show NO significant differences - that validates the split |
| **Consequence** | Misunderstanding the purpose of A/A testing |

### Error 6: Not Accounting for Multiple Comparisons
| Aspect | Description |
|--------|-------------|
| **Incorrect** | Using α=0.05 for each of 15+ comparisons |
| **Correct** | Mentioning Bonferroni correction: α_adjusted = α/n |
| **Consequence** | Increased false positive rate across all tests |

## Expected Key Results Summary

### Dataset Overview
| Metric | Value |
|--------|-------|
| Total events (raw) | 244,126 |
| Total events (filtered) | 242,136 |
| Total users (filtered) | 7,538 |
| Events per user | ~32.3 |
| Data period | 2019-08-01 to 2019-08-07 |
| Data loss from filtering | <1% |

### Experiment Groups
| Group | Role | Users |
|-------|------|-------|
| 246 | Control A | 2,484 |
| 247 | Control B | 2,517 |
| 248 | Treatment (new fonts) | 2,537 |

### Funnel Analysis
| Step | From | To | Conversion |
|------|------|-----|------------|
| 1 | MainScreenAppear (7,423) | OffersScreenAppear (4,597) | 61.9% |
| 2 | OffersScreenAppear (4,597) | CartScreenAppear (3,736) | 81.3% |
| 3 | CartScreenAppear (3,736) | PaymentScreenSuccessful (3,540) | 94.8% |

**End-to-end conversion:** 47.7%

### Statistical Test Results (α = 0.01)

#### A/A Test (246 vs 247)
| Event | p-value | Significant? |
|-------|---------|--------------|
| MainScreenAppear | 0.676 | No |
| OffersScreenAppear | 0.267 | No |
| CartScreenAppear | 0.218 | No |
| PaymentScreenSuccessful | 0.103 | No |
| Tutorial | 0.918 | No |

**Conclusion:** Groups properly split (no differences)

#### A/B Test (248 vs Control)
All comparisons show p-value > α (no significant differences)

**Final Conclusion:** Font change has no statistically significant impact on user behavior at any funnel stage. The change can be implemented or rejected based on other considerations (aesthetics, brand consistency).
