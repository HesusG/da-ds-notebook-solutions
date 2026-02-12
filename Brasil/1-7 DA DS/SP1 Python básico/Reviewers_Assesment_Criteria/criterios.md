# Evaluation Criteria: Basic Python

## Objective
Evaluate the quality of data collected about customers from an e-commerce store (Store 1), applying basic Python techniques for string manipulation, lists, data types, and control structures.

## Project Description
<details>
<summary>Task Statement</summary>

An e-commerce company, Store 1, recently started collecting data about its customers. Store 1's goal is to better understand customer behavior and make data-driven decisions to improve their online experience.

As part of the analytics team, your first task is to evaluate the quality of a sample of collected data and prepare it for future analysis.

**Tasks:**
1. Fix issues in the `user_name` variable (spaces and underscores)
2. Split `user_name` into first and last name
3. Convert `user_age` to integer
4. Handle conversion errors with try/except
5. Convert categories to lowercase using loops
6. Calculate spending metrics (total, minimum, maximum)
7. Use while loop to simulate loyalty program
8. Create formatted strings with f-strings
9. Calculate total revenue by iterating over nested lists
10. Filter users by age (< 30 years)
11. Filter by age AND spending (< 30 years AND > $1000)
12. Filter by purchased category (clothes)
</details>

## Technical Glossary

| Term | Definition |
|------|-----------|
| **String** | Data type representing text in Python |
| **List** | Ordered, mutable data structure that stores multiple elements |
| **For loop** | Repetition structure that iterates over elements of a sequence |
| **While loop** | Repetition structure that executes while a condition is true |
| **try/except** | Structure for exception and error handling |
| **f-string** | Formatted string that allows inserting variables directly |
| **Method** | Function associated with a specific data type |
| **Indexing** | Accessing elements of a sequence by position |

## Expected Results by Task

| Task | Expected Result | Verification |
|------|----------------|-------------|
| **Quiz** | Identified problems: 2, 3, 4 (user_name, user_age, fav_categories) | Option 1 is NOT a problem (user_id can be a string) |
| **Task 1** | `user_name = 'mike reed'` | No extra spaces, underscore replaced |
| **Task 2** | `name_split = ['mike', 'reed']` | List with 2 elements |
| **Task 3** | `user_age = 32` (type int) | Not 32.0 (float) |
| **Task 4** | Message: `'Please provide your age as a numerical value.'` | try/except works |
| **Task 5** | `['electronics', 'sport', 'books']` | All lowercase |
| **Task 6** | `total=1280`, `max=894`, `min=173` | Exact values |
| **Task 7** | `total >= 1500` (e.g.: 1507, varies by random) | Loop stops when reaching 1500 |
| **Task 8** | `'User 32415 is named mike and is 32 years old.'` | Exact string |
| **Task 9** | `revenue = 2109` | Sum: (894+213+173) + (439+390) |
| **Task 10** | 5 names: kate, samantha, emily, jose, james | Users with age < 30 |
| **Task 11** | 2 names: samantha, james | Age < 30 AND spending > 1000 |
| **Task 12** | kate 24, samantha 29, maria 33, lisa 35, james 28 | Purchased 'clothes' |

## Evaluation Rubric - Reviewer Checklist

This project is a guided exercise where each task asks for a specific output. All tasks are required for approval.

- [ ] **[REQUIRED]** Code runs without errors
- [ ] **[REQUIRED]** Quiz: Correctly identifies problems 2, 3, 4 (not 1 — user_id as string is valid)
- [ ] **[REQUIRED]** Task 1: `user_name` results in `'mike reed'`
- [ ] **[REQUIRED]** Task 2: `name_split` results in `['mike', 'reed']`
- [ ] **[REQUIRED]** Task 3: `user_age` is 32 (int, not float)
- [ ] **[REQUIRED]** Task 4: try/except handles non-numeric age input
- [ ] **[REQUIRED]** Task 5: List contains `['electronics', 'sport', 'books']`
- [ ] **[REQUIRED]** Task 6: total=1280, max=894, min=173
- [ ] **[REQUIRED]** Task 7: While loop accumulates spending until >= 1500
- [ ] **[REQUIRED]** Task 8: f-string outputs `'User 32415 is named mike and is 32 years old.'`
- [ ] **[REQUIRED]** Task 9: revenue = 2109
- [ ] **[REQUIRED]** Task 10: Identifies 5 users with age < 30 (kate, samantha, emily, jose, james)
- [ ] **[REQUIRED]** Task 11: Identifies 2 users with age < 30 AND spending > 1000 (samantha, james)
- [ ] **[REQUIRED]** Task 12: Lists 5 users who purchased 'clothes' with their ages

