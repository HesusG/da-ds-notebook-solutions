# Evaluation Criteria: Continuing Basic Python - Music

## Objective
Analyze data from a music streaming service to test hypotheses about musical preferences in different cities (Springfield vs Shelbyville), applying data preprocessing techniques with pandas.

## Project Description
<details>
<summary>Task Statement</summary>

In this project, you will compare the musical preferences of Springfield and Shelbyville residents using data from an online music streaming service.

**Hypothesis to test:**
- User activity differs depending on the day of the week and the city.

**Steps:**
1. **Data overview**: Import pandas, read CSV file, examine data with `head()` and `info()`
2. **Data preprocessing**:
   - Fix header formatting (lowercase, remove spaces)
   - Handle missing values
   - Identify and remove explicit and implicit duplicates
3. **Hypothesis testing**: Compare user behavior in both cities using groupby and filtering
</details>

## Technical Glossary

| Term | Definition |
|------|-----------|
| **DataFrame** | Two-dimensional tabular data structure from pandas |
| **Missing value (NaN)** | Missing data in a DataFrame cell |
| **Explicit duplicate** | Row completely identical to another |
| **Implicit duplicate** | Values that represent the same thing but written differently |
| **groupby** | Method for grouping data by one or more columns |
| **Filtering** | Selection of a data subset based on conditions |
| **Boolean indexing** | Data selection using conditions that return True/False |

## Expected Results - Specific Numbers

### Data Overview
| Metric | Expected Value |
|--------|---------------|
| Total entries | 65,079 rows |
| Columns | 7 (userID, Track, artist, genre, City, time, Day) |
| Data types | All object |

### Missing Values
| Column | Missing Values |
|--------|---------------|
| `track` | 1,343 |
| `artist` | 7,567 |
| `genre` | 1,198 |
| `userID`, `City`, `time`, `Day` | 0 |

### Duplicates
| Type | Count |
|------|-------|
| Explicit duplicates | 3,826 |
| After removal | 0 |
| Unique genres (before) | 269 |
| Unique genres (after removing implicit duplicates) | 266 |

### Hypothesis Result - Songs by City and Day

| City | Monday | Wednesday | Friday | Total |
|------|--------|-----------|--------|-------|
| **Springfield** | 15,740 | 11,056 | 15,945 | 42,741 |
| **Shelbyville** | 5,614 | 7,003 | 5,895 | 18,512 |

**Expected conclusion:** Springfield has more activity than Shelbyville. Similar pattern: more activity at the beginning and end of the week (Monday/Friday), less in the middle (Wednesday).

## Evaluation Rubric - Reviewer Checklist

This project is a guided exercise with specific expected outputs at each step. All criteria are required for approval.

- [ ] **[REQUIRED]** Code runs without errors
- [ ] **[REQUIRED]** Imports pandas and reads the CSV file
- [ ] **[REQUIRED]** Uses `info()` — identifies 65,079 entries and 7 columns
- [ ] **[REQUIRED]** Identifies missing values: track=1343, artist=7567, genre=1198
- [ ] **[REQUIRED]** Identifies 3,826 explicit duplicates
- [ ] **[REQUIRED]** Removes duplicates and confirms 0 remaining
- [ ] **[REQUIRED]** Renames columns to lowercase without spaces
- [ ] **[REQUIRED]** Final columns: `['user_id', 'track', 'artist', 'genre', 'city', 'time', 'day']`
- [ ] **[REQUIRED]** Fills missing values with 'unknown'
- [ ] **[REQUIRED]** Identifies implicit duplicates in `genre`: 'hip', 'hop', 'hip-hop' -> 'hiphop'
- [ ] **[REQUIRED]** Confirms reduction from 269 to 266 unique genres
- [ ] **[REQUIRED]** Uses `groupby()` to count songs by city: Springfield=42741, Shelbyville=18512
- [ ] **[REQUIRED]** Creates `number_tracks(day, city)` function for combined analysis
- [ ] **[REQUIRED]** All 6 correct results for the hypothesis table (Springfield/Shelbyville x Mon/Wed/Fri)
- [ ] **[REQUIRED]** Analyzes results and draws conclusions about the hypothesis

