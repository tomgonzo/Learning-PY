#Challenges 1 - 3 - Rectangle and Square classes with Perimeter Calculation

class Shape():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def what_am_i(self):
		if self.width == self.len:
			shape = "square"
		if self.width != self.len:
			shape = "rectangle"
		print(f"I am a {shape} with width {self.width} and length {self.len}.")


class Square(Shape):
	def calculate_perimeter(self):
		peri = (self.width * 2) + (self.len * 2)
		print(f"My perimeter is {peri}. ")

	def area(self):
		area = self.width * self.len
		print(f"My area is {area}. ")

	def change_size(self, n):
		self.width = self.width + n
		self.len = self.len + n
		print(f"Size change! All sides modified by {n}.")

class Rectangle(Shape):
	def calculate_perimeter(self):
		peri = (self.width * 2) + (self.len * 2)
		print(f"My perimeter is {peri}. ")

	def area(self):
		area = self.width * self.len
		print(f"My area is {area}. ")

	def change_size(self, n):
		self.width = self.width + n
		self.len = self.len + n
		print(f"Size change! All sides modified by {n}.")


w = int(input("What is the length of one side? "))
l = int(input("What's the length of an adjacent side? "))

if w == l:
	sq = Square(w, l)
	print(sq.what_am_i())
	print(sq.area())
	print(sq.calculate_perimeter())
	sq.change_size(1)
	print(sq.area())
	print(sq.calculate_perimeter())

if w != l:
	rec = Rectangle(w, l)
	print(rec.what_am_i())
	print(rec.area())
	print(rec.calculate_perimeter())


