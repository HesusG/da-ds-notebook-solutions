# %%
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

# %%
orders         = pd.read_csv('datasets/instacart_orders.csv', sep=';')
products       = pd.read_csv('datasets/products.csv', sep=';')
departments    = pd.read_csv('datasets/departments.csv', sep=';')
aisles         = pd.read_csv('datasets/aisles.csv', sep=';')
order_products = pd.read_csv('datasets/order_products.csv', sep=';')

# %%
orders.info()

# %%
products.info()

# %%
departments.info()

# %%
aisles.info()

# %%
order_products.info(show_counts=True)

# %% [markdown]
# ## Find and remove duplicate values (and describe why you make your choices)

# %% [markdown]
# ### `orders` data frame

# %%
# Check for duplicated orders
orders[orders.duplicated()]

# %%
# Check for all orders placed Wednesday at 2:00 AM
orders[(orders['order_dow'] == 3) & (orders['order_hour_of_day'] == 2)]

# %%
# Remove duplicate orders
orders = orders.drop_duplicates().reset_index(drop=True)

# %%
# Double check for duplicate rows
orders[orders.duplicated()]

# %%
# Double check for duplicate order IDs only
orders[orders.duplicated(subset='order_id')]

# %% [markdown]
# It looks like there was a Wednesday where all the 2:00 AM orders were duplicated. We removed the duplicate orders from the dataset. Note that there are missing values in the `'days_since_prior_order'` column. We'll come back to those after addressing duplicates in the other tables.

# %% [markdown]
# ### `products` data frame

# %%
# Check for fully duplicate rows
products[products.duplicated()]

# %%
# Check for just duplicate product IDs
products[products.duplicated(subset='product_id')]

# %%
# Check for just duplicate product names (convert names to lowercase to compare better)
products[products['product_name'].str.lower().duplicated()]

# %%
# Check for duplicate product names that aren't missing
products[~(products['product_name'].isna()) & (products['product_name'].str.lower().duplicated())]

# %% [markdown]
# It looks like there are a lot of products in the dataset that have the same name, but different product IDs. These are probably distinct products, so we won't treat them as duplicates. Therefore, the `products` table doesn't contain duplicate values.

# %% [markdown]
# ### `departments` data frame

# %%
departments[departments.duplicated()]

# %%
departments[departments.duplicated(subset='department_id')]

# %% [markdown]
# There are no duplicate values in the `departments` table.

# %% [markdown]
# ### `aisles` data frame

# %%
aisles[aisles.duplicated()]

# %%
aisles[aisles.duplicated(subset='aisle_id')]

# %% [markdown]
# There are no duplicate values in the `aisles` table.

# %% [markdown]
# ### `order_products` data frame

# %%
# Check for fullly duplicate rows
order_products[order_products.duplicated()]

# %%
# Double check for any other tricky duplicates
order_products[order_products.duplicated(subset=['order_id', 'product_id'])]

# %% [markdown]
# There are no duplicate values in the `order_products` table.

# %% [markdown]
# ## Find and remove missing values
# From our work dealing with duplicate values, we noticed that we also have missing values to investigate:
# * The `'product_name'` column of the `products` table
# * The `'days_since_prior_order'` column of the `orders` table
# * The `'add_to_cart_order'` column of the `order_products` table

# %% [markdown]
# ### `products` data frame

# %%
products[products['product_name'].isna()]

# %%
# Are all of the missing product names associated with aisle ID 100?
products[(products['product_name'].isna()) & (products['aisle_id'] != 100)]

# %%
# Are all of the missing product names associated with department ID 21?
products[(products['product_name'].isna()) & (products['department_id'] != 21)]

# %%
# What is this ailse and department?
print(departments[departments['department_id'] == 21]['department'])
print()
print(aisles[aisles['aisle_id'] == 100]['aisle'])

# %%
# Fill missing product names with 'Unknown'
products['product_name'] = products['product_name'].fillna('Unknown')
products.info()

# %% [markdown]
# All of the missing product names have a `'missing'` label for their corresponding departments and aisles. Given the data we have, there is no way for us to determine what these products are called. Therefore, we decided to replace the missing values with the string `'Unknown'`.

# %% [markdown]
# ### `orders` data frame

# %%
orders[orders['days_since_prior_order'].isna()]

# %%
# Are there any missing values where it's not a customer's first order?
orders[(orders['days_since_prior_order'].isna()) & (orders['order_number'] != 1)]

# %% [markdown]
# All of the missing `'days_since_prior_order'` values correspond to a customer's first ever order. This makes sense because there is no prior order! We'll leave the values as `NaN` so the column can remain numeric. Also, the `NaN` values shouldn't interfere with any calculations we might do using this column.

