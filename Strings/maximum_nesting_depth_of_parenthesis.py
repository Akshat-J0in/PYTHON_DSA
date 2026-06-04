"""
Problem Statement:
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
"""



s = "(1+(2*3)+((8)/4))+1"
ans = 0
count = 0
for ch in s:
    if ch == '(':
        count += 1
        ans = max(ans, count)
    elif ch == ')':
        count -= 1
print(ans)
"""
Here we have a string of parentheses and we have to find the maximum nesting depth of the parentheses
We will keep a count variable which will keep track of the number of open parentheses.
if the character is open parentheses then we will increment the count variable and then we will update the answer variable with the maximum of the current answer and the count variable.
If the character is closed parentheses then we will decrement the count variable.
Finally we will return the answer variable which will have the maximum nesting depth of the parentheses.
"""