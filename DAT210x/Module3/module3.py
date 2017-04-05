# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:48:02 2017

@author: shubh
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.style.use('ggplot')
student_dataset = pd.read_csv('C:\\Users\\shubh\\Documents\\Github\\DAT210x\\Module3\\Datasets\\students.data', index_col = 0)
my_series = student_dataset.G3
my_dataframe = student_dataset[['G3', 'G2', 'G1']]
my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.4, normed = True)
student_dataset.plot.scatter(x='G1', y='G3')


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')
ax.scatter(student_dataset.G1, student_dataset.G3, student_dataset['Dalc'], c='r', marker='.')
plt.show()

from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates
data = load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names)
df['target_names'] = [data.target_names[i] for i in data.target]

# Parallel Coordinates Start Here:
plt.figure()
parallel_coordinates(df, 'target_names')
plt.show()

# Andrews Curves Start Here:
from pandas.tools.plotting import andrews_curves
plt.figure()
andrews_curves(df, 'target_names')
plt.show()

