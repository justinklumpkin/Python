'''#String concatenation and type casting

first_name = "IB"
last_name = "Computer Science"
full_name = first_name+ " "+last_name


message = "Hello, " + full_name.title() +"!"
    #.title() gives title case

#say hello to everyone

print (message)

age = 23 #defaults to casting as an integer
message = "Happy " +str(age) + "rd Birthday!" #cast age as string
print (message)
'''

#Lists
#functions - printing lists, sorting, reversing, indexing, title, removing

cars= ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))#doesn't actually edit the list, would need cars = sorted(cars)


print("\nHere is the sorted reverse alphabetical list:")
print(sorted(cars, reverse=True))


#cars = sorted(cars)

print("\nHere is the original list:")
print(cars)


bicycles = ['track','cannondale','redline','specialized']
message = "My first bicycle was a " + bicycles[0].title()+"."

print (message)

motorcycles = ['honda', 'yamaha', 'suzuki','ducati','ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)#.remove() only removes 1st occurance
#motorcycles.insert('toyota')
print (motorcycles)
print ("\nA " + too_expensive.title() +" is too expensive for me.")
#motorcycles.remove('justin')#throws x not in list error


