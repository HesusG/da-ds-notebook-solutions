# %% [markdown]
# # Research for a Telecoms Operator ¶
# 
# You work as an analyst for the telecom operator Megaline. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget. 

# %% [markdown]
# ## Objectives ¶
# 
# We are going to carry out a preliminary analysis of the Surf and Ultimate plans based on a relatively small client selection. We have the data on 500 Megaline clients: who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent in 2018. Our job is to analyze clients' behavior and determine which prepaid plan brings in more revenue. 

# %% [markdown]
# ## Studying the Data
# First we'll import the data and have a look at it. There are five datasets: 

# %%
import pandas as pd
import matplotlib.pyplot as plt 
import math
import numpy as np
from scipy import stats as st
from IPython.display import display

# %%
try:
    calls = pd.read_csv('/datasets/megaline_calls.csv')
    internet = pd.read_csv('/datasets/megaline_internet.csv')
    messages = pd.read_csv('/datasets/megaline_messages.csv')
    plans = pd.read_csv('/datasets/megaline_plans.csv')
    users = pd.read_csv('/datasets/megaline_users.csv')
except:
    calls = pd.read_csv('/Users/Steve Lewis/practicum_datasets/megaline_calls.csv')
    internet = pd.read_csv('/Users/Steve Lewis/practicum_datasets/megaline_internet.csv')
    messages = pd.read_csv('/Users/Steve Lewis/practicum_datasets/megaline_messages.csv')
    plans = pd.read_csv('/Users/Steve Lewis/practicum_datasets/megaline_plans.csv')
    users = pd.read_csv('/Users/Steve Lewis/practicum_datasets/megaline_users.csv')

# %% [markdown]
# ### The 'calls' dataset

# %%
display(calls)

# %%
calls.info()

# %%
calls['duration'].describe()

# %%
calls.duplicated().sum()

# %% [markdown]
# Conclusion: This dataset lists all the calls made by this sample of 500 clients in 2018.  It has 137735 rows and no null values.  The duration of calls is measured in minutes and the data seems reasonable.  However, the data type of 'call_date' needs to be changed from object to datetime.

# %% [markdown]
# ### The 'internet' dataset

# %%
display(internet)

# %%
internet.info()

# %%
internet['mb_used'].describe()

# %%
len(internet.query('mb_used == 0'))

# %%
len(internet.query('mb_used == 0'))/len(internet)

# %%
internet.duplicated().sum()

# %% [markdown]
# Conclusion: This dataset details the internet usage of this sample of 500 clients in 2018. It has 104825 rows and no null values and we notice that 13,737 of the web sessions (13.11%) used no data at all.  Ideally, to confirm if this is legitimate we would need to discuss with the relevant person in the company. However with no further information currently we will assume that the data is correct.
# 
# The data type of session_date also needs to be changed from object to datetime.

# %% [markdown]
# ### The 'messages' dataset

# %%
display(messages)

# %%
messages.info()

# %%
messages.duplicated().sum()

# %% [markdown]
# Conclusion: This dataset lists all the messages sent by the sample of 500 clients in 2018. This dataset has 76051 rows and no null values.  The data type of message_date also needs to be changed from object to datetime.

# %% [markdown]
# ### The 'plans' dataset

# %%
display(plans)

# %%
plans.info()

# %% [markdown]
# Conclusion: This table details the differences between the surf and the ultimate prepaid plans.

# %% [markdown]
# ### The 'users' dataset

# %%
display(users)

# %%
users['city'].value_counts()

# %%
users.info()

# %%
users.duplicated().sum()

# %% [markdown]
# Conclusion: This dataset contains information on the sample of 500 clients in 2018.  The data type of reg_date and churn_date will need to be changed from object to datetime.

# %% [markdown]
# Note that he churn_date column is poorly populated with only 34 values (ie less than 10%).  Let's look at this data in more detail:

# %%
users['churn_date'].value_counts()

# %% [markdown]
# These are the dates that the 34 customers ended their plans.  As per the information given with the data, this means that the other 466 customers remained on their plans at least until the end of 2018.

# %% [markdown]
# Overall Conclusion: the data has very few errors.  We just need to change the date variables as described above.

