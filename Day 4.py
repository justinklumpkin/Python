#conditionals
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car.upper())
    else:
        print(car.title())

#how to check for 'Audi' instead of 'audi'


available_toppings = ['mushrooms', 'olived', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:#looks for req in avail
                                    #this checks if it's in [0]OR[1]OR[2]...
        print("Adding "+ requested_topping +".")#update
    else:
        print("Sorry, we don't have "+requested_topping+".")

print("\nFinished making your pizza!")




answer = 17
if answer != 42:
    print ("That is not the correct answer. Please try again.")

banned_users = ['Garv', 'Shaan', 'Ben']
user = 'marie'

if user.title() not in banned_users:#the banned_user list is in title case
    print(user.title() + ", you can post a response if you wish.")



age = 12
if age<4:
    price = 0
elif age<18 or age>=65:
    price = 5
else:
    price = 10

print ("Your admission cost is $" + str(price) + ".")#concatenates all of them as strings
print ("Other way", price,"better?")# 5 is still outputted as number


#empty list?

my_list =[]
#if empty print 'empty
#else prin 'not empty'

##
##if my_list == []:
##    print('empty')
##else:
##    print('not empty')
if my_list == None:
    print(1)
else:
    print(2)


if not my_list:
    print('empty')
else:
    print('not empty')
