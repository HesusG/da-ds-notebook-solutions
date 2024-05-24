# %%
import pandas as pd
pd.set_option('display.max_columns', None)
from matplotlib import pyplot as plt

from datetime import timedelta

from statsmodels.stats.proportion import proportions_ztest

# %% [markdown]
# # Setting tasks

# %% [markdown]
# New analyst for an international online store. Your predecessor in this position launched an A/B test and quit. All that remains is the technical specification and test results. Technical task:

# - Test name: `recommender_system_test`;
# - Groups: A (control room), B (new payment funnel);
# - Launch date: 2020-12-07
# - Stop date for recruiting new users: 2020-12-21;
# - Stop date: 2021-01-04
# - Audience: 15% of new users from the EU region;
# - Purpose of the test: testing changes associated with the implementation of an improved recommendation system;
# - Expected effect: within 14 days from the moment of registration in the system, users will show better conversion in viewing product cards (`product_page` event), viewing the product basket (`product_card` event) and purchasing (`purchase`). At each step of the funnel `product_page → product_card → purchase` the improvement will be at least 10%;
# - Expected number of test participants: 6000.

# Download the test data, check the correctness of its execution and analyze the results.

# %% [markdown]
# # Analysis of test results

# Let's set the test parameters:

# %%
test_start = pd.to_datetime('2020-12-07')
user_acquisition_duration = 16 - 1 # т.к. нумерация дней идет с 0
activity_duration = 14 - 1
user_acquisition_end = test_start + timedelta(user_acquisition_duration)
test_end = test_start + timedelta(user_acquisition_duration + activity_duration)

required_participants = 6000

test_name = 'recommender_system_test'

# %% [markdown]
# ## 1 Loading and preparing data

# %% [markdown]
# Loading data, converting dates and times:

# %%
# учстники теста
test_participants = pd.read_csv('datasets/final_ab_participants.csv')
# пользователи
new_users = pd.read_csv('datasets/final_ab_new_users.csv').merge(test_participants, on = 'user_id', how = 'left')
new_users['first_date'] = pd.to_datetime(new_users['first_date'])
# события
events = pd.read_csv('datasets/final_ab_events.csv').merge(test_participants, on = 'user_id', how = 'left')
events['event_dt'] = pd.to_datetime(events['event_dt'])
# рекламная активность
marketing_events = pd.read_csv('datasets/ab_project_marketing_events.csv')
marketing_events['start_dt'] = pd.to_datetime(marketing_events['start_dt'])
marketing_events['finish_dt'] = pd.to_datetime(marketing_events['finish_dt'])

# %% [markdown]
# Since we ourselves did not plan the test and did not monitor its implementation, we first need to check the adequacy of its implementation. Let's check:
# - Did the test coincide in time with any marketing events?
# - Did the test audience overlap with competing tests;
# - Was the test audience formed correctly;
# - Was there an even distribution among test groups?

# %% [markdown]
# ## 2 Checking the correctness of the test
# 
# Let's check the coincidence with marketing activities:

# %%
marketing_events['is_eu'] = marketing_events['regions'].apply(lambda x: 'EU' in x.split(', '))
eu_marketing_events = marketing_events.query('is_eu == True')
print('Test time limits: ', test_start, test_end)
eu_marketing_events.query('(start_dt >= @test_start and start_dt <= @test_end) or \
                           (finish_dt >= @test_start and finish_dt <= @test_end)')

# %% [markdown]
# The test strongly overlaps with the New Year's promotion in the EU. This is not very good - you need to avoid such situations.

# Let's see how things are going with competing tests:

# %% [markdown]
# Let's see how we are doing with the test participants:

# %%
test_participants.groupby(['ab_test', 'group']).agg({'user_id': 'nunique'})

# %% [markdown]
# In addition to our test, it turns out there was also a parallel test interface_eu_test. Judging by the name, it was carried out in the EU region and could affect the result of our test. Let's see if there was an audience overlap and, if so, how big:

# %%
new_test_users = test_participants.query('ab_test == @test_name')['user_id'].unique()
both_test_participants = (test_participants[test_participants['user_id'].isin(new_test_users)]
                          .groupby('user_id').agg({'ab_test': 'nunique', 'group': 'nunique'})
                          .query('ab_test > 1 or group > 1').shape[0])
print('Пересечение аудитории тестов: {} ({:.2%})'.format(both_test_participants, 
                                                         both_test_participants / len(new_test_users)))


# %% [markdown]
# Quite a lot, competing tests were clearly launched incorrectly.

