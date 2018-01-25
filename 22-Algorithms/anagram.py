#Anagram!

def anagram(w1, w2):
	w1 = w1.lower() #lowercase so result isn't affected by capital letters
	w2 = w2.lower()
	return sorted(w1) == sorted(w2) #the sorted method rearranges the words


in1 = input("Enter the first word: ")
in2 = input("Enter the second word: ")
print(anagram(in1, in2))
