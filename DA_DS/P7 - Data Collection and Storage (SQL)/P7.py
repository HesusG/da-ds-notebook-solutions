# %% [markdown]
# ## Project Description
# ### Objective
# You're working as an analyst for Zuber, a new ride-sharing company that's launching in Chicago. Your task is to find patterns in the available information. You want to understand passenger preferences and the impact of external factors on rides. You'll study a database, analyze data from competitors, and test a hypothesis about the impact of weather on ride frequency.
# 
# 
# ### Outline
# 
# - Web Scraping
#     - Write a code to parse the data on weather in Chicago in November 2017 from the website: https://code.s3.yandex.net/data-analyst-eng/chicago_weather_2017.html
# - Exploratory Data Analysis I (SQL).
#     - Number of trips by company Nov 15-16, 2017
#     - Number of trips for companies that include 'Yellow' or 'Blue' in name Nov 1-7, 2017
#     - Number of November 2017 trips split by 3 company segments: 'Flash Cab', 'Taxi Affiliation Service', 'Other'
# - Hypothesis Testing (SQL)
#     - Test the hypothesis that the duration of rides from the the Loop to O'Hare International Airport changes on rainy Saturdays.
# - Exploratory Data Analysis (Python)
#     - identify the top 10 neighborhoods in terms of drop-offs
#     - make graphs: taxi companies and number of rides, top 10 neighborhoods by number of dropoffs
#     - draw conclusions based on each graph and explain the results
# 
# - Hypothesis Testing (Python)
# 
#     - The result of the last query contains data on rides from the Loop to O'Hare International Airport. 
# 
#     - Test the hypothesis: "The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays."
# Decide where to set the significance level (alpha) on your own.
#     - Explain: how you formed the null and alternative hypotheses what criterion you used to test the hypotheses and why
# 
# ### Description of data
# SQL Results:
# - company_name: taxi company name
# - trips_amount: the number of rides for each taxi company on November 15-16, 2017.
# - dropoff_location_name: Chicago neighborhoods where rides ended
# - average_trips: the average number of rides that ended in each neighborhood in November 2017
# - start_ts: pickup date and time
# - weather_conditions: weather conditions at the moment the ride started
# - duration_seconds: ride duration in seconds

# %% [markdown]
# ## Exploratory Data Analysis

# %%
# Initialize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as st



# %%
# Import data
company_df = pd.read_csv('/datasets/project_sql_result_01.csv')
trips_df = pd.read_csv('/datasets/project_sql_result_04.csv')

# %%
# Print general/summary info of dataset
company_df.info()


# %% [markdown]
# This dataframe contains taxi company names and the number of rides for each taxi company on November 15-16, 2017. No null values.

# %%
# Descriptive statistics of the data

company_df.describe()

# %% [markdown]
# Tbe average amount of rides per company is 2145 which is considerably less than the most popular company which recorded about 20000 rides on Nov 15-16, 2017.

# %%
# Find top 10 companies
top_10_companies = company_df.sort_values('trips_amount',ascending=False).head(10)
top_10_companies

# %%
# Graph top 10 taxi companies
top_10_companies = top_10_companies.set_index('company_name')
top_10_companies.plot(kind='barh').set_title('Number of Trips per Taxi Company')
plt.xlabel("Company")
plt.ylabel("Number of Trips")
plt.show()

# %% [markdown]
# Flash Cab is overwhelmingly the most popular taxi company, almost double the second, Taxi Affiliation Services.
# 
# 

# %%
# Print general/summary info of dataset

trips_df.info()

# %% [markdown]
# No nulls but average trips is a float which should be an integer as it represented average numnber of trips.
# 
# 

# %%
# Convert average_trips column to int
trips_df['average_trips'] = trips_df.average_trips.astype(int) 


# %%
# Descriptive statistics of the data

trips_df.describe()

# %%
# Find top 10 dropoff locations
top_10_dropoff = trips_df.sort_values('average_trips',ascending=False).head(10)

top_10_dropoff

# %%
# Graph top 10 dropoff locations

top_10_dropoff = top_10_dropoff.set_index('dropoff_location_name')
top_10_dropoff.plot(kind='barh',color='green')
plt.xlabel("Drop Off Location")
plt.ylabel("Average Number of Trips")
plt.title('Average Number of Trips per Drop-off Location')
plt.show()

# %% [markdown]
# Above are the top 10 drop-off locations by number of trips. We can conclude that the most popular area for trips is the Loop neighborhood, which is located near the center of Downtown Chicago.

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
# 
# Sort values for graph is a good practice. If not - yellow comment.
#     
# </div>

# %% [markdown]
# ## Hypothesis Testing

# %%
# Import data
loop_ohare = pd.read_csv('/datasets/project_sql_result_07.csv')
loop_ohare

# %%
# Print general/summary info of dataset

loop_ohare.info()


# %% [markdown]
# This dataframe contains data on rides specificly from the Loop to O'Hare International Airport. There are 1068 entries with no null values.

# %%
# Descriptive statistics 

loop_ohare.describe()

# %% [markdown]
# The average trip duration is  2071 seconds.

# %%
#Check for outliers

sns.boxplot(x="duration_seconds", y="weather_conditions", data=loop_ohare).set_title('Duration (sec) by Weather Condition')
plt.xlabel("Duration in Seconds")
plt.ylabel("Weather Condition");



# %% [markdown]
# According to the descriptive statistics table and boxplot above, there are outliers that may affect the accuracy of our analysis and therefore they will be removed.

# %%
# Remove outliers
condition = 'Good'
Q1 = loop_ohare['duration_seconds'].quantile(0.25)
Q3 = loop_ohare['duration_seconds'].quantile(0.75)
IQR = Q3 - Q1
print('Q1: ', Q1)
print('Q3: ', Q3)
print('IQR: ', IQR)

#
bottom_cutoff = Q1 - (1.5* IQR)
top_cutoff = Q3 + 1.5 * IQR
if bottom_cutoff < 0:
    bottom_cutoff = 0
print('min: ',bottom_cutoff)
print('max: ',top_cutoff)

# %%
# Remove Outliers

loop_ohare_without_outliers = loop_ohare.query('duration_seconds <= @top_cutoff')
sns.boxplot(x="duration_seconds", y="weather_conditions", data=loop_ohare_without_outliers).set_title('Duration (sec) by Weather Condition')
plt.show()

# %% [markdown]
# Test the hypothesis:
# "The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays."
# 
# 
# - Null Hypothesis ($H_O$): "The average duration of rides from the Loop to O'Hare International Airport does not change on rainy Saturdays."
# - Alternate Hypothesis ($H_A$):  "The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays."
# 

# %%
# Hypothesis testing
from scipy import stats as st

alpha = 0.05
sample = loop_ohare_without_outliers.query('weather_conditions == "Good"')
rain_sample = loop_ohare_without_outliers.query('weather_conditions == "Bad"')

results = st.ttest_ind(sample.duration_seconds ,rain_sample.duration_seconds)
print('p-value: ', results.pvalue)

if (results.pvalue < alpha):
        print("We reject the null hypothesis")
else:
        print("We can't reject the null hypothesis")

# %% [markdown]
# As the p-value is less than 0.05, there is a significant difference between the average duration of rides on good weather days vs bad weather days (and very low chance this difference was caused by randomness). Therefore, we can reject the null hypothesis  accept the alternative hypothesis that the average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays.

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
# 
# Graphs in this step are option.
#     
# </div>


