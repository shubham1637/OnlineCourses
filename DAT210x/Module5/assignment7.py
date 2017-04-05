# If you'd like to try this lab with PCA instead of Isomap,
# as the dimensionality reduction technique:
Test_PCA = True
import pandas as pd

def plotDecisionBoundary(model, X, y):
  print "Plotting..."
  import matplotlib.pyplot as plt
  import matplotlib
  matplotlib.style.use('ggplot') # Look Pretty

  fig = plt.figure()
  ax = fig.add_subplot(111)

  padding = 0.1
  resolution = 0.1

  #(2 for benign, 4 for malignant)
  colors = {2:'royalblue',4:'lightsalmon'} 

  
  # Calculate the boundaris
  x_min, x_max = X[:, 0].min(), X[:, 0].max()
  y_min, y_max = X[:, 1].min(), X[:, 1].max()
  x_range = x_max - x_min
  y_range = y_max - y_min
  x_min -= x_range * padding
  y_min -= y_range * padding
  x_max += x_range * padding
  y_max += y_range * padding

  # Create a 2D Grid Matrix. The values stored in the matrix
  # are the predictions of the class at at said location
  import numpy as np
  xx, yy = np.meshgrid(np.arange(x_min, x_max, resolution),
                       np.arange(y_min, y_max, resolution))

  # What class does the classifier say?
  Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
  Z = Z.reshape(xx.shape)

  # Plot the contour map
  plt.contourf(xx, yy, Z, cmap=plt.cm.seismic)
  plt.axis('tight')

  # Plot your testing points as well...
  for label in np.unique(y):
    indices = np.where(y == label)
    plt.scatter(X[indices, 0], X[indices, 1], c=colors[label], alpha=0.8)

  p = model.get_params()
  plt.title('K = ' + str(p['n_neighbors']))
  plt.show()

# 
# TODO: Load in the dataset, identify nans, and set proper headers.
# Be sure to verify the rows line up by looking at the file in a text editor.
#
df = pd.read_csv('Datasets/breast-cancer-wisconsin.data', header = None)
df.columns = ['sample', 'thickness', 'size', 'shape', 'adhesion', 'epithelial', 'nuclei', 'chromatin', 'nucleoli', 'mitoses', 'status']
df.isnull().sum()

# 
# TODO: Copy out the status column into a slice, then drop it from the main
# dataframe. Always verify you properly executed the drop by double checking
# (printing out the resulting operating)! Many people forget to set the right
# axis here.
#
# If you goofed up on loading the dataset and notice you have a `sample` column,
# this would be a good place to drop that too if you haven't already.
#
y = df['status'].copy()
df.drop(labels=['status', 'sample'], inplace=True, axis=1)
df['nuclei'] = pd.to_numeric(df['nuclei'] , errors = 'coerce')

#
# TODO: With the labels safely extracted from the dataset, replace any nan values
# with the mean feature / column value
#
df = df.fillna(df.mean())

#
# TODO: Do train_test_split. Use the same variable names as on the EdX platform in
# the reading material, but set the random_state=7 for reproduceability, and keep
# the test_size at 0.5 (50%).
#
from sklearn.model_selection import train_test_split
data_train, data_test, label_train, label_test = train_test_split(df, y, test_size=0.5, random_state = 7)

#
# TODO: Experiment with the basic SKLearn preprocessing scalers. We know that
# the features consist of different units mixed in together, so it might be
# reasonable to assume feature scaling is necessary. Print out a description
# of the dataset, post transformation. Recall: when you do pre-processing,
# which portion of the dataset is your model trained upon? Also which portion(s)
# of your dataset actually get transformed?
from sklearn import preprocessing
#Prc = preprocessing.StandardScaler().fit(data_train)
#Prc = preprocessing.MinMaxScaler().fit(data_train)
#Prc = preprocessing.MaxAbsScaler().fit(data_train)
Prc = preprocessing.RobustScaler().fit(data_train)
#Prc = preprocessing.Normalizer().fit(data_train)

#X_train = Prc.transform(data_train)
#X_test = Prc.transform(data_test)
X_train = data_train # We do not need to do pre-processing as it is said in the data description that values are already within 1-10 range
X_test = data_test
#
# PCA and Isomap are your new best friends
model = None
if Test_PCA:
  print "Computing 2D Principle Components"
  #
  # TODO: Implement PCA here. Save your model into the variable 'model'.
  # You should reduce down to two dimensions.
  #
  from sklearn.decomposition import PCA
  model = PCA(n_components = 2)
  model.fit(X_train)

else:
  print "Computing 2D Isomap Manifold"
  #
  # TODO: Implement Isomap here. Save your model into the variable 'model'
  # Experiment with K values from 5-10.
  # You should reduce down to two dimensions.
  #
  from sklearn import manifold
  model = manifold.Isomap(n_neighbors = 8, n_components = 2)
  model.fit(data_train)
  
#
# TODO: Train your model against data_train, then transform both
# data_train and data_test using your model. You can save the results right

# back into the variables themselves.
#
X_train = model.transform(X_train)
X_test = model.transform(X_test)

# 
# TODO: Implement and train KNeighborsClassifier on your projected 2D
# training data here. You can use any K value from 1 - 15, so play around
# with it and see what results you can come up. Your goal is to find a
# good balance where you aren't too specific (low-K), nor are you too
# general (high-K). You should also experiment with how changing the weights
# parameter affects the results.
#
from sklearn.neighbors import KNeighborsClassifier
knmodel = KNeighborsClassifier(n_neighbors = 4, weights = 'distance')
knmodel.fit(X_train, label_train)

#
# INFO: Be sure to always keep the domain of the problem in mind! It's
# WAY more important to errantly classify a benign tumor as malignant,
# and have it removed, than to incorrectly leave a malignant tumor, believing
# it to be benign, and then having the patient progress in cancer. Since the UDF (user defineable function)
# weights don't give you any class information, the only way to introduce this
# data into SKLearn's KNN Classifier is by "baking" it into your data. For
# example, randomly reducing the ratio of benign samples compared to malignant
# samples from the training set.

#
# TODO: Calculate + Print the accuracy of the testing set
#
print knmodel.score(X_test, label_test)

plotDecisionBoundary(knmodel, X_test, label_test)
