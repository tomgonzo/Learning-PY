#Chapter 21! Data Structures - ChapterNotes

### Data Structures ###
#A Data Structure is a format used to store and organize information.
#Data Structures are fundamental to programming, and most programmeing
#languages come with them built in. 

#Examples of Python's built-in data structures: lists, tuples, dictionaries

#Let's learn two new data structures: stacks and queues

### Stacks! ###

#A stack is a data structure. Like a list, items can be added and removed
#from stacks. Unlike lists, only the last item can be added or removed.

#Removing an items from a stack is called Popping. 
#Pushing an item into the stack is called pushing. 

#This kinf of data structure, where the last item put in is the first item
#taken out, is called a "last-in-first-out" data structure (LIFO)

#Think of a LIFO like a stack of dishes. To reach the bottom all dishes
#starting from the top must be removed.

#Let's build a stack - copying this to stack.py

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


### Queues! ### 

#Like a list, in that items can be added and removed
#Like a stack, in that items go in and out in a certain order

#A queue is a first-in-first-out data structure (FIFO)
#The first item added is the first item taken out.

#Time to build a queue! Copying over to queue.py

class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.inset(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


# A queue can simulate people waiting in line to buy tickets

import time
import random

class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.inset(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def simulate_line(self, till_show, max_time):
		pq = Queue()
		tix_sold = []

		for i in range(10):
			pq.enqueue("person" + str(i))

		t_end = time.time() + till_show
		now = time.time()
		while now < t_end and not pq.is_empty():
			now = time.time()
			r = random.randint(0, max_time)
			time.sleep(r)
			person = pq.dequeue()
			print(person)
			tix_sold.append(person)

		return tix_sold

queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)




