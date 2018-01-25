#Challenge1! Reverse the string yesterday.

class Stack:
	def __init__(self):
		self.items = []

	def push(self,item): #adds item to top of stack
		self.items.append(item)

	def pop(self): #removes and returns top item
		return self.items.pop()

reverse = ""

word = Stack()

for i in "yesterday":
	word.push(i)

for i in range(len(word.items)):
	reverse += word.pop()

print(reverse)

