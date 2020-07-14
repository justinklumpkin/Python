import csv
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import cm
import numpy as np
import pygal.maps.world
from pygal.maps.world import COUNTRIES
filename = 'E:\Pythonprojects\Military Expenditures\Military Expenditure.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)#grabs the first row of the data which is the headers
    #print(header_row)

    data = []
    data2= [] #stores countries that pygal doesn't map
    #read in data, ignore male/female
    for row in reader:
        if row[2]=='Country':
            country=[]
            country.append(row[0])
            total_spending =0
            for i in range(58,62):
                if row[i]=='':
                    country.append(0)
                else:
                    country.append(float(row[i]))
                    total_spending+=float(row[i])
            country.append(total_spending)
            data.append(country)
        '''elif row[2] =='':
            country=[]
            country.append(row[0])
            total_spending =0
            for i in range(58,62):
                if row[i]=='':
                    country.append(0)
                else:
                    country.append(float(row[i]))
                    total_spending+=float(row[i])
            country.append(total_spending)
            data2.append(country)'''

NATO_Members=['Albania','Belgium','Canada','Croatia','Czech Republic','Denmark',
              'Estonia','France','Germany', 'Greece','Hungary','Iceland','Italy',
              'Latvia','Lithuania','Luxemborg','Montenegro','Netherlands','Norway','Poland',
              'Portugal','Romania','Slovakia','Slovenia','Spain','Turkey', 'United Kingdom','United States']
#print(data[0:15])
#print(len(data))
fig=plt.figure(1)
style.use('ggplot')
def sortLast(val): 
    return val[-1] 
data.sort(key = sortLast, reverse=True)

names=[]
five_year_spending=[]
for d in data:
    names.append(d[0])
    five_year_spending.append(d[-1])
all_country_spending =five_year_spending.copy()
all_names=names.copy()
names2=names.copy()
fys2=five_year_spending.copy()
for i in range(15,len(names2)):
    fys2[14]+=fys2[i]
names2[14] ='Other'
names2=names2[:15]
fys2=fys2[:15]


c=['r','g','b','k','y','c','m','#F4630F','#23FAFA','#6A16A0','#F213EF','#75F213', '#AAAAAA','#893D12','#126854']
plt.pie(fys2,labels=names2, startangle = 90, shadow = True, colors=c)
plt.title('Military Spending from 2014-2018 by Country')

fig=plt.figure(2)



NATO_total=0
for i in range(len(names)-1,-1,-1):
    if names[i] in NATO_Members and names[i]!='United States':
        #print(names[i])
        NATO_total +=five_year_spending[i]
        five_year_spending.pop(i)
        names.pop(i)
for i in range(11,len(names)):
    five_year_spending[10]+=five_year_spending[i]
names[10] ='Other'
names=names[:11]
five_year_spending=five_year_spending[:11]
names.insert(1,'NATO (excluding US)')
five_year_spending.insert(1,NATO_total)
plt.pie(five_year_spending,labels=names, startangle = 90, shadow = True, colors= c)
plt.title('Military Spending from 2014-2018 US vs. NATO vs. Rest of World')
fig=plt.figure(3)

five_year_spending[1]+=five_year_spending[0]
names[1]='NATO'

plt.pie(five_year_spending[1:],labels=names[1:], startangle = 90, shadow = True, colors= c)
plt.title('Military Spending from 2014-2018 by NATO vs. Rest of World')

plt.show()

fig=plt.figure(4)


names[2] ='Other'
for i in range(3,len(five_year_spending)):
    five_year_spending[2]+=five_year_spending[i]
five_year_spending[1]-=five_year_spending[0]#subtract us
five_year_spending[1]/=len(NATO_Members)-1#find average
five_year_spending[2]/=len(data)-len(NATO_Members)#find average
spending=[]
for i in range(0,3):
    spending.append("{:.2e}".format(five_year_spending[i]))

plt.bar(names[0],five_year_spending[0], label=spending[0])
plt.bar(names[1],five_year_spending[1], label=spending[1])
plt.bar(names[2],five_year_spending[2], label=spending[2])

plt.title('Average Military Spending from 2014-2018 US vs. NATO vs. Rest of World')
plt.legend()
plt.show()


pygal_data=[data[0],data[6]]
worldmap_chart = pygal.maps.world.World()
#worldmap_chart.force_uri_protocol = 'http'
def get_country_code(country_name):
    """return the pygal 2-digit country code for
    given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code



countries1={}
for d in data[:10]:
    countries1[get_country_code(d[0])]=d[-1]
countries2={}
for d in data[10:25]:
    countries2[get_country_code(d[0])]=d[-1]
countries3={}
for d in data[25:]:
    countries3[get_country_code(d[0])]=d[-1]

#print(countries)
worldmap_chart.add('Top 10 Spenders', countries1)
worldmap_chart.add('Next 15', countries2)
worldmap_chart.add('Rest of World', countries3)



worldmap_chart.title = 'Military Spending from 2014-2018 by Country'
#worldmap_chart.render_to_file('F:\Pythonprojects\Military Expenditures\military spending map.svg')
#worldmap_chart.render_to_file('E:\Pythonprojects\Military Expenditures\military spending map2.html')


worldmap_chart2 = pygal.maps.world.World()

us={}
nato_countries={}
other_countries={}
for d in data:
    if d[0]=='United States':
        d[0]=get_country_code(d[0])
        us[d[0]]=d[-1]
    elif d[0] in NATO_Members:
        d[0]=get_country_code(d[0])
        nato_countries[d[0]]=d[-1]
    else:
        d[0]=get_country_code(d[0])
        other_countries[d[0]]=d[-1]


#print(countries)
worldmap_chart2.add('United States', us)
worldmap_chart2.add('Other Nato Nations', nato_countries)
worldmap_chart2.add('Rest of World', other_countries)



worldmap_chart2.title = 'Military Spending from 2014-2018 by NATO Membership'
#worldmap_chart2.render_to_file('F:\Pythonprojects\Military Expenditures\military spending nato membership.svg')
#worldmap_chart2.render_to_file('F:\Pythonprojects\Military Expenditures\military spending nato membership2.html')
#worldmap_chart2.render()