# %% [markdown]
# ## Preparing the Data
# Converting the data to the necessary types and eliminating errors in the data.

# %% [markdown]
# ### Converting the data to the necessary types
# We will first change the type of all the date variables to datetime:

# %%
calls['call_date'] = pd.to_datetime(calls['call_date'], format='%Y-%m-%d')

# %%
calls.info()

# %% [markdown]
# The type of call_date has been successfully changed.  Now let's make the other type changes as detailed above:

# %%
calls['call_date'] = pd.to_datetime(calls['call_date'], format='%Y-%m-%d')
internet['session_date'] = pd.to_datetime(internet['session_date'], format='%Y-%m-%d')
messages['message_date'] = pd.to_datetime(messages['message_date'], format='%Y-%m-%d')
users['reg_date'] = pd.to_datetime(users['reg_date'], format='%Y-%m-%d')
users['churn_date'] = pd.to_datetime(users['churn_date'], format='%Y-%m-%d')

# %% [markdown]
# ### Eliminating Errors in the Data
# We didn't find any errors with the dataset so there is no need to perform any operations to eliminate errors in the data.

# %% [markdown]
# ### Calculating New Columns
# We will now find the following:
# - The number of calls made and minutes used per month for each user
# - The number of text messages sent per month for each user
# - The volume of data per month for each user
# - The monthly revenue from each user (subtract the free package limit from the total number of calls, text messages, and data; multiply the result by the calling plan value; add the monthly charge depending on the calling plan)

# %% [markdown]
# <div class="alert alert-block alert-info">
#     
# <b>Senior reviewer's comment</b> <a class="tocSkip"></a>
#     
# Senior Reviewer's Comment It's important to look at how students do rounding:
#     
# Rounding will be done incorrectly by any built-in methods, except for math.ceil and np.ceil (int, round....). 
#     
# Serious mistake, red comment.
#     
# math.ceil with apply is not the optimal way.
#     
# It can be suggested that np.ceil would be a better fit, as can work with the whole column at once. np.ceil with apply is not the optimal way.
#     
# It is possible to say that np.ceil doesn't need apply, because it can work with the whole column at once. A self-written function is not the best way.
#     
# If the function is written correctly, you can give advice that np.ceil is a better fit. If it is incorrect - red comment.
# np.ceil without apply is perfect, here you can only praise.
#     
# If the student did not bring the rounded values of the call duration to an integer type - a yellow comment.
# 
# You can also give the following advice: Usually, a dataframe contains data for several years, and then the month method can lead to an error: for example, June 2019 and June 2020 can become one month.
# The astype('datetime64[M]') method should be used.
# 
# 
# </div>

# %% [markdown]
# ### The number of calls made and minutes used per month for each user

# %% [markdown]
# We first need to extract the month from 'call_date' and store it in a new column.  Then we need to find the total number of calls and the duration of calls for each user_id for each month. Note that Megaline rounds seconds up to minutes. For calls, each individual call is rounded up: even if the call lasted just one second, it will be counted as one minute. We therefore need to create a new colum with these rounded up call durations.

# %%
calls['month'] = pd.DatetimeIndex(calls['call_date']).month

# %%
display(calls)

# %% [markdown]
# Now we create the new column with rounded up call durations:

# %%
def rounding_up_calls (duration):
    rounding = math.ceil(duration)
    return rounding

# %%
calls['duration_rounded_up'] = calls['duration'].apply(rounding_up_calls)

# %%
calls.head()

# %% [markdown]
# Now we create a table with the durations of calls per user per month (using the rounded up call durations):

# %%
calls_pivot = calls.pivot_table(index = ['user_id', 'month'], values = 'duration_rounded_up', aggfunc = ['sum','count'])

# %%
calls_pivot.head()

# %%
calls_pivot.columns = ['minutes_used', 'calls_made']

# %%
calls_pivot = calls_pivot.reset_index()

# %%
calls_pivot.head()

# %%
calls_pivot.shape

# %% [markdown]
# ### The number of text messages sent per month for each user
# Again, we need to extract the month from 'message_date' and store it in a new column.  Then we need to find the total number of messages for each user_id for each month.

# %%
messages['month'] = pd.DatetimeIndex(messages['message_date']).month

# %%
messages.head()

