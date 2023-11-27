'''
	Queue
		- ADT(abstract data type)
		- FIFO (First In- First Out) or First come - first serve
			-- the first element inserted into queue will be the very first one processed
		-- data is inserted at the top(rear) and the data deletion is at the bottom(front)

	Operatation of Queue
		- enqueue
			- insets a new element at the top of a queue
		- dequeue
		- isEmpty
		- isFull
		- isPeek
'''

'''
	Algorithm of Enqueue

	Enqueue(head, tail, value)
	{
		Create a node
		address of new node -> node.data = value
		address of new node -> node.link = NULL
		if(head <> NULL) then
		{
			tail -> node.link = address of new node
		} else	{
			head = address of new node
		}
		tail = address of new node
	}
'''
class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class Queue:
	def __init__(self): 
		self.head = None
		self.tail = None

	def enqueue(self, value):
		new_node = Node(value)

		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

	
	#dequeque
	def dequeue(self):
		current_node = self.head
		if self.head is None:
			return None 
		else:
			removed_node = self.head
			self.head = self.head.next
			return removed_node.data

	def print_queue(self):
		current_node = self.head
		while current_node:
			print(f'Node({current_node.data}, next: {hex(id(current_node.next))}')
			current_node = current_node.next
		print()

queue = Queue()
queue.enqueue('monday')
queue.print_queue()

queue.enqueue('tuesday')
queue.print_queue()

queue.enqueue('wednesday')
queue.print_queue()

'''
	dequeue(head, tail)
	{
		if head <> Null then
		{
			node.delete = head
			print head -> node.data
			head = head -> node.link
			if head = null
			{
				tail = null
			} else {
				print "Underflow or Empty list"
			}
		free(node_delete)
		}
	}
'''
print(f'Dequeued: ({queue.dequeue()}')
queue.print_queue()

print(f'Dequeued: ({queue.dequeue()}')
queue.print_queue()

print(f'Dequeued: ({queue.dequeue()}')
queue.print_queue()

'''