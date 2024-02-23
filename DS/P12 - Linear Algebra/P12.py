# %% [markdown]
# # Statement

# %% [markdown]
# The Sure Tomorrow insurance company wants to solve several tasks with the help of ML and you are asked to evaluate that possibility.
# 
# - Task 1: Find similar customers for a given customer. That can help the company's agents with their marketing.
# - Task 2: Predict whether a new customer is likely to receive an insurance benefit. Can a prediction model do better than a dummy model?
# - Task 3: Predict the number of insurance benefits a new customer is likely to receive. It needs to be solved with a linear regression model.
# - Task 4: Protect clients' personal data without breaking the model from the previous task. It is required to develop a data transformation algorithm that would make it hard to recover personal information from the transformed data, and the quality of model using the transformed date would not suffer. You don't need to tune your model into the best one, just prove that the algorithm works correctly.

# %% [markdown]
# # Initialization

# %%
import itertools
import math
import random

import numpy as np
import pandas as pd

import seaborn as sns

import sklearn.linear_model
import sklearn.metrics
import sklearn.neighbors
import sklearn.preprocessing

from sklearn.model_selection import train_test_split

from IPython.display import display

# %% [markdown]
# # Load Data

# %% [markdown]
# Load data and conduct basic checks it's free from obvious issues.

# %%
df = pd.read_csv('../datasets/insurance_us.csv')

# %% [markdown]
# We rename the colums to make the code look more consistent with its style.

# %%
df = df.rename(columns={'Gender': 'gender', 'Age': 'age', 'Salary': 'income', 'Family members': 'family_members', 'Insurance benefits': 'insurance_benefits'})

# %%
df.sample(10)

# %%
df.info()

# %%
# we may want to fix the age type (from float to int) though this is not critical

# checking all age values are integers indeed and do the conversion if so
if (df['age'] % 1 > 0).sum() == 0:
    df['age'] = df['age'].astype('int')

# %%
df.info()

# %%
df.describe()

# %% [markdown]
# The data looks good, free of typical issues like missing values, extreme values and type mismatches. Proceeding.

# %% [markdown]
# # EDA

# %% [markdown]
# Let's quickly check whether there are certain groups of customers by looking at the pair plot.

# %%
g = sns.pairplot(df, kind='hist')
g.fig.set_size_inches(12, 12)

# %% [markdown]
# Ok, it is a bit difficult to spot obvious groups (clusters) as it is difficult to combine several variables simultaneously (to analyze multivariate distributions). That's where LA and ML can be quite handy.

# %% [markdown]
# # Task 1. Similar Customers

# %% [markdown]
# In the language of ML, it is required to develop a procedure that returns k nearest neighbors (objects) for a given object based on the concept of distance (between objects).
# 
# You may want to review the following lessons to revive knowledge related to this chapter (chapter -> lesson)
# - Distance Between Vectors -> Planar Distance
# - Distance Between Vectors -> Manhattan Distance
# 
# The interpretation of the task gives us possibility to try different distance metrics.

# %% [markdown]
# Write a function that returns k nearest neighbors for a nth object based on a specified distance metric, the number of received insurance benefits should not be taken into account for the task. 
# 
# You can use a ready implementation of the kNN algorithm from scikit-learn (check [the link](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors)) or use your own.
# 
# Test it for four combination of two cases
# - Scaling
#   - the data is not scaled
#   - the data is scaled with the [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html) scaler
# - Distance Metrics
#   - Euclidean
#   - Manhattan
# 
# Answer questions
# - Does the data being not scaled affect the kNN algorithm? If so, how does that appear?
# - Does the Manhattan distance metric return very similar results regardless the scaling?

# %%
feature_names = ['gender', 'age', 'income', 'family_members']

# %%
def get_knn(df, n, k, metric):
    
    """
    Returns k nearest neighbors

    :param df: pandas dataframe used to find similar objects within
    :param n: object no for which the nearest neighbours are looked for
    :param k: the number of the nearest neighbours to return
    :param metric: name of distance metric
    """

    nbrs = sklearn.neighbors.NearestNeighbors(n_neighbors=k, algorithm='brute', metric=metric).fit(df[feature_names])
    nbrs_distances, nbrs_indices = nbrs.kneighbors([df.iloc[n][feature_names]], k, return_distance=True)
    
    df_res = pd.concat([
        df.iloc[nbrs_indices[0]], 
        pd.DataFrame(nbrs_distances.T, index=nbrs_indices[0], columns=['distance'])
        ], axis=1)
    
    return df_res

