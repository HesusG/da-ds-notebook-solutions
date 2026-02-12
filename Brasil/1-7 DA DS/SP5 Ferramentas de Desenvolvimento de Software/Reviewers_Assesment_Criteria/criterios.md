# Evaluation Criteria: Software Development Tools

## Objective
Develop an interactive web application using Streamlit for car advertisement data visualization, demonstrating skills in software development tools.

## Project Description
<details>
<summary>Task Statement</summary>

Create a web application that:
1. Loads and displays car advertisement data
2. Implements interactive visualizations with Plotly Express
3. Includes user controls (checkboxes, sliders)
4. Is deployable on a cloud platform (e.g.: Render)
</details>

## Expected Results - Specific Numbers

### Dataset: vehicles_us.csv

| Metric | Value |
|--------|-------|
| Total rows | 51,525 |
| Total columns | 13 |

### Columns and Missing Values

| Column | Type | Missing |
|--------|------|---------|
| price | int64 | 0 |
| model_year | float64 | 3,619 |
| model | object | 0 |
| condition | object | 0 |
| cylinders | float64 | 5,260 |
| fuel | object | 0 |
| odometer | float64 | 7,892 |
| transmission | object | 0 |
| type | object | 0 |
| paint_color | object | 9,267 |
| is_4wd | float64 | 25,953 |
| date_posted | object | 0 |
| days_listed | int64 | 0 |

### Descriptive Statistics

| Metric | price | model_year | odometer | days_listed |
|--------|-------|------------|----------|-------------|
| Mean | 12,132 | 2009.75 | 115,553 | 39.55 |
| Std | 10,041 | 6.28 | 65,095 | 28.20 |
| Min | 1 | 1908 | 0 | 0 |
| Max | 375,000 | 2019 | 990,000 | 271 |

## Evaluation Rubric - Reviewer Checklist

### BASIC

- [ ] **[REQUIRED]** EDA notebook present with exploratory analysis
- [ ] **[REQUIRED]** Functional app.py file with Streamlit
- [ ] **[REQUIRED]** Loads CSV data correctly
- [ ] **[REQUIRED]** Implements at least 1 checkbox or button
- [ ] **[REQUIRED]** Creates at least 1 chart with Plotly Express
- [ ] **[REQUIRED]** requirements.txt file present
- [ ] **[REQUIRED]** Code without syntax errors

### INTERMEDIATE

- [ ] Implements multiple visualization types (histogram + scatter)
- [ ] Uses sliders to filter data interactively
- [ ] Charts respond to user selections
- [ ] Organized interface with st.header() and st.write()
- [ ] EDA notebook includes info() and describe()
- [ ] Well-structured and readable code

### ADVANCED

- [ ] Application deployed on a cloud platform
- [ ] Combined filters (multiple sliders/checkboxes)
- [ ] Visualizations with colors by category
- [ ] NaN values handled before creating charts
- [ ] README with usage instructions
- [ ] Commented code

## General Approval Criteria

| Level | Requirements |
|-------|------------|
| **Basic** | All BASIC criteria met |
| **Intermediate** | Basic + at least 4 INTERMEDIATE criteria |
| **Advanced** | Intermediate + functional deployment + at least 2 ADVANCED criteria |

## Compliance Examples

### Basic Streamlit structure:
```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Read data
car_data = pd.read_csv('vehicles_us.csv')

# Header
st.header('Car Advertisement Analysis')
```

### Checkbox for control:
```python
hist_check = st.checkbox('Show histogram')

if hist_check:
    st.write('Histogram: Odometer Distribution')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
```

### Slider to filter data:
```python
# Handle NaN before defining min/max
car_data_clean = car_data.dropna(subset=['odometer'])
min_odo = int(car_data_clean['odometer'].min())
max_odo = int(car_data_clean['odometer'].max())

odometer_range = st.slider(
    "Select odometer range:",
    min_value=min_odo,
    max_value=max_odo,
    value=(min_odo, max_odo)
)
```

### Requirements.txt:
```
pandas==1.5.3
streamlit==1.22.0
plotly==5.14.1
```

## Disqualification Criteria

- [ ] Application does not run (critical errors)
- [ ] No interactive visualization exists
- [ ] Data is not loaded or displayed
- [ ] requirements.txt file missing or incomplete
- [ ] Code copied without understanding

## Common Conceptual Errors

### 1. Not handling NaN before creating controls
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `int(df['col'].min())` with NaN | `df['col'].dropna().min()` | Error or incorrect value |

**Correct concept:** Columns with NaN (model_year, cylinders, odometer, paint_color, is_4wd) must be handled before using in sliders.

### 2. Slider with equal values
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `value=(max, max)` | `value=(min, max)` | Slider doesn't work |

### 3. Not using use_container_width
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| `st.plotly_chart(fig)` | `st.plotly_chart(fig, use_container_width=True)` | Poorly sized chart |

### 4. Forgetting to filter data
| Incorrect | Correct | Reason |
|-----------|---------|--------|
| Chart ignores slider | `filtered_data = car_data[car_data['odometer'].between(min, max)]` | Interface is not interactive |

### 5. Not checking if data exists
| Incorrect | Correct | Consequence |
|-----------|---------|------------|
| Create chart directly | `if len(filtered_data) > 0:` | Error when filter returns empty |

### 6. Incompatible versions in requirements.txt
| Problem | Solution |
|---------|---------|
| Deployment fails | Test versions locally before deploying |

## Project Pitfalls

1. **Many NaN values**: The columns model_year, cylinders, odometer, paint_color, and is_4wd have many missing values. The slider should use `.dropna()` before calculating min/max.

2. **is_4wd is binary but float**: The is_4wd column is 1.0 when it's 4WD, NaN when it's not. Treat as a boolean category.

3. **Extreme prices**: Prices range from $1 to $375,000. Consider filtering outliers for clearer visualizations.

4. **model_year starts at 1908**: There are very old vehicles. It may be interesting to filter relevant years (e.g.: > 2000).

5. **Deployment requires correct requirements.txt**: Without requirements.txt or with wrong versions, deployment will fail.
