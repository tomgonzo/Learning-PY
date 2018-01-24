#Chapter 17 - Regular Expressions - ChapterNotes

######Regular Expressions!
#A sequence of characters that define a search pattern.

#Use regular expressions to search a file or other data for a complex pattern.
#We will use grep - a command on Unix-like OS that searches files for patterns
#and returns the text it finds in the file that matches the pattern.

#By default, on Ubuntu, the grep command prints matched words in red in its output.
#On Unix, it does not. For Mac, this can be changed with this Env Var:

$ export GREP_OPTIONS='color=always'

#The grep command accepts two parameters: a regular expression and the filepath
#of the file to search for the pattern defined in the regular expression. The
#simplest kind of pattern to match with a regular expression is a simple match:

#A simple match is a string of words that matches the same string of words.
#An example of a simple match can be seen by entering

$ grep Beautiful zen.text

>> Beautiful is better than ugly.

#Do this in the directory where these ChapterNotes are stored.

#In this command, Beautiful, the first parameter, is the regular expression.
#The second parameter, zen.txt, is the path to the file to look for the regular
#expression in. Beautiful prints in red because it is the matched word.

#grep is case sensitive, unless you pass the flag -i

grep -i

#By default, grep prints the entire line it found a match in. 
#The flag -o will only print the exact word that matches the pattern passed in.

grep -o

#You can use regular expressions in Python with its built-in library, re
#The re module comes with a method called findall. Pass on a regular expression
#as a parameter, then a string and it returns a list with all the items in the 
#string the pattern matches.

import re

l = "Beautiful is better than ugly."

matches = re.findall("Beautiful", l)

print(matches)

>> 'Beautiful'

#The findall method is case sensitive, ignore case by passing in re.IGNORECASE to
#the findall method as the third parameter.

import re

l = "Beautiful is better than ugly."

matches = re.findall("beautiful", l, re.IGNORECASE)

print(matches)

>> 'Beautiful'


######Match Beginning and End!#######
#In GREP, there are special characters that alter your search by defining rules.

#Add the caret character (^) to find occurences in the beginning of a line.

grep ^If zen.txt

#The dollar sign can be used only to match the lines that end with a pattern.

grep idea.$ zen.txt

#An example of using the caret character in Python:
#You must pass re.MULTILINE as the third parameter to findall to look for matches
#on all lines of a multi-line screen.

zen = """Although never is often better than *right* now.
		If the implementation is hard to explain, it's a bad idea.
		If the implementation is easy to explain, it may be a good idea.
		Namespaces are one honking great idea -- let's see more of those!"""

m = re.findall("^If" zen, re.MULTILINE)

print(m)

>> ['If', 'If']


### Matching Multiple Characters ###
#Define a pattern that matches multiple characters by putting them inside
#of brackets in a regular expression.

#If you put [a, b, c] into a regular expression, it will match a, b, or c.

#Instead of matching text in zen.txt, now we'll pipe a string to grep.

$ echo Two too. | grep -a t[ow]o

#The output of echo is passed to greg as input and, therefore, no file
#parameter needs to be passed to grep. The command prints:

Two too

#because the re matches a t, followed by an o or w, followed by an o

#In Python:

import re

string = "Two too"

m = re.findall("t[ow]o", string, re.IGNORECASE)

print(m)

>> ["Two", "too"]

### Matching Digits ###
#In grep match digits using [[:digit:]]

echo 32 by 32 | grep [[:digit:]]

#and in Python...

import re

line = "123?34 hello?" 

m = re.findall ("\d", line, re.IGNORECASE)

print(m)

>> [1, 2, 3, 3, 4]

### Repetition ###
#The asterisk (*) adds repetition to regular expressions.
#With an asterisk, "the preceeding item will be matched zero or more times"
#For instance, use an asterisk to match tw followes by any amount of os"

#-o prints the exact word the re appears in
echo two twoo not too | grep -o two*

>> two twoo

#In a re, a period matches any character. Following a period with an asterisk
#instructs the re to match any character zero or more times. Use a period
#followed by an asterisk to match everything between two characters.

echo __hello__there | grep -o __.*__
#re __.*__ matches any character between and including the two double underscores.

#An asterisk is greedy, it will try to match as much text as it can. For example,
#if you add more words with double underscores, the re from the previos example
#will match everything from the first to last underscore.

#Following up an asterisk with a question mark makes the expression non-greedy
#This is not supported by grep, but can be accomplished in Python:

import re

string = "__hi__ __bye__ __hi__"

m = re.findall("__.*?__", string)

for match in m:
	print(match)

>> __hi__
>> __bye__
>> __hi__

#Non-greedy matching can be used to create the game Mad Libs.
#See madlibs.py

### Escaping characters!
#Escaping means ignoring a character's meaning and matching it instead
#Escape characters in re with a backslash. \


$ echo I love $ | grep \\S

>> I love $

#And in Python...

import re

line = "I love $"

m = re.findall("\\$", line, re.IGNORECASE)

print(m)

>> ['$']

#Additional resources - tstp.io/regex








