#Triangle Area Calculator - Challenge 3

class Triangle:
	def __init__(self, l1, l2, l3):
		self.line1 = l1
		self.line2 = l2
		self.line3 = l3
		print(f"The length of the lines are {l1}, {l2}, and {l3}.")

	def area(self):
		return self.line1 * self.line2 * self.line3


tri = Triangle(42, 42, 42)
print(tri.area())

