"""
Problem Statement:
You are given a valid postfix expression as a string, where:
Operands are single lowercase English letters ('a' to 'z')
Operators are binary: '+', '-', '*', '/'
The expression contains no spaces and is guaranteed to be valid.
"""



# Now here we are going to create a function that will convert postfix to prefix
def postfix_to_prefix(postfix):
    stack = []
    for c in postfix:
        if c.isalnum():
            stack.append(c)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            stack.append(c + op1 + op2)

    return stack[-1]

def main():
    postfix = "ABC/-AK/L-*"
    print("Prefix Expression: ", postfix_to_prefix(postfix))

if __name__ == "__main__":
    main()