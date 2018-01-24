#Programming Paradigms - Chapter 12 Notes

#A programming paradigm is a style of programming. 
#To program professionally, you learn Object-Oriented or Functional paradigms.
#We will learn about procedural, functional, and object oriented programming.

#State!
#One of the fundamental differences between paradigms is handling of state. 
#State is the value of a program's variables while it is running.
#Global State is the value of a program's global variables as it runs.

#Procedural Programming - 
#Programming style in which you write a sequence of steps moving to a solution.
#Each step changes the program's state. "If this, then that"

x = 2
y = 4
z = 8

xyz = x + y + z
>>14

#When programming procedurally, data is stored in global variables
#and manipulated with functions.

rock = []
country = []

def collect_songs():
	song = "Enter a song: "
	ask = "Type r or c. q to quit: "

	while True:
		genre = input(ask)
		if genre = "q":
			break

		if genre = "r":
			rk = input(song)
			rock.append(rk)

		elif genre == ("c"):
			cy = input(song)
			country.append(cy)

		else:
			print("Invalid")

	print(rock)
	print(country)

collect_songs()

#Procedural Programming is fine for small programs like this, however, because
#variables are stored globally, we run into problems when it grows.



#Functional Programming!
#Originating from the lambda calculus: the smallest universal programming language
#Addresses the problems that arise in procedural programming by eliminating global state.

#A functional programmer relies on functions that do not use or change global state.
#The only state they use are the parameters passed to the function.

#The result a function returns is usually passed to another function. 
#Functional programmers avoid global state by passing from function to function.

#Functional code is characterized by the absence of side effects.

#Function with side effects:

a = 0
def increment():
	global a #side effects because it relies on data outside of itself
	a += 1 #and because it changes data outside of the function

#Function with no side effects:

def increment(a):
	return a + 1

#A disadvantage of functional programming is certain problems are easier to
#conceptualize with state. 


#Object-Oriented Programming!
#Also eliminates global state, but instead of storing state in functions
#it stores state in objects.

#In OOP, classes define a set of objects that can interact with each other. 
#Classes are a mechanism for programmers to classify and group similar objects.

#Think of a bag of oranges. 
#Each Orange is an object. 
#All oranges have the same attributes, such as color and weight.
#Use a class to model oranges and create Orange objects with different values. 

#Every object is an instance of a class. Define a class called Orange, and create
#two new Orange objects, each one is an instance of the class Orange; their data 
#type is Orange. Object = Instance.

#A class is a compound statement with a header and suites. To define a class:

class[name]:[suites]

#[name] is the name of the class
#[suites] are the suites defined
#By convention, classes start with capital letter and follow CamelCase.


#A suite in a class can be a simple statement or a compound statement
#called a method. Methods are like functions, but defined inside of a class
#and can only call them on the object the class creates.

#Method names should be all lowercase with words separated by underscores.
#You define methods with the same syntax as functions, with two differences:
# - you must define a method as a suite in a class,
# - it has to accept at least one parameter (except in special cases)

#By convention, always name the first parameter of a method self.

class Orange:
	def __init__(self): 
		print("Created!")

#Self can define an instance variable - a variable belonging to an object.
#Instance variables are normally defined inside of a special method __init__
#Define with the syntax: self.[variable_name] = [variable_value]

class Orange:
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		print("Created!")

#The code in __init__ executes when you create an Orange object.
#This creates two instance variables, weight and color. Then prints "Created!"
#These variables can be used like regular variables in any method in the class.

#Methods surrounded by double underscores, like __init__, are called magic methods.

#You can create a new object with the same syntax you use to call a function
classname(parameters)

#Creating a new object is called instantiating a class.

or1 = Orange(10, "dark orange")

#Once an object is created, get the value of instance variables with syntax:

print(or1.weight)
print(or1.color)

#Change the value of an instance variable with syntax:

or1.weight = 100
or1.color = "light orange"

#Classes can be used to create multiple objects:

or2 = Orange(8, "dark orange")
or3 = Orange(12, "light orange")

#Other functions can be defined inside classes, such as oranges rotting.

class Orange():
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		self.mold = 0 #new instance variable in object to track rot
		print("Created!")

	def rot(self, days, temp):
		self.mold = days * temp

orange = Orange(6, "orange")
orange.rot(10,98) #rot accepts two parameters, days since picked, and average temp

#You can define multiple methods in a class. An example using rectangles:

class Rectangle():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def area(self): #method to return the area of the rectangle
		return self.width * self.len

	def change_size(self, w, l): #method to change the size of the rectangle
		self.width = w
		self.len = l