## General Approval Criteria

| Requirement | Details |
|-------------|---------|
| **Approved** | All 14 criteria above met. Each task has a specific expected output — partial completion is not sufficient. |
| **Needs revision** | Any required criterion not met. Student must fix and resubmit. |

## Disqualification Criteria

- [ ] Code does not run (uncorrected syntax errors)
- [ ] Does not complete at least 8 of the 12 tasks
- [ ] Numerical results completely incorrect (e.g.: revenue != 2109)
- [ ] Direct code copy without demonstrated understanding
- [ ] Use of external libraries not allowed (project is basic Python only)

## Common Conceptual Errors

### 1. Confusion about string immutability
| Error | Explanation | Consequence |
|-------|------------|------------|
| `user_name.strip()` without assignment | Strings are immutable; methods return a NEW string | Original variable doesn't change |

**Correct concept:** In Python, strings are immutable. Methods like `strip()`, `replace()`, `lower()` do NOT modify the original string - they return a NEW string. That's why reassignment is needed: `user_name = user_name.strip()`.

### 2. Confusion between list indices
| Error | Explanation | Correct index |
|-------|------------|--------------|
| `user[1]` for age | List: [id, name, AGE, categories, spending] | `user[2]` |
| `user[3]` for spending | Spending is at index 4 or use -1 | `user[-1]` or `user[4]` |

**Correct concept:** Indices start at 0. For list `[a, b, c, d, e]`, indices are 0, 1, 2, 3, 4. Index -1 always accesses the LAST element.

### 3. Overwriting list instead of appending
| Incorrect | Correct | Incorrect result |
|-----------|---------|-----------------|
| `fav_categories_low = cat.lower()` | `fav_categories_low.append(cat.lower())` | Only last item |

**Correct concept:** To build a list iteratively, use `append()` to ADD each element. Using `=` REPLACES all content.

### 4. Confusion about `in` operator with lists
| Context | Correct usage | Checks |
|---------|--------------|--------|
| `'clothes' in user[3]` | Checks if 'clothes' is IN THE LIST | Exact membership |
| `'cloth' in 'clothes'` | Checks if substring is IN THE STRING | Substring |

**Correct concept:** The `in` operator works differently for strings (checks substring) and lists (checks exact element membership).

### 5. Quiz - Why is user_id NOT a problem?
| Misconception | Reality |
|--------------|---------|
| "IDs must be integers" | IDs can be strings - they are identifiers, not numbers for calculations |
| "Strings use more memory" | For IDs, the difference is negligible and strings avoid issues with leading zeros |

**Correct concept:** The type of `user_id` depends on usage. If we don't perform mathematical operations on it, string is perfectly acceptable and even preferable (preserves leading zeros, e.g.: '00123').

### 6. Confusion about numeric types
| Value | Type | When to use |
|-------|------|------------|
| `32.0` | float | When we need decimals |
| `32` | int | Age, counts (whole numbers) |

**Correct concept:** Age should be int because it's always a whole number. Using float (32.0) uses more memory and can cause issues in comparisons.

## Project Pitfalls

1. **Task 7 - Variable result**: The result changes with each execution due to `randint()`. Only verify if >= 1500, not the exact value.

2. **Task 11 - Order of conditions**: Some solutions use `and`, others use nested if. Both are correct:
   ```python
   # Version 1 - nested if
   if total > 1000:
       if age < 30:
           print(name)

   # Version 2 - and operator
   if total > 1000 and age < 30:
       print(name)
   ```

3. **Task 12 - Print name AND age**: The task asks to print BOTH on the same line. Check if `print(user[1][0], user[2])` or equivalent f-string was used.
