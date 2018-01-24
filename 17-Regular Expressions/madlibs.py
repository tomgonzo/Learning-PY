##Madlibs!
##The game is a paragraph of text with words missing that players are prompted to fill in.


import re

text = """Giraffes have arounsed the curiosity of __PLURALNOUN__ since earliest times.
    The giraffe is the tallest of all living __PLURALNOUN__, but scientists are
    unable to explain how it got its long __BODYPART__. The giraffe's
    tremedous height, which might reach __NUMBER__ __PLURALNOUN__, comes from its
    legs and __BODYPART__."""

def mad_libs(mls):
	"""
	:param mls: string with parts the user should fill out surrounded by double 
	underscores. Underscores cannot be inside hint e.g., no __hint_hint__ only __hint__
	"""

	#Find all things between two underscores in mls and make a list
	#Each one is a hint for the type of word the user needs to supply
	hints = re.findall("__.*?__", mls)

	if hints is not None:
		#loop through the list and use each hint to ask user for word
		for word in hints:
			q = (f"Enter a {word}.")
			new = input (q) #create a new string
			mls = mls.replace(word, new, 1) #replace hint with user-supplied word

		#Once the loop finishes... 
		print('\n')
		#Print the new string with the words collected from the user.
		mls = mls.replace("\n", "")
		print(mls)

	else:
		print("invalid mls")

mad_libs(text)