# %% [markdown]
# ### Project description
# The online store Ice sells video games all over the world. User and expert reviews, genres, platforms (e.g. Xbox or PlayStation), and historical data on game sales are available from open sources.
#
# We need to identify patterns that determine whether a game succeeds or not. This will allow us to spot potential big winners and plan advertising campaigns.

# %% [markdown]
# ### Importing libraries

# %%
import plotly.express as px
import pandas as pd
import sidetable as stb
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from functools import reduce
from scipy import stats
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
pd.options.display.float_format = '{:.2f}'.format

# %% [markdown]
# ### Reading and studying the data

# %%
data = pd.read_csv('datasets/games.csv')

# %%
data
data.info()
data.describe()

# %%
data.duplicated().sum()
data.stb.missing(style=True)

# %% [markdown]
# #### Conclusion

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#     It's great that you checked for duplicates in the dataset and made sure there were none.  I like that you use a variety of methods when studying general information in table. Good job!</div>

# %% [markdown]
# The initial dataset is comprised of 16,715 rows and 11 columns. We can see that we'll need to normalize column names. We identified missing values (up to 51%) in different columns and we found no duplicates. The data types are mostly OK except for Year_of_release and User_score columns.

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Often students try to find the release year - for example, looking for the year in the title of the game using lemmatization.
#
# No need to scold them for it, but you can give advice:
#
# immediately remove such a small proportion of gaps to save time;
#
# check the result - not always 4 digits in the game name indicate the year of release.
#
# Filling gaps in years with mean/median/minimum, etc. values is considered a gross mistake, we mark it with a red comment.
#
#
# </div>

# %% [markdown]
# ### Preparing the data

# %% [markdown]
# #### Lowering headers case and dealing with the missing values

# %%
data.columns = data.columns.str.lower()
data['year_of_release'] = data['year_of_release'].fillna(0).astype('int')
data.loc[data['user_score'] == 'tbd', 'user_score'] = np.nan
data['user_score'] = data['user_score'].astype('float')
data.info()

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#     Very well that you converted the columns to lower case using <code>str.lower()</code>
#
# Agree with your decision not to fill the missing values with the median, for example. But in this case we can just remove missing values :)</div>

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Successful solutions are the following:
#
# entering a unreal value(-1,-999999, etc);
#
# leaving the gaps unchanged.
#
# The second option can potentially lead to problems when analyzing games by region, we need to track this down.
#
# Deleting rows with gaps in the Rating column is considered a gross mistake, we mark it with a red comment. Explanation for the student: "This way our dataset will become much poorer, losing more than a third of the lines that contain information about sales, release date, and platform. The data in these columns will be useful for finding answers to all questions in the assignment, while the rating information is needed for only one question."
#
#
# An attempt to restore the rating by "replacing all gaps with one rating value, for example, E" is considered a gross mistake, we mark it with a red comment. Instead of explaining, I ask the student: "Why do you think that such a replacement is appropriate?"
#
# An attempt to fill in the gaps in a more complex way - for example, splitting games into groups by genre and filling in the gaps with the most popular value of every genre - should be marked with a yellow comment.
#
# Explanation for the student: "You did a great job filling the gaps.But sometimes the gap itself constitutes valuable information.What countries was the ESRB system created for?Will the authors of the local market games in other countries try to get an ESRB rating?"
#
#
# </div>

# %%
data['rating'].unique()

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Successful solutions for handling gaps in columns with reviews of critics / users are the following:
# entering a unreal value;
#
# leaving the gaps unchanged.
#
# The first option could potentially lead to problems when analyzing the impact of reviews on sales, you need to track this.
# Deleting rows with gaps in the Reviews columns is considered a gross mistake, we mark it with a red comment. Explanation for the student: "This way our dataset will become much poorer, losing more than a third of the lines that contain information about sales, release date, and platform.  The data in these columns will be useful for completing the major part of the assignment.  Besides, the newest games usually don't have reviews - and their sales information is the most valuable."
#
#
# An attempt to fill in the gaps by "replacing all gaps with a median / mean value for the entire dataset" is considered a gross mistake, we mark it with a red comment. Instead of explaining, I ask the student: "Why do you think that such a replacement is appropriate?"
#
# An attempt to fill in the gaps in a more complex way - for example, splitting games into groups by genre and filling in the gaps with the mean / median value of every genre - should be marked with a yellow comment.
#
# Explanation for the student: "You did a great job filling the gaps.But such a significant proportion of gaps can hardly be correctly restored from the available values."
#
#
#
#
#
# </div>

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Almost no one replaces rare options with analogues - therefore you can give the following advice as developmental feedback: "Look at how often different rating values occur. Perhaps rare values can be replaced with more common ones.
# Or, if they make up a negligible fraction of the data, they can be deleted."
#
#
# Important - the student can make this substitution later in the project: before evaluating the impact of the ESRB rating on sales in a particular region.
#
#
#
#
#
#
# </div>

