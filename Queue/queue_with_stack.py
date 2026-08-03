"""
Problem Statement:
Implement a First-In-First-Out (FIFO) queue using two stacks.
The implemented queue should support the following operations: push, pop, peek, and isEmpty.
"""



class stackQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x:int):
        self.input.append(x)

    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        if not self.output:
            print("Queue is empty, cannot pop")
            return -1

        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        if not self.output:
            print("Queue is Empty cannot peek")
            return -1

        return self.output[-1]

    def isEmpty(self):
        return not self.input and not self.output

if __name__ == "__main__":
    q = stackQueue()
    q.push(3)
    q.push(4)
    print("The element popped is", q.pop())
    q.push(5)
    print("The front of the queue is", q.peek())
    print("Is the queue empty?", "Yes" if q.isEmpty() else "No")
    print("The element popped is", q.pop())
    print("The element popped is", q.pop())
    print("Is the queue empty?", "Yes" if q.isEmpty() else "No")