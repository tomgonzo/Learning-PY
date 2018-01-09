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

