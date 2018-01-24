#Chapter 13 - Pillars of OOP - ChapterNotes

#Four main steps in OOP that form the Four Pillars of OOP
#These are encapsulation, abstraction, polymorphism, and inheritance
#All four must be present in a programming language to be considered
#an Object-Oriented programming language.


#Encapsulation!
#Refers to two concepts:
#The first is that objects group variables (state) and methods 
#in a single unit - the object. Consider this:

class Rectangle:
	def __init__(self, w, l):
		self.width = w
		self.length = l

	def area(self):
		return self.width * self.length

#In this case, the instance variables len and width hold the object's state.
#The state is grouped in the same unit (object) as the method area.
#The method uses the object's state to return the rectangle's area.

#The second concept, encapsulation, refers to hiding a class's internal data
#This prevents the client, the code outside a class, from directly accessing it.

#Consider this:
#The class data has an instance variable called nums that contains a list.

class Data:
	def __init__(self):
		self.nums = [1, 2, 3, 4, 5]

	def change_data(self, index, n):
		self.nums[index] = n

#Once a Data object is created, the items in nums can be changed in two ways:

data_one = Data()
data_one.nums[0] = 100 #Directly accessing the nums instance variable

data_two = Data()
data_two.change_data(0, 100) #By using the change_data method 

#But what happens if we choose to make nums a tuple instead of a list?
#Many programming languages solve this problem by allowing the definition of
#private variables and private methods: variables and methods that objects can 
#access in the code that implements the methods, but the client cannot.

#Private variables and methods are useful when there's a method or variable
#the class uses internally, but you plan to change the implementation of code
#later, and thus don't want whoever uses the class to rely on them.

#Private variables are an example of encapsulation: they hide a class's
#internal data to prevent the client from directly accessing it.

#Python does not have private variables. All of Python's variables are public.
#Instead, Python uses naming conventions. If there's a variable or method the 
#caller should not access, precede its name with an underscore.

class PublicPrivateExample:
	def __init__(self):
		self.public = "safe"
		self._unsafe = "unsafe"

	def public_method(self): #clients can use this
		pass

	def private_method(self): #clients shouldn't use this
		pass


#When reading this code, know self.public is safe to use, but self._unsafe
#shouldn't be used because it starts with an underscore. Same with methods.


#Abstraction!
#This is the process of "taking away or removing characteristics from something
#in order to reduce it to a set of essential characteristics"

#Abstraction is used in OOP when modeling objects using classes and omit details.
#For example.. say you are modeling a person.

#A person is complex. They have hair color, weight, ethnicity, gender, and more.
#If creating a class to represent a person, some details may not be relevant.
#An example of abstraction is creating a Person class, but omitting attributes.

#The Person objects your class creates are abstractions of people. Representations
#stripped fown to only the characteristics necessary to solve the problem.


#Polymorphism!
#This is presenting the same interface for different underlying forms (data types)
#An example of this is the Print function. Same interface, different data types.

print("Hello World!") #string
print(100) #integer
print(100.1) #float

#We used the print function (one interface) to print them all.

#Imagine we want a program that can draw a triangle, square, or circle

shapes = [tr1, sq1, cr1]

#Drawing without polymorphism:
for a_shape in shapes: 

	if type(a_shape) == "Triangle":
		a_shape.draw_triangle()
	if type(a_shape) == "Square":
		a_shape.draw_square()
	if type(a_shape) == "Circle":
		a_shape.draw_circle()

#Drawing with polymorphism
for a_shape in shapes:
	a_shape.draw()

#To add to the shapes list without polymorphism, we would have to modify the code
#in the for-loop to test a_shape type before calling its draw method.

#With polymorphism, as many shapes can be added to the list as we want,
#and it will be able to draw itself without any additional code.



#Inheritance!
#Inheritance in programming is similar to genetic inheritance.
#Like inherit traits from our parents, classes can inherit from classes.
#The class inherited from is the parent class, and the inheritor a child class.
#In this example, let's model shapes using inheritance.


#This is the parent class, it create Shape objects with width and len
class Shape(): 
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def print_size(self):
		print(f"{self.width} by {self.len}")

#Let's define a child class by passing the name of the parent as a parameter.

class Square(Shape):
	pass

#Because we pass the Shape class to Square as a parameter, Square inherits 
#Shape's variables and methods.

#Because of inheritance, after we create a square with a width and length,
#we can call print_size on it without any additional code. It can also have its
#own variables and methods without affecting the parent class.

class Shape(): 
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def print_size(self):
		print(f"{self.width} by {self.len}")

class Square(Shape):
	def area(self):
		return self.width * self.len


#Inherited methods from parent classes can be overridden by defining a method 
#with the same name in the child class. This is called method overriding.

class Shape(): 
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def print_size(self):
		print(f"{self.width} by {self.len}")

class Square(Shape):
	def area(self):
		return self.width * self.len

	def print_size(self):
		print(f"I am {self.width} by {self.len}.")


#Composition!
#Another important concept. It models the "has a" relationship by storing
#an object as a variable in another object. For example, 

#Using composition to model the relationship between a dog and its owner.

class Dog():
	def __init__(self, name, breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person():
	def __init__(self, name):
		self.name = name

#When we create a Dog object, pass in Person as the Owner parameter.

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)

print(stan.owner.name)
>> Mick Jagger

#Now the stan object "Stanley" has an owner - a person object.
#Mick Jagger is stored in the owner instance variable.















