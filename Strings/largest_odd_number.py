"""
Problem Statement:
Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero.
"""



s = "0214638"

# Approach 1: Using a while loop to find the last odd digit
# s = s.lstrip('0')   

# x = len(s) - 1

# while x >= 0:
#     if s[x] in '13579':
#         substring = x
#         break
#     x -= 1

# print(s[:substring + 1])
"""
Over here we are using a while loop to find the last odd digit in the string.
First we are using the lstrip() function to remove the leading zeros from the string.
Then we are using a while loop to iterate through the string from the end to the beginning.
If we find an odd digit then we will break the loop and we will print the substring from the beginning of the string to the index of the last odd digit.
If we don't find any odd digit then we will print an empty string.
"""



# Approach 2: Using a for loop to find the last odd digit

s = s.lstrip('0')

for i in range(len(s)-1, -1, -1):
    if s[i] in '13579':
        print(s[:i+1])
        break
else:
    print('')
"""
Over here we are using a for loop to find the last odd digit in the string.
First we are using the lstrip() function to remove the leading zeros from the string.
Then we are using a for loop to iterate through the string from the end to the beginning.
If we find an odd digit then we will break the loop and we will print the substring from the beginning of the string to the index of the last odd digit.
If we don't find any odd digit then we will print an empty string.
"""