# Let's remove from the data everything related to the competing test:

# %%
test_participants = test_participants.query('ab_test == @test_name')
new_users = new_users.query('ab_test != "interface_eu_test"')
events = events.query('ab_test != "interface_eu_test"')

# %% [markdown]
# Let's check the correctness of the test audience.

# Let's see if the test included mainly users from the EU:

# %%
report = new_users.query('ab_test == @test_name').groupby('region').agg({'user_id': 'nunique'}).rename(columns = {'user_id': 'Участники'})
report['% участников'] = (report['Участники'] / report['Участники'].sum()).round(2)
report.sort_values(by = 'Участники', ascending = False)

# %% [markdown]
# There is a slight deviation - 5% of the test are users from other regions. This is acceptable.

# Now let’s check whether the test included the required proportion of users from the EU:

# %%
eu_test_users = new_users.query('region == "EU" and ab_test == @test_name').shape[0]
eu_users = new_users.query('region == "EU" and first_date >= @test_start and first_date <= @user_acquisition_end').shape[0]
eu_test_users / eu_users

# %% [markdown]
# It turns out that instead of 15%, 18% of users from the EU are included in the test. Let's check how statistically significant this difference is.

# To do this, we will need to set and adjust the significance level. In this project we are going to run 5 statistical tests:
# - Checking % of EU audience in the test;
# - Checking the correct distribution of participants into test groups;
# - Three tests for each step of the monetization funnel.

# We carry out the Bonferroni correction and perform a z-test:

# %%
alpha = 0.05
alpha = alpha / 5
pvalue = proportions_ztest(eu_test_users, eu_users, value = 0.15)[1]
print('p-value: {}'.format(pvalue))
if pvalue >= alpha: 
    print('Нулевая гипотеза не отвергается: для пользователя из региона EU вероятность попасть в тест составляет 15%.')
else:
    print('Нулевая гипотеза отвергается: для пользователя из региона EU вероятность попасть в тест отличается от 15%.')

# %% [markdown]
# 3% more users were sent to the test than planned. Unpleasant, but not very scary. It is unlikely that 3% could significantly affect the monetization of the entire EU audience.

# Let's check whether users are evenly distributed in groups:

# %%
a_users = new_users.query('group == "A" and ab_test == @test_name').shape[0]
all_participants = new_users.query('ab_test == @test_name').shape[0]
a_users / all_participants

# %% [markdown]
# Должны были поделить участников теста пополам, но, похоже, в группу А попало 57% участников вместо 50. 
# 
# Посмотрим насколько этот результат статистически значим:

# %%
pvalue = proportions_ztest(a_users, all_participants, value = 0.5)[1]
print('p-value: {}'.format(pvalue))
if pvalue >= alpha: 
    print('Нулевая гипотеза не отвергается: вероятность попасть в группу А составляет 50%')
else:
    print('Нулевая гипотеза отвергается: вероятность попасть в группу А отличается от 50%')

# %% [markdown]
# Да, кажется с этим тестом все плохо. Тест явно проведен не в соответствии с ТЗ. Пересечение с параллельным тестом тоже очень неприятная штука. 
# 
# Вывод: тест проведен некорректно.
# 
# Тем не менее, посмотрим что там за результаты получились - может быть заметим что-то полезное для следующих тестов. Сначала проведем анализ накопительных метрик.

# %% [markdown]
# ## 3 Анализ накопительных метрик
# Оставим в данных только записи, касающиеся теста:

# %%
test_participants = test_participants.query('ab_test == @test_name')
new_users = new_users.query('ab_test == @test_name')
events = events.query('ab_test == @test_name')

# %% [markdown]
# Поскольку тест уже проведен, установим текущую длительность привлечения равной полной длительности привлечения:

# %%
current_aquisition_duration = user_acquisition_duration
test_dates = pd.date_range(start = test_start, periods = current_aquisition_duration)

plt.subplots(figsize = (15, 10))

cumulative_test_users = pd.DataFrame(columns = ['A', 'B'])
cumulative_test_carters = pd.DataFrame(columns = ['A', 'B'])
cumulative_test_product = pd.DataFrame(columns = ['A', 'B'])
cumulative_test_payers = pd.DataFrame(columns = ['A', 'B'])


