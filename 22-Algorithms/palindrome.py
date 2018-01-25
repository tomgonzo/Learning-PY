#Palindrome checker!

def palindrome(word):
	word = word.lower()
	return word[::-1] == word #word[::-1] reverses the word

while True:
	word = input("Enter a word: ")
	print(palindrome(word))