# %%
messages_pivot = messages.pivot_table(index = ['user_id', 'month'], values = 'id', aggfunc = 'count')

# %%
messages_pivot.head()

# %%
messages_pivot.columns = ['number_of_texts']

# %%
messages_pivot.head()

# %%
messages_pivot = messages_pivot.reset_index()

# %%
messages_pivot.head()

# %%
messages_pivot.shape

# %% [markdown]
# ### 2.3.3 The Volume of Data per Month for Each User
# We will extract the month from 'session_date' and store it in a new column.  Then we will find the total volume of data used (in megabytes) by each user_id each month.

# %%
internet['month'] = pd.DatetimeIndex(internet['session_date']).month
internet.head()

# %%
internet_pivot = internet.pivot_table(index = ['user_id', 'month'], values = 'mb_used', aggfunc = 'sum')
internet_pivot.head()

# %%
internet_pivot.columns = ['volume_of_data_used']
internet_pivot.head()

# %%
internet_pivot = internet_pivot.reset_index()
internet_pivot.head()

# %%
internet_pivot.shape

# %% [markdown]
# Megaline rounds up the total megabytes used for the month per user to gigabytes. We will therefore create a new column in the table with these rounded up values in gigabytes:

# %%
def rounding_up (mb):
    rounded = math.ceil(mb/1024)
    return rounded

# %%
internet_pivot['data_rounded_up'] = internet_pivot['volume_of_data_used'].apply(rounding_up)

# %%
internet_pivot.head()

# %% [markdown]
# ### The Monthly Revenue from Each User
# To calculate monthly revenue, we first need to join the above three tables together to get the total calls, messages and internet usage by user per month. 
# 
# Then we need to add the plan information (ie whether the user was on Surf or Ultimate) and calculate the *chargeable* calls, texts and messages.
# 
# First we join the calls and messages table:

# %%
calls_and_messages = calls_pivot.merge(messages_pivot, on=['user_id','month'], how='outer')
calls_and_messages.head()

# %%
calls_and_messages.info()

# %% [markdown]
# Now we join the internet table:

# %%
usage_table = calls_and_messages.merge(internet_pivot, on=['user_id','month'], how='outer')
usage_table.head()

# %%
usage_table.shape

# %% [markdown]
# Now we will add the plan information.
# 
# We will first create a subset of the users table containing the user_id, plan and city columns (as we will need the city column later in the project). Then we will join it to the usage_table.

# %%
plans = users[['user_id', 'plan', 'city']]
plans.head()

# %%
users['plan'].value_counts()

# %%
usage_table_plans = usage_table.merge(plans, on=['user_id'], how='outer')
usage_table_plans.head()

# %% [markdown]
# <div class="alert alert-block alert-info">
#     
# <b>Senior reviewer's comment</b> <a class="tocSkip"></a>
#     
# **Converts MB to GB.**
#     
# If it's not done - gross mistake, red comment.
#     
# Remembers that 1 GB = 1024 MB, not 1000.
#    
#     
# MB can be converted to GB at any stage of the project, up to and including the calculation of revenue.
#     
# The task does NOT say to round GB to an integer. If students don't do it, that's fine.
# 
# **Merging tables**
#     
#  In this sprint, many students merge tables for the first time. It is extremely important to comment on how successful this merger was. Above is the best method in my opinion:
#     
# Preliminary data grouping by users and months.
#     
# Combining calls, SMS and Internet data by user and month with the how='outer' parameter.
#     
# Adding the user's fare and city data to the table using how='left' parameter
#     
# There may be other correct ways to merge, for example:
#     
# First, creating a "perfect array" of all possible combinations of users and months corresponding to the period under study, then adding the rest of the data to it.
#     
# After grouping, the reset_index method is not applied to the resulting arrays, the arrays themselves are combined by index.
#     
# The most common mistakes:
#     
# The student merges arrays by users only.
#     
# Sometimes does not conduct a preliminary grouping.
#     
# Usually this is a problem for teachers, reviewers rarely see this, since most often Python does not cope with such a heavy merger.
# 
# This is a gross mistake and red comment. Tell the student that it's possible to merge not only by one column, but to use two or more columns as a join key.
#     
# Add an approximate calculation of the number of rows received in the correct merger, show that the student got more rows.
# If necessary, indicate the importance of preliminary data grouping.
#     
# The student is merging call, SMS and Internet data NOT with the how='outer' parameter.
#     
# This leads to the loss of the number of unique users. Gross mistake, red comment. It is worth counting (or suggesting to count) the number of unique users in the merged table as a confirmation of an error.
#     
# When pre-grouping, the student displays the month of the service in the column name, for example: df_calls.pivot_table(index=['user_id'], columns = ['month'], values='duration', aggfunc=['count', 'sum']) As a result, technically the merger is carried out without errors, but the final dataframe contains more than 40 columns and is difficult to work with.
#     
# In such cases I mark it as a gross mistake with a red comment. Optionally, you can leave a yellow comment, indicating that it's possible to use two columns at the same time as a join key.
# 
# If everything is done correctly, but no check for correctness of the merger was conducted - give advice to conduct such checks, providing a couple of possible examples.
#     
# I suggest not commenting or commenting in green all minor shortcomings - merging with tariff rates, merging with all columns of the table containing users data, etc.
#     
# Yes, this is not optimal, but otherwise at this stage many will simply not pass the project.
#     
# **Filling gaps in a merged table**
#     
# It is important that the student fills in these gaps with zeros.
#     
# This will affect subsequent calculations.
#     
# If it's not done - gross mistake, red comment.
#     
#     
# </div>

