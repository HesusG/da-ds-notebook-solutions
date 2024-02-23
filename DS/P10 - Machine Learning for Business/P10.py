# %% [markdown]
# # Machine Learning for Business

# %% [markdown]
# ## Inicialization

# %%
# Cargar todas las librerías
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# %%
# Se cargan las bases de datos de las tres regiones.
try:
    region_1 = pd.read_csv("geo_data_0.csv")
    region_2 = pd.read_csv("geo_data_1.csv")
    region_3 = pd.read_csv("geo_data_2.csv")

except:
    region_1 = pd.read_csv("https://code.s3.yandex.net/datasets/geo_data_0.csv")
    region_2 = pd.read_csv("https://code.s3.yandex.net/datasets/geo_data_1.csv")
    region_3 = pd.read_csv("https://code.s3.yandex.net/datasets/geo_data_2.csv")

# %% [markdown]
# ### Data exploration

# %%
print(region_1.info())
print()
print()
print(region_2.info())
print()
print()
print(region_3.info())
print()
print()

# %% [markdown]
# #### Sample from each region

# %%
region_1.head(20)

# %%
region_2.head(20)

# %%
region_3.head(20)

# %%
print('Region 1')
print(region_1.describe())
print()
print()
print('Region 2')
print(region_2.describe())
print()
print()
print('Region 3')
print(region_3.describe())
print()
print()

# %% [markdown]
# #### Features histograms

# %%
columns = ["f0","f1","f2","product"]
print('Region 1 histograms')
print()
print()
plt.subplots(figsize = (20,5))
for i,column in enumerate(columns):    
    grafico=sns.histplot(data=region_1, x=column, bins=50,ax=plt.subplot(1, len(columns), i + 1))
    plt.xticks(rotation = 45)  
   



# %%
print('Region 2 histograms')
print()
print()
plt.subplots(figsize = (20,5))
for i,column in enumerate(columns):    
    grafico=sns.histplot(data=region_2, x=column, bins=50,ax=plt.subplot(1, len(columns), i + 1))
    plt.xticks(rotation = 45)
   



# %%
print('Region 3 histograms')
print()
print()
plt.subplots(figsize = (20,5))
for i,column in enumerate(columns):    
    grafico=sns.histplot(data=region_3, x=column, bins=50,ax=plt.subplot(1, len(columns), i + 1))
    plt.xticks(rotation = 45)


# %% [markdown]
# #### Scatter plots

# %%
print('Scatter Region 1')
print()
fig, ax=plt.subplots()
ax.scatter(region_1["f0"],region_1["product"])
plt.title("Scatter")
plt.xlabel('f0')
plt.ylabel('Product')
plt.show()

fig, ax=plt.subplots()
ax.scatter(region_1["f1"],region_1["product"])
plt.xlabel('f1')
plt.ylabel('Product')
plt.show()

fig, ax=plt.subplots()
ax.scatter(region_1["f2"],region_1["product"])
plt.xlabel('f2')
plt.ylabel('Product')
plt.show()

# %%
region_1.corr()

# %%
print('Scatter Region 2')
print()
fig, ax=plt.subplots()
ax.scatter(region_2["f0"],region_2["product"])
plt.xlabel('f0')
plt.ylabel('Product')
plt.show()

fig, ax=plt.subplots()
ax.scatter(region_2["f1"],region_2["product"])
plt.xlabel('f1')
plt.ylabel('Product')
plt.show()

fig, ax=plt.subplots()
ax.scatter(region_2["f2"],region_2["product"])
plt.xlabel('f2')
plt.ylabel('Product')
plt.show()

# %%
region_2.corr()

# %%
print('Scatter Region 3')
print()
fig, ax=plt.subplots()
ax.scatter(region_3["f0"],region_3["product"])
plt.xlabel('f0')
plt.ylabel('Product')
plt.show()

fig, ax=plt.subplots()
ax.scatter(region_3["f1"],region_3["product"])
plt.xlabel('f1')
plt.ylabel('Product')
plt.show()

