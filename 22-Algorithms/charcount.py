#Character Counter Algorithm

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