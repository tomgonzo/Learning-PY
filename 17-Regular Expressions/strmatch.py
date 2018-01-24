#Matching Digits! Challenges 2 and 3

import re

#Match all the digits in this string
text = "Arizona 479, 501, 870, California 209, 213, 650"

#first match and print all the digits
zing = re.findall("\d", text)

print(zing)

#now find and print words that start with any character followed by two o's


texter = "The ghost that says boo haunts the loo."

zinger = re.findall(".oo", texter)

print(zinger)