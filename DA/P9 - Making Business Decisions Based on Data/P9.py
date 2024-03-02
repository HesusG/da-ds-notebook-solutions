# %%
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', None)

# %% [markdown]
# # Part 1. Hypotheses prioritization

# %%
hypothesis = pd.read_csv('datasets/hypotheses_us.csv', sep=";")

print(hypothesis)

# %%
hypothesis['ICE'] = hypothesis['Impact']*hypothesis['Confidence']/hypothesis['Effort']
hypothesis['RICE'] = hypothesis['Reach']*hypothesis['Impact']*hypothesis['Confidence']/hypothesis['Effort']

# %%
print(hypothesis.sort_values(by='ICE', ascending=False))
print(hypothesis.sort_values(by='RICE', ascending=False))

# %% [markdown]
# The priority of these hypotheses changes respective of the prioritization framework used.
# 
# Hypothesis #8 has the highest priority when ICE is used, but gets average results with RICE, as despite having high Impact and Confidence values, its Reach is very low.
# 
# This case demonstrates the difference between the two frameworks. When you take Reach into account, the priority may rise for some hypotheses (e.g., hypotheses 7,2), and fall for others (e.g., hypotheses 8,0)

# %% [markdown]
# # Part 2. A/B test analysis

# %% [markdown]
# ## Preparing data

# %%

orders = pd.read_csv('datasets/orders_us.csv', sep=',')
orders['date'] = orders['date'].map(lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))

visitors = pd.read_csv('datasets/visitors_us.csv', sep=',')
visitors['date'] = visitors['date'].map(lambda x: dt.datetime.strptime(x, '%Y-%m-%d'))

print(orders.head(5))
print(visitors.head(5))

# %%
datesGroups = orders[['date','group']].drop_duplicates()

ordersAggregated = datesGroups.apply(
lambda x: orders[np.logical_and(orders['date'] <= x['date'], orders['group'] == x['group'])].agg({
    'date' : 'max',
    'group' : 'max',
    'transactionId' : pd.Series.nunique,
    'visitorId' : pd.Series.nunique,
    'revenue' : 'sum'}), axis=1).sort_values(by=['date','group'])

visitorsAggregated = datesGroups.apply(
lambda x: visitors[np.logical_and(visitors['date'] <= x['date'], visitors['group'] == x['group'])].agg({
'date' : 'max',
'group' : 'max',
'visits' : 'sum'}), axis=1).sort_values(by=['date','group'])

cumulativeData = ordersAggregated.merge(visitorsAggregated, left_on=['date', 'group'], right_on=['date', 'group'])
cumulativeData.columns = ['date', 'group', 'orders', 'buyers', 'revenue', 'visitors']

print(cumulativeData.head(5))

# %%
print(orders['date'].min())
print(orders['date'].max())
print(len(orders))

# %% [markdown]
# ## Plotting graphs

# %% [markdown]
# ### Ploting a cumulative revenue graph by groups

# %%
cumulativeRevenueA = cumulativeData[cumulativeData['group']=='A'][['date','revenue', 'orders']]
cumulativeRevenueB = cumulativeData[cumulativeData['group']=='B'][['date','revenue', 'orders']]

plt.plot(cumulativeRevenueA['date'], cumulativeRevenueA['revenue'], label='A')
plt.plot(cumulativeRevenueB['date'], cumulativeRevenueB['revenue'], label='B')
plt.legend()

# %% [markdown]
# Towards the middle of the test group В has considerably increased its revenue as compared to group A, but then kept growing at the same pace as group A. This may imply that there was at least one expensive order at the time
# 

# %% [markdown]
# ### Plotting a cumulative average order size graph by groups and its relative difference

# %%
plt.plot(cumulativeRevenueA['date'], cumulativeRevenueA['revenue']/cumulativeRevenueA['orders'], label='A')
plt.plot(cumulativeRevenueB['date'], cumulativeRevenueB['revenue']/cumulativeRevenueB['orders'], label='B')
plt.legend()


# %% [markdown]
# We may draw the same conclusions as from the cumulative revenue graph. We can see that the value of average order size in group B began decreasing and normalizing but is still far from being equalized. This must be accounted for when making a decision on the A/B test results.

# %%
mergedCumulativeRevenue = cumulativeRevenueA.merge(cumulativeRevenueB, left_on='date', right_on='date', how='left', suffixes=['A', 'B'])

plt.plot(mergedCumulativeRevenue['date'], (mergedCumulativeRevenue['revenueB']/mergedCumulativeRevenue['ordersB'])/(mergedCumulativeRevenue['revenueA']/mergedCumulativeRevenue['ordersA'])-1)
plt.axhline(y=0, color='black', linestyle='--')