# %% [markdown]
# #### Calculating total sales revenue

# %%
data['total_sales'] = data[['na_sales', 'eu_sales',
                            'jp_sales', 'other_sales']].sum(axis=1)
data.nlargest(5, ['total_sales'])
data.info()

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#
#    `total_sales` is calculated correctly. Thanks for using `sum(axis=1)`. This way your code looks more professionally.
#
#
# </div>
#

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Typically students don't use the games[['na_sales','eu_sales','jp_sales', 'other_sales']].sum(axis = 1) construction - you can mention it as a tip.
#
#
#
#
#
#
#
# </div>

# %% [markdown]
# #### Conclusion

# %% [markdown]
# We lowered the case for headers and changed data type for Year_of_release column.
# We dealt with the missing values in the following way:
#
#    *Year_of_release*: We don't have many missing values here so we changed them to zero as it doesn't affect the results of our analysis.
#
#    *Critic_score*: there's nothing we can do to fill it in so we leave the missing values as they are.
#
#    *User_score*: again there's nothing we can do to fill in missing values or values for games where rating is pending ('tbd'). We changed 'tbd' values to 'NaN' in order to change data type leave is as it is.
#
# We leave the other missing values as they are because those are object data types that we can not fill in. Still they might not have any visible impact on the results of our analysis.
#
# Finally we calculated Total_sales column as requested.

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
# Thanks for the detailed conclusions!</div>

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Frequent gross mistakes, red comment:
#
# forgetting about the tbd value;
#
# deleting lines with tdb;
#
# handling gaps and tdb in different ways.
#
#
# Make sure that the student has provided data types in the critic_score, user_score, year_of_release columns - otherwise, we mark it as a gross mistake, a red comment, or a yellow comment, depending on the number of other mistakes.
# Obviously, if the entire project is already highlighted in red, then there is no point in converting a float into an int.
#
#
#
#
#
# </div>

# %% [markdown]
# ### Analyzing the data

# %% [markdown]
# #### Looking at games releases

# %%
df_count = data[
    ['year_of_release', 'name']].groupby(['year_of_release']).count().sort_values(by='name').reset_index(
)
df_count = df_count[df_count['year_of_release'] != 0]

# %%
fig, ax = plt.subplots(figsize=(15, 10))
ax.vlines(x=df_count.year_of_release, ymin=0, ymax=df_count.name,
          alpha=0.5, linewidth=10, color='green')
ax.set_title('Games releases per year', size=15)
ax.set_ylabel('Number of games')
ax.set_xlabel('Year of release')
ax.set_xticks(df_count.year_of_release)
ax.set_xticklabels(df_count.year_of_release, rotation=90)

# %% [markdown]
# **Comment:**
# *The graph shows the amount of games released per year. We can see a rapid growth in late 90's with a peack in late 2008-2009 and stagnation in 2010's.*

# %% [markdown]
# #### Looking at sales distribution

# %%
df_sales = data[['platform', 'total_sales']].groupby(
    ['platform']).sum().sort_values(by='total_sales').reset_index(
)
df_sales['z_score'] = (df_sales['total_sales'] -
                       df_sales['total_sales'].mean())/df_sales['total_sales'].std()
df_sales['color'] = ['red' if x < 0 else 'green' for x in df_sales['z_score']]
df_sales

# %%
plt.figure(figsize=(15, 10))
plt.hlines(
    y=df_sales.platform, xmax=df_sales.z_score, xmin=0, color=df_sales.color, linewidth=10, alpha=0.5
)
plt.ylabel('Platform')
plt.xlabel('Z score')
plt.title('Sales revenue per platform', size=15)

