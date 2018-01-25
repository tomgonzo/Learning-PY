#Exercise! Let's create a queue

class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

a_queue = Queue() #create a new empty queue
print(a_queue.is_empty()) #return True if it's empty

#now add items to the queue and check its size
for i in range(5):
	a_queue.enqueue(i)

print(a_queue.size())

#remove items from the queue
for i in range(5):
	print(a_queue.dequeue())

print()

print(a_queue.size())