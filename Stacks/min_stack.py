class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return

        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self):
        if not self.stack:
            return

        return self.stack[-1]

    def getmin(self):
        if not self.min_stack:
            return
        return self.min_stack[-1]

s = MinStack()
s.push(5)
s.push(3)
s.push(7)
s.push(2)

print(s.getmin())
s.pop()
print(s.getmin())
s.pop()
print(s.top())
print(s.getmin())