# %% [markdown]
# We now need to calculate the 'chargeable' minutes, texts and data for each month.  These are the minutes, texts and data outside of the monthly allowances. 
# 
# We will need the following pricing data relating to the two tariffs: Surf and Ultimate.

# %% [markdown]
# <div class="alert alert-block alert-info">
#     
# <b>Senior reviewer's comment</b> <a class="tocSkip"></a>
#     
# Here student used many functions and create many columns. Weshould add yellow comment and tell about one function for all parametres.
#     
#     
# Be sure to comment on whether the revenue was calculated correctly by the student.
#     
# *Most frequent gross mistakes (red comments):*
#     
# Forgets about monthly payment.
# Confusion with converting of Mb to Gb.
#     
# You can convert GB to MB, but it's impossible not to convert anything, because of the data in the tariff table.
#     
# The "overrun" of minutes, GB and SMS is not calculated correctly.
#     
# For example, they get negative values for overspending and deduct "underspent" money from the subscription fee.
#     
# *Yellow comments:*
#     
# Calculate additional columns for overspending by type of service.
# 
# Sometimes they don't even delete them after the calculation.
#     
# Do not use the apply function and method.
#     
# When calculating, instead of references to the cells of the df_tariffs table they use numbers from it: For example, 1950 instead of df_tariffs[df_tariffs['tariff_name'] == 'ultra']['rub_monthly_fee'].
# 
# </div>

# %%
surf_monthly_charge = 20
surf_monthly_minutes = 500
surf_monthly_messages = 50
surf_monthly_data = 15
surf_call_charge = 0.03
surf_message_charge = 0.03
surf_data_charge = 10

ultimate_monthly_charge = 70
ultimate_monthly_minutes = 3000
ultimate_monthly_messages = 1000
ultimate_monthly_data = 30
ultimate_call_charge = 0.01
ultimate_message_charge = 0.01
ultimate_data_charge = 7

# %% [markdown]
# We will define a function to calculate the chargeable minutes, texts and data outside of the monthly allowances:

# %%
def chargeable_calls (row):
    plan = row['plan']
    minutes_used = row['minutes_used']
    
    if plan == 'surf':
        if minutes_used > 500:
            chargeable = minutes_used - 500
        else:
            chargeable = 0
    if plan == 'ultimate':
        if minutes_used > 3000:
            chargeable = minutes_used - 3000
        else:
            chargeable = 0
    return chargeable

# %%
usage_table_plans['chargeable_calls'] = usage_table_plans.apply(chargeable_calls, axis =1)
usage_table_plans.head()

# %% [markdown]
# The new column has beed added successfully.  We will investigate it further:

# %%
len(usage_table_plans.query('chargeable_calls != 0'))

# %%
usage_table_plans.query('chargeable_calls != 0')['chargeable_calls'].describe()