# %% [markdown]
# Scaling the data.

# %%
feature_names = ['gender', 'age', 'income', 'family_members']

transformer_mas = sklearn.preprocessing.MaxAbsScaler().fit(df[feature_names].to_numpy())

df_scaled = df.copy()
df_scaled.loc[:, feature_names] = transformer_mas.transform(df[feature_names].to_numpy())

# %%
df_scaled.sample(5)

# %% [markdown]
# Now, let's get similar records for a given one for every combination

# %%
k=5
n = random.randint(0, len(df_scaled))

for df_source, metric in itertools.product([df, df_scaled], ['euclidean', 'manhattan']):

    if df_source is not df_scaled:
        is_scaled = False
    else:
        is_scaled = True
        
    print(f'metric={metric}, scaled={is_scaled}')
    
    # getting the nearest neighbors
    df_nn = get_knn(df_source, n=n, k=5, metric=metric)
    
    # if this is the scaled data, let's add the original data to the result (easier to compare)
    if is_scaled:        
        df_nn = pd.concat([df.loc[df_nn.index], df_nn], axis=1, keys=['original', 'scaled'])
        
    display(df_nn)
    print()

# %% [markdown]
# Answers to the questions

# %% [markdown]
# **Does the data being not scaled affect the kNN algorithm? If so, how does that appear?** 
# 
# There are different results returned by kNN for the original data and the scaled one with the same distance metric. In case of not scaling the data, kNN treat values of _income_ and _family_members_ equally important regardless of the fact their values are of very different ranges, and that forces customers with the same income but a different number of family members appear as similar whereas it is unlikely to be so in the real life. In the case of scaling the data, the variables become comparable, and results are much more consistent with what we can see in the real-life: customers of similar age and with similar number of family members but slightly different income appear together.

# %% [markdown]
# **Does the Manhattan distance metric return very similar results regardless the scaling?** 
# 
# Yes, it does. The distance metric is affected by the scaling. The effect is the same as above. Minimal numerical difference is taken as advantage regardless of how variables might be different with their values.

# %% [markdown]
# # Task 2. Is Customer Likely to Receive Insurance Benefit?

# %% [markdown]
# In the world of ML, let's treat it as the binary classification task.

# %% [markdown]
# With _insurance_benefits_ being more than zero as the target, evaluate whether the kNN classification approach can do better than a dummy model.
# 
# Instructions:
# - Build a KNN-based classifier and measure its quality with the F1 metric for k=1..10 for both the original data and the scaled one. That'd be interesting to see how k may influece the evaluation metric, and whether scaling the data makes any difference. You can use a ready implemention of the kNN classification algorithm from scikit-learn (check [the link](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)) or use your own.
# - Build the dummy model which is just a random one for this case. It returns "1" with some probability. Let's test the model with four probability values: 0, the probability of paying any insurance benefit, 0.5, 1.
# 
# The probability of paying any insurance benefit can be defined as
# 
# $$
# P\{\text{insurance benefit received}\}=\frac{\text{number of clients received any insurance benefit}}{\text{total number of clients}}.
# $$
# 
# Split the whole data in the 70:30 proportion for the training/testing parts.

# %%
# calculating the target

df['insurance_benefits_received'] = (df['insurance_benefits'] > 0).astype('int')

# %%
# checking for the class imbalance

df['insurance_benefits_received'].value_counts()

# %% [markdown]
# The data is imbalanced but let's see whether the algorithm will manage to solve this task without upsamling.

# %%


# %%
def eval_classifier(y_true, y_pred):
    
    f1_score = sklearn.metrics.f1_score(y_true, y_pred)
    print(f'F1: {f1_score:.2f}')
    
    cm = sklearn.metrics.confusion_matrix(y_true, y_pred, normalize='all')
    print('Confusion Matrix')
    print(cm)

