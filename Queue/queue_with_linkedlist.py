class Node:
    def __init__(self, d):
        self.val = d
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.start = self.end = None
        self.size = 0

    def push(self,x):
        element = Node(x)

        if self.start is None:
            self.start = self.end = element
        else:
            self.end.next = element
            self.end = element

        self.size += 1

    def pop(self):
        if self.start is None:
            return -1

        value = self.start.val
        temp = self.start
        self.start = self.start.next
        del temp
        self.size -= 1

        return value

    def peek(self):
        if self.start is None:
            return -1

        return self.start.val

    def is_empty(self):
        return self.size == 0

q = LinkedListQueue()

# List of commands
commands = ["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]
# List of inputs
inputs = [[], [3], [7], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        q.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(q.pop(), end=" ")
    elif commands[i] == "peek":
        print(q.peek(), end=" ")
    elif commands[i] == "isEmpty":
        print("true" if q.is_empty() else "false", end=" ")
    elif commands[i] == "LinkedListQueue":
        print("null", end=" ")