#Three Requireds and Two Optionals - Challenge 3

def bridge(a, b, c, d=10, e=50):
	"""
	Performs a clusterfuck of operations.
	:param a: float.
	:param a: float.
	:param a: float.
	:param a: optional float.
	:param a: optional float.
	:this could return anything based on input.
	"""
	return a ** b % c + d * e

result = bridge(40, 29, 60, 23)
print(result)