# %% [markdown]
# We see that there were 566 user-months in the period when the company earned additonal income from calls.
# 
# Now we will calculate and add similar columns for messages and data.

# %%
def chargeable_messages (row):
    plan = row['plan']
    number_of_texts = row['number_of_texts']
    
    if plan == 'surf':
        if number_of_texts > 50:
            chargeable = number_of_texts - 50
        else:
            chargeable = 0
    if plan == 'ultimate':
        if number_of_texts > 1000:
            chargeable = number_of_texts - 1000
        else:
            chargeable = 0
    return chargeable

# %%
usage_table_plans['chargeable_messages'] = usage_table_plans.apply(chargeable_messages, axis =1)
usage_table_plans.head()

# %%
def chargeable_data (row):
    plan = row['plan']
    data_rounded_up = row['data_rounded_up']
    
    if plan == 'surf':
        if data_rounded_up > 15:
            chargeable = data_rounded_up - 15
        else:
            chargeable = 0
    if plan == 'ultimate':
        if data_rounded_up > 30:
            chargeable = data_rounded_up - 30
        else:
            chargeable = 0
    return chargeable

# %%
usage_table_plans['chargeable_data'] = usage_table_plans.apply(chargeable_data, axis =1)
usage_table_plans.head()

# %%


# %%


# %% [markdown]
# Now we have all the data we need to calculate and add a monthly revenue column:

# %%
def monthly_rev(row):
    plan = row['plan']
    chargeable_calls = row['chargeable_calls']
    chargeable_messages = row['chargeable_messages']
    chargeable_data = row['chargeable_data']
    
    if plan == 'surf':
        revenue = surf_monthly_charge +((chargeable_calls * surf_call_charge) + (chargeable_messages * surf_message_charge)+ (chargeable_data * surf_data_charge))
    else:
        revenue = ultimate_monthly_charge +((chargeable_calls * ultimate_call_charge) + (chargeable_messages * ultimate_message_charge)+ (chargeable_data * ultimate_data_charge))
    return revenue

# %%
usage_table_plans['monthly_revenue'] = usage_table_plans.apply(monthly_rev, axis =1)
usage_table_plans.head()

# %% [markdown]
# The 'usage_table_plans' dataset now gives us the information requested: 
# - The number of calls made and minutes used per month
# - The number of text messages sent per month
# - The volume of data per month
# - The monthly revenue from each user.

# %% [markdown]
# ## Analysing the Data
# We will now investigate the customers' behavior by plotting histograms of the minutes, texts and volume of data the users of each plan require per month. 
# We will also calculate the mean, variance and standard deviation.

# %%
variables = ['minutes_used', 'number_of_texts', 'volume_of_data_used']
plans = ['surf', 'ultimate']

# %%
for col in variables:
    for tariff in plans:
        usage_table_plans[usage_table_plans['plan'] == tariff][col].plot(kind = 'hist', bins = 100)
    plt.title(col)
    plt.legend(plans)
    plt.show()

# %% [markdown]
# These graphs plot the distributions of the monthly consumption by users of call minutes, messages and data. The data covers 500 users, 339 on the surf plan and 161 on the ultimate plan. 

# %% [markdown]
# <div class="alert alert-block alert-info">
#     
# <b>Senior reviewer's comment</b> <a class="tocSkip"></a>
#     
# Also, when describing distributions, students try to understand what kind they belong to.
#     
# It is not obligatory to do this, but if they still do and make mistakes - you need to correct them.
#     
# If they divide all distributions into "similar to normal" and "very different from normal" - that's correct.
# 
# 
# </div>

# %% [markdown]
# <div class="alert alert-block alert-info">
#     
# <b>Senior reviewer's comment</b> <a class="tocSkip"></a>
#     
# For next cells:    
#     
# When describing distributions, students try to understand what kind they belong to.
#     
# It is not obligatory to do this, but if they still do and make mistakes - you need to correct them.
#     
# If they divide all distributions into "similar to normal" and "very different from normal" - that's correct.
# 
# 
# </div>

# %% [markdown]
# ### Analysis of Call Minutes used

# %%
usage_table_plans.query('plan == "surf"')['minutes_used'].max()

