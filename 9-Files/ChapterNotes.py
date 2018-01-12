#Chapter 9 - Files - ChapterNotes

#Python can be used to work with files. 
#Python can read from and write to files.

#Reading from a file means accessing the file's data.
#Writing to a file means adding or changing data in the file.

#Writing to Files!
#The first step to working with files is to open it with the built-in open function.
#The open function takes two parameters:
#A str representing the path and another for the mode to open the file in.

#The file path represents the location on the computer where a file resides.
#You should not write file paths yourself. To avoid problems, create file paths
#with the built-in os module. The path function build the file path for you.

import os
os.path.join("Users", "bob", "st.txt")

>> 'Users/bob/st.txt'

#Creating file paths with the path function ensures they will work on any operating system.

#The mode passed to the open function determines the actions you will be able
#to perform on the file you open. Here are a few of the modes:

#"r" opens file for reading only
#"w" opens file for writing only. Overwrites if file exists. If not, creates file.
#"w+" opens for reading and writing. Overwrites if file exists, creates if not.

#"w" and "w+" create a file in the folder where the program runs from if it doesn't exist.

#The open function returns a file object, which can be used to read/write to your file.
#Use the write method to write to the file, and close to close it.
#If you open a file using the open method, you must close it with the close method.
#Opening files and not closing them can cause problems with the program.

#Here is an example of opening, writing to, and closing a file.

st = open("st.txt", "w")
st.write("Hi from Python")
st.close()

#Automatically closing files!
#There is a preferred syntax for opening files that prevents having to remember to close.
#To use this, put all the code that needs access to the file object inside a with-statement.
#with-statement: compound statement with an action that automatically occurs when left.

#The syntax for opening a file using a with-statement is:
with open(file_path),(mode) as [variable_name]:[your_code]

#file_path represents the file path
#mode represents the mode to open the file in
#variable_name represents the name of the variable the file object is assigned to
#your_code represents the code that has access to the variable the file object is assigned to

#Using this syntax automatically closes the file after [your_code] executes
#Here is an example using this syntax:

with open("st.txt", "w") as f:
	f.write("Hi from Python!")

#As long as you are inside the with-statement, you can access the file object.

#Reading from files!
#To read, pass r as the mode. The read method returns an iterable containing each line of the file.

#Example:

with open("st.txt", "r") as f:
	print(f.read())

>> "Hi from Python!"

#Now you can access this data later in your program!

#CSV Files!
#Python has a built-in module to work with csv files.
#After opening a csv file, the csv module converts the file into a csv object.
#The csv module has a method called writer that accepts a file object and a delimiter.

#The writer method returns a csv object that has a method called writerow.
#The writerow method accepts a list as a parameter, and can be used to write to csv.
#Every item in the list gets written - separater by a passed delimiter - to a row in the csv file.
#writerow creates a single row, so it must be called multiple times for multiple rows.

import csv

with open("st.csv", "w", newline ='') as f:
	w = csv.writer(f, delimiter=",")
	w.writerow(["one", "two", "three"])
	w.writerow(["four", "five", "six"])

#This program creates a new file called st.csv, and when opened in a text editor looks like this:
#one,two,three,four,five,six

#The csv module can also read the contents of a file.
#To read from a csv file, pass r as the mode to the open function.
#Then inside the with-statement call the reader method, passing the file object and comma as delimiter.
#This returns an iterable that can be used to access each row in the file.

import csv

with open("st.csv", "r") as f: #st.csv is opened for reading 
	r = csv.reader(f, delimiter=",") #converted to csv object using reader method
	for row in r: #Iterate through csv object using a loop
		print(",".join(row)) #call the join method to add a comma between each piece and print contents.

>> one, two, three
>> four, five, six

