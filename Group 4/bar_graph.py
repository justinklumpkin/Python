from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import cm
import numpy as np
filename='efficiency.txt'
f= open(filename, 'r')


names=[]
values=[]
for i in range(3):
    line=f.readline()
    names.append(line)
    line=f.readline()
    values.append(float(line))


style.use('ggplot')
plt.bar(names[0], values[0], label="Aluminum: "+'{:.4%}'.format(values[0]),color='r',width=.7)
plt.bar(names[1], values[1], label="Maple: "+'{:.4%}'.format(values[1]),color='b',width=.7)
plt.bar(names[2], values[2], label="Plastic: "+'{:.4%}'.format(values[2]),color='g',width=.7)

plt.legend()
plt.xlabel('Material')
plt.ylabel('Momentum Transfer Efficiency')
plt.title('Bat Material vs. Momentum Transfer')
'''
label = [0.249, 0.141, 0.209]
 
# Text on the top of each barplot
for i in range(3):
    plt.text(x = 2*i+0.5 , y = [values[0]+0.1,values[1]+0.1,values[2]+0.1], s = label[i], size = 6)'''

plt.show()

f.close()