# %%
# generating output of a random model

def rnd_model_predict(P, size, seed=42):

    rng = np.random.default_rng(seed=seed)
    return rng.binomial(n=1, p=P, size=size)

# %%


# %%
for P in [0, df['insurance_benefits_received'].sum() / len(df), 0.5, 1]:

    print(f'The probability: {P:.2f}')
    y_pred_rnd = rnd_model_predict(P, size=len(df))
        
    eval_classifier(df['insurance_benefits_received'], y_pred_rnd)
    
    print()

# %%


# %%
X = df[['age', 'gender', 'income', 'family_members']].to_numpy()
y = df['insurance_benefits_received'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

for n_neighbors in range(1, 11):
    
    print(f'n_neighbors={n_neighbors}')
    neigh = sklearn.neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
    neigh.fit(X_train, y_train)

    y_test_pred = neigh.predict(X_test)
    
    eval_classifier(y_test, y_test_pred)    
    
    print()

# %%


# %%
X = df_scaled[['age', 'gender', 'income', 'family_members']].to_numpy()
y = df['insurance_benefits_received'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

for n_neighbors in range(1, 11):
    
    print(f'n_neighbors={n_neighbors}')
    neigh = sklearn.neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
    neigh.fit(X_train, y_train)

    y_test_pred = neigh.predict(X_test)
    
    eval_classifier(y_test, y_test_pred)    
    
    print()

# %% [markdown]
# It is interesting to note the classification is the best (according to F1) with just k=1, kNN is quite good for this task. Scaling the data can increase the quality significantly, and it is a must. The random model behaves much worse than the kNN one.

# %% [markdown]
# # Task 3. Regression (with Linear Regression)

# %% [markdown]
# With _insurance_benefits_ as the target, evaluate what RMSE would be for a Linear Regression model.

# %% [markdown]
# Build your own implementation of LR. For that, recall how the linear regression task's solution is formulated in terms of LA. Check RMSE for both the original data and the scaled one. Can you see any difference in RMSE between these two cases?
# 
# Let's denote
# - $X$ — feature matrix, each row is a case, each column is a feature, the first column consists of unities
# - $y$ — target (a vector)
# - $\hat{y}$ — estimated tagret (a vector)
# - $w$ — weight vector
# 
# The task of linear regression in the language of matrices can be formulated as
# 
# $$
# y = Xw
# $$
# 
# The training objective then is to find such $w$ that it would minimize the L2-distance (MSE) between $Xw$ and $y$:
# 
# $$
# \min_w d_2(Xw, y) \quad \text{or} \quad \min_w \text{MSE}(Xw, y)
# $$
# 
# It appears that there is analytical solution for the above:
# 
# $$
# w = (X^T X)^{-1} X^T y
# $$
# 
# The formula above can be used to find the weights $w$ and the latter can be used to calculate predicted values
# 
# $$
# \hat{y} = X_{val}w
# $$

# %% [markdown]
# Split the whole data in the 70:30 proportion for the training/validation parts. Use the RMSE metric for the model evaluation.

# %%
class MyLinearRegression:
    
    def __init__(self):
        
        self.weights = None
    
    def fit(self, X, y):
        
        # adding the unities
        X2 = np.append(np.ones([len(X), 1]), X, axis=1)
        self.weights = np.linalg.inv(X2.T @ X2) @ X2.T @ y

    def predict(self, X):
        
        # adding the unities
        X2 = np.append(np.ones([len(X), 1]), X, axis=1)
        y_pred = X2 @ self.weights
        
        return y_pred

# %%


# %%
def eval_regressor(y_true, y_pred):
    
    rmse = math.sqrt(sklearn.metrics.mean_squared_error(y_true, y_pred))
    print(f'RMSE: {rmse:.2f}')
    
    r2_score = math.sqrt(sklearn.metrics.r2_score(y_true, y_pred))
    print(f'R2: {r2_score:.2f}')

# %%


# %%
X = df[['age', 'gender', 'income', 'family_members']].to_numpy()
y = df['insurance_benefits'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

lr = MyLinearRegression()

lr.fit(X_train, y_train)
print(lr.weights)

y_test_pred = lr.predict(X_test)
eval_regressor(y_test, y_test_pred)

# %%
X = df_scaled[['age', 'gender', 'income', 'family_members']].to_numpy()
y = df['insurance_benefits'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

lr = MyLinearRegression()

lr.fit(X_train, y_train)
print(lr.weights)

y_test_pred = lr.predict(X_test)
eval_regressor(y_test, y_test_pred)

# %% [markdown]
# # Task 4. Hiding Data

# %% [markdown]
# It is suggested to obfuscate data by multiplying the numerical features (remember, they can be seen as the matrix $X$) by an invertible matrix $P$. 
# 
# $$
# X' = X \times P
# $$
# 
# Try to do that and check how the features' values will look like after the transformation. BTW, the intertible property is important here so make sure that $P$ is invertible indeed.
# 
# You may want to review the 'Matrices and Matrix Operations -> Matrix Mupliplication' lesson to recall the rule of matrix multiplication and its implementation with numpy.

# %%
personal_info_column_list = ['gender', 'age', 'income', 'family_members']
df_pn = df[personal_info_column_list]

# %%
X = df_pn.to_numpy()

# %% [markdown]
# Generating a random matrix P.

# %%
rng = np.random.default_rng(seed=42)
P = rng.random(size=(X.shape[1], X.shape[1]))

# %% [markdown]
# Checking the matrix $P$ is invertible

# %%
P_det = np.linalg.det(P)

# if a matrix's determinant is not equal to zero, it is invertible
print(P_det)

# %% [markdown]
# Transforming the data

# %%
Xt = X @ P

# %% [markdown]
# Can you guess of age, income after the transformation?

# %%
dft = pd.DataFrame(Xt, columns=df_pn.columns)
df2 = pd.concat([df, dft], axis=1, keys=['original', 'transformed'])

# %%
df2.sample(5)

# %% [markdown]
# No, it is difficult to guess it by just looking at it.

# %% [markdown]
# Can you recover the original data from $X'$ if you know $P$? Try to check that with calculations by moving $P$ from the right side of the formula above to the left one. The rules of matrix multiplcation are really helpful here.

# %% [markdown]
# Reversed transformation

# %%
P_inv = np.linalg.inv(P)

# %%
Xn = Xt @ P_inv

# %%
dfn = pd.DataFrame(Xn, columns=df_pn.columns)
df3 = pd.concat([df_pn, dft, dfn], axis=1, keys=['original', 'transformed', 'reversed'])

# %% [markdown]
# Print all three cases for few customers
# - the original data
# - the transformed one
# - the reversed (recovered) one

# %%
df3.sample(5)

# %% [markdown]
# Let's try to make figures a bit easier to read

# %%
df3.sample(5).astype('int')

# %% [markdown]
# You can probably see that some values are not exactly the same as they are in the original data. What is a reason for that?

# %% [markdown]
# All integer values were converted to float because during the transformation all figures got fractional part.
# 
# Some values are not exactly zeros as in the original data because of the precision limitation.

# %% [markdown]
# Let's check whether the features' original/transformed values correlate

# %%
import scipy.stats

for name in personal_info_column_list:
    r, p = scipy.stats.spearmanr(df3['original'][name], df3['transformed'][name])
    print(f'{name:15} r={r:5.2f}, p={p:.2f}')

# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(x=df3['original']['age'], y=df3['transformed']['age'], ax=ax)
ax.set_xlabel('original age')
ax.set_ylabel('transformed age')

fig.tight_layout()

# %%
fig, ax = plt.subplots(figsize=(7, 5))

sns.scatterplot(x=df3['original']['income'], y=df3['transformed']['income'], ax=ax)
ax.set_xlabel('original income')
ax.set_ylabel('transformed income')

fig.tight_layout()

# %% [markdown]
# ## Proof That Data Obfuscation Can Work with LR

# %% [markdown]
# The regression task has been solved with linear regression in this project. Your next task is to prove _analytically_ that the given obfuscation method won't affect linear regression in terms of predicted values i.e. their values will remain the same. Can you believe that? Well, you don't have to, you should prove it!

# %% [markdown]
# So, the data is obfuscated and there is $X \times P$ instead of just $X$ now. Consequently, there are other weights $w_P$ as
# $$
# w = (X^T X)^{-1} X^T y \quad \Rightarrow \quad w_P = [(XP)^T XP]^{-1} (XP)^T y
# $$
# 
# How would $w$ and $w_P$ be linked if you simplify the formula for $w_P$ above? 
# 
# What would be predicted values with $w_P$? 
# 
# What does that mean for the quality of linear regression if you measure it with RMSE?
# 
# Check Appendix B Properties of Matrices in the end of the notebook. There are useful formulas in there!
# 
# No code is necessary in this section!

# %% [markdown]
# **Answer**

# %% [markdown]
# The quality of Linear Regression as measured with RMSE or R2 is not changed because of the transformation.

# %% [markdown]
# **Analytical proof**

# %% [markdown]
# $$
# \begin{align}
# w_P &= [(XP)^T XP]^{-1} (XP)^T y \\
#     &= [P^T X^T X P]^{-1} (XP)^T y \\
#     &= [(P^T X^T X) P]^{-1} (XP)^T y \\
#     &= P^{-1} [P^T X^T X]^{-1} (XP)^T y \\
#     &= P^{-1} [X^T X]^{-1} [P^T]^{-1} (XP)^T y \\
#     &= P^{-1} [X^T X]^{-1} [P^T]^{-1} P^T X^T y \\
#     &= P^{-1} [X^T X]^{-1} I X^T y \\
#     &= P^{-1} [X^T X]^{-1} X^T y \\    
#     &= P^{-1} \boxed{[X^T X]^{-1} X^T y}
# \end{align}
# $$

# %% [markdown]
# So, we have derived that

# %% [markdown]
# $$w_P = P^{-1} [X^T X]^{-1} X^T y $$

# %% [markdown]
# or

# %% [markdown]
# $$
# \begin{align}
# w_P &= P^{-1} w \\
# P w_P &= P P^{-1} w \\
# P w_P &= w \\
# w &= P w_P \\
# \end{align}
# $$

# %% [markdown]
# Accordingly

# %% [markdown]
# $$\hat{y} = X w = X P w_p = \boxed{X' w_P}$$ 

# %% [markdown]
# One can see that the predicted value are not changed so any evaluation metrics that compare true values and predicted ones will return same values regardless of the transformation.

# %% [markdown]
# ## Test Linear Regression With Data Obfuscation

# %% [markdown]
# Now, let's prove Linear Regression can work with the chosen obfuscation transformation computationally.
# 
# Build a procedure or a class that runs Linear Regression optionally with the obfuscation. You can use either a ready implementation of Linear Regression from sciki-learn or your own.
# 
# Run Linear Regression for the original data and the obfuscated one, compare the predicted values and the RMSE, $R^2$ metric values. Is there any difference?

# %% [markdown]
# **Procedure**
# 
# - Create a square matrix $P$ of random numbers
# - Check that it is invertible. If not, repeat the generation until we get an invertible matrix..
# - Multiply the feature matrix $X$ by matrix $P$
# - Use $XP$ as the new feature matrix

# %% [markdown]
# **Validation**
# 
# We will use results of the previous paragraph: that when multiplying features by an invertible matrix, the quality of the linear regression as measured with MSE will not change. But multiplying by random numbers will make the initial values unrecoverable without knowing the random matrix.

# %%
X = df[['age', 'gender', 'income', 'family_members']].to_numpy()
y = df['insurance_benefits'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

# %%


# %%
model = sklearn.linear_model.LinearRegression()

model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

eval_regressor(y_test, y_pred_test)

# %%


# %%
det = 0
eps = 1e-5

while det < eps:
    rng = np.random.default_rng()
    P = rng.random(size=(X_train.shape[1], X_train.shape[1]))

    # let's check that the matrix is invertible
    det = np.linalg.det(P)

# if a matrix's determinant is not equal to zero, it is invertible
print(f'Generated the random matrix P with the determinant {det:.2f}')
print(P)
print()

Xt = X @ P

Xt_train = X_train @ P
Xt_test = X_test @ P

# %%
model_t = sklearn.linear_model.LinearRegression()

model_t.fit(Xt_train, y_train)

yt_pred_train = model_t.predict(Xt_train)
yt_pred_test = model_t.predict(Xt_test)

eval_regressor(y_test, yt_pred_test)

# %% [markdown]
# We can see that the evaluation metrics are the same for both the cases. Isn't that a fascinating example of LA?!

# %% [markdown]
# # Conclusions

# %% [markdown]
# - kNN is quite a simple algorithm but still capable for finding similar objects and the classification task.
# - Computation of matrix operations does not lead to exact figures as we calculate them on paper, this is because computers are limited with their computing precision.
# - Working with formulas can be both fun and useful.
# - It is possible to transform numerical features with an invertible matrix and they will still be useful for certain ML algorythms like linear tegression as the transformation does not affect predicted values.
# - Linear Algebra is a key component to Machine Learning, it allows organizing objects with their numerical features into matrices and use matrix operations to solve problems.

# %% [markdown]
# # Checklist (TBC)

# %% [markdown]
# Type 'x' to check. Then press Shift+Enter.

# %% [markdown]
# - [x]  Jupyter Notebook is open
# - [ ]  Code is error free
# - [ ]  The cells are arranged in order of logic and execution
# - [ ]  Task 1 performed
#     - [ ]  There is the procedure that can return k similar customers for a given one
#     - [ ]  The procedure is tested for all four proposed combinations
#     - [ ]  The questions re the scaling/distances are answered
# - [ ]  Task 2 performed
#     - [ ]  The random classification model is built and tested for all for probability levels
#     - [ ]  The kNN classification model is built and tested for both the original data and the scaled one, the F1 metric is calculated.
# - [ ]  Task 3 performed
#     - [ ]  The linear tegression solution is implemented with matrix operations.
#     - [ ]  RMSE is calculated for the implemented solution.
# - [ ]  Task 4 performed
#     - [ ]  The data is obfuscated with a random and invertible matrix P
#     - [ ]  The obfuscated data is recoved, few examples are printed out
#     - [ ]  The analytical proof that the transformation does not affect RMSE is provided 
#     - [ ]  The computational proof that the transformation does not affect RMSE is provided
# - [ ]  Conclusions are made

# %% [markdown]
# # Appendix A Writing Formulas in Jupyter Notebooks

# %% [markdown]
# You can write formulas in Jupyter Notebook in a markup language provided by a high-quality publishing system called $\LaTeX$ (pronounced «Lah-tech»), and they will look like formulas in textbooks.
# 
# To put a formula in a text, put the dollar sign (\\$) before and after the formula's text e.g. $\frac{1}{2} \times \frac{3}{2} = \frac{3}{4}$ or $y = x^2, x \ge 1$.
# 
# If a formula should be in its paragraph, put the double dollar sign (\\$\\$) before and after the formula text e.g.
# 
# $$
# \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i.
# $$
# 
# The markup language of [LaTeX](https://en.wikipedia.org/wiki/LaTeX) is very popular among people who use formulas in their articles, books and texts. It can be complex but its basics are easy. Check this two page [cheatsheet](http://tug.ctan.org/info/undergradmath/undergradmath.pdf) for learning how to compose the most common formulas.

# %% [markdown]
# # Appendix B Properties of Matrices

# %% [markdown]
# Matrices have many properties in Linear Algebra. There are listed few of them here which can help with the analytical proof in this project.

# %% [markdown]
# <table>
# <tr>
# <td>Distributivity</td><td>$A(B+C)=AB+AC$</td>
# </tr>
# <tr>
# <td>Non-commutativity</td><td>$AB \neq BA$</td>
# </tr>
# <tr>
# <td>Associative property of multiplication</td><td>$(AB)C = A(BC)$</td>
# </tr>
# <tr>
# <td>Multiplicative identity property</td><td>$IA = AI = A$</td>
# </tr>
# <tr>
# <td></td><td>$A^{-1}A = AA^{-1} = I$
# </td>
# </tr>    
# <tr>
# <td></td><td>$(AB)^{-1} = B^{-1}A^{-1}$</td>
# </tr>    
# <tr>
# <td>Reversivity of the transpose of a product of matrices,</td><td>$(AB)^T = B^TA^T$</td>
# </tr>    
# </table>