# %% [markdown]
# **Comment:**
# *Here we can see most profitable platforms (green) and less profitable (red). We calculated z_score to show how far each platform revenue is from overall mean value (z-score=0).*

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#    Wow, it's really great that you use the z-score for the determining of the most dominant platforms for the whole period 👏 👏 👏   </div>

# %% [markdown]
# #### Looking at platforms lifetime

# %%
df_lifetime = pd.pivot_table(
    data, index='year_of_release', columns='platform', values='total_sales', aggfunc='sum').fillna(0
                                                                                                   )
df_lifetime = df_lifetime.iloc[1:, :]
df_lifetime

# %%
sns.set(rc={'figure.figsize': (15, 10)})
sns.lineplot(data=df_lifetime)
plt.ylabel('Revenue')
plt.xlabel('Year')
plt.title('Platforms lifetime', size=15)

# %% [markdown]
# **Comment:**
# *This graph shows a platform lifetime from first sales to oblivion. We can see that on average popular platforms "live" for about 10 years before they fade away.*

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#   I like that you use a variety of charts in your research. </div>

# %% [markdown]
# #### Choosing relevant data for analysis

# %%
good_data = data[data.year_of_release >= 2013]

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# The ideal period would be 2014-2016 or 2015-2016 or 2013- 2016 - that is, a period of 2-3 years, including the data for 2016.
# A period of 4-5 years including or excluding data for 2016 is considered acceptable.
#
# If a student took a period of more than 5 years - this is a gross mistake and a red comment.
#
# Message to the student: "It is uncommon to use data for more than 2-3 years when forecasting next year's sales, even in case of traditional businesses.   And in the dynamic computer games industry, taking longer time intervals should be avoided as it will definitely lead to tracking some obsolete trends. But you shouldn't take too short a period either."
#
# If a student took a period of 4-5 years, we write the same text in a yellow comment.
#
# Deleting the data for 2016 is not considered a gross mistake - at least the student read the text of the assignment till the end and tried to put what he read into practice.
#
# But there should be the following note in a yellow comment: "Usually, the forecast for the next year is made in October, when the current year is not yet closed.At the same time, the data of the current year is not deleted, since it contains the most recent information, albeit not complete. Therefore, it is better to leave 2016 in the dataset for further analysis."
#
#
#
#
# </div>

# %%
df_lifetime_new = pd.pivot_table(
    good_data, index='year_of_release', columns='platform', values='total_sales', aggfunc='sum').fillna(0)
sns.set(rc={'figure.figsize': (15, 10)})
sns.lineplot(data=df_lifetime_new)
plt.ylabel('Revenue')
plt.xlabel('Year')
plt.title('New platforms lifetime', size=15)

# %% [markdown]
# **Comment:**
# *This graph shows platforms revenue over time within the chosen period, i.e. 2013-2016. We can see that revenue of all platforms is declining.*

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Also student can plot different plots for platforms.
#
#
#
#
# </div>

# %%
# Reviewer's code
plot_data = good_data.groupby(['year_of_release', 'platform']).agg({
    'total_sales': 'sum'}).reset_index()

fig = px.line(plot_data, x="year_of_release", y="total_sales",
              color='platform', title="New platforms lifetime")
fig.show()

# %%
plt.figure(figsize=(15, 10))
sns.boxplot(x='platform', y='total_sales', data=good_data)
plt.ylim(0, 3)
plt.ylabel('Revenue')
plt.xlabel('Platform')
plt.title('Revenue distribution per game', size=15)

# %% [markdown]
# **Comment:**
# *Here we can see revenue distribution per game for each platform. The most perspective platforms as per graph are PS3, PS4, WiiU, Wii, X360 and XOne.*

# %% [markdown]
# #### Finding correlation between sales and ratings

# %%
PS4_df = good_data.groupby(
    ['platform', 'name'])[['total_sales', 'critic_score', 'user_score']].sum(
).query('platform == "PS4" & critic_score > 0 & user_score > 0').reset_index(
)

# %%
PS4_df['total_sales'].corr(PS4_df['critic_score'])

