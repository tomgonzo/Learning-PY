#Challenge 1! Looking for Dutch in Zen.

import os
import re

with open("zen.txt", "r") as zen:
	scribe = zen.read()

scout = re.findall("Dutch", scribe, re.IGNORECASE)

print(scout)

