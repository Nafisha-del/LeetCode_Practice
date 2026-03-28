class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
    
# --------- Using all functions ---------

s = Stack()

# Check if stack is empty
print("Is stack empty?", s.isEmpty())

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Traverse stack
print("Stack elements:")
s.traverse()

# Peek top element
print("Top element:", s.peek())

# Pop element
print("Popped element:", s.pop())

# Traverse after pop
print("Stack after pop:")
s.traverse()

# Check if empty
print("Is stack empty now?", s.isEmpty())

# Pop remaining elements
s.pop()
s.pop()

# Try popping from empty stack
print("Pop on empty stack:", s.pop())

# Try peeking empty stack
print("Peek on empty stack:", s.peek())