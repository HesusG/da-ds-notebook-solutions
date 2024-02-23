# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import math
from scipy import stats

from datetime import datetime, timedelta

from statsmodels.stats.proportion import proportions_ztest

# %% [markdown]
# # Постановка задачи

# %% [markdown]
# Вы - новый аналитик международного интернет-магазина. Ваш предшественник на этой позиции запустил А/B-тест и уволился. Осталось только техническое задание и результаты теста. Техническое задание:
# 
# - Наименование теста: `recommender_system_test`;
# - Группы: А (котрольная), B (новая платежная воронка);
# - Дата запуска: 2020-12-07
# - Дата остановки набора новых пользователей: 2020-12-21;
# - Дата остановки: 2021-01-04
# - Аудитория: 15% новых пользователей из региона EU;
# - Назначение теста: тестирование изменений, связанных с внедрением улучшенной рекомендательной системы;
# - Ожидаемый эфект: за 14 дней с момента регистрации в системе пользователи покажут лучшую конверсию в просмотр карточек товаров (событие `product_page`), просмотр  корзины товаров (событие `product_card`) и покупку (`purchase`). На каждом из шагов воронки `product_page → product_card → purchase` улучшение составит не менее 10%;
# - Ожидаемое количество участников теста: 6000.
# 
# Загрузите данные теста, проверьте корректность его проведения и проанализируйте полученные результаты.

# %% [markdown]
# # Анализ результатов теста
# 
# Установим параметры теста:

# %%
test_start = pd.to_datetime('2020-12-07')
user_acquisition_duration = 16 - 1 # т.к. нумерация дней идет с 0
activity_duration = 14 - 1
user_acquisition_end = test_start + timedelta(user_acquisition_duration)
test_end = test_start + timedelta(user_acquisition_duration + activity_duration)

required_participants = 6000

test_name = 'recommender_system_test'

# %% [markdown]
# ## 1 Загрузка и подготовка данных

# %% [markdown]
# Загружаем данные, преобразуем даты и веремя:

# %%
# учстники теста
test_participants = pd.read_csv('final_ab_participants.csv')
# пользователи
new_users = pd.read_csv('final_ab_new_users.csv').merge(test_participants, on = 'user_id', how = 'left')
new_users['first_date'] = pd.to_datetime(new_users['first_date'])
# события
events = pd.read_csv('final_ab_events.csv').merge(test_participants, on = 'user_id', how = 'left')
events['event_dt'] = pd.to_datetime(events['event_dt'])
# рекламная активность
marketing_events = pd.read_csv('ab_project_marketing_events.csv')
marketing_events['start_dt'] = pd.to_datetime(marketing_events['start_dt'])
marketing_events['finish_dt'] = pd.to_datetime(marketing_events['finish_dt'])

# %% [markdown]
# Так, как мы сами не планировали тест и не следили за его проведением, нам прежде всего нужно проверить адекватность его проведения. Проверим: 
# - Совпадал ли тест по времени с какими-нибудь маркетинговыми событиями?
# - Не пересекалась ли аудитория теста с конкурирующими тестами;
# - Была ли аудитория теста сформирована правильно;
# - Было ли распределение по тестовым группам равномерно.

# %% [markdown]
# ## 2 Проверка корректности проведения теста
# 
# Проверим совпадение с маркетинговыми активностями:

# %%
marketing_events['is_eu'] = marketing_events['regions'].apply(lambda x: 'EU' in x.split(', '))
eu_marketing_events = marketing_events.query('is_eu == True')
print('Временные границы теста: ', test_start, test_end)
eu_marketing_events.query('(start_dt >= @test_start and start_dt <= @test_end) or \
                           (finish_dt >= @test_start and finish_dt <= @test_end)')

# %% [markdown]
# Тест сильно пересекается с новогодней промкой в EU. Это не слишком хорошо - нужно избегать таких ситуация.
# 
# Посмотрим как дела с конкурирующими тестами:

# %% [markdown]
# Посмотрим, как у нас обстоят дела с участниками теста:

# %%
test_participants.groupby(['ab_test', 'group']).agg({'user_id': 'nunique'})

# %% [markdown]
# Кроме нашего теста, оказывается был еще параллельный тест interface_eu_test. Судя по названию, он проводился в EU-регионе и мог повлиять на результат нашего теста. Посмотрим, было ли пересечение аудитории и если да, то насколько большое:

# %%
new_test_users = test_participants.query('ab_test == @test_name')['user_id'].unique()
both_test_participants = (test_participants[test_participants['user_id'].isin(new_test_users)]
                          .groupby('user_id').agg({'ab_test': 'nunique', 'group': 'nunique'})
                          .query('ab_test > 1 or group > 1').shape[0])
print('Пересечение аудитории тестов: {} ({:.2%})'.format(both_test_participants, 
                                                         both_test_participants / len(new_test_users)))


# %% [markdown]
# Довольно много, конкурирующие тесты были явно некорректно запущены.
# 
# Уберем из данных все, что касается конкурирующего теста:

# %%
test_participants = test_participants.query('ab_test == @test_name')
new_users = new_users.query('ab_test != "interface_eu_test"')
events = events.query('ab_test != "interface_eu_test"')

# %% [markdown]
# Проверим корректность аудитории теста.
# 
# Посмотрим, попадали ли в тест в основном пользователи из EU:

# %%
report = new_users.query('ab_test == @test_name').groupby('region').agg({'user_id': 'nunique'}).rename(columns = {'user_id': 'Участники'})
report['% участников'] = (report['Участники'] / report['Участники'].sum()).round(2)
report.sort_values(by = 'Участники', ascending = False)

# %% [markdown]
# Есть небольшое отклонение - 5% теста это пользователи из других регионов. Это допустимо.
# 
# Теперь проверим, попадала ли в тест нужная пропорция пользователей из EU:

# %%
eu_test_users = new_users.query('region == "EU" and ab_test == @test_name').shape[0]
eu_users = new_users.query('region == "EU" and first_date >= @test_start and first_date <= @user_acquisition_end').shape[0]
eu_test_users / eu_users

# %% [markdown]
# Получается, что в тест вместо 15% попадают 18% пользователей из EU. Проверим насколько эта разница статистически значима.
# 
# Для этого, нам понадобится установить и откорректировать уровень значимости. В этом проекте мы собираемся провести 5 статистических тестов:
# - Проверка % EU-аудитории в тесте;
# - Проверка корректности распределения учстников по группам теста;
# - Три теста для каждого из шагов воронки монетизации.
# 
# Проводим коррекцию методом Бонферрони и проводим z-тест:

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
# На 3% больше пользователей отправили в тест чем планировали. Неприятно, но не сильно страшно. Врядли 3% могли существенно повлиять на монетизацию всей EU-аудитории.
# 
# Проверим, равномерно ли были распределены пользователи в группах:

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
    cumulative_test_users = cumulative_test_users.append(current_test_users, sort = False)
    
    
    ##карточка продукта
    current_test_prod = events.query('event_name == "product_page"').query('event_dt <= @dt').groupby('user_id').agg({'details': 'count'})
    current_test_product = (new_users.merge(current_test_prod, on = 'user_id', how = 'inner')
                                     .query('first_date <= @dt')
                                     .groupby('group').agg({'user_id': 'nunique'}).T)
    current_test_product['date'] = dt
    current_test_product['test_day'] = i
    cumulative_test_product = cumulative_test_product.append(current_test_product, sort = False)
    
    ##корзина заказа
    current_test_cart = events.query('event_name == "product_cart"').query('event_dt <= @dt').groupby('user_id').agg({'details': 'count'})
    current_test_carters = (new_users.merge(current_test_cart, on = 'user_id', how = 'inner')
                                     .query('first_date <= @dt')
                                     .groupby('group').agg({'user_id': 'nunique'}).T)
    current_test_carters['date'] = dt
    current_test_carters['test_day'] = i
    cumulative_test_carters = cumulative_test_carters.append(current_test_carters, sort = False)
    
    ##платящие участники теста
    current_test_purchases = events.query('event_name == "purchase"').query('event_dt <= @dt').groupby('user_id').agg({'details': 'sum'})
    current_test_payers = (new_users.merge(current_test_purchases, on = 'user_id', how = 'inner')
                                    .query('first_date <= @dt')
                                    .groupby('group').agg({'user_id': 'nunique'}).T)
    current_test_payers['date'] = dt
    current_test_payers['test_day'] = i
    cumulative_test_payers = cumulative_test_payers.append(current_test_payers, sort = False)
    
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