# %%
usage_table_plans.query('plan == "ultimate"')['minutes_used'].max()

# %%
usage_table_plans.query('plan == "surf"')['minutes_used'].mean()

# %%
usage_table_plans.query('plan == "surf"')['minutes_used'].median()

# %%
usage_table_plans.query('plan == "ultimate"')['minutes_used'].mean()

# %%
usage_table_plans.query('plan == "ultimate"')['minutes_used'].median()

# %%
np.var(usage_table_plans.query('plan == "surf"')['minutes_used'])

# %%
np.std(usage_table_plans.query('plan == "surf"')['minutes_used'])

# %%
np.var(usage_table_plans.query('plan == "ultimate"')['minutes_used'])

# %%
np.std(usage_table_plans.query('plan == "ultimate"')['minutes_used'])

# %% [markdown]
# Analysis: The distribution of minutes used per month seems to approximate a 'normal' distribution for both the Surf and Ultimate plans.  They both look to be skewed to the right and this is confirmed by the means of each being higher than the medians. The mean for Surf is 436.5 minutes and for Ultimate 434.7 minutes.  The maximum monthly usage for those on the Surf plan (in this sample) was 1510 minutes, compared to 1369 for the Ultimate plan. The standard deviation for Ultimate is 237.7 which is greater than the variance for Surf (at 229.2).

# %% [markdown]
# ### Analysis of Text Messages Sent

# %%
usage_table_plans.query('plan == "surf"')['number_of_texts'].mean()

# %%
usage_table_plans.query('plan == "ultimate"')['number_of_texts'].mean()

# %%
np.var(usage_table_plans.query('plan == "surf"')['number_of_texts'])

# %%
np.var(usage_table_plans.query('plan == "ultimate"')['number_of_texts'])

# %%
np.std(usage_table_plans.query('plan == "surf"')['number_of_texts'])

# %%
np.std(usage_table_plans.query('plan == "ultimate"')['number_of_texts'])

# %% [markdown]
# Analysis: The distribution of the number of texts sent per month looks less like a 'normal' distribution and more like a downward exponential curve for both the Surf and Ultimate plans.  
# The mean for Surf is 40.1 texts per month and for ultimate is higher at 46.2 texts per month.  
# The standard deviations for both plans are very similar: 33.0 for Surf and 32.9 for Ultimate.

# %% [markdown]
# ### Analysis of Data Used (mb)

# %%
usage_table_plans.query('plan == "surf"')['volume_of_data_used'].mean()

# %%
usage_table_plans.query('plan == "ultimate"')['volume_of_data_used'].mean()

# %%
np.var(usage_table_plans.query('plan == "surf"')['volume_of_data_used'])

# %%
np.var(usage_table_plans.query('plan == "ultimate"')['volume_of_data_used'])

# %%
np.std(usage_table_plans.query('plan == "surf"')['volume_of_data_used'])

# %%
np.std(usage_table_plans.query('plan == "ultimate"')['volume_of_data_used'])

# %% [markdown]
# Analysis: The distribution of the volume of data used per month looks very much like a 'normal' distribution for both the Surf and Ultimate plans.
# The mean for Ultimate is higher at 17,238mb compared to 16,717mb for Surf.
# However, the standard deviations for both plans are very similar: 7,882mb for Surf and 7,825mb for Ultimate.

# %% [markdown]
# Conclusion: the behavious of customers on the Surf and Ultimate plans is actually quite similar.  Despite the Ultimate plan being more expensive and having greater allowances, Surf customer use slightly more call minutes per month, on average.  Ultimate customers send more text messages on average than Surf customers (46.2 compared to 40.1) and the standard deviations for both are similar.  Ultimate customers do use more data per month that Surf customers, but not significantly more: 17.2GB compared to 16.7GB. Again, the standard deviations for both are very similar.

# %% [markdown]
# <div class="alert alert-block alert-info">
#     
# <b>Senior reviewer's comment</b> <a class="tocSkip"></a>
#     
# We need to formulate H0 and H1. Use right words: reject/can't reject. Not accept, not right, not true. Sometimes students write it. It is a mistake.
# 
# Students should use st.ttest_ind. They have big theory lesson about it.
# </div>