# %%
print("Positive correlation between Revenue and critics' rating for PS4")
plt.figure(figsize=(15, 10))
sns.scatterplot(x="critic_score", y="total_sales", data=PS4_df, alpha=0.7)
plt.ylabel('Revenue')
plt.xlabel('Rating')
plt.title('PS4 Correlation of critic score and sales revenue', size=15)

# %%
PS4_df['total_sales'].corr(PS4_df['user_score'])

# %%
print("A weak negative correlation between Revenue and users' rating for PS4")
plt.figure(figsize=(15, 10))
sns.scatterplot(x="user_score", y="total_sales", data=PS4_df, alpha=0.7)
plt.ylabel('Revenue')
plt.xlabel('Rating')
plt.title('PS4 Correlation of user score and sales revenue', size=15)

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#     Wonderful visualization! 😊  Yep, the platform PS4 is the most popular.</div>

# %%
X360_df = good_data.groupby(
    ['platform', 'name'])['total_sales', 'critic_score', 'user_score'].sum(
).query('platform == "X360" & critic_score > 0 & user_score > 0').reset_index(
)

# %%
X360_df['total_sales'].corr(X360_df['critic_score'])

# %%
print("Positive correlation between Revenue and critics' rating for X360")
plt.figure(figsize=(15, 10))
sns.scatterplot(x="critic_score", y="total_sales", data=X360_df, alpha=0.7)
plt.ylabel('Revenue')
plt.xlabel('Rating')
plt.title('X360 Correlation of critic score and sales revenue', size=15)

# %%
X360_df['total_sales'].corr(X360_df['user_score'])

# %%
print("A weak positive correlation between Revenue and users' rating for X360")
plt.figure(figsize=(15, 10))
sns.scatterplot(x="user_score", y="total_sales", data=X360_df, alpha=0.7)
plt.ylabel('Revenue')
plt.xlabel('Rating')
plt.title('X360 Correlation of user score and sales revenue', size=15)

# %%


def corr_func(platform):
    data = good_data[good_data['platform'] == platform]
    corr = good_data[good_data['platform'] == platform][[
        'critic_score', 'user_score', 'total_sales']].corr()['total_sales']
    data.plot(y='total_sales', x='critic_score',
              kind='scatter', alpha=0.7, grid=True)
    plt.title(platform)
    data.plot(y='total_sales', x='user_score',
              kind='scatter', alpha=0.7, grid=True)
    plt.title(platform)
    print(platform, corr)
    print('-----')


# %%
platforms = ['PS4', 'WiiU', 'XOne', 'PS3', 'X360', 'Wii']
for i in platforms:
    corr_func(i)

# %% [markdown]
# #### Finding out how revenue is affected by genre

# %%
print('Almost all genres show good sales revenue')
df_genre = good_data.groupby(['genre', 'name'])[
    'total_sales'].sum().reset_index()
df_genre = df_genre.query('1<total_sales<10')
plt.figure(figsize=(15, 10))
sns.boxplot(x='genre', y='total_sales', data=df_genre)
plt.ylabel('Revenue')
plt.xlabel('Genre')
plt.title('Revenue distribution per game', size=15)

# %% [markdown]
# #### Conclusion

