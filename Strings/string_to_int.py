"""
Problem Statement:
Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).
Steps to Implement: 1. First, ignore any leading whitespace characters ' ' until the first non-whitespace character is found.
2. Check the next character to determine the sign. If it’s a '-', the number should be negative. If it’s a '+', the number should be positive. If neither is found, assume the number is positive.
3. Read the digits and convert them into a number. Stop reading once a non-digit character is encountered or the end of the string is reached. Leading zeros should be ignored during conversion.
4. The result should be clamped within the 32-bit signed integer range: [-2147483648, 2147483647]. If the computed number is outside this range, return -2147483648 if the number is less than -2147483648, or return 2147483647 if the number is greater than 2147483647.
5. Finally, return the computed number after applying all the above steps.
"""



def atoi(s):
    i = 0

    while i < len(s) and s[i] == ' ':
        i += 1
    
    sign = 1
    if i < len(s):
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
    
    def dfs(idx,num):
        if idx >= len(s) or not s[idx].isdigit():
            return num
        
        num = num * 10 + int(s[idx])
        return dfs(idx+1,num)
    
    num = dfs(i,0)
    num = sign * num

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

S = "   -42"
print(atoi(S))
"""
Here in this code, we are first taking the input from the user, to give us the string.
Then we are initializing a variable i to 0, to keep track of the index of the string.
Then we are running a loop to ignore any leading whitespace characters until the first non-whitespace character is found.
Then we are checking the next character to determine the sign. If it’s a '-', the number should be negative.
If it’s a '+', the number should be positive. If neither is found, we assume the number is positive.
Then we are defining a recursive function dfs to read the digits and convert them into a number.
We stop reading once a non-digit character is encountered or the end of the string is reached. Leading zeros are ignored during conversion.
Then we are multiplying the computed number with the sign to get the final result.
Then we are clamping the result within the 32-bit signed integer range and returning it.
"""