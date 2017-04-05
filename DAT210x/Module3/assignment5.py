#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pandas.tools.plotting import andrews_curves

wheat_data = pd.read_csv('C:\\Users\\shubh\\Documents\\Github\\DAT210x\\Module3\\Datasets\\wheat.data', index_col = 0)

plt.figure()
andrews_curves(wheat_data, 'wheat_type', alpha = 0.4)
plt.show()

wheat_data = wheat_data.drop(['area', 'perimeter'], axis = 1)
plt.figure()
andrews_curves(wheat_data, 'wheat_type', alpha = 0.4)
plt.show()