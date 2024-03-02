# %% [markdown]
# # Отток клиентов

# %% [markdown]
# Beta Bank customers are leaving: little by little, chipping away every month. The bankers figured out it’s cheaper to save the existing customers than to attract new ones.
# 
# We need to predict whether the customer will leave the bank soon. You have the data on clients’ past behavior and termination of contracts with the bank. 
# 
# Build a model with the maximum possible *F1* score. To pass the project, you need an *F1* score of at least 0.59. Check the *F1* for the test set.
# 
# Additionally, measure the *AUC-ROC* metric and compare it with the *F1*.
# 
# Data source: [https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)

# %% [markdown]
# # 1. Data preparation

# %% [markdown]
# ### Data research

# %%
import pandas as pd
pd.set_option('display.max_columns', None)

data = pd.read_csv('datasets/Churn.csv')

data.head()

# %%
data.dtypes

# %%
data.info()

# %%
types = pd.DataFrame(data.dtypes)
list(types[types[0] == 'object'].index)

# %%
var_non_informative = ['RowNumber', 'CustomerId', 'Surname']
var_numeric = ['CreditScore', 'Age', 'Tenure', 'Balance', 
               'NumOfProducts', 'HasCrCard', 'IsActiveMember', 
               'EstimatedSalary']
var_categorical = ['Geography', 'Gender']

# %% [markdown]
# ### Removing abundant features

# %%
data = data.drop(var_non_informative, axis=1) 

# %% [markdown]
# ### Encoding categorical features

# %%
data = pd.get_dummies(data, drop_first=True, columns=var_categorical)

# %% [markdown]
# ### Filling in the missing values

# %%
data['Tenure'] = data['Tenure'].fillna(value=data['Tenure'].median())

# %% [markdown]
# ### Splitting into samples

# %%
from sklearn.model_selection import train_test_split

train_valid, test = train_test_split(data, test_size=0.2)
train, valid = train_test_split(train_valid, test_size=0.25)

features_train = train.drop(['Exited'], axis=1)
target_train = train['Exited']
features_valid = valid.drop(['Exited'], axis=1)
target_valid = valid['Exited']
features_test = test.drop(['Exited'], axis=1)
target_test = test['Exited']

print(features_train.shape)
print(features_valid.shape)
print(features_test.shape)

# %% [markdown]
# ### Scaling

# %%
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features_train[var_numeric] = scaler.fit_transform(features_train[var_numeric])
features_valid[var_numeric] = scaler.transform(features_valid[var_numeric])
features_test[var_numeric] = scaler.transform(features_test[var_numeric])

# %% [markdown]
# # 2. Task research

# %% [markdown]
# ### Class balance

# %%
target_train.value_counts(normalize=True).plot(kind='bar')

# %% [markdown]
# **Conclusion:** there is class imbalance

# %% [markdown]
# ### Quality of unadjusted models

# %%
from sklearn.metrics import f1_score, roc_auc_score

# %%
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=12345)
    
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)
probablities_valid = model.predict_proba(features_valid)[:, 1]

print('F1 =', f1_score(target_valid, predicted_valid))
print('AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.tree import DecisionTreeClassifier

for depth in [1, 2, 4, 6, 8, None]:
    model = DecisionTreeClassifier(random_state=12345, max_depth=depth)

    model.fit(features_train, target_train)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("max_depth =", depth)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.ensemble import RandomForestClassifier

for estim in range(10, 101, 10):
    model = RandomForestClassifier(random_state=12345, n_estimators=estim)

    model.fit(features_train, target_train)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("n_estimators =", estim)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %% [markdown]
# **Conclusion:** neither of models reaches required quality.

# %% [markdown]
# # 3. Fixing imbalance

# %% [markdown]
# ### Class weight adjustment

# %%
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=12345, class_weight='balanced')
    
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)
probablities_valid = model.predict_proba(features_valid)[:, 1]

