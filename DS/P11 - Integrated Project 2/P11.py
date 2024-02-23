# %% [markdown]
# # Project description
# 
# Prepare a prototype of a machine learning model for Zyfra. The company develops efficiency solutions for heavy industry.
# 
# The model should predict the amount of gold recovered from gold ore. You have the data on extraction and purification.. 
# 
# The model will help to optimize the production and eliminate unprofitable parameters.
# 
# You need to:
# 
# 1. Prepare the data;
# 2. Perform data analysis;
# 3. Develop and train a model.
# 
# To complete the project, you may want to use documentation from *pandas*, *matplotlib*, and *sklearn.*

# %%
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# # 1. Data preparation

# %% [markdown]
# ### Downloading

# %%
df_train = pd.read_csv('gold_recovery_train.csv', index_col='date', parse_dates=True)
df_test = pd.read_csv('gold_recovery_test.csv', index_col='date', parse_dates=True)

df_train.shape, df_test.shape

# %%
df_train.head()

# %%
df_full = pd.read_csv('gold_recovery_full.csv', parse_dates=True, index_col='date')

# %% [markdown]
# ### Calculation validity check

# %%
# Check the formula: whether the calculation result matches the provided data.

def recovery_calc(row):
    numerator = row['rougher.output.concentrate_au']*(row['rougher.input.feed_au']-row['rougher.output.tail_au'])
    denominator = row['rougher.input.feed_au']*(row['rougher.output.concentrate_au']-row['rougher.output.tail_au'])
    return numerator/denominator*100

df_formula = df_train.copy()
df_formula['formula'] = df_formula.apply(lambda x: recovery_calc(x), axis=1)

answer = (df_formula['formula'] - df_formula['rougher.output.recovery']).abs().mean()

print('Difference between the expected value and measured value is {}'.format(answer))

# %% [markdown]
# Therefore, the formula is correct, which is supported by the available data.

# %% [markdown]
# ### Preprocessing (missing values)

# %%
df_full.isnull().mean().sort_values(ascending=False).head(10)

# %% [markdown]
# The missing values are few with no missing values in targets. Fill them with previous values.

# %%
df_train = df_train.fillna(method='ffill')
df_test = df_test.fillna(method='ffill')

# %% [markdown]
# ### List of unavailable parameters

# %%
missed_test_columns = set(list(df_train.columns.values))-set(list(df_test.columns.values))
missed_test_columns

# %% [markdown]
# Some calculation and output process characteristics are unavailable in the test set. These parameters are unavailable in the test set because they are impossible to obtain/measure during the technological process.

# %% [markdown]
# # 2. Data analysis

# %% [markdown]
# ### Concentration changes

# %%
steps_template = [
    'rougher.input.feed_{}',
    'rougher.output.concentrate_{}',
    'primary_cleaner.output.concentrate_{}',
    'final.output.concentrate_{}',
]

def plot_concentrate_progress(component):
    steps = [s.format(component) for s in steps_template]
    for step in steps:
        df_full[step].hist(alpha=0.5, bins=20)
    plt.legend(steps)

# %%
plot_concentrate_progress('au')
plt.title('Gold concentration change')

# %%
plot_concentrate_progress('ag')
plt.title('Silver concentration change')

# %%
plot_concentrate_progress('pb')
plt.title('Lead concentration change')

# %% [markdown]
# It is obvious that as the process progresses, the proportion of gold `Au` in the concentrate increases significantly, the proportion of silver `Ag` decreases (mainly during the second purification), and the proportion of lead `Pb` increases (mainly during flotation).

# %% [markdown]
# ### Particle size comparison for train and test

# %%
def filter_outliers(series):
    return series[series.between(series.quantile(0.01), series.quantile(0.99))]

def compare_train_test_feature(feature):
    filter_outliers(df_train[feature]).plot.kde()
    filter_outliers(df_test[feature]).plot.kde()
    plt.legend(['train', 'test'])

# %%
compare_train_test_feature('rougher.input.feed_size')

# %% [markdown]
# It is obvious that at the start of the process, the particle size is intended to be kept at 55-60 microns. There is a slight shift from the normal distribution towards larger particle size. Also for the test set, there is a greater significance of very small particles. Visually, there is now significant difference between train and test.

# %% [markdown]
# ### Total amount of substance

# %%
features_input_concentrate = [
    'rougher.input.feed_au',
    'rougher.input.feed_ag',
    'rougher.input.feed_pb',
    'rougher.input.feed_sol',
]

