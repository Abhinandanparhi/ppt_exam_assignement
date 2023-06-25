class Queue:
    def __init__(self):
        self.items = []  # Create an empty list to store the queue elements

    def enqueue(self, item):
        self.items.append(item)  # Add the item to the rear of the queue

    def dequeue(self):
        if self.isEmpty():
            return None  # If the queue is empty, return None
        return self.items.pop(0)  # Remove and return the front element of the queue

    def isEmpty(self):
        return len(self.items) == 0  # Check if the queue is empty

# Example usage:
queue = Queue()  # Create a new queue

queue.enqueue(1)  # Enqueue elements into the queue
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3

print(queue.isEmpty())  # Output: True
