import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
wheat_data = pd.read_csv('C:\\Users\\shubh\\Documents\\Github\\DAT210x\\Module3\\Datasets\\wheat.data', index_col = 0)
df1 = wheat_data.loc[:, ['area', 'perimeter']]
df2 = wheat_data.loc[:, ['asymmetry', 'groove']]

#
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
df1.plot.hist(alpha=0.75)


#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
df2.plot.hist(alpha=0.75)


#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
# .. your code here ..


# Display the graphs:
plt.show()

