#String Manipulation Chapter Notes

#If a string spans more than one line, use triple quotes.

""" line one
	line two
	line three
"""

#Strings are iterable, and characters can be looked up 
#from left to right using an index.

author = "Kafka"
author[0] >> 'K'

#Trying to call a number past the last index will raise an IndexError exception.

#Negative index can also be used to look up
#from right to left.

author[-1] >> 'a'

#Strings are Immutable
#To change a string, create a new string.

ff = "Fond Frick"
ff = "Fickle Fin"

print(ff) >> 'Fickle Fin'

#Concatenation
#Two or more strings can be added with the addition operator.
#The result is a string made up from characters of the first string then the next.
#Adding strings is called Concatenation. 

"cat" + "in" + "hat"
>> 'catinhat'

'cat' + ' in' + ' the' + ' hat'
>> 'cat in the hat'

#String Multiplication
#You can multiply a string by a number with the multiplication operator

"Sawyer" * 3
>> SawyerSawyerSawyer

#Changing Case - achieved using method

