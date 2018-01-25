#fizzbuzz

def fizz_buzz():
	for i in range(1,101): #start by iterating through 1-100
		if i % 3 == 0 and i % 5 == 0: #check if a number is divisible by 3 and 5
			print("FizzBuzz")

		elif i % 3 == 0: #check if a number is divisible by 3
			print("Fizz")

		elif i % 5 == 0: #check if a number is divisible by 5
			print("Buzz")

		else: #if not divisible by either, print the number
			print(i)

fizz_buzz()