# %% [markdown]
# We may draw the same conclusions as from the graphs with the average order size and revenue. Moreover, we observe strong fluctuations in the first half of the test.

# %% [markdown]
# ### Plotting a cumulative conversion graph by groups and its relative difference

# %%
cumulativeData['conversion'] = cumulativeData['orders']/cumulativeData['visitors']

cumulativeDataA = cumulativeData[cumulativeData['group']=='A']
cumulativeDataB = cumulativeData[cumulativeData['group']=='B']

plt.plot(cumulativeDataA['date'], cumulativeDataA['conversion'], label='A')
plt.plot(cumulativeDataB['date'], cumulativeDataB['conversion'], label='B')
plt.legend()
plt.axis(["2019-08-01", '2019-08-31', 0, 0.04]) # TODO FIXME

# %% [markdown]
# Group B forged ahead at the beginning of the test and remained a leader in conversion throughout the whole test

# %%
mergedCumulativeConversions = cumulativeDataA[['date','conversion']].merge(cumulativeDataB[['date','conversion']], left_on='date', right_on='date', how='left', suffixes=['A', 'B'])

plt.plot(mergedCumulativeConversions['date'], mergedCumulativeConversions['conversionB']/mergedCumulativeConversions['conversionA']-1)
plt.axhline(y=0, color='black', linestyle='--')
plt.axhline(y=0.1, color='grey', linestyle='--')
plt.axis(["2019-08-01", '2019-08-31', -0.25, 0.25])

# %% [markdown]
# We come to the same conclusion. However, we can see that starting from the second half of the test the differences in conversion in group B decreases as compared to group A and is likely to equalize.

# %% [markdown]
# ## Analyzing anomalies

# %% [markdown]
# ### Anomalous users by the number of orders

# %%
ordersByUsers = orders.drop(['group', 'revenue', 'date'], axis=1).groupby('visitorId', as_index=False).agg({'transactionId' : pd.Series.nunique})

ordersByUsers.columns = ['userId','orders']

print(ordersByUsers.sort_values(by='orders',ascending=False).head(10))

x_values = pd.Series(range(0,len(ordersByUsers)))

plt.scatter(x_values, ordersByUsers['orders'])

# %% [markdown]
# The graph shows that the 3-4 orders per user is the limit for regular users.

# %% [markdown]
# Let's calculate the 95th and 99th percentiles of the number of orders per user.

# %%
np.percentile(ordersByUsers['orders'], [90, 95, 99])

# %% [markdown]
# 5% os users made more than 2 orders. So we'll consider the users anomalous if they made 3 or more orders.

# %% [markdown]
# ### Abnormally expensive orders

# %%
print(orders.sort_values(by='revenue',ascending=False).head(10))

x_values = pd.Series(range(0,len(orders['revenue'])))

plt.scatter(x_values, orders['revenue'])

# %% [markdown]
# From this graph we can detect only 2 clearly anomalous orders. We get a more detailed view within the range from $0 to $1500

# %%
plt.scatter(x_values, orders['revenue'])
plt.axis([0, 1210, 0, 1500])

# %% [markdown]
# We can see that $400-800 is the limit for regular orders.

# %% [markdown]
# Let's calculate the 95th and 99th percentiles of order prices

# %%
np.percentile(orders['revenue'], [90, 95,99])

# %% [markdown]
# As we expected, the limit of regular orders is around $400: 5% of orders cost more than $430. We'll set this very sum as the limit

# %% [markdown]
# ## Let's calculate statistical significance using the raw data

# %%
import scipy.stats as stats

# %% [markdown]
# ### Conversion

# %%
ordersByUsersA = orders[orders['group']=='A'].groupby('visitorId', as_index=False).agg({'transactionId' : pd.Series.nunique})
ordersByUsersA.columns = ['visitorId', 'orders']

ordersByUsersB = orders[orders['group']=='B'].groupby('visitorId', as_index=False).agg({'transactionId' : pd.Series.nunique})
ordersByUsersB.columns = ['visitorId', 'orders']

sampleA = pd.concat([ordersByUsersA['orders'],pd.Series(0, index=np.arange(visitors[visitors['group']=='A']['visitors'].sum() - len(ordersByUsersA['orders'])), name='orders')],axis=0)
sampleB = pd.concat([ordersByUsersB['orders'],pd.Series(0, index=np.arange(visitors[visitors['group']=='B']['visitors'].sum() - len(ordersByUsersB['orders'])), name='orders')],axis=0)