## General Approval Criteria

| Requirement | Details |
|-------------|---------|
| **Approved** | All 15 criteria above met. Each step has a specific expected output — partial completion is not sufficient. |
| **Needs revision** | Any required criterion not met. Student must fix and resubmit. |

## Disqualification Criteria

- [ ] Does not import or use pandas
- [ ] Missing values and duplicates not handled
- [ ] Numerical results very different from expected
- [ ] Does not test the hypothesis (does not group by city and day)
- [ ] Code does not run

## Common Conceptual Errors

### 1. Using `str.replace()` instead of DataFrame `replace()`
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `df['genre'].str.replace('hip', 'hiphop')` | `df['genre'].replace('hip', 'hiphop')` | `str.replace()` does PARTIAL replacement within strings (e.g.: 'hiphop' becomes 'hiphophop') |

**Correct concept:** The pandas `replace()` method substitutes EXACT values. The `str.replace()` method substitutes SUBSTRINGS. For implicit duplicates, use `replace()`.

### 2. Not using `inplace=True` or reassignment
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `df.drop_duplicates()` | `df.drop_duplicates(inplace=True)` or `df = df.drop_duplicates()` | Original DataFrame is not modified |

**Correct concept:** Pandas methods generally return a modified COPY. To change the original: use `inplace=True` or reassign the result.

### 3. Confusing `fillna()` with FutureWarning
| Problematic | Safe | Explanation |
|------------|------|------------|
| `df[col].fillna('unknown', inplace=True)` | `df[col] = df[col].fillna('unknown')` | In modern pandas, `inplace=True` on slices can generate warnings |

### 4. Using `&` without parentheses in multiple conditions
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `df[df['day'] == 'Monday' & df['city'] == 'Springfield']` | `df[(df['day'] == 'Monday') & (df['city'] == 'Springfield')]` | Operator precedence error |

**Correct concept:** The `&` operator has higher precedence than `==`. ALWAYS use parentheses in multiple conditions.

### 5. Confusing count() and len()
| Method | What it does | When to use |
|--------|-------------|------------|
| `df['col'].count()` | Counts NON-null values | When there are missing values |
| `len(df)` | Counts ALL rows | Total rows including NaN |
| `df.shape[0]` | Total number of rows | Alternative to len() |

### 6. Not checking unique values before replacing
| Problem | Solution |
|---------|---------|
| Not knowing which implicit duplicates exist | `df['genre'].sort_values().unique()` to see all values |

**Correct concept:** ALWAYS visualize unique values with `.unique()` or `.value_counts()` before deciding what to replace.

## Project Pitfalls

1. **Headers with internal spaces**: The original column `'  userID'` has spaces AT THE BEGINNING. `strip()` removes spaces from the ends, but doesn't change 'userID' to 'user_id'. It's necessary to use `rename()` separately.

2. **Difference in genre count**:
   - Before: 269 unique genres
   - After: 266 unique genres
   - Removed: 'hip', 'hop', 'hip-hop' -> all became 'hiphop' (3 values -> 1)

3. **Hypothesis interpretation**: The data shows that:
   - Springfield has ~2.3x more activity than Shelbyville
   - Both cities have more activity on Monday/Friday, less on Wednesday
   - The weekly pattern is SIMILAR between cities (not different as the hypothesis suggests)

   **Correct conclusion**: The hypothesis is PARTIALLY true. Activity differs in VOLUME (Springfield > Shelbyville), but the weekly PATTERN is similar.

4. **Case sensitivity in cities**: City names maintain capitalization ('Springfield', 'Shelbyville'). Filters must use exactly these names.
