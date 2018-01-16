#Hexagon Perimeter - Challenge 4

class Hexagon:
	def __init__(self, a):
		self.sidelen = a
		print(f"The length of one side of the Hexagon is {a}.")

	def perimeter(self):
		return self.sidelen * 6


hexa = Hexagon(42)
print(hexa.perimeter())
