# %% [markdown]
# Rusty Bargain used car sales service is developing an app to attract new customers. In that app, you can quickly find out the market value of your car. You have access to historical data: technical specifications, trim versions, and prices. You need to build the model to determine the value. 
# 
# Rusty Bargain is interested in:
# 
# - the quality of the prediction;
# - the speed of the prediction;
# - the time required for training

# %%
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# %% [markdown]
# # 1. Data preparation

# %% [markdown]
# ### Downloading

# %%
data = pd.read_csv('autos.csv')
print(data.shape)
data.head()

# %% [markdown]
# ### Preprocessing

# %% [markdown]
# Unnecessary features (can't be used in the product):
# 
# - dates
# - zip-code

# %%
data = data.drop(['DateCrawled', 'DateCreated', 'PostalCode', 'LastSeen'], axis=1)
data.head()

# %%
data['NumberOfPictures'].value_counts()

# %% [markdown]
# Deleting constant feature

# %%
data = data.drop(['NumberOfPictures'], axis=1)
data.head()

# %%
data.describe()

# %% [markdown]
# The registration year of 1000 and 9999 is clearly incorrect, delete entries with incorrect values.
# 
# Power cannot be equal to 0.

# %%
data = data[data['RegistrationYear'] < 2050]
data = data[data['RegistrationYear'] > 1900]
data = data[data['Power'] != 0]

data.reset_index()
data.shape

# %%
data.isna().sum(axis=0)

# %% [markdown]
# Missing values are only in categorical columns. They can be filled with a new value "unknown".

# %%
data = data.fillna('unknown')
data.isna().sum(axis=0)

# %% [markdown]
# ### Feature encoding

# %%
categorical_features = [
    'VehicleType',
    'Gearbox', 
    'Model',
    'FuelType', 
    'Brand',
    'NotRepaired', 
]

# %% [markdown]
# **OHE-encoding**
# 
# Here, some features will have to be removed due to the large number of values

# %%
for feature in categorical_features:
    print(data[feature].value_counts())

# %%
data_ohe = data.drop(['Model', 'Brand'], axis=1)
data_ohe = pd.get_dummies(data_ohe)
print(data_ohe.shape)
data_ohe.head()

# %% [markdown]
# Ordinal encoding

# %%
from sklearn.preprocessing import OrdinalEncoder

data[categorical_features] = OrdinalEncoder().fit_transform(data[categorical_features])

data.head()

# %% [markdown]
# ### Split into train-validation-test

# %%
from sklearn.model_selection import train_test_split

index_train_valid, index_test = train_test_split(data.index, test_size=0.2, random_state=12345)
index_train, index_valid = train_test_split(index_train_valid, test_size=0.25, random_state=54321)

data_train = data.loc[index_train]
data_valid = data.loc[index_valid]
data_test = data.loc[index_test]

data_ohe_train = data_ohe.loc[index_train]
data_ohe_valid = data_ohe.loc[index_valid]
data_ohe_test = data_ohe.loc[index_test]

print(data_train.shape)
print(data_valid.shape)
print(data_test.shape)

print(data_ohe_train.shape)
print(data_ohe_valid.shape)
print(data_ohe_test.shape)

# %% [markdown]
# # 2. Model training

# %%
from sklearn.metrics import mean_squared_error

def rmse(y, a):
    return mean_squared_error(y, a)**0.5

# %% [markdown]
# Constant model

# %%
pred_mean = np.ones(data['Price'].shape) * data['Price'].mean()
print(rmse(data['Price'], pred_mean))

# %% [markdown]
# ### Models with OHE

# %%
features_train = data_ohe_train.drop(['Price'], axis=1)
target_train = data_ohe_train['Price']
features_valid = data_ohe_valid.drop(['Price'], axis=1)
target_valid = data_ohe_valid['Price']
features_test = data_ohe_test.drop(['Price'], axis=1)
target_test = data_ohe_test['Price']

# %% [markdown]
# **Linear regression**

# %%
%%time

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(features_train, target_train)

# %%
%%time

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)
pred_test = model.predict(features_test)

# %%
print("Train RMSE:", rmse(target_train, pred_train).round(5))
print("Valid RMSE:", rmse(target_valid, pred_valid).round(5))
print("Test RMSE: ", rmse(target_test, pred_test).round(5))

