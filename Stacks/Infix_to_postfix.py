def prec(c):
    if c == "^":
        return 3
    elif c == "*" or c == "/":
        return 2
    elif c == "-" or c == "+":
        return 1


def InfixPostfix(s):
    stack = []
    result = ""

    for c in s:

        # If character is an operand, directly add it to result
        if c.isalnum():
            result += c

        # If opening bracket, add it to stack
        elif c == "(":
            stack.append(c)

        # If closing bracket, pop until opening bracket
        elif c == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()

            stack.pop()  # Remove "("

        # If character is an operator
        else:
            while stack and stack[-1] != "(" and prec(c) <= prec(stack[-1]):
                result += stack.pop()

            stack.append(c)

    # Empty remaining stack
    while stack:
        result += stack.pop()

    print(f"Postfix expression: {result}")


if __name__ == "__main__":
    exp = "(p+q)*(m-n)"

    print(f"Infix expression: {exp}")

    InfixPostfix(exp)