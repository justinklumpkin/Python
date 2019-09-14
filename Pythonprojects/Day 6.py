#while loop and input


prompt = "If you submit your name, we can personalize the messages"
prompt+= "\nWhat is your name? "

name = input(prompt)

print("\nHello, " +name+ "!")


prompt = "\nTell me something, and I will repeat it back to you: "
prompt+= "enter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False

    else:
        print(message)

height = input("How tall are you, in inches? ")#normal input is a string
height = int(height)
height = int(input("How tall are you, in inches? "))

if height >=36:
    print("nYou're tall enough to ride")
else:
    print("\nYou'll be able to ride when you're older")


number = input ("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number%2 == 0:
    print(str(number)+" is even.")
else:
    print(str(number)+" is odd.")


#start with users that need to be verified
    #and an empty list for confirmed users
unconfirmed = ['alice', 'brian','candace']
confirmed = []

#verify each user until there are no more unconfirmed
#move them from unconfirmed to confirmsed

while unconfirmed:#loops untol length ==0
    current = unconfirmed.pop()#removes last element
    print("Verifying user: " +current.title())
    confirmed.append(current)

#display confirmed users
print("Confirmed users:")
for user in confirmed:
    print(user.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


responses = {}
# set a flag to indicate that poling is active
polling_active = True

while polling_active:
    #prompt for name and response
    name = input("\nWhat's your name?")
    response = input("Which mountain do you want to climb?")

    #store
    responses[name] = response

    #find out in anyone else is voting
    repeat = input ("would you like to add a response(yes/no)")
    if repeat == 'no':
        polling_active = False

#polling is complete, display

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name+ " wants to climb "+response+".")
                
