class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear == None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        
        temp = self.front
        self.front = temp.next
        # If queue becomes empty after dequeue
        if self.front is None:
            self.rear = None
            
        self.length -= 1
        return temp.data
    
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
# --------- Using all functions ---------

s = Queue()

# Check if empty
print("Is queue empty?", s.isEmpty())

# Push elements
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)

# Printing
print("Printing queue:")
s.printQueue()

# Check size
print("Queue size:", s.size())

# Peek top element
print("Top element:", s.peek())

# Pop element
print("Popped element:", s.dequeue())

# Check size again
print("Queue size after pop:", s.size())

# Check if empty again
print("Is queue empty now?", s.isEmpty())

# Pop all to test empty case
s.dequeue()
s.dequeue()

# Try popping from empty stack
print("Pop on empty queue:", s.dequeue())

# Try peeking empty stack
print("Peek on empty queue:", s.peek())