#Challenge 2 - Circle?
#Circle class with area method

import math

class Circle:
	def __init__(self, r):
		self.radius = r
		print(f"Circle with Radius {r} created.")

	def area(self):
		return self.radius ** 2 * math.pi

c1 = Circle(10)
print(c1.area())	