import csv
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import cm
import numpy as np
import pygal.maps.world
from pygal.maps.world import COUNTRIES
import Natomilitaryspending
filename = 'F:\Pythonprojects\Military Expenditures\Democracy Index.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)#grabs the first row of the data which is the headers
    #print(header_row)


    data = []
    for row in reader:
        if int(row[2])>2014:
            if len(data)==0 or row[1] != data[-1][0]:
                country=[]
                country.append(row[1])
                country.append(float(row[3]))
                data.append(country)
            else:
                data[-1][1]+=float(row[3])

for d in data:
    d[1]/=5
    d[1] = float(str('%.2f'%d[1]))
for i in range(0,len(data)-1):
    if data[i][0] in Natomilitaryspending.all_names:
        data[i].append(Natomilitaryspending.all_country_spending[Natomilitaryspending.all_names.index(data[i][0])])
    #print('.')
#print(len(data), len(Natomilitaryspending.all_country_spending))

for d in data:
    if len(d)<=2:
        data.remove(d)

def sortSpending(val): 
    return val[2] 
data.sort(key = sortSpending, reverse=True)

xdata=[]
ydata=[]
for d in data:
    if len(d)>2:
        xdata.append(d[1])
        ydata.append(d[2])
fig =plt.figure(1)
plt.scatter(xdata[:10], ydata[:10], label= 'Top 10 Spenders', color='red')
plt.scatter(xdata[10:25], ydata[10:25], label= 'Next 15', color='blue')
plt.scatter(xdata[25:], ydata[25:], label= 'Rest of World', color='green')
plt.xlabel('Democracy Index')
plt.xlabel('Democracy Index')
plt.title('Democracy vs. Military Spending')
z = np.polyfit(xdata, ydata, 1)
p = np.poly1d(z)
yhat = p(xdata)                         # or [p(z) for z in x]
ybar = np.sum(ydata)/len(ydata)          # or sum(y)/len(y)
ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
sstot = np.sum((ydata - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
Rsquared = ssreg / sstot

plt.plot(xdata,p(xdata),"r--", label=("y=%.0fx+(%.0f)"%(z[0],z[1])+" r^2:%.4f"%(Rsquared)))
plt.legend()
plt.show()

fig =plt.figure(2)
plt.scatter(xdata[10:25], ydata[10:25], label= 'Next 15', color='blue')
plt.scatter(xdata[25:], ydata[25:], label= 'Rest of World', color='green')
plt.xlabel('Democracy Index')
plt.xlabel('Democracy Index')
plt.title('Democracy vs. Military Spending')
z = np.polyfit(xdata[10:], ydata[10:], 1)
p = np.poly1d(z)
yhat = p(xdata[10:])                         # or [p(z) for z in x]
ybar = np.sum(ydata[10:])/len(ydata[10:])          # or sum(y)/len(y)
ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
sstot = np.sum((ydata[10:] - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
Rsquared = ssreg / sstot
plt.plot(xdata[10:],p(xdata[10:]),"r--", label=("y=%.0fx+(%.0f)"%(z[0],z[1])+" r^2:%.4f"%(Rsquared)))
plt.legend()
plt.show()

fig =plt.figure(3)
plt.scatter(xdata[25:], ydata[25:], label= 'Rest of World', color='green')
plt.xlabel('Democracy Index')
plt.xlabel('Democracy Index')
plt.title('Democracy vs. Military Spending')
z = np.polyfit(xdata[25:], ydata[25:], 1)
p = np.poly1d(z)
yhat = p(xdata[25:])                         # or [p(z) for z in x]
ybar = np.sum(ydata[25:])/len(ydata[25:])          # or sum(y)/len(y)
ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
sstot = np.sum((ydata[25:] - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
Rsquared = ssreg / sstot
plt.plot(xdata[25:],p(xdata[25:]),"r--", label=("y=%.0fx+(%.0f)"%(z[0],z[1])+" r^2:%.4f"%(Rsquared)))

plt.legend()

plt.show()

