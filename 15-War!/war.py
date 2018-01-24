#Let's build the card game WAR!

from random import shuffle

#Let's create a class to model the playing cards
class Card:
	suits = ["Spades", "Hearts", "Diamonds", "Clubs"] #class variable for possible suits

	values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
			 "Queen", "King", "Ace"] #class variable for possible card values

	def __init__(self, v, s): #card objects have two instance variables, 
		self.value = v #each represented by an integer
		self.suit = s  #that together represent what kind of card it is


	#The definitions in the magic methods __lt__ and __gt__ allow you to compare
	#two Card objects in an expression using > and <

	#The code in these methods determines if the card is greater than or less than
	#the other card passed in as a parameter.

	def __lt__(self, c2):
		if self.value < c2.value:
			return True

		if self.value == c2.value: #The code also handles if the cards have the same value
			return True

		else:
			return False

		return False

	def __gt__(self, c2):
		if self.value > c2.value:
			return True

		if self.value == c2.value: #and will use the suit to break the tie
			if self.suit > c2.suit:
				return True
			else:
				return False

		return False

	def __repr__(self):
		v = self.values[self.value] + " of " + self.suits[self.suit]

		return v

class Deck: #class to represent a deck of cards
	def __init__(self):
		self.cards = [] #list of cards!
		for i in range (2,15): #index for card values
			for j in range(4): #index for card suits
				self.cards.append(Card(i, j)) #append the generated cards to the list
		shuffle(self.cards) #randomly arrange the items in the cards list

	def rm_card(self): #this method removes and returns a card from the list
		if len(self.cards) == 0:
			return #return None if the list of cards is empty
		return self.cards.pop()

class Player: #class to represent player, keep tracks of their cards, and track wins
	def __init__(self, name):
		self.wins = 0 #track how many rounds have been won
		self.card = None #card the player is currently holding
		self.name = name #player's name


class Game: #Now a class to represent the game
	def __init__(self):
		name1 = input("Enter a name for Player 1: ") #collect player 1 name
		name2 = input("Enter a name for Player 2: ") #collect player 2 name
		self.deck = Deck() #create a new deck object, store in instance variable 
		self.p1 = Player(name1) #create two player obects
		self.p2 = Player(name2)

	def wins(self, winner):
		w = f"{winner} wins this round!"
		print(w)

	def draw(self, p1n, p1c, p2n, p2c):
		d = f"{p1n} drew {p1c}; {p2n} drew {p2c}"
		print(d)

	def play_game(self): #this method starts the game
		cards = self.deck.cards
		print("The War begins!")
		while len(cards) >= 2: #keep the game going as long as there are two or more cards
			m = "Type q to quit. Press Enter key to draw: "
			response = input(m)
			if response == "q":
				break
			p1c = self.deck.rm_card()
			p2c = self.deck.rm_card()
			p1n = self.p1.name
			p2n = self.p2.name
			self.draw(p1n, p1c, p2n, p2c)
			if p1c > p2c:
				self.p1.wins += 1
				self.wins(self.p1.name)
			else:
				self.p2.wins += 1
				self.wins(self.p2.name)

		win = self.winner(self.p1, self.p2)
		print(f"War is over. {win} wins!")

	def winner(self, p1, p2):
		if p1.wins > p2.wins:
			return p1.name
		if p1.wins < p2.wins:
			return p2.name
		return "It was a tie!"

game = Game()
game.play_game()


