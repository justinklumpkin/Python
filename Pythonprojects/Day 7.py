def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " +username.title()+ "!")

greet_user('jesse')



def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a(n) " +animal_type +".")
    print("My "+animal_type +"'s name is " +pet_name.title()+".")

#a dog named scrappy
describe_pet('scrappy')
describe_pet(pet_name='scrapy')

#hamster named furball
describe_pet('furball', 'hamster')
describe_pet(pet_name='furball', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='furball')