for i, dt in enumerate(test_dates):

    #участники теста
    current_test_users = new_users.query('first_date <= @dt').groupby('group').agg({'user_id': 'nunique'}).T
    current_test_users['date'] = dt
    current_test_users['test_day'] = i
    cumulative_test_users = pd.concat([cumulative_test_users, current_test_users], sort = False)
    
    ##карточка продукта
    current_test_prod = events.query('event_name == "product_page"').query('event_dt <= @dt').groupby('user_id').agg({'details': 'count'})
    current_test_product = (new_users.merge(current_test_prod, on = 'user_id', how = 'inner')
                                     .query('first_date <= @dt')
                                     .groupby('group').agg({'user_id': 'nunique'}).T)
    current_test_product['date'] = dt
    current_test_product['test_day'] = i
    cumulative_test_product = pd.concat([cumulative_test_product, current_test_product], sort = False)
    
    ##корзина заказа
    current_test_cart = events.query('event_name == "product_cart"').query('event_dt <= @dt').groupby('user_id').agg({'details': 'count'})
    current_test_carters = (new_users.merge(current_test_cart, on = 'user_id', how = 'inner')
                                     .query('first_date <= @dt')
                                     .groupby('group').agg({'user_id': 'nunique'}).T)
    current_test_carters['date'] = dt
    current_test_carters['test_day'] = i
    cumulative_test_carters = pd.concat([cumulative_test_carters, current_test_carters], sort = False)

    ##платящие участники теста
    current_test_purchases = events.query('event_name == "purchase"').query('event_dt <= @dt').groupby('user_id').agg({'details': 'sum'})
    current_test_payers = (new_users.merge(current_test_purchases, on = 'user_id', how = 'inner')
                                    .query('first_date <= @dt')
                                    .groupby('group').agg({'user_id': 'nunique'}).T)
    current_test_payers['date'] = dt
    current_test_payers['test_day'] = i
    cumulative_test_payers = pd.concat([cumulative_test_payers, current_test_payers], sort = False)

#новые участники теста без накопления
pd.pivot_table(new_users, 
               index = 'first_date', 
               columns = 'group', 
               values = 'user_id', 
               aggfunc = 'count').plot(ax = plt.subplot(2, 3, 1), grid = True)
plt.title('Новые участники теста в день')
plt.xlabel('Дата')
plt.xticks(rotation = 45)
plt.legend()

#участники теста
cumulative_test_users = cumulative_test_users.query('date >= @test_start and date <= @user_acquisition_end').set_index('test_day')[['A', 'B']]
cumulative_test_users['Всего'] = cumulative_test_users['A'] + cumulative_test_users['B']
cumulative_test_users.plot(ax = plt.subplot(2, 3, 2), grid = True)
plt.axhline(y = required_participants, label = 'Ожидаемое число участников', color = 'red', linestyle = '--')
plt.title('Участники теста')
plt.legend()
plt.xlabel('День теста')

#конверсии 
cumulative_test_payers = cumulative_test_payers.query('date >= @test_start and date <= @user_acquisition_end').set_index('test_day')[['A', 'B']]
cumulative_test_payers.div(cumulative_test_users)[['A', 'B']].fillna(0).plot(ax = plt.subplot(2, 3, 3), grid = True)
plt.title('Конверсия в покупку')
plt.legend()
plt.xlabel('День теста')

#конверсии в корзину
cumulative_test_carters = cumulative_test_carters.query('date >= @test_start and date <= @user_acquisition_end').set_index('test_day')[['A', 'B']]
cumulative_test_carters.div(cumulative_test_users)[['A', 'B']].fillna(0).plot(ax = plt.subplot(2, 3, 4), grid = True)
plt.title('Конверсия в корзину заказа')
plt.legend()
plt.xlabel('День теста')

#конверсии в корзину
cumulative_test_product = cumulative_test_product.query('date >= @test_start and date <= @user_acquisition_end').set_index('test_day')[['A', 'B']]
cumulative_test_product.div(cumulative_test_users)[['A', 'B']].fillna(0).plot(ax = plt.subplot(2, 3, 5), grid = True)
plt.title('Конверсия в карточку продукта')
plt.legend()
plt.xlabel('День теста')

plt.tight_layout()
plt.show()

# %% [markdown]
# Выводы и наблюдения:
# - Данные показывают недельную сезонность, наобходимый уровень участников был достигнут. В этой части тест был спланирован верно;
# - Конверсии в каждый из шагов воронки ощутимо разошлись, похоже, что лидировала группа А. 
# 
# Проверим это с помощью статистических тестов.

# %% [markdown]
# ## 4 Проверка гипотез

# %% [markdown]
# Проверим, есть ли отличие между группами в конверсии в покупку. Используем z-тест, поскольку тестируется пропорция:

