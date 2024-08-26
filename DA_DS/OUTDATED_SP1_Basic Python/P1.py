# %% [markdown]
# An e-commerce company, Store 1, has recently started collecting data about its customers. Store 1's end goal is to better understand its customer behavior and make data-driven decisions to improve their online experience.
# 
# As a member of the analytical team, your first task is to assess the quality of a sample of collected data and prepare it for future analysis.

# %% [markdown]
# # Quiz
# 
# Store 1 aims to ensure consistency in data collection. As part of this effort, the quality of the data collected on users needs to be evaluated. You have been asked to review the collected data and propose changes. Below you will see data about a particular user. Please review the data and identify any potential issues.

# %%
user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']

# %% [markdown]
# **Options:**
# 
# 1. the data type for `user_id` should be changed from a string to an integer.
#     
# 2. The `user_name` variable contains a string that has unnecessary spacing and an underscore between the first and last names.
#     
# 3. The data type of `user_age` is incorrect.
#     
# 4. The `fav_categories` list contains strings in upper case. We should convert the values in the list to lower case instead.

# %% [markdown]
# Write in the markdown cell below the number of the options that you've identify as issues. If you identified mutiple issues, separate number by commas. For example, if you think that numbers 1 and 3 are correct, write 1, 3. 

# %% [markdown]
# **Write your answer and explain your reasoning:**
# 

# %% [markdown]
# # Task 1
# 
# Let's implement the changes we identified. First, we want to correct the issues with the `user_name` variable. As we found, it has unnecessary spaces and an underscore as a separator between the first and the last name. Your goal is to remove the spaces and then replace the underscore with the space. 

# %%
user_name = ' mike_reed '
user_name = user_name.strip()
user_name = user_name.replace('_', ' ')

print(user_name)

# %% [markdown]
# ********Hint********
# 
# There is a method, `strip()`, that can remove spaces from the beginning and end of a string. Additionally, the `replace()` method can be used to replace a part of a string. In this case, we want to replace underscores (`_`) with spaces.

# %% [markdown]
# # Task 2
# 
# Next, we need to split the updated `user_name` into two substrings to obtain a list that contains two values: the string for the first name and the string for the last name.

# %%
user_name = 'mike reed'
name_split = user_name.split()

print(name_split)

# %% [markdown]
# ********Hint********
# 
# The `split()` method is used to split a string. By default, it uses a space as a separator.

# %% [markdown]
# # Task 3
# 
# Great! Now we want to work with the `user_age` variable. As we mentioned earlier, it has an incorrect data type. Let's fix this issue by transforming the data type and print the final result.

# %%
user_age = 32.0
user_age = int(user_age)

print(user_age)

# %% [markdown]
# ********Hint********
# 
# Which data type will get rid of the floating point part?

# %% [markdown]
# # Task 4
# 
# As we all know, data is not always perfect. We have to consider scenarios where the `user_age` value cannot be converted to an integer. To prevent our system from crashing, we must take steps in advance.
# 
# Write a code that attempts to convert the `user_age` variable to an integer and assigns the transformed value to `user_age_int`. If the attempt fails, we print a message, asking a user to provide their age as a numerical value with the message: `Please provide your age as a numerical value.`

# %%
user_age = 'thirty two'

try:
	user_age_int = int(user_age)
except:
	print('Please provide your age as a numerical value.')

# %% [markdown]
# # Task 5
# 
# Finally, note that all favorite categories are stored in uppercase. To fill up a new list called `fav_categories_low` with the same categories but in lowercase, iterate over the values in the `fav_categories` list, modify them, and append the new values to the `fav_categories_low` list. As always, print the final result.

# %%
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

for category in fav_categories:
	lowered_category = category.lower()
	fav_categories_low.append(lowered_category)

print(fav_categories_low)

# %% [markdown]
# ********Hint********
# 
# Create a `for` loop that iterates over the `fav_categories` list. Use the `lower()` method to transform each category to lowercase. Then, use the `append()` method to add the updated values to the `fav_categories_low` list.

# %% [markdown]
# # Task 6
# 
# We have obtained additional information about our user’s spending habits, including the amount spent in each of their favorite categories. Management is interested in the following metrics:
# 
# - Total amount spent by the user
# - Minimum amount spent
# - Maximum amount spent
# 
# Let's calculate these values and print them:

# %%
fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category)
max_amount = max(spendings_per_category)
min_amount = min(spendings_per_category)

print(total_amount)
print(max_amount)
print(min_amount)

# %% [markdown]
# ********Hint********
# 
# What are the three methods that can be applied to a list to calculate its minimum, maximum, and total values?

