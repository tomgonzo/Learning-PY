#Hangman game!

import random

wordlist = ["wakeful", "determined", "cup", \
			"camp", "harass", "maddening", "buzz", \
			"eminent", "hydrant", "bubble", 
			"complex", "coach"]

picker = random.randint(0,(len(wordlist) - 1))
chosen = wordlist[picker]



#The hangman function stores the game.
def hangman(word):  #It accepts word as a parameter.
	wrong = 0 #The variable wrong tracks the number of wrong guesses
	lwrong = []
	stages = ["", #This will draw the hangman
				"\n________        ",
				"\n|       |       ",
				"\n|       0       ",
				"\n|      /", "|", "\      ",
				"\n|      / ", "\      ",
				"\n|__________     ",
				""
				]

	rletters = list(word) #Tracks letters left to guess.
	board = ["__"] * len(word) #progress display
	win = False #tracks wether the game has been won
	print("Welcome to Hangman!")

	while wrong < len(stages) - 3: #the game continues as long as there are stages left
		print("\n") #blank space so game looks nice in shell
		msg = "Guess a letter: "
		char = input(msg) #collect the guess, store in variable char
		if char in rletters: #if the guess is in rletters, we need to update the board
			while char in rletters:
				cind = rletters.index(char) #get the index of the letter guessed
				board[cind] = char #replace the blank in board with the correct letter
				rletters[cind] = '$' #change the correct guess in rletters to a dollar sign
		else:
			wrong += 1 #if the guess is wrong, increment wrong by 1
			lwrong.append(char)

		print((" ".join(board))) #print the scoreboard
		print(("Wrong Guesses: ", " ".join(lwrong)))
		e = wrong + 1
		print("".join(stages[:e])) #print the hangman
		if "__" not in board: #check if the game has been won
			print(f"\nYou win! It was {word}.")
			print(f"{wrong} mistakes were made.\n")
			win = True
			break
	if not win:
		print("".join(stages[:10]))
		print(f"\nYou lose! It was {word}.")
		print(f"{wrong} mistakes were made.\n")

hangman(chosen)

