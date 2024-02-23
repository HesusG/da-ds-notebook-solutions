# %%
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import accuracy_score, precision_score, recall_score



pd.set_option('display.precision', 15)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 300)

# %%
import warnings
warnings.filterwarnings('ignore')

# %%
#функция для отображения гистограмм всех признаков для целевого поля
def feat_hist(x, group_col, key_cols):
    x_new = x.copy()
    x_new[key_cols] = df[key_cols]
    for c in key_cols:
        for cl in x[group_col].unique():
            sns.distplot(x_new[x_new[group_col]==cl][c], 
                         label='{} = {}'.format(group_col, str(cl)), bins = 10)
        plt.title(c)
        plt.legend()
        plt.show()

# %%


# %% [markdown]
# # Загружаем данные

# %%
df = pd.read_csv('gym_churn.csv')
df.head()

# %%
df.columns

# %%
df.shape

# %%
df.info()

# %%
df.describe()

# %%
df.groupby('Churn').mean()

# %%
feat_hist(df, 'Churn', df.columns)

# %%
df.corr()

# %%
plt.figure(figsize = (13,13))
sns.heatmap(df.corr(), annot = True)
plt.show()

# %%


# %% [markdown]
# ## Churn prediction

# %%
X_train, X_val, y_train, y_val = train_test_split(df.drop(columns = ['Churn']), df['Churn'], test_size = 0.2)

# %% [markdown]
# Logistic Regression model:

# %%
lr_model = LogisticRegression()

# %%
lr_model.fit(X_train, y_train)

# %%
y_proba_lr = lr_model.predict_proba(X_val)
y_pred_lr  = lr_model.predict(X_val)

# %%
print('Accuracy score for logistic regression is: {:.2f}'.format(accuracy_score(y_val, y_pred_lr)))
print('Precision score for logistic regression is: {:.2f}'.format(precision_score(y_val, y_pred_lr)))
print('Recall score for logistic regression is: {:.2f}'.format(recall_score(y_val, y_pred_lr)))

# %% [markdown]
# Random forest model:

# %%
rf_model = RandomForestClassifier(n_estimators=100)

# %%
rf_model.fit(X_train, y_train)

# %%
y_proba_rf = rf_model.predict_proba(X_val)
y_pred_rf = rf_model.predict(X_val)

# %%
print('Accuracy score for random forest is: {:.2f}'.format(accuracy_score(y_val, y_pred_rf)))
print('Precision score for random forest is: {:.2f}'.format(precision_score(y_val, y_pred_rf)))
print('Recall score for random forest is: {:.2f}'.format(recall_score(y_val, y_pred_rf)))

# %% [markdown]
# Обе модели дают достаточно неплохие результаты. Доля правильных ответов у обеих моделей одинаковвая, а вот метрики точности и полноты немного лучше у логистической регрессии. Возможно, потому что случайгый лес слишком сильно переобучается. В любом случае для начала мы можем сделать выбор в пользу первой

# %%


# %% [markdown]
# ## Clustering

# %%
sc = StandardScaler()
x_sc = sc.fit_transform(df.drop(columns = ['Churn']))

# %%
linked = linkage(x_sc, method = 'ward')

# %%
plt.figure(figsize=(15, 10))  
dendrogram(linked,
            orientation='top')
plt.title('Hierarchial clustering for GYM')
plt.show()

# %%
km = KMeans(n_clusters = 5)
labels = km.fit_predict(df.drop(columns = ['Churn']))

# %%
df['cluster_km'] = labels

# %%
df.groupby(['cluster_km']).count()

# %%
df.groupby(['cluster_km']).sum()

# %%
feat_hist(df, 'cluster_km', df.columns)

# %%
#посмотрим на долю оттока по кластерам
df.groupby(['cluster_km']).mean()['Churn']

# %% [markdown]
# Самый отточный кластер - "2". Самые"надежные" клиенты - из кластеров "0" и "4"

# %%


# %%



