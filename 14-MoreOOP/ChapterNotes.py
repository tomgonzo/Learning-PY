#Chapter 14 ChapterNotes

print("Treat your code like poetry and take it to the edge of the bare minimum.")

#In Python, classes are objects that are an instance of class "type"

class Square:
	pass

print(Square)

#In this example the class Square is an object and it prints the location in memory

#Classes have two types of variables: class variables and instance variables
#Instance variables belong to objects.

class Rectangle():
	def __init__(self, l, w):
		self.width = w #this is an instance variable
		self.length = l #this too

	def print_size(self):
		print(f"{self.width} by {self.length}")

#Class variables belong to the onject Python creates for each class definition
#and the objects they create. Class variables are defined like regular variables,
#except inside of a class.

#Class variables can be accesed with class objects, and objects creates with a class.

#They are accessed the same way as instance variables, preceded by self.
#The primary use is sharing data between all instances of a class without global variables.


class Rectangle():
	recs = [] #this is a class variable
	#This is defined outside the __init__ method because it's only called on object creation
	#This allows sharing data between the objects created by a class, without global variable

	def __init__(self, w, l):
		self.width = w
		self.length = l
		self.recs.append((self.width, self.len)) #append new tuple to the recs list

	def print_size(self):
		print(f"{self.width} by {self.length}")

r1 = Rectangle(10,24)
r2 = Rectangle(20,40)
r3 = Rectangle(100,200)

print(Rectangle.recs)


#Magic Methods!
#Every class in Python inherits from a parent class called Object.
#Python utilizes methods inherited from Object in different situations.

class Lion:
	def __init__(self, name):
		self.name = name

lion = Lion("Dilbert")
print(lion) #When you print a Lion object...
#This calls a magic method called __repr__, inherited from Object, and prints
#whatever it returns. In this case: 

>> <__main__.Lion object at 0x0298409823 #Object's location in memory.

#The __repr__ magic method can be overridden to print something else.

class Lion:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

lion = Lion("Dilbert")
print(lion) 

>> "Dilbert"

#Operands in an expression must have a magic method the operator uses
#to evaluate the expression. For example, 

#In the expression 2 + 2, each integer object has a magic method
#called __add__ that Python calls to evaluate the expression. 

#If you define an __add__ method in a class, you can use the objects it
#creates as operands in an expression with the addition operator.

class AlwaysPositive:
	def __init__(self, number):
		self.n = number

	def __add__(self, other):
		return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

>> 10

#Is!
#The keyword...
#The keyword is returns True if two objects are the same object, and False if not.

class Person:
	def __init__(self):
		self.name = "Bob"

bob = Person()
same_bob = bob #both of these variables point to the same Person object.
print(bob is same_bob) >> True

another_bob = Person() #this is another Person object
print(bob is another_bob) >> False


#Is can be used to check if a variable is None:

x = 10

if x is None:
	print("x is none :(")
else:
	print("x is not None") >>

x = None
if x is None:
	print("x is none :(") >>
else:
	print("x is not None")





