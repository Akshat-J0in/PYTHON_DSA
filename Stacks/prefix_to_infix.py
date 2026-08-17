"""
Problem Statement:
You are given a valid arithmetic expression in prefix notation.
Your task is to convert it into a fully parenthesized infix expression.
Prefix notation (also known as Polish notation) places the operator before its operands.
In contrast, infix notation places the operator between operands.
"""



# Now this is the main fuction where we are going to convert the prefix to infix
def prefix_to_infix(prefix):
    stack = []
    for c in reversed(prefix):
        if c.isalnum():
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            stack.append(f"({op1}{c}{op2})")
    return stack[-1]

# The main function where we are setting our prefix expression and passing it to our main function
def main():
    prefix = "*-A/BC-/AKL"
    print("Infix expression: ", prefix_to_infix(prefix))

if __name__ == "__main__":
    main()