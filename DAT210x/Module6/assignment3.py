#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn import manifold

X = pd.read_csv('Datasets/parkinsons.data', index_col = 0)
# print X.head(2)

y = X['status'].copy()
X.drop(labels=['status'], inplace=True, axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 7)
Nrmlzr = preprocessing.StandardScaler().fit(X_train) #Normalizer, MaxAbsScaler, MinMaxScaler, KernelCenterer, StandardScaler
X_train = Nrmlzr.transform(X_train)
X_test = Nrmlzr.transform(X_test)

#model = PCA(n_components = 8)
model = manifold.Isomap(n_neighbors = 4, n_components = 5)

model.fit(X_train)
X_train = model.transform(X_train)
X_test = model.transform(X_test)

svc = SVC()
svc.fit(X_train, y_train)
score = svc.score(X_test, y_test)
print score


best_score = 0
c_range = np.arange(0.05, 2.05, 0.05)
gamma_range = np.arange(0.001, 0.101, 0.001)

for c in c_range:
    for gamma1 in gamma_range:
        svc = SVC(gamma = gamma1, C = c)
        svc.fit(X_train, y_train)
        score = svc.score(X_test, y_test)
        if score > best_score:
            best_score = score
            C = c
            G = gamma1
print best_score, "   ", C, "    ", G, "   "