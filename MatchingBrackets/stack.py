# Stack Data Structure - includes basic fucntions needed for the stack operations

class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def get_full_stack(self):
		return self.items