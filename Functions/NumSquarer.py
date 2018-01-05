#NumSquarer - Challenge 1

def squarer(numbah, powah):
	"""
	Returns Numbah raised to the Powah
	:param numbah: float.
	:param powah: float.
	:return: float result of numbah ** powah.
	"""
	return numbah ** powah

numbah = input("Give me a number:")
powah = input("Raise to the power of:")

result = squarer(numbah, powah)
print(result)
