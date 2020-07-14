#includes age and ethnic info
import csv
from matplotlib import pyplot as plt
from matplotlib import style
#filename = 'E:\Pythonprojects\Singapore\singapore-residents-by-age-group-ethnic-group-and-sex-end-june-annual.csv'
filename = 'F:\Pythonprojects\Singapore\singapore-residents-by-age-group-ethnic-group-and-sex-end-june-annual.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)#grabs the first row of the data which is the headers
    #print(header_row)

    age = []
    chinese_male = []
    chinese_female=[]
    malay_age = []
    malay_male = []
    malay_female=[]
    indian_male=[]
    indian_female=[]
    other_male=[]
    other_female=[]
    #read in data, ignore male/female
    for row in reader:
        if int(row[0])==2018:
            if row[1]=='Total Male Chinese' and row[2].find('Over')==-1:
                age.append(row[2][0:-6])
                chinese_male.append(int(row[3]))
            elif row[1]=='Total Female Chinese' and row[2].find('Over')==-1:
                chinese_female.append(int(row[3]))
            elif row[1]=='Total Male Malays' and row[2].find('Over')==-1:
                malay_male.append(int(row[3]))
            elif row[1]=='Total Female Malays' and row[2].find('Over')==-1:
                malay_female.append(int(row[3]))
            elif row[1]=='Total Male Indians' and row[2].find('Over')==-1:
                indian_male.append(int(row[3]))
            elif row[1]=='Total Female Indians' and row[2].find('Over')==-1:
                indian_female.append(int(row[3]))
            elif row[1]=='Other Ethnic Groups (Males)' and row[2].find('Over')==-1:
                other_male.append(int(row[3]))
            elif row[1]=='Other Ethnic Groups (Females)' and row[2].find('Over')==-1:
                other_female.append(int(row[3]))

            

style.use('ggplot')

#Female Chinese
fig =plt.figure(1)
ax1 = plt.subplot(121)
plt.barh(age, chinese_female, align='center', color='r')
ax1.invert_xaxis()
plt.grid(True,color='k')
ax1.yaxis.tick_right()
plt.xlabel('Female Population', fontsize = 20)
plt.ylabel('Age', fontsize = 20)
plt.tick_params(axis='y',labelsize=15)
plt.tick_params(axis='x',labelsize=14, rotation=20)
fig.suptitle('Chinese Population Distribution by Age (2018)', fontsize = 20)

#Male Chinese
ax2 = plt.subplot(122, sharey=ax1)
plt.barh(age, chinese_male, align='center', color='b')
ax2.set_yticklabels(age, visible = False)
plt.xlabel('Male Population', fontsize = 20)
plt.grid(True,color='k')
plt.ylabel('Age', fontsize = 20)
plt.tick_params(labelsize=14)
plt.tick_params(axis='x',labelsize=14, rotation=20)
ax2.yaxis.set_label_position("right")


#Female Malay
fig =plt.figure(2)
ax1 = plt.subplot(121)
plt.barh(age, malay_female, align='center', color='r')
ax1.invert_xaxis()
plt.grid(True,color='k')
ax1.yaxis.tick_right()
plt.xlabel('Female Population', fontsize = 20)
plt.ylabel('Age', fontsize = 20)
plt.tick_params(axis='y',labelsize=15)
plt.tick_params(axis='x',labelsize=14, rotation=20)
fig.suptitle('Malay Population Distribution by Age (2018)', fontsize = 20)


#Male Malay
ax2 = plt.subplot(122, sharey=ax1)
plt.barh(age, malay_male, align='center', color='b')
ax2.set_yticklabels(age, visible = False)
plt.xlabel('Male Population', fontsize = 20)
plt.grid(True,color='k')
plt.ylabel('Age', fontsize = 20)
plt.tick_params(labelsize=14)
plt.tick_params(axis='x',labelsize=14, rotation=20)
ax2.yaxis.set_label_position("right")

#Female Indian
fig=plt.figure(3)
ax1 = plt.subplot(121)
plt.barh(age, indian_female, align='center', color='r')
ax1.invert_xaxis()
plt.grid(True,color='k')
ax1.yaxis.tick_right()
plt.xlabel('Female Population', fontsize = 20)
plt.ylabel('Age', fontsize = 20)
plt.tick_params(axis='y',labelsize=15)
plt.tick_params(axis='x',labelsize=14, rotation=20)
fig.suptitle('Indian Population Distribution by Age (2018)', fontsize = 20)


#Male Indian
ax2 = plt.subplot(122, sharey=ax1)
plt.barh(age, indian_male, align='center', color='b')
ax2.set_yticklabels(age, visible = False)
plt.xlabel('Male Population',fontsize = 20)
plt.grid(True,color='k')
plt.ylabel('Age', fontsize = 20)
plt.tick_params(labelsize=14)
plt.tick_params(axis='x',labelsize=14, rotation=20)
ax2.yaxis.set_label_position("right")

#Female Other
fig=plt.figure(4)
ax1 = plt.subplot(121)
plt.barh(age, other_female, align='center', color='r')
ax1.invert_xaxis()
plt.grid(True,color='k')
ax1.yaxis.tick_right()
plt.xlabel('Female Population', fontsize = 20)
plt.ylabel('Age', fontsize = 20)
plt.tick_params(axis='y',labelsize=15)
plt.tick_params(axis='x',labelsize=14, rotation=20)
fig.suptitle('Other Population Distribution by Age (2018)', fontsize = 20)


#Male Other
ax2 = plt.subplot(122, sharey=ax1)
plt.barh(age, other_male, align='center', color='b')
ax2.set_yticklabels(age, visible = False)
plt.xlabel('Male Population', fontsize = 20)
plt.grid(True,color='k')
plt.ylabel('Age', fontsize = 20)
plt.tick_params(labelsize=14)
plt.tick_params(axis='x',labelsize=14, rotation=20)
ax2.yaxis.set_label_position("right")



plt.show()

