# %% [markdown]
# # Studying eating establishments in LA
# You’ve decided to open a small robot-run cafe in Los Angeles. The project is promising but expensive, so you and your partners decide to try to attract investors. They’re interested in the current market conditions—will you be able to maintain your success when the novelty of robot waiters wears off?
# 
# You’re an analytics guru, so your partners have asked you to prepare some market research. You have open-source data on restaurants in LA.

# %% [markdown]
# ### Step 1. Download the data and prepare it for analysis

# %%
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# %%
rest = pd.read_csv('rest_data_us.csv')

# %%
rest.info()

# %%
rest.head()

# %%
rest['id'] = rest['id'].astype('str')

# %%
rest[rest['number'] == 0].count()

# %% [markdown]
# ### Step 2. Data analysis

# %% [markdown]
# Investigate the proportions of the various types of establishments. Plot a graph.

# %%
rest['object_type'].unique()

# %%
grouped_rest = rest.groupby('object_type').count()
grouped_rest

# %%
ax = sns.barplot(grouped_rest.index,grouped_rest['id'])
labels = ax.get_xticklabels()
ax.set_xticklabels(labels, rotation=90)

# %% [markdown]
# Investigate the proportions of chain and nonchain establishments. Plot a graph.

# %%
grouped_chain = rest.groupby('chain').count()

# %%
ax = sns.barplot(grouped_chain.index,grouped_chain['id'])
labels = ax.get_xticklabels()
ax.set_xticklabels(labels, rotation=90)

# %% [markdown]
# Which type of establishment is typically a chain?

# %%
grouped_chain_object = pd.pivot_table(rest, values ='object_name', index = 'object_type', columns = ['chain'], aggfunc='count')
grouped_chain_object

# %%
grouped_chain_object['ratio'] = grouped_chain_object[True]/(grouped_chain_object[True]+grouped_chain_object[False])
grouped_chain_object

# %%
grouped_chain_object['ratio'].plot.bar()

# %% [markdown]
# What's typical for chains: many establishments with a small number of seats or a few establishments with a lot of seats?

# %%
rest_chain = rest[rest['chain']==True]

# %%
rest_chain['object_name'].value_counts().head()

# %%
check = rest_chain[rest_chain['object_name'] == 'KFC'].sort_values(by='number', ascending=False)
check

# %%
rest_chain.number.hist()

# %% [markdown]
# Determine the average number of seats for each type of restaurant. On average, which type of restaurant has the greatest number of seats? Plot graphs.

# %%
rest.groupby('object_type').agg(mean=('number','mean'),median=('number','median'))

# %%
rest.groupby('object_type').agg(mean=('number','mean'),median=('number','median')).plot(kind='barh')

# %% [markdown]
# Put the data on street names from the address column in a separate column

# %%
rest_address = rest['address'].apply(lambda x: ' '.join(x.split(' ')[1:])).to_frame()
rest_address['a'] = 1

# %%
rest_address.groupby('address').count().sort_values(by='a', ascending = False)[0:10]

# %% [markdown]
# Plot a graph of the top ten streets by number of restaurants.

# %%
rest_address_top = rest_address.groupby('address').count().sort_values(by='a', ascending = False)[0:10]

# %%
rest_address_top.plot.bar()

# %% [markdown]
# Find the number of streets that only have one restaurant.

# %%
rest_address.groupby('address').count().sort_values(by='a', ascending = False).\
loc[lambda x: x['a'] == 1].count()[0]

# %% [markdown]
# For streets with a lot of restaurants, look at the distribution of the number of seats. What trends can you see?

# %%
rest_pr = rest[rest['address'].str.contains("W SUNSET BLVD")]
rest_pr

# %%
rest_pr.number.hist()

# %%



