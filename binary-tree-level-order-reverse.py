#Source: https://github.com/careermonk/DataStructureAndAlgorithmicThinkingWithPython/blob/master/src/chapter06trees/LevelOrderTraversalInReverse.py
#Level order and Level order reverse

import sys
sys.path.append("./mylib")
import Tree

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	# method for setting the data field of the node    
	def setData(self, data):
		self.data = data
	# method for getting the data field of the node   
	def getData(self):
		return self.data
	# method for setting the next field of the node
	def setNext(self, next):
		self.next = next
	# method for getting the next field of the node    
	def getNext(self):
		return self.next
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def hasNext(self):
		return self.next != None

    
class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp
	
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()

    def isEmpty(self):
        return self.head == None
	
class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print("Sorry, the queue is empty!")
			raise IndexError
		return self.rear.getData()

	def queueFront(self):
		if self.front is None:
			print("Sorry, the queue is empty!")
			raise IndexError
		return self.front.getData()

	def deQueue(self):
		if self.rear is None:
			print("Sorry, the queue is empty!")
			raise IndexError
		result = self.rear.getData()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
		
	def isEmpty(self):
		return self.size == 0
		
def insertInBinaryTreeUsingLevelOrder(root, data):
	newNode = Tree.BinaryTree(data)
	if root is None:
		root = newNode
		return root

	q = Queue()
	q.enQueue(root)
	node = None
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO

		if data == node.getData():
			return root
		if node.left is not None:
			q.enQueue(node.left)
		else:
			node.left = newNode
			return root	
		if node.right is not None:
			q.enQueue(node.right)
		else:
			node.right = newNode
			return root

def levelOrderTraversalInReverse(root):
	if root is None:
		return 0

	q = Queue()
	s = Stack()
	q.enQueue(root)
	node = None
	count = 0
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		if node.left is not None:
			q.enQueue(node.left)

		if node.right is not None:
			q.enQueue(node.right)
		s.push(node)
		
	while(not s.isEmpty()):
		print(s.pop().getData(),end=" ")
	print("")
	
def levelOrderTraversal(a,result):
	#print (a)
	while a:
		#print ("aaa")
		tmp = a.pop(0)
		result.append(tmp.data)
		if tmp.left is not None:
			a.append(tmp.left)
		if tmp.right is not None:
			a.append(tmp.right)
		levelOrderTraversal(a, result)	

root = Tree.BinaryTree(1)
root.insertLeft(2)
root.insertRight(3)
root.getLeft().insertLeft(4)
root.getLeft().insertRight(5)
root.getRight().insertLeft(6)
root.getRight().insertRight(7)
result = []
levelOrderTraversal([root], result)
print("LevelOrder traversal: %s" % (result))
print("LevelOrder traversal (reversal) : ",end="")
levelOrderTraversalInReverse(root)