# %% [markdown]
# ### `order_products` data frame

# %%
order_products[order_products['add_to_cart_order'].isna()]

# %%
# What are the min and max values in this column?
print(order_products['add_to_cart_order'].min())
print(order_products['add_to_cart_order'].max())

# %%
# Save all order IDs with at least one missing value in 'add_to_cart_order'
miss_cart_order_ids = sorted(list(order_products[order_products['add_to_cart_order'].isna()]['order_id'].unique()))

# %%
# Do all orders with missing values have more than 64 products?
order_products[order_products['order_id'].isin(miss_cart_order_ids)].groupby('order_id').size().sort_values()

# %%
# Replace missing values with 999 and convert column to integer type
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].fillna(999).astype('int')
order_products.info(show_counts=True)

# %% [markdown]
# For some reason, any item placed in the cart 65th or later has a missing value in the `'add_to_cart_order'` column. Maybe the data type of that column in the database could only hold integer values from 1 to 64. We've decided to replace the missing values with a code value, 999, that represents an unknown placed in cart order above 64. We also converted the column to integer data type. We just need to be careful to remember this if we perform calculations using this column during our analysis.
# 
# Other sensible code values we could've used are 0 or -1 because they don't show up elsewhere in the dataset and they don't have any real physical meaning for this variable.
# 
# Also note that, for orders with exactly 65 items, we could replace the missing value with 65. But we're going to neglect that for now since we can't determine the 65th item for all orders with 66 items or more.

# %% [markdown]
# # [A] Easy (must complete all to pass)

# %% [markdown]
# ### [A1] Verify that the `'order_hour_of_day'` and `'order_dow'` values in the `orders` tables are sensible (i.e. `'order_hour_of_day'` ranges from 0 to 23 and `'order_dow'` ranges from 0 to 6)

# %%
sorted(orders['order_hour_of_day'].unique())

# %%
sorted(orders['order_dow'].unique())

# %% [markdown]
# ### [A2] What time of day do people shop for groceries?

# %%
hour_of_day_counts = orders['order_hour_of_day'].value_counts().sort_index()
hour_of_day_counts.plot(kind='bar',
                        title='Orders by time of day',
                        xlabel='Hour of day',
                        ylabel='Number of orders'
                       )
plt.show()

# %% [markdown]
# Most orders occur between 9:00 AM and 5:00 PM, with peaks at 10:00 AM and 3:00 PM

# %% [markdown]
# ### [A3] What day of the week do people shop for groceries?

# %%
day_of_week_counts = orders['order_dow'].value_counts().sort_index()
day_of_week_counts.plot(kind='bar',
                        title='Orders by day of week',
                        xlabel='Day of week',
                        ylabel='Number of orders'
                       )
plt.show()

# %% [markdown]
# The data dictionary does not state which integer corresponds to which day of the week. Assuming Sunday = 0, then people place more orders at the beginning of the week (Sunday and Monday).

# %% [markdown]
# ### [A4] How long do people wait until placing another order?

# %%
orders['days_since_prior_order'].value_counts().sort_index().plot(kind='bar',
                                                                  title='Days since prior order',
                                                                  xlabel='Number of days',
                                                                  ylabel='Number of orders'
                                                                 )
plt.show()

# %% [markdown]
# The 0 values probably correspond to customers who placed more than one order on the same day.
# 
# The max value of 30 days might be an error. Let's remove that value from the distribution.

# %%
mask = orders['days_since_prior_order'] < 30
orders[mask]['days_since_prior_order'].value_counts().sort_index().plot(kind='bar',
                                                                  title='Days since prior order',
                                                                  xlabel='Number of days',
                                                                  ylabel='Number of orders'
                                                                 )
plt.show()

# %% [markdown]
# Based on this subset of the data, most people wait between 2 to 10 days in between orders. The most common wait time is 7 days. In other words, it's common for people to place weekly grocery orders. Interestingly, in the tail of the distribution we also see small spikes at 14, 21, and 28 days. These would correspond to orders every 2, 3, or 4 weeks.

# %% [markdown]
# # [B] Medium (must complete all to pass)

# %% [markdown]
# ### [B1] Is there a difference in `'order_hour_of_day'` distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you see.

# %%
wed_mask = orders['order_dow'] == 3
hod_counts_wed = orders[wed_mask]['order_hour_of_day'].value_counts().sort_index()

hod_counts_wed

# %%
sat_mask = orders['order_dow'] == 6
hod_counts_sat = orders[sat_mask]['order_hour_of_day'].value_counts().sort_index()

hod_counts_sat