print('F1 =', f1_score(target_valid, predicted_valid))
print('AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.tree import DecisionTreeClassifier

for depth in [1, 2, 4, 6, 8, None]:
    model = DecisionTreeClassifier(random_state=12345, 
                                   max_depth=depth, class_weight='balanced')

    model.fit(features_train, target_train)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("max_depth =", depth)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.ensemble import RandomForestClassifier

for estim in range(10, 101, 10):
    model = RandomForestClassifier(random_state=12345, 
                                   n_estimators=estim, class_weight='balanced')

    model.fit(features_train, target_train)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("n_estimators =", estim)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %% [markdown]
# **Conclusion:** взвешивание классов помогает некоторым алгоритмам, но недостаточно weight adjustment helps some of the algorithms but it is not enough

# %% [markdown]
# ### Upsampling

# %%
from sklearn.utils import shuffle

def upsample(features, target, repeat):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_upsampled = pd.concat([features_zeros] + [features_ones] * repeat)
    target_upsampled = pd.concat([target_zeros] + [target_ones] * repeat)
    
    features_upsampled, target_upsampled = shuffle(
        features_upsampled, target_upsampled, random_state=12345)
    
    return features_upsampled, target_upsampled

features_upsampled, target_upsampled = upsample(features_train, target_train, 3)

# %%
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=12345)
    
model.fit(features_upsampled, target_upsampled)
predicted_valid = model.predict(features_valid)
probablities_valid = model.predict_proba(features_valid)[:, 1]

print('F1 =', f1_score(target_valid, predicted_valid))
print('AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.tree import DecisionTreeClassifier

for depth in [1, 2, 4, 6, 8, None]:
    model = DecisionTreeClassifier(random_state=12345, max_depth=depth)

    model.fit(features_upsampled, target_upsampled)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("max_depth =", depth)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.ensemble import RandomForestClassifier

for estim in range(10, 101, 10):
    model = RandomForestClassifier(random_state=12345, n_estimators=estim)

    model.fit(features_upsampled, target_upsampled)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("n_estimators =", estim)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %% [markdown]
# ### Downsampling

# %%
def downsample(features, target, fraction):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_downsampled = pd.concat(
        [features_zeros.sample(frac=fraction, random_state=12345)] + [features_ones])
    target_downsampled = pd.concat(
        [target_zeros.sample(frac=fraction, random_state=12345)] + [target_ones])
    
    features_downsampled, target_downsampled = shuffle(
        features_downsampled, target_downsampled, random_state=12345)
    
    return features_downsampled, target_downsampled

features_downsampled, target_downsampled = downsample(features_train, target_train, 0.3)

# %%
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(random_state=12345)
    
model.fit(features_downsampled, target_downsampled)
predicted_valid = model.predict(features_valid)
probablities_valid = model.predict_proba(features_valid)[:, 1]

print('F1 =', f1_score(target_valid, predicted_valid))
print('AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.tree import DecisionTreeClassifier

for depth in [1, 2, 4, 6, 8, None]:
    model = DecisionTreeClassifier(random_state=12345, max_depth=depth)

    model.fit(features_downsampled, target_downsampled)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("max_depth =", depth)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %%
from sklearn.ensemble import RandomForestClassifier

for estim in range(10, 101, 10):
    model = RandomForestClassifier(random_state=12345, n_estimators=estim)

    model.fit(features_downsampled, target_downsampled)
    predicted_valid = model.predict(features_valid)
    probablities_valid = model.predict_proba(features_valid)[:, 1]

    print("n_estimators =", estim)
    print('  F1 =', f1_score(target_valid, predicted_valid))
    print('  AUC-ROC =', roc_auc_score(target_valid, probablities_valid))

# %% [markdown]
# ### Findings

# %% [markdown]
# 1) The best model: upsampling + RandomForest(n_estimators=100)
# 
# 2) F1 and AUC-ROC in general grow simultaneously, but sometimes their maxima don't match (for example, see RandomForest with weight adjustment)

# %% [markdown]
# # 4. Model testing

# %% [markdown]
# ### Training using complete data

# %%
features_full_train = pd.concat([features_train, features_valid])
target_full_train = pd.concat([target_train, target_valid])

features_upsampled, target_upsampled = upsample(features_full_train, target_full_train, 3)

model = RandomForestClassifier(random_state=12345, n_estimators=100)
model.fit(features_upsampled, target_upsampled)

# %%
predicted_test = model.predict(features_test)
probablities_test = model.predict_proba(features_test)[:, 1]

print('F1 =', f1_score(target_test, predicted_test))
print('AUC-ROC =', roc_auc_score(target_test, probablities_test))


