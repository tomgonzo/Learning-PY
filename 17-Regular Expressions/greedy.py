#make something greedy non-greedy

import re

this = "__here__ __is__ _a_ _string_ _to_ _dice_ _up"

that = re.findall("_.*?_", this)

for match in that:
	print(match)

