#List Printing with index - Challenge 3

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
i=0

for show in shows: #create a variable show for each item in shows
	new = shows[i] #define a variable "new" with item in shows
	newin = str(i) #define variable newin with str value of index
	print(newin) + " - " + (new) #print both index and show name
	i += 1 #increase i by 1