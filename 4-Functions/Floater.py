#String-to-Float with EH - Challenge 5

try:
	entry = input("Number Please:")
	entry = float(entry)
	print (entry)

except NameError:
	print("I said number...")
