#TwoFunctions - Challenge 4

def divider(x):
	print("Dividing"),(x),("by two.")
	return x/2

def multiplier(y):
	print("Multiplying"),(y),("times four.")
	return y * 4


x = input("Enter X: ")

y = divider(x)

z = multiplier(y)

print("End result is"),(z),(".")