# %% [markdown]
# ## Testing Hypotheses
# We will now test the following hypotheses:
# - Hypothesis 1: The average revenue from users of Ultimate and Surf calling plans differs.
# - Hypothesis 2: The average revenue from users in NY-NJ area is different from that of the users from other regions.

# %% [markdown]
# ### Hypothesis 1
# We will compare the means of the two plans and test the hypothesis that the average revenue from users of Ultimate and Surf calling plans differs (ie that one could be greater or less than the other).  This is a 2 sided test from data for two independent data sources. 

# %%
usage_table_plans.query('plan == "surf"')['monthly_revenue'].mean()

# %%
usage_table_plans.query('plan == "ultimate"')['monthly_revenue'].mean()

# %%
np.std(usage_table_plans.query('plan == "surf"')['monthly_revenue'])

# %%
np.std(usage_table_plans.query('plan == "ultimate"')['monthly_revenue'])

# %% [markdown]
# The average monthly revenue for Ultimate customers (72.69 USD) appears greater than for Surf customers (63.44 USD). However, the standard distributions are very different, so we will formulate a null and alternative hypothesis and use the data sets to perform a statistical test.
# 
# The null hypothesis will be: 'the means of the two datasets are equal'. We will use a critical statistical significance level (alpha) of 0.05.  If the p-value < alpha, we reject the hypothesis that the mean monthly revenues of the two customer groups are equal.

# %%
alpha = 0.05
sample_1 = usage_table_plans.query('plan == "surf"')['monthly_revenue']
sample_2 = usage_table_plans.query('plan == "ultimate"')['monthly_revenue']
results = st.ttest_ind(sample_1, sample_2, equal_var = False) 
# we set equal_var to False as we don't consider the variances of the statistical populations from which the samples are taken to be are approximately equal.

print('p-value: ', results.pvalue)

if results.pvalue < alpha:
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis") 

# %% [markdown]
# The p-value is very small.  It tells us that if the means of the two datasets were indeed the same, only around a 0.000001% of the values would have the same mean. That is, there is a very small probability of them randomly being the same. This probability is low enough to conclude that **we can reject the null hypothesis that the average revenues are the same for both groups**. So yes, it is probable that the average revenue from Users of Surf and Ultimate dies indeed differ.

# %% [markdown]
# ### Hypothesis 2
# We will examine the claim that the average revenue from users in NY-NJ area is different from that of the users from other regions. We will compare the means of the groups. This is  a 2 sided test for paired samples.

# %%
usage_table_plans['city'].value_counts()

# %%
NY_NJ = usage_table_plans[usage_table_plans['city'].str.contains('NY-NJ')]
len(NY_NJ)

# %% [markdown]
# We will compare the data from users in the 'New York-Newark-Jersey City, NY-NJ-PA MSA' to the others in the dataset.

# %%
Not_NY_NJ = usage_table_plans.query('city not in @NY_NJ.city')
len(Not_NY_NJ)

# %%
len(usage_table_plans)

# %% [markdown]
# As 2303 = 378 + 1925, we have successfully split our dataset along the NY-NJ border.

# %% [markdown]
# We will formulate a null and alternative hypothesis and use the data sets to perform a statistical test.
# 
# The null hypothesis will again be: 'the means of the two datasets are equal'. We will again use a critical statistical significance level (alpha) of 0.05.  If the p-value < alpha, we reject the hypothesis that the mean monthly revenues of the two customer groups are equal.

# %%
alpha = 0.05
sample_3 = NY_NJ['monthly_revenue']
sample_4 = Not_NY_NJ['monthly_revenue']

results1 = st.ttest_ind(sample_3, sample_4)

print('p-value: ', results1.pvalue)

if results1.pvalue < alpha:
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis") 

# %% [markdown]
# This time the p-value is greater than alpha, the critical statistical significance level. This states that if the means of the two datasets were indeed the same, 11.1% of the random samples would have the same mean.  Given this, **we cannot reject the null hypothesis that the average revenue from users in the NY-NJ area is the same as that of users in other regions**. So we cannot say that the averages are different in the two geographical regions.

