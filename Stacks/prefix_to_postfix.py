"""
Problem Statement:
You are given a valid prefix expression consisting of binary operators and single-character operands.
Your task is to convert it into a valid postfix expression.
"""



# Now this function will help us to convert the prefix expression to the postfix expression
def prefix_to_postfix(prefix):
    stack = []

    for c in reversed(prefix):
        if c.isalnum():
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            stack.append(op1 + op2 + c)

        return stack[-1]

# Now we will create the main function for this program:
def main():
    prefix = "*-A/BC-/AKL"
    print("Postfix Expression: ", prefix_to_postfix(prefix))

# Now we run this program
if __name__ == "__main__":
    main()