fig, ax=plt.subplots()
ax.scatter(region_3["f2"],region_3["product"])
plt.xlabel('f2')
plt.ylabel('Product')
plt.show()

# %%
region_3.corr()

# %%

region_1 = region_1.drop(["id"], axis=1)
region_2 = region_2.drop(["id"], axis=1)
region_3 = region_3.drop(["id"], axis=1)


print(region_1.info())
print()
print()
print(region_2.info())
print()
print()
print(region_3.info())

# %% [markdown]
# ### Missing values and duplicated

# %%
print(region_1.isna().sum())
print()
print()
print(region_2.isna().sum())
print()
print()
print(region_3.isna().sum())
print()
print()

# %%
print(region_1.duplicated().sum())
print()
print()
print(region_2.duplicated().sum())
print()
print()
print(region_3.duplicated().sum())


# %% [markdown]
# ## Model training

# %%
state= np.random.RandomState(54321)

def train1(data, random=state):
    features = data.drop(columns=["product"])
    target = data["product"]         

    features_train,features_valid,target_train,target_valid = train_test_split(features,target,
                                                                                       test_size= 0.25, random_state= random)
    rl = LinearRegression()
    rl.fit(features_train,target_train)
    predict_date = rl.predict(features_valid) 


    rmse = mean_squared_error(target_valid, predict_date,squared=False)


    mean_reserve= predict_date.mean()
    print('RMSE',rmse)
    print('Mean volume', mean_reserve)
    print("--------------------------------------------------------------------------------")
    
    output= pd.DataFrame(dict(predicted_value=predict_date,real_value=target_valid))
    return output
regiones= ["Region 1","Region 2","Region 3"]
datas = [region_1, region_2, region_3]
predict_region = {}
        
for data, region in zip(datas,regiones): 
    predict_region[region] = train1(data)     

# %%
print(predict_region["Region 1"])
print("--------------------------")
print(predict_region["Region 2"])
print("--------------------------")
print(predict_region["Region 3"])
print("--------------------------")

# %% [markdown]
# ## Revenue calculation

# %% [markdown]
# ### Revenue calculation per region

# %%
presupuesto =100_000_000
income = 4500
pozos = 200

volumen_min= presupuesto/income 
volumen_min_pozo = volumen_min/pozos 
print('Minimum value: ',volumen_min)
print('Each well must have: ',volumen_min_pozo)


# %%
def benefit(df):
    best_well=df.sort_values(by="predicted_value", ascending=False)['real_value'].head(200) 
    volumen_well = best_well.sum() 
    benefits= ((volumen_well*income)-presupuesto) 
    return benefits

print('El beneficio de la Región 1 es', benefit(predict_region["Region 1"]))
print('El beneficio de la Región 2 es', benefit(predict_region["Region 2"]))
print('El beneficio de la Región 3 es', benefit(predict_region["Region 3"]))

# %% [markdown]
# ## Risk and profit calculation

# %% [markdown]
# ### Bootstrapping

# %%
state= np.random.RandomState(54321)
def boots_func(df, n_muestras=1000): 
    benefit_muestra=[]
    for i in range(n_muestras):
        wells = df.sample(n=500,replace=True, random_state=state) 
        benefit_muestra.append(benefit(wells))
    benefit_muestra = pd.Series(benefit_muestra)
    return benefit_muestra 

boots_func(predict_region["Region 1"])

# %% [markdown]
# ### Confidence interval, loss, profit

# %%
def calc(serie_benef,region):
    alpha = 0.05 
    interv_low = serie_benef.quantile(alpha/2) 
    interv_up = serie_benef.quantile(1-alpha/2) 
    benefit_mean = serie_benef.mean() 
    perdida = ((serie_benef < 0).mean()) 
    print(f'Confidence intervals for {region}:',(interv_low, interv_up))
    print(f'Average profit for {region}:',benefit_mean)
    print(f'Risk {region}:{perdida:%}')
    print("...................................................................................")

benef_dict ={}
for region, data in predict_region.items(): 
    serie_benefit2 = boots_func(data)
    calc(serie_benefit2,region=region)
    benef_dict[region] = serie_benefit2  


