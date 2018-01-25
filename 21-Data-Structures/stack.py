#Manually creating a Stack. 


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

stack = Stack() #create a new stack - it will be empty
print(stack.is_empty()) #this method will return True

#now add a new item to the stack
stack.push(1) #adding 1 to the stack
print(stack.is_empty()) #is it empty?

#now let's see what happens when we pop
item = stack.pop() #returns and removes the last item on the stack
print(item) #print the returned item that was removed
print(stack.is_empty())

#let's push a bunch of things into the stack
for i in range(0,6):
	stack.push(i)

print(stack.peek()) #print the last item in the stack
print(stack.size()) #how many items long is the stack?


#Let's reserve a string with a Stack!
strstack = Stack()
for c in "Hello":
	strstack.push(c)

reverse = ""

for i in range(len(strstack.items)):
	reverse += strstack.pop()

print(reverse)