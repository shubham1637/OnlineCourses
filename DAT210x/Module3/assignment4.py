import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
wheat_data = pd.read_csv('C:\\Users\\shubh\\Documents\\Github\\DAT210x\\Module3\\Datasets\\wheat.data', index_col = 0)



#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# Also get rid of the 'area' and 'perimeter' features
# 
wheat_data = wheat_data.drop(['area', 'perimeter'], axis = 1)
 

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
plt.figure()
parallel_coordinates(wheat_data, 'wheat_type', alpha = 0.4)
plt.show()


