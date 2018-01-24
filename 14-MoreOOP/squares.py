#Challenge 1 and 2! List of Squares

class Square:
	square_list = []

	def __init__(self, l):
		self.len = l
		self.square_list.append(self.len)

	def __repr__(self):
		return (f"{self.len} by {self.len} by {self.len} by {self.len}")

sq1 = Square(10)
sq2 = Square(20)
sq3 = Square(40)

print(Square.square_list)

print(sq1)
print(sq2)