# %%
report = test_participants.merge(events.query('event_name == "purchase"').groupby('user_id').agg({'details': 'count'}), on = 'user_id', how = 'left')
report['is_buyer'] = (report['details'] > 0).astype(int)
report = (report.groupby('group').agg({'user_id': 'count', 'is_buyer': 'sum'})
                                 .rename(columns = {'user_id': 'Участники', 'is_buyer': 'Покупатели'}))
report['Конверсия'] = (report['Покупатели'] / report['Участники']).round(2)
report

# %%
count = list(report['Покупатели'].values)
nobs = list(report['Участники'].values)

pvalue = proportions_ztest(count, nobs)[1]
print('p-value: {}'.format(pvalue))
if pvalue >= alpha: 
    print('Нулевая гипотеза не отвергается: между группами A и B нет различий в % конверсии в покупку.')
else:
    print('Нулевая гипотеза отвергается: между группами A и B есть различие % конверсии в покупку.')

# %% [markdown]
# Проверим, есть ли отличие между группами в % пользователей, посетивших страницу продукта. Используем z-тест, поскольку тестируется пропорция:

# %%
report = test_participants.merge(events.query('event_name == "product_page"').groupby('user_id').agg({'event_dt': 'count'}), on = 'user_id', how = 'left')
report['is_buyer'] = (report['event_dt'] > 0).astype(int)
report = (report.groupby('group').agg({'user_id': 'count', 'is_buyer': 'sum'})
                                 .rename(columns = {'user_id': 'Участники', 'is_buyer': 'Пользователи на странице продукта'}))
report['Конверсия'] = (report['Пользователи на странице продукта'] / report['Участники']).round(2)
report

# %%
count = list(report['Пользователи на странице продукта'].values)
nobs = list(report['Участники'].values)

pvalue = proportions_ztest(count, nobs)[1]
print('p-value: {}'.format(pvalue))
if pvalue >= alpha: 
    print('Нулевая гипотеза не отвергается: между группами A и B нет различий в % пользователей, видевших страницу продукта.')
else:
    print('Нулевая гипотеза отвергается: между группами A и B есть различие % пользователей, видевших страницу продукта.')

# %% [markdown]
# Проверим, есть ли отличие между группами в % пользователей, посетивших страницу корзины. Используем z-тест, поскольку тестируется пропорция:

# %%
report = test_participants.merge(events.query('event_name == "product_cart"').groupby('user_id').agg({'event_dt': 'count'}), on = 'user_id', how = 'left')
report['is_buyer'] = (report['event_dt'] > 0).astype(int)
report = (report.groupby('group').agg({'user_id': 'count', 'is_buyer': 'sum'})
                                 .rename(columns = {'user_id': 'Участники', 'is_buyer': 'Пользователи на странице корзины'}))
report['Конверсия'] = (report['Пользователи на странице корзины'] / report['Участники']).round(2)
report

# %%
count = list(report['Пользователи на странице корзины'].values)
nobs = list(report['Участники'].values)

pvalue = proportions_ztest(count, nobs)[1]
print('p-value: {}'.format(pvalue))
if pvalue >= alpha: 
    print('Нулевая гипотеза не отвергается: между группами A и B нет различий в % пользователей, видевших страницу корзины.')
else:
    print('Нулевая гипотеза отвергается: между группами A и B есть различие % пользователей, видевших страницу корзины.')

# %% [markdown]
# Разница в пользу контрольной группы А, которую мы видели при анализе накопительных метрик, подтвержается статистическими тестами. Похоже, что улучшенная рекомендательная система ничего не улучшила, а даже наоборот. Конечно, тест у нас проведен некорректно, но к этим улучшениями нужно относиться с подозрением. Рекомендуем провести еще один тест - на этот раз соответствующий ТЗ.

# %% [markdown]
# # Выводы

# %% [markdown]
# Выводы:
# 1. Тест был проведен некорректно:
#     - Тест совпал по времени с новогодними промо в регионе EU;
#     - Участники теста параллельно участвовали в еще одном тесте;
#     - В тест было набрано на 3% больше участников из региона EU, чем нужно;
#     - Участники теста были неравномерно распределены между тестовыми группами в группу А попало 57% участников.
# Таким образом, результаты теста нельзя считать валидными и основывать на них какие-либо бизнес решения.
# 
# 2. Тем не менее, результаты теста показывают, что к новой рекомендательной системе нужно относиться с подозрением - конверсия в тестовой группе была намного ниже, чем в контрольной.
# 
# 3. Рекомендуется провести еще один тест, чтобы получить корректные результаты.


