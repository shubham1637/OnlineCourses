import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')

#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
samples = list()
colors = list()
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
import os
directory = "Datasets/ALOI/32/"
for filename in os.listdir(directory):
    if filename.endswith(".png"): 
        img = misc.imread(os.path.join(directory, filename))
        img = img[::2, ::2]
        img = (img).reshape(-1)
        samples.append(img)
        colors.append('b')
print len(samples)
#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.

directory = "Datasets/ALOI/32i/"
for filename in os.listdir(directory):
    if filename.endswith(".png"): 
        img = misc.imread(os.path.join(directory, filename))
        img = img[::2, ::2]
        img = (img).reshape(-1)
        samples.append(img)
        colors.append('r')
print len(samples)

#
# TODO: Convert the list to a dataframe
#
df = pd.DataFrame(samples)

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
from sklearn import manifold
iso = manifold.Isomap(n_neighbors = 6, n_components = 3)
iso.fit(df)
manifold = iso.transform(df)

#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(manifold[:,0], manifold[:,1], marker='.', alpha=0.7, c= colors)
plt.show()

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')
ax.scatter(manifold[:,0], manifold[:,1], manifold[:,2], c= colors, marker='.')
plt.show()