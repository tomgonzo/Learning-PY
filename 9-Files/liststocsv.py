#This program prints a lists of lists into a CSV. - Challenge 3

masterlist = [["Top Gun", "Risky Business", "Minority Report"],
			 ["Titanic", "The Revenant", "Inception"],
			 ["Training Day", "Man on Fire", "Flight"]]

import csv

with open ("movies.csv", "w", newline = '') as m:
	x = csv.writer(m, delimiter = ",")
	x.writerow(masterlist[0])
	x.writerow(masterlist[1])
	x.writerow(masterlist[2])


with open ("movies.csv", "r") as f:
	r = csv.reader(f, delimiter = ",")
	for row in r:
		print(",".join(row))