# %% [markdown]
# First we looked at game releases per year. We built a histogram and see that the distribution is skewed to the left. No wonder as the game industry began to grow rapidly in late 90’s.
#
# We grouped the data by platform and total revenue and calculated a z_score which shows for each platform how far total revenue is from the overall mean in terms of standard deviation. Then we built a graph showing the distribution of revenue for all the platforms.
#
# We also created a dataset showing a platform lifetime from the first sales to oblivion and built a lineplot showing this lifetime. We can see that on average a platform “lives” about 10 years before it completely fades away. Still that's a large period for decided to take the last ten years of data into consideration for our project as it will include all the relevant platforms.
#
# Using a lineplot for selected data we can see that the leading platforms in the last few years were PS3, PS4, XOne, X360 and 3DS. However, the graph shows that sales revenue for all platforms is declining.
#
# We built a boxplot based on selected data grouped by name and platform in order to determine how revenue is distributed across platforms. We found out that the platforms we chose previously are indeed the leading ones with higher total revenues and higher mean values than the rest. Except for WiiU platform that apparently has major outliers, namely Super Mario series which brought outstanding revenues to the platform in middle 2010’s.
#
# We chose two popular platforms - PS4 and X360 - to see how critic and user rating can affect sales. We built scatterplots for each case and we can see a robust positive correlation for critic reviews (nearly 0.4 for both platforms), i.e. higher score usually brings more revenue. However, the correlation between user score and revenue is about zero which means that sales revenue is not affected much by users’ opinion.
#
# Finally, we built a box plot to see how revenue is distributed among genres. We cut off the revenue outliers to have a closer look. We can see that all genres except Adventure, Puzzle and Strategy show good sales and high mean values. This might be the case because genres get mixed and a single game can be assigned multiple genres, like Action-Fighting or Simulation-Racing games.

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#
# Great job! Especially impressed:
#
# - typical lifespan you determine correctly
#
# - z-score for the determining of the most popular platforms for the whole period
#
# - you have the titles and axes captions for all the graphs
#
#
#
#
# Thank you for in-depth analysis and logical conclusions! </div>

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# For example, seeing that the correlation coefficient between sales and user ratings is "-0.05", a student can write: "there is a weak negative correlation between sales and user ratings".
#
# Pay attention to this and explain how to interpret such values correctly.
#
# Having put a unreal value when processing gaps, students forget to exclude it from the graphs and correlation calculation.
# An example of graphs and calculations containing an error is given in the cell below.
#
# As a result, they receive distorted calculations.You need to get them to filter these values.
#
# A student might analyze of only 1 platform - in this case, draw his attention to the next item of the task: "Relate the conclusions with game sales on other platforms."
#
# You could also mention that the conclusions drawn on the basis of calculations for several platforms look "weighty" and more convincing.
#
#
# Often students look only at the total sales of games by genre and conclude that Action is the most profitable genre.
# This is a gross mistake, red comment.
#
# Get the student to study average/median sales: "Total sales are a poor metric for finding the most profitable genre.
# High overall sales figures can hide a lot of small games with low sales.
#
# Or 2-3 stars and a bunch of failures.
# It would be better to find a genre of games that consistently generate high revenue; to do so, you should consider average or median sales."
#
#
#
#
# </div>

# %% [markdown]
# ### Creating a user profile for each region

# %%
na_platform = good_data.groupby(
    ['platform'])['na_sales'].sum().reset_index().sort_values(by='na_sales', ascending=False
                                                              )
jp_platform = good_data.groupby(
    ['platform'])['jp_sales'].sum().reset_index().sort_values(by='jp_sales', ascending=False
                                                              )
eu_platform = good_data.groupby(
    ['platform'])['eu_sales'].sum().reset_index().sort_values(by='eu_sales', ascending=False
                                                              )
na_platform.sum()
na_platform.head()
eu_platform.sum()
eu_platform.head()
jp_platform.sum()
jp_platform.head()

# %% [markdown]
# <div style="border:solid orange 2px; padding: 20px"> <b>Remarks:</b><br>
#   For a clearer analysis of the game market in different regions it is better to use charts. For example, you can add pie plots or bar plots :)</div>

# %%
na_genre = good_data.groupby(
    ['genre'])['na_sales'].sum().reset_index().sort_values(by='na_sales', ascending=False).head()
jp_genre = good_data.groupby(
    ['genre'])['jp_sales'].sum().reset_index().sort_values(by='jp_sales', ascending=False).head()
eu_genre = good_data.groupby(
    ['genre'])['eu_sales'].sum().reset_index().sort_values(by='eu_sales', ascending=False).head()
na_genre.head()
eu_genre.head()
jp_genre.head()

# %%
good_data.groupby(['rating'])[['na_sales', 'eu_sales', 'jp_sales']].agg(
    'sum').sort_values(by='na_sales', ascending=False)


# %% [markdown]
# #### Conclusion