# %% [markdown]
# # Task 7
# 
# The company wants to offer discounts to its loyal customers. Customers who make purchases totaling more than $1500 are considered loyal and will receive a discount.
# 
# Our goal is to create a `while` loop that checks the total amount spent and stops when it is reached. To simulate new purchases, the `new_purchase` variable generates a number between 30 and 80 on every loop iteration. This represents the amount of money spent on a new purchase, and thgis is what you need to add to the total.
# 
# Once the target amount is reached and the `while` loop is terminated, the final amount will be printed.

# %%
from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent < target_amount: # write your code here
	new_purchase = randint(30, 80) # we generate a random number from 30 to 80
	total_amount_spent += new_purchase # write your code here

print(total_amount_spent)

# %% [markdown]
# ********Hint********
# 
# In the `while` loop, you need to compare `total_amount_spent` with the `target_amount`. During each iteration of the loop, update the `total_amount_spent` variable by adding the `new_purchase` value to it.

# %% [markdown]
# # Task 8
# 
# Now we have all of the information about a customer in a way we want it to be. The management of a company asked us to come up with a way to summarize all of the information about a user. Your goal is to create a formatted string that uses information from the `user_id`, `user_name` and `user_age` variables. 
# 
# Here is the final string that we want to create: `User 32415 is mike who is 32 years old.`

# %%
user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info = f'User {user_id} is {user_name[0]} who is {user_age} years old.'
print(user_info)

# %% [markdown]
# ********Hint********
# 
# To create a string, you can use either the `format()` method or the f-string. To extract the first name from the `user_name` list, you can use slicing.

# %% [markdown]
# As you may know, companies collect and store data in a particular manner. Store 1 wants to store all information about its customers in a table. 
# 
# |user_id|user_name       |user_age|purchase_category            |spending_per_category |
# |'32415'|'mike', 'reed'  |32      |'electronics','sport','books'|894, 213, 173         |
# |'31980'|'kate', 'morgan'|24      |'clothes','shoes'            |439, 390              |
# 
# In technical terms, a table is simply a nested list that has a sublist for every user. 
# 
# Store 1 has created such a table for its users. It is stored in the `users` variable. Each sublist contains the user's ID, first and last names, age, favorite categories, and the amount spent in each category.

# %% [markdown]
# # Task 9
# 
# To calculate the revenue for the company, follow these steps:
# 
# 1. Use a `for` loop to iterate over the `users` list.
# 2. Extract the list of spendings for each user and sum up the values.
# 3. Update the revenue value with the total for each user.
# 
# This will give you the total revenue for the company that you’ll print at the very end.

# %%
users = [
	  # this is the beginning of the first sublist
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
        [894, 213, 173] 
    ], # this is the end of the first sublist

    # this is the beginning of the second sublist
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'],
        [439, 390]
    ] # this is the end of the second sublist
]

revenue = 0

for user in users:
	spendings_list = user[-1]
	total_spendings = sum(spendings_list)
	revenue += total_spendings

print(revenue)

# %% [markdown]
# ********Hint********
# 
# To extract the list of spendings made by a user, use indexing and assign it to the `spendings_list` variable. Then, use the built-in function to calculate the sum of the `spending_list`. Finally, update the `revenue` value by adding the `total_spendings` to it using augmented assignment.

# %% [markdown]
# # Task 10
# 
# Loop through the users list we’ve given you and print the first names of the clients who are less than 30 years old.

# %%
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

for user in users:
	if user[2] < 30:
	    print(user[1][0])

# %% [markdown]
# **Hint:**
# 
# Use a for loop to iterate over each row in the table. Use `if` inside a `for` loop to print the name of the user. The field `age` has the index 2.

# %% [markdown]
# # Task 11
# 
# Let’s put tasks 9 and 10 together and print the first names of users who are less than 30 years and have total spending bigger than 1000 dollars.

# %%
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

for user in users:
    spendings_list = user[-1]
    total_spendings = sum(spendings_list) 

    if user[2] < 30 and total_spendings > 1000:
        print(user[1][0])

# %% [markdown]
# **Hint:**
# 
# Use a for loop to iterate over each row in the table. Use `if` inside a `for` loop to print the name of the user. The field `age` has the index 2. Use the `sum` function to sum the spending and then check if it is bigger than 1000 dollars.

# %% [markdown]
# # Task 12
# 
# Now let’s print the first name and age of all the users who have shopped for clothes. Print the first name and age in the same print statement.

# %%
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

for user in users:
    categories = user[-2]
    for category in categories:
        if category == 'clothes':
            print(user[1][0], user[2])

# %% [markdown]
# **Hint:**
# 
# Use a for loop to iterate over each row in the table. Then use another loop to check if this user shopped for clothes, and if yes, print the first name and age inside the same print statement, separating by comma: `print(firstname, age)`.

# %% [markdown]
# #Write any comments or final thoughts here