# %% [markdown]
# ### Models with ordinal encoding

# %%
features_train = data_train.drop(['Price'], axis=1)
target_train = data_train['Price']
features_valid = data_valid.drop(['Price'], axis=1)
target_valid = data_valid['Price']
features_test = data_test.drop(['Price'], axis=1)
target_test = data_test['Price']

# %% [markdown]
# **Random forrest**

# %%
from sklearn.ensemble import RandomForestRegressor

for depth in [1, 2, 4, 6, 8, None]:
    model = RandomForestRegressor(max_depth=depth, n_estimators=100)
    model.fit(features_train, target_train)
    
    pred_train = model.predict(features_train)
    pred_valid = model.predict(features_valid)
    print("Depth:", depth)
    print("Train RMSE:", rmse(target_train, pred_train).round(5))
    print("Valid RMSE:", rmse(target_valid, pred_valid).round(5))

# %%
%%time

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, max_depth=None)
model.fit(features_train, target_train)

# %%
%%time

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)
pred_test = model.predict(features_test)

# %%
print("Train RMSE:", rmse(target_train, pred_train).round(5))
print("Valid RMSE:", rmse(target_valid, pred_valid).round(5))
print("Test RMSE: ", rmse(target_test, pred_test).round(5))

# %% [markdown]
# **Gradient boosting LightGBM**

# %%
%%time

import lightgbm as lgb

model = lgb.LGBMRegressor(num_iterations=1000, vebose=1, metric='rmse')
model.fit(features_train, target_train, 
          eval_set=(features_valid, target_valid),
          categorical_feature=categorical_features)

# %%
%%time

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)
pred_test = model.predict(features_test)

# %%
print("Train RMSE:", rmse(target_train, pred_train).round(5))
print("Valid RMSE:", rmse(target_valid, pred_valid).round(5))
print("Test RMSE: ", rmse(target_test, pred_test).round(5))

# %%
%%time

import lightgbm as lgb

model = lgb.LGBMRegressor(num_iterations=1000, vebose=1, metric='rmse')
model.fit(features_train, target_train, 
          eval_set=(features_valid, target_valid))

# %%
%%time

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)
pred_test = model.predict(features_test)

# %%
print("Train RMSE:", rmse(target_train, pred_train).round(5))
print("Valid RMSE:", rmse(target_valid, pred_valid).round(5))
print("Test RMSE: ", rmse(target_test, pred_test).round(5))

# %% [markdown]
# **Gradient boosting CatBoost**

# %%
%%time

from catboost import CatBoostRegressor

model = CatBoostRegressor(iterations=1000,
                          learning_rate=0.1,
                          cat_features=categorical_features,
                          metric_period=50)
model.fit(features_train, target_train, 
          eval_set=(features_valid, target_valid))

# %%
%%time

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)
pred_test = model.predict(features_test)

# %%
print("Train RMSE:", rmse(target_train, pred_train).round(5))
print("Valid RMSE:", rmse(target_valid, pred_valid).round(5))
print("Test RMSE: ", rmse(target_test, pred_test).round(5))

# %%
%%time

from catboost import CatBoostRegressor

model = CatBoostRegressor(iterations=1000,
                          learning_rate=0.1,
                          metric_period=50)
model.fit(features_train, target_train, 
          eval_set=(features_valid, target_valid))

# %%
%%time

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)
pred_test = model.predict(features_test)

# %%
print("Train RMSE:", rmse(target_train, pred_train).round(5))
print("Valid RMSE:", rmse(target_valid, pred_valid).round(5))
print("Test RMSE: ", rmse(target_test, pred_test).round(5))

# %% [markdown]
# # 3. Model analysis

# %% [markdown]
# | Model | RMSE | Prediction time, с | Training time, with |
# |----|----|-------|--------|
# | Линейная регрессия | 3220 | 0.156 | 0.4 |
# | LightGBM(1000) | 1640 | 8.47 | 12.9 |
# | CatBoost(1000) | 1730 | 0.899 | 27.2 |
# 
# 
# - The fastest (in training and prediction) model is linear regression. But the quality is low
# - The model with the best quality is gradient boosting LightGBM with 1000 trees.
# - The model with balanced prediction speed and quality is gradient boosting CatBoost with 1000 trees without category processing

# %%



