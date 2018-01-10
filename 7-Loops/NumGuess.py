#InfiniteLoop for user to guess number - Challenge 4

num = [2, 4, 6, 8, 10] #number pool that wins

while True: #infinite loop
	answer = raw_input("Guess a number or type q to quit: ")

	if answer == "q": #exit point of infinite loop
		break

	try:
		answer = int(answer) #just in case a letter other than q gets added

	except ValueError: #re-prompt for input
		print("Guess a number or type q to quit: ")

	if answer in num:
		print("Great guess!")
		
	else:
		print("Nope. Try again!")