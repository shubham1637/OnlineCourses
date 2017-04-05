import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]
print df.head()


# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
df.columns = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PTS/G', 'SOG', 'PCT', 'GWG', 'PP_G', 'PP_A', 'SH_G', 'SH_A']

# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
df = df.dropna(axis=0, thresh=4).reset_index(drop=True)

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
df = df.loc[df.TEAM != 'TEAM',:].reset_index(drop=True)


# TODO: Get rid of the 'RK' column
#
df = df.drop(labels=['RK'], axis=1)


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
df = df.reset_index(drop=True)
print df.head()

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#
print df.dtypes
numeric_col = ['GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PTS/G', 'SOG', 'PCT', 'GWG', 'PP_G', 'PP_A', 'SH_G', 'SH_A']
df[numeric_col] = df[numeric_col].apply(pd.to_numeric, errors = 'coerce')
print df.dtypes
# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
print df.isnull().sum()
print len(df.index)
print len(df.PCT.unique())
print df.GP[15] + df.GP[16]
