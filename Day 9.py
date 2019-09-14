def greet_users(names):
    '''Print a simple greeting to each user in the list'''
    for name in names:
        msg = "Hello, "+name.title() +"!"
        print(msg)


usernames = ['hannah', 'ty', 'mergot']
greet_users(usernames)


def print_models(unprinted_designs, completed_models):
    '''
    Simulate printing each design until there are none left.
    Move each design to completd models after printing
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #simulate creating a 3d print from the design
        print('Printing model: '+current_design)
        completed_models.append(current_design)

def show_completed_models (completed_models):
    '''show the models that were printed'''
    print("\nThe followig models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(coompleted_models)

#Preventinnd a function from modifying a list, send a copy
#function_name(list_name[:])
#print_models(unprinted_designs[:],completed_models)
