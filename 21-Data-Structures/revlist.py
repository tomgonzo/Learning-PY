#Challenge 2! Reverse a list of numbers

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self): #returns True if stack is empty, False otherwise
		return self.items == []

	def push(self,item): #adds item to top of stack
		self.items.append(item)

	def pop(self): #removes and returns top item
		return self.items.pop()

	def peek(self): #returns the top item, does not remove
		last = len(self.items)-1
		return self.items[last]

	def size(self): #returns integer representing stack size
		return len(self.items)

numbers = Stack()

for i in range(1,6):
	numbers.push(i)

print(numbers.size())
print(numbers.items)

reverse = []

for i in range(len(numbers.items)):
	reverse.append(numbers.pop())

print(reverse)