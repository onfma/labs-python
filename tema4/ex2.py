# Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return not self.queue

queue = Queue()
queue.push(5)
queue.push(10)
queue.push(15)

print(queue.pop())  # Output: 5
print(queue.peek())  # Output: 10
print(queue.pop())  # Output: 10
print(queue.pop())  # Output: 15
print(queue.pop())  # Output: None
