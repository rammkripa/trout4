# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd

import seaborn as sns

iris = sns.load_dataset("iris")
iris.head()

sns.displot(iris['petal_width'])

import numpy as np
np.average(iris['petal_width'])

print("hello world")

iris['sepal_length'].median()

iris['species'].value_counts()

iris['species']

sns.displot(iris['sepal_length'])

sns.scatterplot(x = iris['sepal_length'], y = iris['sepal_width'])

# +
#Hello world
# -
# ### Hellow World ###


def func(x):
    return x**4


func(4)

sns.violinplot(data = iris, x = 'species', y = 'sepal_length')


