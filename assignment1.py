class Stack:
    def __init__(self):
        self.items = []  # Create an empty list to store the stack elements

    def push(self, item):
        self.items.append(item)  # Add the item to the top of the stack

    def pop(self):
        if self.isEmpty():
            return None  # If the stack is empty, return None
        return self.items.pop()  # Remove and return the top element of the stack

    def isEmpty(self):
        return len(self.items) == 0  # Check if the stack is empty

# Example usage:
stack = Stack()  # Create a new stack

stack.push(1)  # Push elements onto the stack
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

print(stack.isEmpty())  # Output: True
