#Chapter 7 Chapternotes. Loops!

#A loop is a piece of code that continually executes instructions un til a condition is satisfied.

#For-Loops
#A for-loop is a loop used to iterate through an iterable. The process is called iterating. 
#For Loops can be used to define instructions that execute once for every item in an iterable,
#and each item can be accessed and manipulated from within the defined instructions. 

#For-Loops can be defined using the syntax:
#[variable_name] in [iterable_name]: [instructions]
#[variable_name] is a variable name assigned to the value of each item in the iterable. 
#[instructions] is the code to be executed each time through the loop.

#Here is an example using a for-loop to iterate through the characters of a string.

name = "Ted"
for character in name:
	print(character)

>> T
>> e
>> d

#Each time around the loop, the variable "character" gets assigned to an item in the iterable "name".
#The process continues until every itemn in the iterable has been assigned to the variable "character"

#Here is another example, using a for-loop to iterate through the items in a list.

shows = ["GOT", "Narcos", "Vice"]
for show in shows:
	print (show)

>> GOT
>> Narcos
>> Vice

#...and a Tuple. 

coms = ("A. Development", "Friends", "Always Sunny")
for show in coms:
	print (show)

>> A. Development
>> Friends
>> Always Sunny

#... and through keys in a Dictionary.

people = {"G. Bluth II":"A. Development", "Barney":"HIMYM", "Dennis":"Always Sunny"}
for character in people:
	print (character)

>> Dennis
>> Barney
>> G. Bluth II

#For-Loops can be used to change the items in a mutable iterable, like a list.
#In this example the loop iterates through the list "tv". 
#An Index Variable keeps track of the current item in the list. 
#Index Variables hold an integer representing an index in an iterable. 

tv = ["GOT", "Narcos", "Vice"]
i = 0 #The Index Variable i starts at 0
for show in tv:
	new = tv[i] #The Index Variable gets the current item from the list, which is stored in variable new. 
	new = new.upper() #The UPPER method is applied to new
	tv[i] = new #The item in the current index is replaced with contents of new
	i += 1 #Index variable is incremented by 1

print(tv)

>> ["GOT", "NARCOS", "Vice"]

#Accessing items and their index is so common, Python has another syntax for this:

tv = ["GOT", "Narcos", "Vice"]
for i, show in enumerate(tv): #pass tv to enumerate, i tracks the current index
	new = tv[i] #iterate through the result
	new = new.upper()
	tv[i] = new

print(tv)

>> ["GOT", "NARCOS", "Vice"]

#For-loops can be used to move data between mutable iterables. 
#This example uses two for-loops to take strings from two different lists, capitalize
#each character in them, and put them into a new list.

tv = ["GOT", "Narcos", "Vice"]
coms = ("Arrested Development", "friends", "Always Sunny")
all_shows = []

for show in tv: #iterate through all items in the list tv
	show = show.upper() #upper method capitalizes each item in list
	all_shows.append(show) #append items to all_shows list

for show in coms: #iterate through all items in the list coms
	show = show.upper() #upper method capitalizes each item in list
	all_shows.append(show) #append items to all_shows list

print(all_shows)

>> ["GOT", "NARCOS", "VICE", "ARRESTED DEVELOPMENT", "FRIENDS", "ALWAYS SUNNY"]

#Range!
#The range function creates a sequence of integers, which can be iterated with a for loop. 
#The range function takes two parameters: where sequence starts and stops. 
#The sequence returned includes the first parameter, but not the second parameter. 
#This example uses range to create a sequence of numbers and print them.

for i in range(1,11): 
	print(i) 

>> 1
...
>> 9
>> 10

#While-loops!
#While loops execute code as long as an expression evaluates to True. 
#The syntax for a while loop is:
#while[expression]:[code_to_execute]
#[Expression] determines whether or not the loop continues.
#[code_to_execute] represents the code the loop executes as long as it does.

x = 10
while x > 0:
	print('{}'.format(x)) #print value of x
	x -= 1 #decrease x by 1

print("Happy New Year!")

>> 10
>> 9
...
>> 1
>> "Happy New Year!"

#The while loop executes as long as the expression defined in the header evaluates to true.
#A loop that never ends is called an infinite loop. 

while True: #a loop that evaluates to True will run forever
	print("Hello World!")

#Break!
#Break-statements - a statement with the keyword break - can be used to terminate a loop.

for i in range(0,100):
	print(i)
	break #adding this statement makes the loop only run once.

>> 0

#As soon as python hits the break-statement, the loop ends. 
#For example, a while-loop and the break keyword can be used to keep asking for input
#until the user types q to quit. 

qs = ["What is your name?", "What is your favorite color?", "What is your quest?"]
n = 0 #n is an index variable
while True: #Each time through the loop, the program will ask a question. 
	print("Type q to quit")
	a = input(qs[n])
	if a == "q":
		break
	n = (n + 1) % 3 #if the first number in an expression using modulo is smaller, the result is the first number.

>> "Type q to quit"
>> "What is your name?"

#Continue!
#The continue-statement can stop a current iteration of a loop and move on to the next iteration. 
#In this example, say you want to print all numbers between 1-5 except 3.

for i in range(1,6):
	if i == 3:
		continue #Allows the loop to continue instead of ending like the break statement would.
	print(i)

>> 1
>> 2
>> 4
>> 5

#The same result can be achieved using a while-loop and a continue statement.

i = 1
while i <= 5:
	if i == 3:
		i += 1
		continue
	print(i)
	i += 1

>> 1
>> 2
>> 4
>> 5

#Nested Loops!
#There is no limit to the number of loops possible inside other loops. 
#When a loop is inside another loop, the second loop is the outer Loop. 
#The nested loop is the inner loop.
#When using a nested loop, the inner iterates once for each time around the outer.

for i in range(1,3):
	print(i)
	for letter in ["a", "b", "c"]: #this loop will iterate however many times the outer loop runs
		print(letter)

>> 1
>> a
>> b
>> c
>> 2
>> a
...

#Two for-loops can be used to add each number in a list to all the numbers in another list. 

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1: #this loop iterates through every integer in list1
	for j in list2: #this loop iterates through every integer in list2,
		added.append(i+j) #adds it to the integer from list1, and appends it to the added list

print(added)

>> [6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11, 9, 10, 11, 12]

#for-loops can be nested inside while-loops, and vice-versa.

while input('y or n') != 'n': #this program prints the numbers 1-5 until the user enters n
	for i in range(1,6):
		print(i)

>> y or n?y
>> 1
>> 2
>> 3
>> 4
>> 5
>> y or n?n
>>
