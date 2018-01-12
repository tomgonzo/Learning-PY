#Ask user for input, save to file, then print. - Challenge 1 + 2

import os

loc = os.path.join("Users",
			 "tomgonzo", 
			 "Documents", 
			 "GitHub", 
			 "Learning PY", 
			 "9-Files", 
			 "file.txt")


with open("file.txt", "w") as f:
	f.write(input("What do you want to save to a file?"))

with open("file.txt", "r") as r:
	print(r.read())
