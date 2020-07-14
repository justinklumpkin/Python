import csv
import numpy as np
filename = 'E:\Pythonprojects\KNN Project\houses.csv'
samp_file = open("E:\Pythonprojects\KNN Project\Sample.txt","r")
'''import random#choose random   data to usee
start_pts=[]
for r in range(0, 269, 10):
    start_pts.append(r)
samp=random.sample(start_pts, 19)

for s in samp:
    print(str(s))
    samp_file.write(str(s)+' ')'''
samp =[]
for line in samp_file:#inputs the randomly generated data point indexes so the same
                        #ones are retrieved each time
    samp.append(int(line[:line.find(' ')]))

with open(filename) as f:#input data
    reader = csv.reader(f)
    header_row = next(reader)

    houses=[]
    
    for row in reader:
        houses.append(row[:9])#only want name and numerical rows
    f.close()
#Separate Training from Testing Data
train=[]
for pt in samp:
    for i in range(0,10):
        train.append(houses[pt+i])
    #print(houses[pt][0])

test=[]
for h in houses:
    if h not in train:
        test.append(h)
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
for h in train:
    for i in range(1, len(h)-1):
        h[i]=(float(h[i])-mins[i])/(maxes[i]-mins[i])#float(h[i])#
    h[-1]=float(h[-1])
#don't normalize output variables
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
neighbor = knn.KNeighborsClassifier(n_neighbors=n_neighbors,weights=weights,p=p).fit(X_train, y_train)
print('neighbors: '+str(n_neighbors),'\np: '+str(p), '\nweights: '+str(weights))
#print(y_test[0], neighbor._predict_one(X_test[0]))
print(neighbor.score(X_train, y_train))
print(neighbor.score(X_test, y_test))
