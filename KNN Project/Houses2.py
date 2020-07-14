import csv
import numpy as np
filename = 'F:\Pythonprojects\KNN Project\houses.csv'


with open(filename) as f:#input data
    reader = csv.reader(f)
    header_row = next(reader)

    houses=[]
    
    for row in reader:
        houses.append(row[:9])#only want name and numerical rows
    f.close()
#Separate Training from Testing Data
train=[]
test=[]
for i in range(len(houses)):
    if i%10<7:
        train.append(houses[i])
    else:
        test.append(houses[i])
        #print(h[0])

#create normalization formula for each column based on training data
mins=['',10000000000,1000000,100000,1000,1000,1000,1000,10000000]
maxes=['',0,0,0,0,0,0,0,0]

for h in train:
    for i in range(1, len(h)):
        h[i]=float(h[i])
        if h[i]>float(maxes[i]):
            maxes[i]=h[i]
        elif h[i]<mins[i]:
            mins[i]=h[i]

#normalize data
#don't normalize output variables

for h in train:
    for i in range(1, len(h)-1):
        h[i]=(float(h[i])-mins[i])/(maxes[i]-mins[i])#float(h[i])#
    h[-1]=float(h[-1])
for h in test:
    for i in range(1, len(h)-1):
        h[i]=(float(h[i])-mins[i])/(maxes[i]-mins[i])#float(h[i])#
    h[-1]=float(h[-1])

#separate input and output variables, convert to np.array
Y_tr=[]
X_tr=[]
for h in train:
    Y_tr.append(h[-1])
    X_tr.append(h[1:8])

X_tst=[]
Y_tst=[]
for h in test:
    Y_tst.append(h[-1])
    X_tst.append(h[1:8])

X_train=np.array(X_tr)
y_train=np.array(Y_tr)
X_test=np.array(X_tst)
y_test=np.array(Y_tst)

#print(X_test,y_test)


#call knn algorithm
import KNN_inverse_distance as knn
n_neighbors=1
p=2
weights='uniform'
scalars=[1,1,1.2,1.2,1,.8,.9]
neighbor = knn.KNeighborsClassifier(n_neighbors=n_neighbors,weights=weights,p=p, scalars=scalars).fit(X_train, y_train)
print('neighbors: '+str(n_neighbors),'\np: '+str(p), '\nweights: '+str(weights))
#print(y_test[0], neighbor._predict_one(X_test[0]))
print(neighbor.score(X_train, y_train))
print(neighbor.score(X_test, y_test))