# %% [markdown]
# ## Overall Conclusion
# In this project we analysed a sample of customer data of  of telecom operator Megaline which offers its clients two prepaid plans, Surf and Ultimate.  Our job was to analyze clients' behavior and determine which prepaid plan brings in more revenue. 
# 
# The distribution of call minutes used per month seemed to approximate a 'normal' distribution for both the Surf and Ultimate plans.  The mean call minutes used per month for Surf is 436.5 minutes and for Ultimate 434.7 minutes.  The maximum monthly usage for those on the Surf plan in this sample was 1510 minutes, compared to 1369 for the Ultimate plan. The standard deviation for Ultimate is 237.7 which is greater than the variance for Surf (at 229.2).
# 
# The distribution of the number of texts sent per month looked less like a 'normal' distribution. The mean for Surf is 40.1 texts per month and for ultimate is higher at 46.2 texts per month.  The standard deviations however for both plans are very similar: 33.0 for Surf and 32.9 for Ultimate.
# 
# The distribution of the volume of data used per month looks very much like a 'normal' distribution for both the Surf and Ultimate plans. The mean for Ultimate is higher at 17,238mb compared to 16,717mb for Surf. However, the standard deviations for both plans are very similar: 7,882mb for Surf and 7,825mb for Ultimate.
# 
# We conclude that the behaviour of customers on the Surf and Ultimate plans is very similar. Despite the Ultimate plan being more expensive and having greater allowances, Surf customer use slightly more call minutes per month, on average. Ultimate customers do use more data per month that Surf customers, but not significantly more: 17.3GB compared to 16.7GB. Again, the standard deviations for both are very similar.  
# 
# Given this it would appear that the Ulimate plan should be more profitable and we discovered that the mean revenue from Surf is 63.44USD and from Ultimate 72.68USD. Given however that the standard deviations for each are very different (57.34USD for Surf and 12.63USD for Ultimate) we ran a statistical test to check the probability that the means were indeed different.
# 
# We concluded, given the low p-value that there is a very small probability of them randomly being the same. This probability was low enough to conclude that we can reject the probability that the average revenues are the same for both groups. So yes, **it is probable that the average revenue from Users of Surf and Ultimate does differ**.
# 
# We than ran a second statistical test to check if the average revenue from users in NY-NJ area is different from that of the users from other regions. This time the p-value was higher than the critical statistical significance level. Given this, we could not reject the null hypothesis that the average revenue from users in the NY-NJ area is the same as that of users in other regions. So **we cannot say that the averages are different in the two geographical regions**.

# %% [markdown]
# <div class="alert alert-block alert-info">
#     
# <b>Senior reviewer's comment</b> <a class="tocSkip"></a>
#     
# The final conclusion must necessarily reflect the purpose of the study - it is necessary to determine a profitable tariff plan for a mobile operator.
#     
# If the student did not do this - gross mistake, red comment.
#     
# At the same time, students may come to different conclusions.
#     
# For instance, the author's solution mentions that the Smart tariff is more profitable, because:
#     
# "Users of the Ultra tariff spend chaotically, there is no clear trend over the months.
#     
# However, on average, most customers stay within the monthly fee - less than a quarter of customers pay extra for exceeding the limits.
#     
# Most often, users exceeded the Internet traffic limits.
#     
# This is the reason for the higher percentage of revenue from Smart tariff users.
#     
# In addition, the maximum revenue in the sample corresponds to the subscriber of this tariff plan."
#     
# The following chart can be used for confirmation:
#     
# Although the last graph shows that the average monthly fee for the Smart tariff is growing, which is not the case for the Ultra tariff, we only have data on the annual dynamics.
#     
# That is, it may be due to seasonality.
#     
# To be sure that growth will continue, we need data for at least a few months of the previous year.
#     
# The monthly payments of Ultra tariff users rarely exceed the monthly fee.
#     
# But they don´t spend the full package of services, and at the same time, their monthly payment is statistically much higher than the monthly payment of the Smart tariff.
#     
# Therefore, for the time being, the Ultra tariff is more profitable for the mobile operator.
#     
# Conclusion: in case experts give different recommendations, then it is not the tariff indicated by the student as the most profitable that you need to focus on.
#     
# Instead, look at the arguments provided in favor of this conclusion.
#     
# Absence of justification is a gross mistake, red comment.
# 
# </div>


