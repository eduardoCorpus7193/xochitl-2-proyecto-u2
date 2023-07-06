class Node:
    def __init__(self, data):
        # Constructor to initialize a node
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # Constructor to initialize the stack
        self.top = None

    def is_empty(self):
        # Check if the stack is empty
        return self.top is None

    def push(self, data):
        # Push an element onto the stack
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        # Pop the top element from the stack
        if self.is_empty():
            return None

        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        # Peek the top element of the stack without removing it
        if self.is_empty():
            return None
        return self.top.data
'''
# Create a stack
my_stack = Stack()

# Push elements onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Peek the top element of the stack
print(my_stack.peek())  # Output: 3

# Pop elements from the stack
print(my_stack.pop())  # Output: 3
print(my_stack.pop())  # Output: 2

# Check if the stack is empty
print(my_stack.is_empty())  # Output: False

# Pop another element from the stack
print(my_stack.pop())  # Output: 1

# Check if the stack is empty again
print(my_stack.is_empty())  # Output: True
'''