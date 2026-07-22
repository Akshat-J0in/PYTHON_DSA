"""
Problem Statement:
Implement a First-In-First-Out (FIFO) queue using an array.
The implemented queue should support the following operations: push, dequeue, pop, and isEmpty.
"""



class ArrayQueue:
    def __init__(self):
        self.arr = [0] * 10

        self.start = -1
        self.end = -1

        self.currSize = 0
        self.maxSize = 10

    def push(self, x):
        if self.currSize == self.maxSize:
            print("Queue is full")
            return
        
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end + 1) % self.maxSize
        
        self.arr[self.end] = x
        self.currSize += 1

    def pop(self):
        if self.start == -1:
            print("Queue is empty")
            return
        
        popped = self.arr[self.start]

        if self.currSize == 1:
            self.end = -1
            self.start = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        
        self.currSize -= 1
        return popped
    
    def peek(self):
        if self.start == -1:
            print("Queue is Empty")
            return
        return self.arr[self.start]
    
    def isEmpty(self):
        return self.currSize == 0
    
if __name__ == "__main__":
    queue = ArrayQueue()
    commands = ["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            queue.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(queue.pop(), end=" ")
        elif commands[i] == "peek":
            print(queue.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if queue.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayQueue":
            print("null", end=" ")