# %% [markdown]
# We created multiple dataframes to see the top players on each market in terms of platform, genre and rating.
#
# First of all we looked at platforms and see that revenue is not equally distributed across the regions: NA brought 438 million to game developers in the respective period which is 3 times more than Japan. We can see that PS3 is doing better in EU region than in NA region and that XBox is not in top five in Japan. This might be because the market is special and relatively small and doesn't respond to global trends. We can see that top five platforms in Japan are originally local brands: Sony and Nintendo.
#
# Secondly, we looked at top five genres for each region and again NA and EU look alike except for the fifth place: Misc. (NA) vs. Racing (EU). Japan top five genres have Role-playing on top, Action is second and Shoter's the last.
#
# Finally, the ESRB rating for NA and EU regions are the same - "M", "E", "E10+", "T". This means that for these two regions the age of players has similar distribution.
# In Japan however the revenue distribution differs - "T" is on the 1st place, than "E" and "M".

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#     Technically everything is correct here, I really like your detailed conclusions, but due to the fact that the period previously selected was not actual, the platforms here are not quite up to date. As soon as you fix the actual period, everything will be okay here. Can you please write here your guesses as to what may be related similarities and differences in the most popular platforms in different regions?</div>

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Common gross mistake, red comment: Students don't replace gaps in the rating column with a unreal value and end up losing the entire data on unrated games.
#
# Message to the student: "Using this method of calculation, you completely excluded unrated games from the analysis.
# But the sales of these particular games may indicate a key difference between regions.
#
# Students can be given the following advice:
#
# if the graph for each region is built by a separate line of code - plot 3 graphs side by side using subplots;
#
# if subplots is successfully applied - check if there is a "two level header" - both for all three graphs together, and for each of the three separately;
#
# when analyzing platforms and genres, everything that is not included in the TOP-5? should be combined into "others" - so that the analysis picture is more complete.
#
# Average user ratings for Action and Sports are different
#
#
#
#
#
# </div>

# %% [markdown]
# ### Hypotheses testing

# %% [markdown]
# #### Hypothesis 1: Average user ratings of the Xbox One and PC platforms are the same

# %%
hyp_data = good_data.query(
    'user_score > 0 & platform == "XOne" or user_score > 0 & platform == "PC"')
fig, ax = plt.subplots(figsize=(15, 10))
sns.histplot(hyp_data, x='user_score', hue='platform')
plt.ylabel('Frequency')
plt.xlabel('Rating')
plt.title('User rating distribution per platform', size=15)

# %%
# Reviewer's code
hyp_data[(hyp_data['platform'] == 'PC') & (hyp_data['user_score'] == 0)]

# %%
fig, ax = plt.subplots(figsize=(5, 10))
ax = sns.boxplot(x='platform', y='user_score', data=hyp_data)
plt.ylabel('Rating')
plt.xlabel('Platform')
plt.title('User rating distribution per platform', size=15)

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#
#  It's great that you visualized the sample distributions!  </div>

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Graphs is an option.
#
#
#
#
#
# </div>

# %%
hyp_data.groupby(['platform'])['user_score'].agg('mean')

# %%
XOne_df = hyp_data.query('platform == "XOne"')
PC_df = hyp_data.query('platform == "PC"')

# %% [markdown]
# **We formulate the hypotheses as follows:**
#
#  - Null-hypothesis: There are no statistically significant differences between the average user ratings of Xbox One and PC platforms;
#  - Alternative hypothesis: The differences between average user ratings of the Xbox One and PC platforms are statistically significant.
#
# *We choose alpha parameter equal **5%** as a standart threshold for our kind of business.*

# %%
alpha = 0.05

# %%
p_value_levene = stats.levene(
    XOne_df['user_score'], PC_df['user_score']).pvalue
if p_value_levene < alpha:
    print('Reject H0: variance of sample 1 is not equal to variance of sample 2')
else:
    print("Fail to Reject H0: We don't have enough evidence to say that variances of sample 1 and sample 2 are not the same")

# %%
p_value = stats.ttest_ind(
    XOne_df['user_score'], PC_df['user_score'], nan_policy='omit', equal_var=False).pvalue
if p_value < alpha:
    print("Reject H0: There are statistically significant differences between the average average user ratings of Xbox One and PC platforms.")
else:
    print("Fail to Reject H0: We don't have enough evidence to say that the difference between average user ratings of the Xbox One and PC platforms is statistically insignificant.")
p_value

# %% [markdown]
# #### Hypothesis 2: Average user ratings for the Action and Sports genres are the same

