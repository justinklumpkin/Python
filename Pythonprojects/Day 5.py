#Dictionaries
#Key-values, not sequential

alien_0 = {'xpos':0, 'ypos': 25, 'speed': 'med'}
print("Original position: "+str(alien_0['xpos']))


#move alien to right
#figure out how far based on speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'med':
    x_increment = 2
else:
    #this one is fast
    x_increment = 3

# the new pos is the old pos plus increment
alien_0['xpos'] = alien_0['xpos']+x_increment

print("New position: " +str(alien_0['xpos']))

alien_1 = {'color':'green', 'points':5}
del alien_1['points']
print (alien_1)

favorite_languages = {
    'Aditi':'python',
    'Becky':'c++',
    'Davis':'German Something',
    'Samraj':'python',
    'Esther':'Canon D'
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+language.title() +"")

#make an empty list for storing aliens
aliens=[]

#Make 30 green aliens
for alien_number in range(0, 30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color']= 'yellow'
        alien['speed'] = 'med'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:
    print(alien)
print("...")


#store information about a pizza being ordered.
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
    }

#summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza "+ "with these toppings:")

for topping in pizza['toppings']:
    print("\t" +topping)
    