df_full[features_input_concentrate].sum(1).hist(bins=20)

# %%
features_rough_concentrate = [
    'rougher.output.concentrate_au',
    'rougher.output.concentrate_ag',
    'rougher.output.concentrate_pb',
    'rougher.output.concentrate_sol',
]

df_full[features_rough_concentrate].sum(1).hist(bins=20)

# %%
features_final_concentrate = [
    'final.output.concentrate_au',
    'final.output.concentrate_ag',
    'final.output.concentrate_pb',
    'final.output.concentrate_sol',
]

df_full[features_final_concentrate].sum(1).hist(bins=20)

# %% [markdown]
# There are a significant number of observations close or equal to zero. Most likely this is due to the failure of the measuring equipment. Such observations must be removed from the data.
# 
# The model will be used to select equipment parameters, so the failure examples are not interesting for modeling. They need to be removed not only from the training set, but also from the test set.

# %%
THRESHOLD = 0.01

df_train = df_train[df_train[features_input_concentrate].sum(1) > THRESHOLD]
df_train = df_train[df_train[features_rough_concentrate].sum(1) > THRESHOLD]
df_train = df_train[df_train[features_final_concentrate].sum(1) > THRESHOLD]

print(df_train.shape)

df_full_test = df_full.loc[df_test.index]
df_test = df_test[df_full_test[features_input_concentrate].sum(1) > THRESHOLD]
df_test = df_test[df_full_test[features_rough_concentrate].sum(1) > THRESHOLD]
df_test = df_test[df_full_test[features_final_concentrate].sum(1) > THRESHOLD]

print(df_test.shape)

# %% [markdown]
# The sample sizes have not reduced greatly. Can proceed to modeling.

# %% [markdown]
# # 3. Model

# %% [markdown]
# ### Sample forming

# %%
features = df_test.columns.values

# %%
targets = ['rougher.output.recovery', 'final.output.recovery']

# %%
features_train = df_train[features].reset_index(drop=True)
target_train = df_train[targets].reset_index(drop=True)
target_train.columns = [0, 1]

# %%
target_train.head()

# %%
features_test = df_test[features].reset_index(drop=True)
target_test = df_full[targets].loc[df_test.index].reset_index(drop=True)
target_test.columns = [0, 1]

# %% [markdown]
# ### Расчёт sMAPE

# %%
def smape(y_true, y_pred):
    error = (y_true - y_pred).abs()
    scale = (y_true.abs() + y_pred.abs()) / 2
    
    return (error / scale).mean()


def smape_weighted(y_true, y_pred):
    rougher = smape(y_true[0], y_pred[0])
    final = smape(y_true[1], y_pred[1])
    return 0.25 * rougher + 0.75 * final

# %%
pred_median = target_train.copy()
pred_median[0] = target_train[0].median()
pred_median[1] = target_train[1].median()
print(smape_weighted(target_train, pred_median))

pred_median = target_test.copy()
pred_median[0] = target_train[0].median()
pred_median[1] = target_train[1].median()
print(smape_weighted(target_test, pred_median))

# %% [markdown]
# ### Training and validation of models

# %%
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold

def score_model(model, cv=4):
    scores = []
    for subtrain_index, valid_index in KFold(n_splits=cv).split(features_train):
        features_subtrain = features_train.loc[subtrain_index].reset_index(drop=True)
        target_subtrain = target_train.loc[subtrain_index].reset_index(drop=True)
        features_valid = features_train.loc[valid_index].reset_index(drop=True)
        target_valid = target_train.loc[valid_index].reset_index(drop=True)
        
        model.fit(features_subtrain, target_subtrain)
        pred_valid = pd.DataFrame(model.predict(features_valid))
        
        scores.append(smape_weighted(target_valid, pred_valid))
        
    return pd.Series(scores).mean()

# %%
model = LinearRegression()
lr_score = score_model(model)
print("LR:", lr_score)

# %%
%%time

for depth in range(1, 5):
    model = RandomForestRegressor(max_depth=depth, n_estimators=50, random_state=12345)
    score = score_model(model)
    print("RF, depth =", depth, "score =", score)

# %% [markdown]
# ### Model testing using the test sample

# %%
%%time

model = RandomForestRegressor(max_depth=4, n_estimators=50, random_state=12345)
model.fit(features_train, target_train)

pred = pd.DataFrame(model.predict(features_train))
print("train:", smape_weighted(target_train, pred))

pred = pd.DataFrame(model.predict(features_test))
print("test:", smape_weighted(target_test, pred))

# %%



