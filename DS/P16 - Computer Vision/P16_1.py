# %% [markdown]
# ## Initialization

# %% [markdown]
# ## Load Data

# %% [markdown]
# The dataset is stored in the `datasets/faces/` folder, there you can find
# - The `final_files` folder with 7.6k photos
# - The `labels.csv` file with labels, with two columns: `file_name` and `real_age`
# 
# Given the fact that the number of image files is rather high, it is advisable to avoid reading them all at once, which would greatly consume computational resources. We recommend you build a generator with the ImageDataGenerator generator. This method was explained in Chapter 3, Lesson 7 of this course.
# 
# The label file can be loaded as an usual CSV file.

# %%
import pandas as pd
pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# Loading the dataframe

# %%
labels = pd.read_csv(r'datasets/faces/labels.csv')

# %%
labels.info()

# %%
labels.head()

# %% [markdown]
# Viewing the shape of the dataframe

# %%
labels.shape

# %% [markdown]
# Viewing the images

# %%
train_datagen = ImageDataGenerator(rescale=1./255)

# %%
train_gen_flow = train_datagen.flow_from_dataframe(
        dataframe=labels,
        directory='datasets/faces/final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        seed=12345)

# %%
features, target = next(train_gen_flow)

# %%
fig = plt.figure(figsize=(10,10))
for i in range(15):
    fig.add_subplot(4, 4, i+1)
    plt.imshow(features[i])
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

# %%


# %% [markdown]
# ## EDA

# %% [markdown]
# Viewing the details of the dataframe

# %%
labels.describe()

# %% [markdown]
# Plotting all of the ages used

# %%
sns.barplot(data=labels, x="file_name", y="real_age")

# %% [markdown]
# Plotting a histogram to better represent the ages used

# %%
sns.distplot(labels["real_age"],  hist=True, bins=25)

# %% [markdown]
# Plotting a boxplot to see the extremes of the data along with the median and quartiles

# %%
sns.boxplot(labels['real_age'])

# %% [markdown]
# ### Findings

# %% [markdown]
# Look like the average age is 31 and the standard deviation is 17, which means the highest populations represented are between the ages of 14 - 48.

# %% [markdown]
# The model could have issues being able to classify the extreme age categories. Therefore the elderly could have issues getting verified for age because of the lack of photos from that age group. The younger age group, will be an issue but the probability of someone under the age of 14 trying to buy alcohol is extremely low.

# %% [markdown]
# ## Modelling

# %% [markdown]
# Define the necessary functions to train your model on the GPU platform and build a single script containing all of them along with the initialization section.
# 
# To make this task easier, you can define them in this notebook and run a ready code in the next section to automatically compose the script.
# 
# The definitions below will be checked by project reviewers as well, so that they can understand how you built the model.

# %%
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam

# %%
def load_train(path):
    labels = pd.read_csv(path+'labels.csv')

    train_datagen = ImageDataGenerator(rescale= 1./255, validation_split=0.25)

    train_datagen_flow = train_datagen.flow_from_dataframe(
        dataframe = labels,
        directory = path + 'final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='training',
        horizontal_flip=True,
        vertical_flip = True,
        rotation_range=90,
        seed=42)

    return train_gen_flow

# %%
def load_test(path):
    labels = pd.read_csv(path + 'labels.csv')

    test_datagen = ImageDataGenerator(rescale= 1./255, validation_split=0.25)

    test_datagen_flow = test_datagen.flow_from_dataframe(
        dataframe = labels,
        directory = path + 'final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset='validation',
        seed=42)

    # place your code here

    return test_gen_flow

# %%

def create_model(input_shape):
    backbone = ResNet50(
    input_shape=input_shape, weights='imagenet', include_top=False
    )

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(10, activation='relu'))

    optimizer = Adam(lr=0.0001)
    model.compile(
        optimizer=optimizer,
        loss='mean_squared_error',
        metrics=['mae'],
    )

    return model

# %%
def train_model(model, train_data, test_data, batch_size=None, epochs=10,
                steps_per_epoch=None, validation_steps=None):
    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)

    if validation_steps is None:
        validation_steps = len(test_data)

    model.fit(train_data,
              validation_data=test_data,
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2, shuffle=True)

    return model

