# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:50:48 2017

@author: shubh
"""

import pandas as pd
df = pd.read_csv('C:\\Users\\shubh\\Documents\\Github\\DAT210x\\Module2\\Datasets\\direct_marketing.csv')
df.head(5)
df.describe()
df.columns
df.index
print df.tail(5)
df.dtypes

from sklearn.feature_extraction.text import CountVectorizer

corpus = [
"Authman ran faster than Harry because he is an athlete.",
"Authman and Harry ran faster and faster.",
]
print corpus
bow = CountVectorizer()
X = bow.fit_transform(corpus)
bow.get_feature_names()
X.toarray()

from scipy import misc
