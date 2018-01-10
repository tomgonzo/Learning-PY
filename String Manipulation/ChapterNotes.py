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

#Changing Case - achieved using method.
#String to Uppercase, use UPPER method

"We hold these truths...".Upper()
>> 'WE HOLD THESE TRUTHS...'

#Similarly, change to lowercase using LOWER method
"SO IT GOES".lower()
>> "so it goes"

#Change the first letter to capital letter using CAPITALIZE method
"four score and...".capitalize()
>> "Four score and..."

#Format!
#Create new strings using the FORMAT method. This looks for curly brackets
#in the string, and replaces them with parameters passed in.

"William {}".format("Faulkner")
>> "William Faulkner"

#Variables can also be passed as parameters

last = "Faulkner"
"William {}".format(last)
>> "William Faulkner"

# We're also not limited to one set of curly brackets.

author = "William Faulkner"
year = "1897"
"{} was born in {}".format(author,year)
>> "William Faulkner was born in 1897"

#Format can be useful when creating strings from user input.

n1 = input("Enter a name")
v = input("Enter a verb")
adj = input("Enter an adjective")
n2 = input("Enter a noun")

r = """The {} {} the {} {}""".format(n1,v,adj,n2)

print(r)

#Split!
#Strings have a mthod called split, which separates one string into two or more strings. 
#You pass the split method a string as a parameter, to be used to divide the original string.
#The result is a list with the items. The string passed to split is not included.

"Hello. Yes!".split(".")
>> ['Hello','Yes!']

#Join!
#The join method lets you add new characters between every character in a string.

first_three = "abc"
result = "+".join(first_three)

result
>> 'a+b+c'

#A list of strings can be turned into a single string by calling 
#the join method on an empty string, and passing the list as a parameter.

words = ["The","fox","jumps","over","the","fence","."]
one = "".join(words)

one
>> "Thefoxjumpsoverthefence."

#The resulting string can have a space between each word by calling
#join on a string with a space in it.

words = ["The","fox","jumps","over","the","fence","."]
one = " ".join(words)

one
>> "The fox jumps over the fence ."

#Strip!
#The strip method removes leading and trailing whitespace from a string.

s = "      The"
s = s.strip()
s

>> "The"

#Replace
#The replace method replaces every occurence of a string with another string.
#The first parameter is the string to replace.
#The second parameter is the string to replace the occurence with.

equ = "All animals are equal."
equ = equ.replace("a","@")
print(equ)

>> 'All @nim@als @re equ@l.'

#Finding an index
#The index method gets the index of the first occurence of a character in a string.
#Pass the character you're looking for as a parameter.

"animals".index("m")
>> 3

#Python returns a ValueError exception if no match is found.
#Use exception handling if you're not sure a match will exist.

try:
	"animals".index("z")
except:
	print("Not found.")

>> Not found.

#In
#The in keyword checks if a string is in another string.
#It returns either True or False.

"Cat" in "Cat in the Hat."

>> True

"Bat" in "Cat in the Hat"

>> False

#Put the keyword not in front of in to check if one string is not in another string.

"Potter" not in "Harry"

>> True

#Escaping Strings!
#If you use quotes inside a string, you get a syntax error.
#Fix this error by prefacing quotes with backslashes.

"She said "Surely"" >> SyntaxError

"She said \"Surely\"" >> She said "Surely"

#Escaping a string means putting a symbol in front of a character that normnally 
#has a special meaning in Python. Python uses a backslash for escaping.
# You don't need to escape single quotes inside of a string of double quotes.

"She said 'Surely'" >> She said 'Surely'

#Double quotes can also be used inside single quotes.

'She said "Surely"' >> She said 'Surely'

#Newline!
#Putting \n inside a string represents a newline.

print("line1\nline2\nline3")

>>line1
>>line2
>>line3

#Slicing
#Slicing is a way to return a new iterable from a subset of items in another iterable. 
#The syntax for slicing is [iterable][[start_index:end_index]]
#Example: How to slice a list:

fict = ["Tolstoy","Camus","Orwell","Huxley","Austin"]
fict[0:3]
>> "Tolstoy", "Camus", "Orwell"

#The start index includes the item at that index, 
#but the end index includes the item before the end index.

#Example of slicing a string:

ivan = "In place of death there was light."
ivan[0:17]
ivan[17:33]

>> "In place of death"
>> " there was light"

#If the start index is 0, it can be left blank.

ivan = "In place of death there was light."
ivan[:17]

>> "In place of death"

#If the end index is the last item, you can leave the end index empty.

ivan = "In place of death there was light."
ivan[17:]

>> " there was light."

#Leaving both the start and end index empty returns the entire iterable.

ivan = "In place of death there was light."
ivan[:]

>> "In place of death there was light."
