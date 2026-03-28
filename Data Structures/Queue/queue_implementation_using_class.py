class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
# --------- Using all functions ---------

s = Queue()

# Check if empty
print("Is queue empty?", s.isEmpty())

# Push elements
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)

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