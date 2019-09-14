#more with lists and loops
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician.title() + ", that was a great trick!")
    print ("I can't wait to see your next trick, " + magician.title()+".\n")

print("Thank you everyone, that was a great magic show!")

#for loop ends when the indent is over


#make numerical lists

numbers = list(range(1,6))#starting value 1st, and 1st value not to include is second parameter
print (numbers)

even_numbers = list(range(2,11,2))#3rd parameter is count by
print (even_numbers)

squares =[] #this is a list

for value in range(1, 11):
    square = value**2
    squares.append(square)

print (squares)


print (min(squares))
print (max(squares))
print (sum(squares))
