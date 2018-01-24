#True or False - Challenge 2

class Object:
	pass

object1 = Object()

object2 = object1

if object1 is object2:
	print("They're the same!")

else:
	print("Nope, different!")

object1 = Object()

object2 = Object()

if object1 is object2:
	print("They're the same!")

else:
	print("Nope, different!")