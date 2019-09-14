def make_pizza(size, *toppings):#notice the *, makes empty tuple
    '''Summarize the pizza '''
    print("\nMaking a "+str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers', 'cheese')           


def build_profile(first, last, **user_info): #empty dictionary
    '''Build a dictionary containing everything about user'''
    profile ={}
    profile['first_name']=first
    profile['last_name']=last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                             field='physics')
print(user_profile)
