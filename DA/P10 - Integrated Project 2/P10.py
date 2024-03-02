# %%
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

# %% [markdown]
# + Step 1. Open the data file and read the general information

# %%
data = pd.read_csv('datasets/logs_exp.csv', sep='\t')
data.head()

# %%
data.info()

# %%
data.describe()

# %% [markdown]
# Everything's great. We don't have missing values. Data types match our expectations. We can clearly see that we have all three experiments: 246, 247, 248

# %% [markdown]
# + Rename the columns in a way that's convenient for you

# %%
data.rename(columns={
    'EventName': 'event',
    'DeviceIDHash': 'user',
    'EventTimestamp': 'timestamp',
    'ExpId': 'exp_id',
}, inplace=True)
data.head()

# %% [markdown]
# + Check for missing values and data types. Correct the data if needed

# %% [markdown]
# As we've already seen, everything's OK

# %% [markdown]
# + Add a date and time column and a separate column for dates

# %%
data['date_time'] = pd.to_datetime(data['timestamp'], unit='s')
data['date'] = data['date_time'].dt.floor('1D')
data.head()

# %% [markdown]
# + How many events are in the logs? 
# + How many users are in the logs?
# + What's the average number of events per user?

# %%
events = len(data)
users = len(data['user'].unique())
events_per_user = events / users
print(f'{events} events')
print(f'{users} users')
print(f'{events_per_user} events_per_user')

# %% [markdown]
# + What period of time does the data cover? Find the maximum and the minimum date. Plot a histogram by date and time. Can you be sure that you have equally complete data for the entire period? Older events may be included in logs for more recent days for some users for technical reasons, and this delay could skew the overall picture. Find the moment at which the data starts to be complete and ignore the earlier section. What period does the data actually represent?

# %%
print(data['date_time'].min(), data['date_time'].max())

# %%
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
data['date_time'].hist(bins=100, figsize=(14, 5))

# %%
data.pivot_table(index='date', values='user', aggfunc='count').plot(style='o-', grid=True)

# %%
data.query('date_time > "2019-07-31 21:00"', inplace=True)
data.head()

# %%
data['date_time'].hist(bins=7*24, figsize=(14, 5))

# %% [markdown]
# We have the data for the week from 2019-08-01 to 2019-08-07 (with a three hour shift).
# Students are not likely to notice such a slight shift, so I doubt that we should focus on that.

# %% [markdown]
# + Did you lose many events and users when excluding the older data?

# %%
events = len(data)
users = len(data['user'].unique())
events_per_user = events / users
print(f'{events} events')
print(f'{users} users')
print(f'{events_per_user} events_per_user')

# %% [markdown]
# We lost less than 1%.

# %% [markdown]
# + Make sure you have users from all three experimental groups.

# %%
data['exp_id'].value_counts()

# %% [markdown]
# + See what events are in the logs and their frequency of occurrence. Sort them by frequency. 

# %%
data.pivot_table(index='event', values='user', aggfunc='count').sort_values('user', ascending=False)

# %% [markdown]
# + Find the number of users who performed each of these actions. Sort the events by the number of users. Calculate the proportion of users who performed the action at least once.

# %%
users_per_event = (
    data
    .pivot_table(index='event', values='user', aggfunc=lambda x: x.nunique())
    .sort_values('user', ascending=False)
)
users_per_event

# %%
users_per_event / len(data['user'].unique())

# %% [markdown]
# + In what order do you think the actions took place. Are all of them part of a single sequence? You don't need to take them into account when calculating the funnel.

# %% [markdown]
# We'll take all the data in decreasing order of frequency, except Tutorial

# %% [markdown]
# + Use the event funnel to find the share of users that proceed from each stage to the next. (For instance, for the sequence of events A → B → C, calculate the ratio of users at stage B to the number of users at stage A and the ratio of users at stage C to the number at stage B.) 

# %%
users_funnel = users_per_event[:-1]
users_funnel = (users_funnel / users_funnel.shift())[1:]
users_funnel

# %% [markdown]
# + At what stage do you lose most of users?

# %% [markdown]
# TThe most considerable drop is observed at the first stage, on passing from MainScreenAppear to OffersScreenAppear. Probably the mechanics should be enhanced so that users passed to OffersScreen.

# %% [markdown]
# + What share of users make the entire journey from their first event to payment?

# %%
print('{} make it from the main screen to successful payment'
      .format((users_per_event.loc['PaymentScreenSuccessful'] / users_per_event.loc['MainScreenAppear'])['user']))

