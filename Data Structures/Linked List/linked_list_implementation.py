# Linked List Implementation using Python with:
## 1. Finding the lowest value (findLowestValue)
## 2. Delete a specific node (deleteNode)
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       
# Find Lowest Value 
def findLowestValue(head):
    if head is None:   
        return None
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next 
    return minValue

# Delete Specific Node
def deleteNode(head, nodeToDelete):
    if head is None:  
        return None
    # If head needs to be deleted
    if head == nodeToDelete:
        return head.next 
    current = head
    while current.next and current.next!=nodeToDelete:
        current = current.next 
    # Node not found
    if current.next is None:
        print("Node not found")
        return head
    # Delete node
    current.next = current.next.next
    return head

# Helper function to print list
def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# --------- Test ---------
print("Original List:")
printList(node1)

# Find minimum
print("Lowest value:", findLowestValue(node1))

# Delete a node (example: delete node3 → value 3)
node1 = deleteNode(node1, node3)

print("After deleting 3:")
printList(node1)