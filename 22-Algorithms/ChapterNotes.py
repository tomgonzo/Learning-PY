#Chapter 22 - Algorithms - ChapterNotes.py

#An algorithm is a series of steps that solve a problem.

#Fizzbuzz!!!
#Fizzbuzz is a popular interview question designed to eliminate candidates.

#Write a program that prints the numbers 1-100
#For multiples of 3 print "Fizz" instead of the number
#For multiples of 5 print "Buzz" instead of the number
#For multiples of both 3 and 5 print "FizzBuzz"

def fizz_buzz():
	for i in range(1,101):
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")

		elif i % 3 == 0:
			print("Fizz")

		elif i % 5 == 0:
			print("Buzz")

		else:
			print(i)



### Sequential Search! ###

#A search algorithm finds information ina. data structure like a list.
#A sequential search is a simple search algorithm that checks each item
#in a data structure to see if the item matches what it's looking for.

#Example of Sequential Search:

def ss(number_list, n):
	found = False
	for i in number_list:
		if i == n:
			found = True
			break
	return found

numbers = range(0,100)

s1 == ss(numbers, 2)
print(s1)
s2 == ss(numbers, 202)
print(s2)

### Palindrome ###

#This algorithm checks if a word is a palindrome

def palindrome(word):
	word = word.lower()
	return word[::-1] == word

while True:
	word = input("Enter a word: ")
	print(palindrome(word))


### Anagrams! ###

#Anagrams are recreated by rearranging the letters of another word.
#Determine if two words are anagrams by rearranging the letters of both
#in alphabetical order.

def anagram(w1, w2):
	w1 = w1.lower()
	w2 = w2.lower()
	return sorted(w1) == sorted(w2)

in1 = input("Enter the first word: ")
in2 = input("Enter the second word: ")
print(anagram(in1, in2))


### Count Character Occurences! ####

#This algorithm returns the number of times each character occurs
#It iterates one by one through each character, and keeps track
#of occurences in a dictionary

def count_characters(string):
	count_dict = {}
	for c in string:
		if c in count_dict:
			count_dict[c] += 1
		else:
			count_dict[c] = 1

	print(count_dict)

word = input("Please enter a word: ")

count_characters(word)


### Recursion! ###

#Recursion is a method of solving problems by breaking the problem up
#into smaller pieces until it can be easily solved.

#Up to now we built iterative algorithms, they solve problems by 
#repeating steps over and over, typically using a loop.

#Recursive Algorithms rely on functions that call themselves. Any 
#problem that can be solved iteratively can be solved recursively.
#Recursive algorithms tend to be more elegant solutions. 

#Recursive algorithms are written inside functions. The function must
#have a base case: a condition to end the algorithm so it doesn't run
#forever. Inside the function, the function calls itself. Each time it 
#does, it gets closer to the base case. 

#Eventually, the base case condition is satisfied, the problem is 
#solved, and the function stops calling itself. An algorithm that 
#follows these rules satisfied the three laws of recursion:

#1. A recursive algorithm must have a base case.
#2. A recursive algorithm must change its state and move toward
#the base case.
#3. A recursive algorithm must call itself, recursively.

#Example! Printing the lyrics to 99 bottles of beer on the wall.

def bottles_of_beer(bob):
	if bob < 1:
		print("No more bottles of beer on the wall. :(")
		return

	tmp = bob
	bob -= 1
	print(f"""{tmp} bottles of beer on the wall. 
			{tmp} bottles of beer. Take one down, pass it around,
			{bob} bottles of beer on the wall.""")

	bottles_of_beer(bob)

bottles_of_beer(99)





