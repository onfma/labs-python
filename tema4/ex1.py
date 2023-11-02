# Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek 
# (the last two methods should return None if no element is present in the stack).

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return not self.stack

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print(stack.pop())  # Output: 15
print(stack.peek())  # Output: 10
print(stack.pop())  # Output: 10
print(stack.pop())  # Output: 5
print(stack.pop())  # Output: None
