#Horses and Riders - Challenge 4

class Horse:
	def __init__(self, name, rider):
		self.name = name
		self.rider = rider


class Rider:
	def __init__(self, rider):
		self.rider = rider

r1 = Rider("El Cid")

h1 = Horse("Bavieca", r1)

print(f"The horse is called {h1.name}.")
print(f"Its rider is {h1.rider.rider}.")