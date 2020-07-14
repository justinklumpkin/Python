import csv
from matplotlib import pyplot as plt
from matplotlib import style
filename = 'E:\Pythonprojects\Singapore\singapore-residents-by-ethnic-group-and-sex-end-june-annual.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)#grabs the first row of the data which is the headers
    #print(header_row)


    total_data = []
    #read in data, ignore male/female
    for row in reader:
        if int(row[0])>=2000 and (int(row[0]) <= 2018):
            if row[1].find('Male')==-1 and row[1].find('Female')==-1:
                total_data.append(row)

#store chinese data in separate list
chinesex = []
chinesey = []
for row in total_data:
    if row[1]=='Total Chinese':
        chinesex.append(row[0])
        chinesey.append(int(row[2]))

#store malay data in separate list
malayx = []
malayy = []
for row in total_data:
    if row[1]=='Total Malays':
        malayx.append(row[0])
        malayy.append(int(row[2]))
    
#store indian data in separate list
indianx = []
indiany = []
for row in total_data:
    if row[1]=='Total Indians':
        indianx.append(row[0])
        indiany.append(int(row[2]))

#store other data in separate list
otherx = []
othery = []
for row in total_data:
    if row[1]=='Other Ethnic Groups (Total)':
        otherx.append(row[0])
        othery.append(int(row[2]))
#plot
style.use('ggplot')

plt.plot(chinesex,chinesey, color='g', label ='Chinese',linewidth=3)
plt.plot(malayx,malayy, color='r',label = 'Malays', linewidth = 3)
plt.plot(indianx,indiany, color='b',label = 'Indians', linewidth = 3)
plt.plot(otherx,othery, color='c',label = 'Other', linewidth = 3)
plt.title('Population Distribution by Ethnicity', fontsize = 40)
plt.ylabel('Population', fontsize = 20)
plt.xlabel('Year', fontsize = 20)
plt.tick_params(labelsize=15, rotation=45)
#plt.xticks( fontsize = 15)
plt.legend()#shows the label in a legend
plt.grid(True,color='k')
plt.show()
