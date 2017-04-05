import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
wheat_data = pd.read_csv('C:\\Users\\shubh\\Documents\\Github\\DAT210x\\Module3\\Datasets\\wheat.data', index_col = 0)



fig = plt.figure()

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')
ax.scatter(wheat_data.area, wheat_data.perimeter, wheat_data.asymmetry, c='red', marker='.')
plt.show()


fig = plt.figure()
#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')
ax.scatter(wheat_data.width, wheat_data.groove, wheat_data.length, c='green', marker='.')
plt.show()