# %%
hod_counts = pd.concat([hod_counts_wed, hod_counts_sat], axis=1)
hod_counts.columns = ['Wednesday', 'Saturday']
hod_counts

# %%
hod_counts.plot(kind='bar',
                title='Comparison of orders for Wednesday and Saturday',
                xlabel='Hour of day',
                ylabel='Number of orders'
               )
plt.show()

# %% [markdown]
# There's a small dip from 11h to 13h on Wednesdays. This dip is absent on Saturdays. Maybe this dip can be attributed to people who don't use Instacart because they have lunch somewhere between 11h and 13h.

# %% [markdown]
# ### [B2] What's the distribution for the number of orders per customer?

# %%
order_count_per_user = orders.groupby('user_id')['order_id'].count().sort_values()
order_count_per_user

# %%
order_count_per_user.plot(kind='hist',
                          bins=28,
                          title='Distribution of total orders'
                         )
plt.xlabel('Number of orders')
plt.ylabel('Number of customers')
plt.show()

# %% [markdown]
# Most customers in the dataset have placed between 1 and 10 orders, with number of orders per customer sharply decreasing after just 1 order.

# %% [markdown]
# ### [B3] What are the top 20 popular products (display their id and name)?

# %%
df_merge = order_products.merge(products, on='product_id')
df_merge

# %%
top_products = df_merge.groupby(['product_id', 'product_name']).size().sort_values(ascending=False)
top_products.head(20)

# %%
top_products.head(20).plot.bar()
plt.show()

# %% [markdown]
# The top 20 items are all produce, except for the milk. Looks like people want delicious and nutritious!

# %% [markdown]
# # [C] Hard (must complete at least two to pass)

# %% [markdown]
# ### [C1] How many items do people typically buy in one order? What does the distribution look like?

# %%
num_items = order_products.groupby('order_id').count()['product_id']
histogram_vals = num_items.value_counts().sort_index()
histogram_vals

# %%
histogram_vals.plot(kind='bar',
                title='Items purchased in one order',
                xlabel='Number of items',
                ylabel='Number of orders'
               )
plt.show()

# %%
histogram_vals[histogram_vals.index < 35].plot(kind='bar',
                title='Items purchased in one order',
                xlabel='Number of items',
                ylabel='Number of orders'
               )
plt.show()

# %% [markdown]
# The typical order contains 5 or 6 items, with most orders having between 1 and 20 items.

# %% [markdown]
# ### [C2] What are the top 20 items that are reordered most frequently (display their names and product IDs)?

# %%
reorder_products = order_products[order_products['reordered'] == 1]
reorder_products.head(10)

# %%
df_merge = reorder_products.merge(products, on='product_id')
df_merge

# %%
top_reordered_products = df_merge.groupby(['product_id', 'product_name']).size().sort_values(ascending=False)
top_reordered_products.head(20)

# %%
top_reordered_products.head(20).plot.bar()
plt.show()

# %% [markdown]
# It looks like produce and dairy comprise the most reordered products as well. It makes sense that perishables would be the most reordered items.

# %% [markdown]
# ### [C3] For each product, what proportion of its orders are reorders?

# %%
order_products['reordered'].unique()

# %%
df_merge = order_products.merge(products)
reorder_rate = df_merge.groupby(['product_id', 'product_name'])['reordered'].mean()
reorder_rate

# %%
reorder_rate_as_df = reorder_rate.sort_values(ascending=False).reset_index()
reorder_rate_as_df.sort_values(by='product_id')

# %% [markdown]
# ### [C4] For each customer, what proportion of their products ordered are reorders?

# %%
df_merge = order_products.merge(orders)
reorder_pct = df_merge.groupby('user_id')['reordered'].mean()
reorder_pct

# %%
reorder_pct_as_df = reorder_pct.sort_values(ascending=False).reset_index()
reorder_pct_as_df

# %% [markdown]
# ### [C5] What are the top 20 items that people put in their carts first? 

# %%
df_merge = order_products.merge(products)
first_in_cart = df_merge[df_merge['add_to_cart_order'] == 1]
first_in_cart

# %%
first_count = first_in_cart.groupby(['product_id', 'product_name'])['product_id'].count().sort_values(ascending=False)
first_count

# %%
first_count_as_df = first_count.reset_index(name='count')
first_count_as_df.head(20)

# %% [markdown]
# The products that are most often placed into the cart first are produce, dairy, and beverages such as soda or water. I couldn't really say why that is without experience using Instacart because this could have more to do with app design than properties of the products. I do notice that there is considerable overlap between this result and the previous result for most popular and most reordered item types. It could simply be that the app prioritizes popular items as the first suggested purchases, so it happens to be more convenient for customers to place these items in their cart first.

# %%



