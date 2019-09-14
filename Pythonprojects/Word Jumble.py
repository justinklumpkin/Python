#1) create word Jumble
#2) 10 similar lemgth words (and topic)
 #to be stored in a list
#3) Randomly select a word and scramble it
#4) Try to figure out word
#5) you have 5 guesses to figure it out
#-----------------------------------
#create a dictionary to store a hint about the word

import random
word_bank = {
    'fruit':['apple','banana', 'blueberry','strawberry','tomato','grape', 'pineapple', 'plantain','orange','tangerine'],
    'cars': ['toyota','honda','hyundai','chevrolet','ford','nissan','dodge','mazda', 'jeep','volkswagen']
}

car_hints ={'toyota':'prius','honda':'civic','hyundai':'elantra','chevrolet':'bolt','ford':'F150','nissan':'rogue','dodge':'charger','jeep':'cherokee', 'mazda':'mx-3','volkswagen':'beetle'}
answer = word_bank['cars'][random.randint(0,10)]
#print(answer)
answer_copy = answer
length = len(answer_copy)

rand = random.randint(0,10)
scrambled_answer = ""
while len(answer_copy)!=0:
    rand = random.randint(0, length)
    scrambled_answer=scrambled_answer+answer_copy[rand:rand+1]
    if rand == 0:
        answer_copy=answer_copy[1:]
    elif rand== len(answer_copy)-1:
        answer_copy=answer_copy[:len(answer_copy)-1]
    else:
        answer_copy = answer_copy[:rand]+answer_copy[rand+1:]
    
#print(scrambled_answer+" "+answer_copy+".")
        
#Guessing game
print("The category is " + "CARS.\nScrambled word: "+scrambled_answer+"\nType 'QUIT' to end or 'HINT' for a hint at any time.")
guesses = 5
while guesses > 0:
    guess = input("\nYou have "+str(guesses)+" guess(es) remaining.\nScrambled word: "+scrambled_answer+"\nGuess: ")
    if guess=='QUIT':
        print("program ended.\n")
        guesses = 0
    elif guess=='HINT':
        print("\n\n\tHint: "+car_hints[answer].title())
        if guesses==1:
            print("You are out of guesses, the answer is "+answer+".")
    elif guess ==answer:
        print("Correct! The answer is '" + guess.title()+"'.\nyou had "+str(guesses-1)+" guess(es) remaining.")
        guesses = 0
    elif guesses == 1:
        print("Sorry, '" + guess +"' is incorrect and you are out of guesses.\nThe answer was '"+answer+"'")
    else:
        print("Sorry, '" + guess +"' is incorrect.\nYou have "+str(guesses)+" guess(es) remaining.")
    guesses= guesses-1