# %% [markdown]
# ## Prepare the Script to Run on the GPU Platform

# %% [markdown]
# Given you've defined the necessary functions you can compose a script for the GPU platform, download it via the "File|Open..." menu, and to upload it later for running on the GPU platform.
# 
# N.B.: The script should include the initialization section as well. An example of this is shown below.

# %%
# prepare a script to run on the GPU platform

init_str = """
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
"""

import inspect

with open('run_model_on_gpu.py', 'w') as f:

    f.write(init_str)
    f.write('\n\n')

    for fn_name in [load_train, load_test, create_model, train_model]:

        src = inspect.getsource(fn_name)
        f.write(src)
        f.write('\n\n')

# %% [markdown]
# ### Output

# %% [markdown]
# Place the output from the GPU platform as an Markdown cell here.

# %% [markdown]
# * Train for 178 steps, validate for 60 steps
# 
# * Epoch 1/10
# * 2023-06-05 16:11:01.123641: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
# * 2023-06-05 16:11:01.357887: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
# * 178/178 - 46s - loss: 382.1084 - mae: 14.4312 - val_loss: 1064.5504 - val_mae: 27.8982
# * Epoch 2/10
# * 178/178 - 38s - loss: 71.5657 - mae: 6.3091 - val_loss: 694.3267 - val_mae: 21.1118
# * Epoch 3/10
# * 178/178 - 38s - loss: 36.5007 - mae: 4.6485 - val_loss: 269.1267 - val_mae: 12.1678
# * Epoch 4/10
# * 178/178 - 39s - loss: 22.2315 - mae: 3.6570 - val_loss: 129.6283 - val_mae: 8.6992
# * Epoch 5/10
# * 178/178 - 38s - loss: 16.6927 - mae: 3.1819 - val_loss: 88.4709 - val_mae: 7.0212
# * Epoch 6/10
# * 178/178 - 38s - loss: 13.2796 - mae: 2.8518 - val_loss: 68.4655 - val_mae: 6.2144
# * Epoch 7/10
# * 178/178 - 38s - loss: 12.2345 - mae: 2.7427 - val_loss: 76.3566 - val_mae: 6.4656
# * Epoch 8/10
# * 178/178 - 37s - loss: 11.8866 - mae: 2.6308 - val_loss: 71.2983 - val_mae: 6.3095
# * Epoch 9/10
# * 178/178 - 38s - loss: 9.9428 - mae: 2.4048 - val_loss: 66.6300 - val_mae: 6.1906
# * Epoch 10/10
# * 178/178 - 38s - loss: 7.5713 - mae: 2.0873 - val_loss: 85.0505 - val_mae: 7.1976
# 
# * 60/60 - 9s - loss: 85.0505 - mae: 7.1976
# * Test MAE: 7.1976m

# %% [markdown]
# ## Conclusions

# %% [markdown]
# The model reached the test MAE value of 7.1976, which reached our goal value. Interesting enough when I added more layers to the model the MAE increased substantially, therefore I kept the number of layers low.

# %% [markdown]
# We can conclude also, that our model has a high probability of being better at classifying in the age groups of 14-48 years old, which should be great for the company. If a customer is younger than that an employee should immediately be able to recognize that, vise versa, if a customer is over the age of 50, your employee should be able to figure out that information, as well. Between the ages of 15-30 is where I feel it can get tricky trying to tell if a customer is over the age of 21 or not and our model is well suited to predict that information.

# %% [markdown]
# # Checklist

# %% [markdown]
# - [x]  Notebook was opened
# - [x]  The code is error free
# - [x]  The cells with code have been arranged by order of execution
# - [x]  The exploratory data analysis has been performed
# - [x]  The results of the exploratory data analysis are presented in the final notebook
# - [x]  The model's MAE score is not higher than 8
# - [x]  The model training code has been copied to the final notebook
# - [x]  The model training output has been copied to the final notebook
# - [x]  The findings have been provided based on the results of the model training

# %%