# %%
hyp_data2 = good_data.query(
    'user_score > 0 & genre == "Sports" or user_score > 0 & genre == "Action"')
fig, ax = plt.subplots(figsize=(15, 10))
sns.histplot(hyp_data2, x='user_score', hue='genre')
plt.ylabel('Frequency')
plt.xlabel('Rating')
plt.title('User rating distribution per genre', size=15)

# %%
fig, ax = plt.subplots(figsize=(5, 10))
ax = sns.boxplot(x='genre', y='user_score', data=hyp_data2)
plt.ylabel('Rating')
plt.xlabel('Genre')
plt.title('User rating distribution per platform', size=15)

# %%
hyp_data2.groupby(['genre'])['user_score'].agg('mean')

# %%
Sports_df = hyp_data2.query('genre == "Sports"')
Action_df = hyp_data2.query('genre == "Action"')

# %% [markdown]
# **We formulate the hypotheses as follows:**
#
#  - Null-hypothesis: Average user ratings for the Action and Sports genres belong to the same statistical population;
#  - Alternative hypothesis: Average user ratings for the Action and Sports genres do not belong to the same statistical population.
#
# *We choose alpha parameter equal **5%** as a standart threshold for our kind of business.*

# %%
alpha = 0.05

# %%
p_value_levene = stats.levene(
    Sports_df['user_score'], Action_df['user_score']).pvalue
if p_value_levene < alpha:
    print('Reject H0: variance of sample 1 is not equal to variance of sample 2')
else:
    print("Fail to Reject H0: We don't have enough evidence to say that variances of sample 1 and sample 2 are not the same")

# %%
p_value = stats.ttest_ind(
    Sports_df['user_score'], Action_df['user_score'], nan_policy='omit', equal_var=False).pvalue
if p_value < alpha:
    print("Reject H0: Average user ratings for the Action and Sports genres do not belong to the same statistical population.")
else:
    print("Fail to Reject H0: We don't have enough evidence to say that average user ratings for the Action and Sports genres belong to different statistical populations.")
p_value

# %% [markdown]
# #### Conclusion

# %% [markdown]
# We formulated and run the tests on both hypotheses and see that in the first case we failed to reject the null-hypothesis and in the second case we rejected the null-hypothesis.

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>Senior Reviewer's comment </b> <a class="tocSkip"></a>
#
# Students do not formulate hypotheses / formulate only 1 hypothesis / formulate hypotheses incorrectly.
#
# They try to apply the criterion for one sample st.ttest_1samp to two samples.
#
# They don't remove gaps (if there are any left) - get results.pvalue equal to NaN.
#
# Students do not remove unreal values (if they were entered) - and get errors in calculations.
#
# The Equal_Var parameter is not set based on the calculation of dispersions. The approach has changed, we do not require it anymore.
#
# They conclude that the tests "confirm" one of the hypotheses - it is impossible to confirm the hypothesis in statistics.
# They don't output results.pvalue, so if it's calculated incorrectly (e.g. equals to NaN) it will not be visible.
# Samples are "averaged" beforehand: for example, 500 values are selected from each, trying to bring both samples to the same size.
#
# You should write that equality of sample sizes is not required for testing hypotheses, moreover, it is more common to use samples that are not equal in size.
#
#
#
#
#
# </div>

# %% [markdown]
# ### Overall conclusion