print("{0:.5f}".format(stats.mannwhitneyu(sampleA, sampleB)[1]))
print("{0:.3f}".format(sampleB.mean()/sampleA.mean()-1))


# %% [markdown]
# Conversion in group B is greater than that of group A by 13.8%. P-value is below 0.05, so we can reject the null hypothesis and conclude that there is a statistically significant difference between the groups.

# %% [markdown]
# ### Average order size

# %%
print("{0:.3f}".format(stats.mannwhitneyu(orders[orders['group']=='A']['revenue'], orders[orders['group']=='B']['revenue'])[1]))
print("{0:.3f}".format(orders[orders['group']=='B']['revenue'].mean()/orders[orders['group']=='A']['revenue'].mean()-1))

# %% [markdown]
# P-value is above 0.05, so there is no statistically significant difference between the groups, if we consider the average order size, calculated using the "raw" data (despite the 25% difference).

# %% [markdown]
# ## Collecting anomalous users

# %%
usersWithManyOrders = pd.concat([ordersByUsersA[ordersByUsersA['orders'] > 2]['visitorId'], ordersByUsersB[ordersByUsersB['orders'] > 2]['visitorId']], axis = 0)
usersWithExpensiveOrders = orders[orders['revenue'] > 430]['visitorId']
abnormalUsers = pd.concat([usersWithManyOrders, usersWithExpensiveOrders], axis = 0).drop_duplicates().sort_values()
print(abnormalUsers.head(5))

# %% [markdown]
# ## Calculating statistical significance of differences using the "filtered" data

# %% [markdown]
# ### Conversion

# %%
sampleAFiltered = pd.concat([ordersByUsersA[np.logical_not(ordersByUsersA['visitorId'].isin(abnormalUsers))]['orders'],pd.Series(0, index=np.arange(visitors[visitors['group']=='A']['visitors'].sum() - len(ordersByUsersA['orders'])),name='orders')],axis=0)

sampleBFiltered = pd.concat([ordersByUsersB[np.logical_not(ordersByUsersB['visitorId'].isin(abnormalUsers))]['orders'],pd.Series(0, index=np.arange(visitors[visitors['group']=='B']['visitors'].sum() - len(ordersByUsersB['orders'])),name='orders')],axis=0)

print("{0:.5f}".format(stats.mannwhitneyu(sampleAFiltered, sampleBFiltered)[1]))
print("{0:.3f}".format(sampleBFiltered.mean()/sampleAFiltered.mean()-1))

# %% [markdown]
# After analyzing the "filtered" data p-value turned out to be even smaller and still below 0.05, so there is a statistically significant difference in conversion between the groups. Group B is 17.1$ better than group A

# %% [markdown]
# ### Average order size

# %%
print("{0:.3f}".format(stats.mannwhitneyu(
    orders[np.logical_and(
        orders['group']=='A',
        np.logical_not(orders['visitorId'].isin(abnormalUsers)))]['revenue'],
    orders[np.logical_and(
        orders['group']=='B',
        np.logical_not(orders['visitorId'].isin(abnormalUsers)))]['revenue'])[1]))

print("{0:.3f}".format(
    orders[np.logical_and(orders['group']=='B',np.logical_not(orders['visitorId'].isin(abnormalUsers)))]['revenue'].mean()/
    orders[np.logical_and(
        orders['group']=='A',
        np.logical_not(orders['visitorId'].isin(abnormalUsers)))]['revenue'].mean() - 1))

# %% [markdown]
# But there is still no statistical significance in the average order size. What's important is that the "raw" data showed that the average order size in segment B was 25% bigger, and now it's 3% smaller as compared to segment A. This means anomalous orders indeed affect the test results

# %% [markdown]
# ## Making a decision from the A/B test

# %% [markdown]
# ### Facts

# %% [markdown]
#  * A/B has lasted for a month
#  * During this. time period 1197 orders were made
#  * The graph of difference in conversion is close to equalizing
#  * The graph of the average order size hasn't equalized yet
#  * Both "raw"and "filtered data" showed a statistically significant difference in conversion between the groups
#  * Neither "raw"nor "filtered data" showed any statistically significant difference in the average order size between the groups

# %% [markdown]
# So we can come to the conclusion that the groups have the same average purchase size, but group И has a better conversion rate. Despite the fact that the average order size graphs didn't equalize, the absence of statistically significant differences in average order size by both raw and filtered data, and a considerable reduction of difference between the groups with filtered data prompt that there is no use waiting for the graphs to equalize and that we can make a decision right now

# %% [markdown]
# Hooray! We've finished our A/B test and it proved to be successful!

# %%



