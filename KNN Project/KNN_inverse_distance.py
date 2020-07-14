import numpy as np
from collections import defaultdict
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

class KNeighborsClassifier(object):
    def __init__(self, n_neighbors=5, weights='uniform', p=2, scalars=[]):
        self.n_neighbors = n_neighbors
        self.weights=weights
        self.p=p
        self.scalars=scalars
    def fit(self, X, y):
        self.X = X
        self.y = y
        return self

    def _predict_one(self, test):
        distances = sorted((self._distance(x, test), y) for x, y in zip(self.X, self.y))
        weights = self._compute_weights(distances[:self.n_neighbors])
        weights_by_class = defaultdict(list)
        for d,c in weights:
            weights_by_class[c].append(d)
        
        counts=[(sum(val), key) for key, val in weights_by_class.items()]
        majority = max(counts)
##        print(max(counts))
        return majority[1]


    def predict(self, X):
        return [self._predict_one(i) for i in X]
    def _distance(self, data1, data2):
        """returns Manhattan distance"""
        if self.p==1:
            if self.scalars!=[]:
                total =0
                for i in range(len(self.scalars)):
                    total+=self.scalars[i]*(abs(data1[i]-data2[i]))
                total= np.sqrt(total)
                return total
            else:
                return sum(abs(data1-data2))
        elif self.p==2:
            if self.scalars!=[]:
                total =0
                for i in range(len(self.scalars)):
                    total+=self.scalars[i]*(abs(data1[i]-data2[i])**2)
                total= np.sqrt(total)
                return total
            else:
                return np.sqrt(sum(abs(data1-data2)**2))
        else:
            raise ValueError("p not recognized: should be 1 or 2")
    def _compute_weights(self, distances):
        """computes uniform weights"""
        if self.weights=='uniform':
            return[(1,y) for d,y in distances]
        elif self.weights =='distance':
            matches = [(1, y) for d, y in distances if d == 0]
            if matches:
                return matches
            else:
                return [(1/d,y) for d,y in distances]
        else:
            raise ValueError("weights not recognized: should be 'uniform', 'scalars', or 'distance'")
    def score(self,X,y):
        return sum(1 for p, t in zip(self.predict(X), y) if abs(p-t)<5) / len(y)

#X_train, X_temp, y_train, y_temp = train_test_split(iris.data, iris.target, test_size=.3)
#X_validation, X_test, y_validation, y_test = train_test_split(X_temp, y_temp, test_size=.5)

#neighbor = KNeighborsClassifier(p=1).fit(X_train, y_train)

#print(neighbor.score(X_train, y_train))
#print(neighbor.score(X_validation, y_validation))



'''
neighbor = KNeighborsClassifier(p=2)
print(neighbor._distance(np.array([-1, -1]),np.array([1, -2])))

neighbor = KNeighborsClassifier(weights='distance')
print(neighbor._compute_weights(np.array([(1, 0), (2, 0), (3, 1)])))

X = np.array([[1, 1], [4, 4], [5, 5]])
y = np.array([1,0,0])
neighbor = KNeighborsClassifier(n_neighbors=3, weights='distance').fit(X, y)
print(neighbor._predict_one(np.array([0, 0])))

'''