# %% [markdown]
# + How many users are there in each group?

# %%
users_per_group = data.pivot_table(index='exp_id', values='user', aggfunc=lambda x: x.nunique())['user']
users_per_group

# %% [markdown]
# + We have two control groups in the A/A test, where we check our mechanisms and calculations. See if there is a statistically significant difference between the samples 246 and 247.
# + Select the most popular event. In each of the control groups, find the number of users who performed this action. Find their share. Check whether the difference between the groups is statistically significant. Repeat the procedure for all other events (it will save time if you create a special function for this test). Can you that the groups were split properly?

# %%
users_events_per_group = data.pivot_table(index='event', values='user', columns='exp_id', aggfunc=lambda x: x.nunique())
users_events_per_group

# %%
from scipy import stats
import numpy as np
import math

def check_hypothesis(successes1, successes2, trials1, trials2, alpha=0.01):
    # proportion of successes in the first group:
    p1 = successes1/trials1

    # proportion of successes in the second group:
    p2 = successes2/trials2

    # proportion of successes in the combined dataset:
    p_combined = (successes1 + successes2) / (trials1 + trials2)

    # the difference of proportions in datasets
    difference = p1 - p2
    
    # calculating the statistic in standard deviations of standard normal distribution
    z_value = difference / math.sqrt(p_combined * (1 - p_combined) * (1/trials1 + 1/trials2))

    # setting standard normal distribution (mean= 0, standard deviation=1)
    distr = stats.norm(0, 1) 

    # calculating the statistic in standard deviations of standard normal distribution
    z_value = difference / math.sqrt(p_combined * (1 - p_combined) * (1/trials1 + 1/trials2))


    p_value = (1 - distr.cdf(abs(z_value))) * 2

    print('p-value: ', p_value)

    if (p_value < alpha):
        print("Rejecting the null hypothesis: there is a significant difference between the proportions")
    else:
        print("Failed to reject the null hypothesis, there is no reason to consider the proportions different")  

# %%
check_hypothesis(users_events_per_group.loc['MainScreenAppear', 246],
                 users_events_per_group.loc['MainScreenAppear', 247],
                 users_per_group.loc[246],
                 users_per_group.loc[247],
                )                 

# %%
def check_event_hypithesis(users_events_per_group, users_per_group,
                           event,
                           exp1, exp2
                          ):
    frac1 = users_events_per_group.loc[event, exp1] / users_per_group.loc[exp1]
    frac2 = users_events_per_group.loc[event, exp2] / users_per_group.loc[exp2]
    print(f'{frac1} with {event} event in group {exp1}')
    print(f'{frac2} with {event} event in group {exp2}')
    check_hypothesis(users_events_per_group.loc[event, exp1],
                     users_events_per_group.loc[event, exp2],
                     users_per_group.loc[exp1],
                     users_per_group.loc[exp2],
                    )

# %%
for event in users_events_per_group.index:
    check_event_hypithesis(users_events_per_group, users_per_group,
                          event, 246, 247)
    print()

# %% [markdown]
# We can state with a high degree of confidence that the results in control groups are equal. I.e., division into groups and calculations seem to be correct.

# %% [markdown]
# + Do the same thing for the group with altered fonts. Compare the results with those of each of the control groups for each event in isolation. Compare the results with the combined results for the control groups. What conclusions can you draw from the experiment?

# %%
for event in users_events_per_group.index:
    check_event_hypithesis(users_events_per_group, users_per_group,
                          event, 246, 248)
    print()

# %% [markdown]
# We can't see any great difference here either. Although the proportion of events per user has decreased, the differences remain statistically insignificant.

# %%
for event in users_events_per_group.index:
    check_event_hypithesis(users_events_per_group, users_per_group,
                          event, 247, 248)
    print()

# %% [markdown]
# In this case all the events, except payment, grew less in number, but all the differences are really slight.

# %%
users_events_per_group_control = users_events_per_group.copy()
users_events_per_group_control.loc[:, 247] += users_events_per_group_control.loc[:, 246]
users_events_per_group_control.drop(columns=246, inplace=True)
users_events_per_group_control

# %%
users_per_group_control = users_per_group.copy()
users_per_group_control.loc[247] += users_per_group_control.loc[246]
users_per_group_control.drop(246, inplace=True)
users_per_group_control

# %%
for event in users_events_per_group.index:
    check_event_hypithesis(users_events_per_group_control, users_per_group_control,
                          event, 247, 248)
    print()

# %% [markdown]
# Although all proportions have decreased, the differences are far from statistical significance.


