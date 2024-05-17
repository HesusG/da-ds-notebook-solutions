# %% [markdown]
# # Project description
# 
# Sweet Lift Taxi company has collected historical data on taxi orders at airports. To attract more drivers during peak hours, we need to predict the amount of taxi orders for the next hour. Build a model for such a prediction.
# 
# The RMSE metric on the test set should not be more than 48.
# 
# ### Project instructions
# 
# 1. Download the data and resample it by one hour.
# 2. Analyze the data.
# 3. Train different models with different hyperparameters. The test sample should be 10% of the initial dataset. 
# 4. Test the data using the test sample and provide a conclusion.
# 
# ### Data description
# 
# The data is stored in the `taxi.csv` file. The number of orders is in the '*num_orders*' column.

# %%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

# %% [markdown]
# # 1. Data preparation

# %%
data = pd.read_csv('datasets/taxi.csv', parse_dates=[0], index_col=[0])
print(data.shape)
data.head()
data_raw = data
# %%
data.plot()

# %%
data = data.resample('1H').sum()

# %%
data.plot()

# %%
print(data.shape)

# %% [markdown]
# # 2. Analysis

# %%
from statsmodels.tsa.seasonal import seasonal_decompose

# %%
decomposed = seasonal_decompose(data)

plt.figure(figsize=(6, 8))
plt.subplot(311)
decomposed.trend.plot(ax=plt.gca())
plt.title('Trend')
plt.subplot(312)
decomposed.seasonal.plot(ax=plt.gca())
plt.title('Seasonality')
plt.subplot(313)
decomposed.resid.plot(ax=plt.gca())
plt.title('Residuals')
plt.tight_layout()
plt.show() 
# %%
plt.figure(figsize=(6, 8))
plt.subplot(311)
decomposed.trend.plot(ax=plt.gca())
plt.title('Trend')
plt.subplot(312)
decomposed.seasonal['1 March 2018'].plot(ax=plt.gca())
plt.title('Seasonality')
plt.subplot(313)
decomposed.resid.plot(ax=plt.gca())
plt.title('Residuals')
plt.tight_layout()
plt.show() 

# %% [markdown]
# **Findings:** There is an obvious six-month trend of increasing number of orders. Also one-day seasonality can be observed: at around 6 a.m. the number of orders is minimal due to small number of flights in the morning. The maximum is observed around midnight (a lot of arriving flights, other modes of transportation are unavailable).

# %% [markdown]
# # 3. Training

# %%
def make_features(data, max_lag=4, rolling_mean_size=10):
    data['month'] = data.index.month
    data['day'] = data.index.day
    data['dayofweek_num'] = data.index.dayofweek
    data['hour'] = data.index.hour

    for lag in range(1, max_lag + 1):
        data['lag_{}'.format(lag)] = data['num_orders'].shift(lag)
        
    data['rolling_mean'] = data['num_orders'].shift().rolling(rolling_mean_size).mean()


make_features(data)
data = data.dropna()
print(data.shape)
data.head()

# %%
from sklearn.model_selection import train_test_split

train_valid, test = train_test_split(data, shuffle=False, test_size=0.1)
train, valid = train_test_split(train_valid, shuffle=False, test_size=0.1)

print(train.index.min(), train.index.max())
print(train.shape)
print(valid.index.min(), valid.index.max())
print(valid.shape)
print(test.index.min(), test.index.max())
print(test.shape)

# %%
features_train = train.drop(['num_orders'], axis=1)
target_train = train['num_orders']
features_valid = valid.drop(['num_orders'], axis=1)
target_valid = valid['num_orders']
features_test = test.drop(['num_orders'], axis=1)
target_test = test['num_orders']

# %%
from sklearn.metrics import mean_squared_error

def rmse(true, pred):
    return mean_squared_error(true, pred)**0.5


print('Mean value:', test['num_orders'].mean())
pred_previous = test.shift()
pred_previous.iloc[0] = train.iloc[-1]
print('RMSE prev:', rmse(test['num_orders'], pred_previous['num_orders']))
pred_mean = np.ones(test['num_orders'].shape) * train['num_orders'].mean()
print('RMSE mean:', rmse(test['num_orders'], pred_mean))

# %%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(features_train, target_train)

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)

print("RMSE train:", rmse(target_train, pred_train))
print("RMSE valid:", rmse(target_valid, pred_valid))

# %%

from sklearn.ensemble import RandomForestRegressor

for max_depth in [2, 4, 6, 8, 10, 12, None]:
    model = RandomForestRegressor(n_estimators=500, max_depth=max_depth)
    model.fit(features_train, target_train)

    pred_train = model.predict(features_train)
    pred_valid = model.predict(features_valid)

    print('max_depth =', max_depth)
    print("RMSE train:", rmse(target_train, pred_train))
    print("RMSE valid:", rmse(target_valid, pred_valid))
    print()

# %%

from lightgbm import LGBMRegressor

model = LGBMRegressor(learning_rate=0.02, num_iterations=2000, objective='rmse')
model.fit(features_train, target_train, 
          eval_set=(features_valid, target_valid))

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)

print("RMSE train:", rmse(target_train, pred_train))
print("RMSE valid:", rmse(target_valid, pred_valid))

# %%

from catboost import CatBoostRegressor

model = CatBoostRegressor(iterations=2000,
                          learning_rate=0.02,
                          metric_period=100,
                          loss_function='RMSE')

model.fit(features_train, target_train, 
          eval_set=(features_valid, target_valid))

pred_train = model.predict(features_train)
pred_valid = model.predict(features_valid)

print("RMSE train:", rmse(target_train, pred_train))
print("RMSE valid:", rmse(target_valid, pred_valid))

# %% [markdown]
# # 4. Testing

# %%
features_train_valid = train_valid.drop(['num_orders'], axis=1)
target_train_valid = train_valid['num_orders']

# %%
model = LinearRegression()

model.fit(features_train_valid, target_train_valid)

pred_train = model.predict(features_train_valid)
print("RMSE train:", rmse(target_train_valid, pred_train))

pred_test = model.predict(features_test)
print("RMSE test:", rmse(target_test, pred_test))

# %%
model = RandomForestRegressor(n_estimators=500)

model.fit(features_train_valid, target_train_valid)

pred_train = model.predict(features_train_valid)
print("RMSE train:", rmse(target_train_valid, pred_train))

pred_test = model.predict(features_test)
print("RMSE test:", rmse(target_test, pred_test))

# %%
model = CatBoostRegressor(iterations=2000,
                          learning_rate=0.02,
                          loss_function='RMSE',
                          verbose=False)

model.fit(features_train_valid, target_train_valid)

pred_train = model.predict(features_train_valid)
print("RMSE train:", rmse(target_train_valid, pred_train))

pred_test = model.predict(features_test)
print("RMSE test:", rmse(target_test, pred_test))

# %% [markdown]
# **Findings:**
# 
# 1) The quality between train and test doesn't differ significantly
# 
# 2) Random forrest works the best

# %%


plt.show()
