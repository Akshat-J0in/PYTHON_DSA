"""
Problem Statement:
Check Balanced Parentheses.
Given string str containing just the characters '(', ')', '{', '}', '[' and ']',
check if the input string is valid and return true if the string is balanced otherwise return false.
"""



class ArrayStack:
    def __init__(self, size=1000):
        self.stackArray = [0] * size
        self.capacity = size
        self.topIndex = -1

    def push(self, x):
        if self.topIndex >= self.capacity - 1:
            print("Stack Overflow")
            return
        self.topIndex += 1
        self.stackArray[self.topIndex] = x

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return -1
        top_element = self.stackArray[self.topIndex]
        self.topIndex -= 1
        return top_element

    def isEmpty(self):
        return self.topIndex == -1


if __name__ == "__main__":
    s = "()[{}()]"
    stack = ArrayStack()

    valid = True

    for ch in s:
        if ch in "({[":
            stack.push(ch)
        else:
            if stack.isEmpty():
                valid = False
                break

            top = stack.pop()

            if (ch == ')' and top != '(') or \
               (ch == ']' and top != '[') or \
               (ch == '}' and top != '{'):
                valid = False
                break

    if not stack.isEmpty():
        valid = False

    if valid:
        print("true")
    else:
        print("false")