#slicing

players = ['Yuvalm', 'Keyhan', 'Holden','Tarini','Revanth']

#play around with upper and lower bounds
print(players[0:3])#includes index 0, 1 and 2
print(players[3:])#includes index 3 to end
print(players[:4])#includes up to 4 exclusive
print(players[-3:])#includes last 3 indexes
print(players[-2:5])#['Tarini', 'Revanth']

print(players[-10:-1])

#worry about length with -indexes

print("Here are the first threee players on my team:")
for player in players[:3]:
    print(player.title())

for player in players[-3:]:
    print(player.title())

my_foods = ['pizza', 'falafel','carrot cake']
friend_foods = my_foods[:] #copies list into new list
                        #this is a clone
#friend_foods = my_foods --> this is an alias

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


#Tuples
dimensions = (200,50)
print ("Original dimensions:")
print("Look here -->", dimensions)
for dimension in dimensions:
    print (dimension)
print (dimensions[0])

#dimensions[0] =5 #can't reassign only one value. must reassign the whole tuple
print(dimensions)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print (dimension)

