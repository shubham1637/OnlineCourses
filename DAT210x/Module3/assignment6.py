import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
wheat_data = pd.read_csv('C:\\Users\\shubh\\Documents\\Github\\DAT210x\\Module3\\Datasets\\wheat.data', index_col = 0)



#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
# .. your code here ..


#
# TODO: Compute the correlation matrix of your dataframe
# 
cr = wheat_data.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
plt.imshow(cr, cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(wheat_data.columns))]
plt.xticks(tick_marks, wheat_data.columns, rotation='vertical')
plt.yticks(tick_marks, wheat_data.columns)

plt.show()



