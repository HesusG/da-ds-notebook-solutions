# %% [markdown]
# ## Initialization

# %%
import pandas as pd
pd.set_option('display.max_columns', None)
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

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
labels = pd.read_csv('datasets/faces/labels.csv')

labels.info()

# %%
labels.head()

# %%
fig = plt.figure(figsize=(10,10))

for i in range(12):
    fig.add_subplot(4, 3, i+1)
    plt.imshow(Image.open('datasets/faces/final_files/' + labels['file_name'][i]))
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

# %% [markdown]
# By outputting a sample of the images, we can see that they are likely drawn from many sources such as as TV/Film and social media.
# 
# Also, we can see that the images were preprocessed so that the faces are all similar sizes, centered in the frame, and rotated as needed to be vertically oriented. Most features neutral or smiling facial expressions. Lighting conditions vary, some are wearing hats or glasses or have hair covering parts of  their face but there are no other facial obstructions.

# %% [markdown]
# ## EDA

# %%
# observe the distribution of ages
fig = px.histogram(labels['real_age'])
rolling_mean = labels.groupby('real_age').count().rolling(window=5).mean().dropna().reset_index()
fig.add_scatter(x=rolling_mean['real_age'], y=rolling_mean['file_name'], mode='lines', name='Rolling Mean')


# %%
# look for correlations between index position (file name) and age
px.scatter(labels['real_age'])

# %% [markdown]
# ### Findings

# %% [markdown]
# Ages have a roughly normal, slightly right skewed distribution centered around 25. There are some ages, particularly 25 and multiples of 10 (e.g. 30, 40) that have counts that stick out above the trendline.
# 
# There is no apparent correlation between file names and real ages.
# 
# There is a relatively large sample of pictures for young children less than 8 - this data may not be as useful as data for people nearer the drinking age.

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

    """
    It loads the train part of dataset from path
    """

    train_datagen = ImageDataGenerator(rescale=1/255.,
                                      validation_split=0.25)

    train_gen_flow = train_datagen.flow_from_dataframe(
        labels,
        directory='datasets/faces/final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(150, 150),
        batch_size=16,
        class_mode='raw',
        subset='training',
        seed=617)

    return train_gen_flow

# %%
def load_test(path):

    """
    It loads the validation/test part of dataset from path
    """
    test_datagen = ImageDataGenerator(rescale=1/255.,
                                      validation_split=0.25)

    test_gen_flow = test_datagen.flow_from_dataframe(
        labels,
        directory='datasets/faces/final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(150, 150),
        batch_size=16,
        class_mode='raw',
        subset='validation',
        seed=617)

    return test_gen_flow

# %%
def create_model(input_shape):

    """
    It defines the model
    """

    backbone = ResNet50(
        input_shape=input_shape, weights='imagenet', include_top=False
    )

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1, activation='relu'))

    optimizer = Adam(lr=0.0001)
    model.compile(optimizer=optimizer, loss='mean_absolute_error',
                  metrics=['mae'])


    return model

# %%
def train_model(model, train_data, test_data, batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):

    """
    Trains the model given the parameters
    """

    if steps_per_epoch is None:
        steps_per_epoch = len(train_data)
    if validation_steps is None:
        validation_steps = len(test_data)

    model.fit(train_data,
              validation_data=test_data,
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2)

    return model

# %% [markdown]
# ### Prepare the Script to Run on the GPU Platform

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

labels = pd.read_csv('datasets/faces/labels.csv')
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
# Train for 356 steps, validate for 119 steps
# 
# Epoch 1/20
# 
# 2023-05-28 10:58:32.532870: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
# 
# 2023-05-28 10:58:33.993322: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
# 
# 356/356 - 65s - loss: 11.1080 - mae: 11.1095 - val_loss: 27.7789 - val_mae: 27.7723
# 
# Epoch 2/20
# 
# 356/356 - 35s - loss: 7.3094 - mae: 7.3103 - val_loss: 9.7070 - val_mae: 9.7080
# 
# Epoch 3/20
# 
# 356/356 - 35s - loss: 6.0212 - mae: 6.0208 - val_loss: 9.0571 - val_mae: 9.0676
# 
# Epoch 4/20
# 
# 356/356 - 35s - loss: 5.0915 - mae: 5.0919 - val_loss: 6.7187 - val_mae: 6.7213
# 
# Epoch 5/20
# 
# 356/356 - 35s - loss: 4.5280 - mae: 4.5277 - val_loss: 6.6355 - val_mae: 6.6417
# 
# Epoch 6/20
# 
# 356/356 - 35s - loss: 3.9675 - mae: 3.9677 - val_loss: 6.9997 - val_mae: 7.0079
# 
# Epoch 7/20
# 
# 356/356 - 35s - loss: 3.5931 - mae: 3.5926 - val_loss: 7.0273 - val_mae: 7.0303
# 
# Epoch 8/20
# 
# 356/356 - 35s - loss: 3.4088 - mae: 3.4088 - val_loss: 6.3779 - val_mae: 6.3833
# 
# Epoch 9/20
# 
# 356/356 - 35s - loss: 3.1256 - mae: 3.1257 - val_loss: 6.7880 - val_mae: 6.7968
# 
# Epoch 10/20
# 
# 356/356 - 35s - loss: 2.8990 - mae: 2.8984 - val_loss: 6.3002 - val_mae: 6.3048
# 
# Epoch 11/20
# 
# 356/356 - 36s - loss: 2.7770 - mae: 2.7771 - val_loss: 6.1990 - val_mae: 6.2056
# 
# Epoch 12/20
# 
# 356/356 - 36s - loss: 2.7293 - mae: 2.7289 - val_loss: 6.3254 - val_mae: 6.3299
# 
# Epoch 13/20
# 
# 356/356 - 37s - loss: 2.5904 - mae: 2.5902 - val_loss: 7.3467 - val_mae: 7.3534
# 
# Epoch 14/20
# 
# 356/356 - 42s - loss: 2.5084 - mae: 2.5079 - val_loss: 7.0347 - val_mae: 7.0371
# 
# Epoch 15/20
# 
# 356/356 - 36s - loss: 2.4109 - mae: 2.4107 - val_loss: 6.1430 - val_mae: 6.1494
# 
# Epoch 16/20
# 
# 356/356 - 35s - loss: 2.2784 - mae: 2.2782 - val_loss: 6.2913 - val_mae: 6.2923
# 
# Epoch 17/20
# 
# 356/356 - 35s - loss: 2.2918 - mae: 2.2916 - val_loss: 6.4319 - val_mae: 6.4370
# 
# Epoch 18/20
# 
# 356/356 - 35s - loss: 2.1623 - mae: 2.1624 - val_loss: 6.3695 - val_mae: 6.3756
# 
# Epoch 19/20
# 
# 356/356 - 35s - loss: 2.1098 - mae: 2.1099 - val_loss: 6.7736 - val_mae: 6.7811
# 
# Epoch 20/20
# 
# 356/356 - 35s - loss: 2.0834 - mae: 2.0835 - val_loss: 6.3694 - val_mae: 6.3721
# 
# WARNING:tensorflow:sample_weight modes were coerced from
# 
#   ...
# 
#     to
# 
#   ['...']
# 
# 119/119 - 9s - loss: 6.3694 - mae: 6.3721
# 
# Test MAE: 6.3721
# 

# %% [markdown]
# ## Conclusions

# %% [markdown]
# This model performed very well against the target metric of an MAE of 8, achieving an MAE of 6.37 after 20 epochs. Review of the outputs suggests the the algorithm plateaued after only a few epochs and continued to range between ~6.2-7.3 until the 20 epochs had been reached.

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


