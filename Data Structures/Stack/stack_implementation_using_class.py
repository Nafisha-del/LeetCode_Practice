class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
# --------- Using all functions ---------

s = Stack()

# Check if empty
print("Is stack empty?", s.isEmpty())

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Check size
print("Stack size:", s.size())

# Peek top element
print("Top element:", s.peek())

# Pop element
print("Popped element:", s.pop())

# Check size again
print("Stack size after pop:", s.size())

# Check if empty again
print("Is stack empty now?", s.isEmpty())

# Pop all to test empty case
s.pop()
s.pop()

# Try popping from empty stack
print("Pop on empty stack:", s.pop())

# Try peeking empty stack
print("Peek on empty stack:", s.peek())