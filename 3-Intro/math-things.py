#Challenges! Division!

#Create the Output Function, which returns the result.
def output(num, den, q, r):
	output = "The quotient of {} and {} is {} with a remainder of {}.".format(num, den, q, r)
	print(output)

#Define two variables and two indexes
numerator = 1
denominator = 1
i = 1
j = 1

#First, collect the numerator
while i == 1:
	try:
		num = input("What's the numerator? Type quit to exit.")
		if num == "quit":
			break
		numerator = float(num)
		i += 1
	except ValueError:
		print("The numerator must be a number. Try again or type quit to exit.")

#Then collect the denominator

while (num != "quit") and (j == 1):
	try:
		den = input("What's the denominator? Type quit to exit.")
		if den == "quit":
			break
		denominator = float(den)
		j += 1
	except ValueError:
		print("The denominator must be a number. Try again or type quit to exit.")


#Define two new variables. 
if (num != "quit") and (den != "quit"):
	q = int(num) / int(den)
	r = int(num) % int(den)
	output(num, den, q, r) #Call the output function, pass all variables