# %% [markdown]
# **Working on the dataset**
#
# Our goal was to study the data, analyze the aspects affecting sales revenue of games in order to spot potential winners. We've got a dataset that contained name of the game, year of release, platform, genre, sales revenue in different regions and different ratings. We examined the datasets and discovered some weired data and some missing data.
#
# **Data preprocessing**
#
# We lowered the case for headers and changed data type for Year_of_release column.
# We dealt with the missing values in the following way:
#
#    *Year_of_release*: We don't have many missing values here so we changed them to zero as it doesn't affect the results of our analysis.
#
#    *Critic_score*: we looked for games with same names but missing score and filled it. We changed the rest to zero as there's nothing we can do to fill it in.
#
#    *User_score*: again we looked for games with same names but missing score and filled it. However here we had to first create a separate dataframe that would not contain 'tbd' values. As well as we did previously, we changed the rest of 'NaN' and 'tbd' values to zero as there's nothing we can do to fill them in.
#
# We leave the other missing values as they are because those are object data types that we can not fill in. Still they might not have any visible impact on the results of our analysis.
#
# Finally we calculated Total_sales column as requested.
#
# **Making calculations**
#
# First we looked at game releases per year. We built a histogram and see that the distribution is skewed to the left. No wonder as the game industry began to grow rapidly in late 90’s.
#
# We grouped the data by platform and total revenue and calculated a z_score which shows for each platform how far total revenue is from the overall mean in terms of standard deviation. Then we built a graph showing the distribution of revenue for all the platforms.
#
# We also created a dataset showing a platform lifetime from the first sales to oblivion and built a lineplot showing this lifetime. We can see that on average a platform “lives” about 10 years before it completely fades away and decided to take the last ten years of data into consideration for our project as it will include all the relevant platforms.
#
# Using a lineplot for selected data we can see that the leading platforms in the last few years were PS3, PS4, XOne, X360 and 3DS. However, the graph shows that sales revenue for all platforms is declining.
#
# We built a boxplot based on selected data grouped by name and platform in order to determine how revenue is distributed across platforms. We found out that the platforms we chose previously are indeed the leading ones with higher total revenues and higher mean values than the rest. Except for WiiU platform that apparently has major outliers, namely Super Mario series which brought outstanding revenues to the platform in middle 2010’s.
#
# We chose two popular platforms - PS4 and X360 - to see how critic and user rating can affect sales. We built scatterplots for each case and we can see a robust positive correlation for critic reviews (nearly 0.4 for both platforms), i.e. higher score usually brings more revenue. However, the correlation between user score and revenue is about zero which means that sales revenue is not affected much by users’ opinion.
#
# Finally, we built a box plot to see how revenue is distributed among genres. We cut off the revenue outliers to have a closer look. We can see that all genres except Adventure, Puzzle and Strategy show good sales and high mean values. This might be the case because genres get mixed and a single game can be assigned multiple genres, like Action-Fighting or Simulation-Racing games.
#
# **Creating a user profile for each region**
#
# First of all we looked at platforms and see that revenue is not equally distributed across the regions: NA brought 438 million to game developers in the respective period which is 3 times more than Japan. We can see that PS3 is doing better in EU region than in NA region and that XBox is not in top five in Japan. This might be because the market is special and relatively small and doesn't respond to global trends. We can see that top five platforms in Japan are originally local brands: Sony and Nintendo.
#
# Secondly, we looked at top five genres for each region and again NA and EU look alike except for the fifth place: Misc. (NA) vs. Racing (EU). Japan top five genres have Role-playing on top, Action is second and Shoter's the last.
#
# Finally, the ESRB rating for NA and EU regions are the same - "M", "E", "E10+", "T". This means that for these two regions the age of players has similar distribution.
# In Japan however the revenue distribution differs - "T" is on the 1st place, than "E" and "M".
#
# **Testing hypotheses**
#
# We formulated and tested the following hypotheses:
# 1. Average user ratings of the Xbox One and PC platforms are the same.
# 2. Average user ratings for the Action and Sports genres are the same.
#
# We chose alpha parameter equal to 5% as it is a standard for this type of busines and everything falling below this threshold can be considered accidential.
#
# As a result we failed to reject the first null-hypothesis meaning ***we don't have enough evidense to state whether the average user ratings of the Xbox One and PC platforms are not the same.***
#
# And the second null-hypothesis was rejected which means that in the second case ***the average user ratings for the Action and Sports genres are not the same.***
#
# **Our conclusion**
#
# We can draw the following conclusions:
# 1. The lifetime of a platform is about 10 years;
# 2. The most profitable platforms in the chosen period are those made by Microsoft, Sony and Nintendo;
# 3. Sales revenue usually depends on critics' score and does not depend on users' opinion;
# 4. The trending genres are Action, Shooter, Sports and Role-playing;
# 5. In order to succeed the ESRB rating must be either "E" or "M".

# %% [markdown]
# <div style="border:solid green 2px; padding: 20px"> <b>Success:</b><br>
#    I like that you wrote such in-depth conclusions on the whole study, proved them with numbers and made logical assumptions. Thank you for your work! It's really great! 👏👏👏</d
