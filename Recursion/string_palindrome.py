#problem Statement:
"""Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.
For example:
Input: Str = 'ABCDCBA'
Output: Palindrome"""

# Approach 1:
# def palindrome(val,start,end):
#     if start >= end:
#         return True
#     if val[start] != val[end]:
#         return False
#     return palindrome(val,start+1,end-1)
#
# val = input("Enter a string: ")
# print(palindrome(val,0,len(val)-1))
"""Here in this approach, i have first taken the input from the user.
then i have used a recursive function where the parameter are the user input, start index that is 0 and the end index that is len-1.
then i have set the base condition where if start becomes greater than or equal to end then we return true.
then the other condition where if val[start] that is the first character is not equal to val[end] that is the last character then we return false.
then i have made a recursive call where i have called the function again including the user input,incremented start value and decremented end value."""

# Approach 2:
def palindrome(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
val = input("Enter a string: ")
print(palindrome(val))
"""This is a simple and easy to understand approach where i have first taken a user input.
then i have made a recursive function where if the length of the string becomes less than or equal to 1 then return true.
the other condition is if s[0] that is the first character is not equal to s[-1] that is the last character then return false.
then i have made a recursive call where return the function along with the string which is sliced where we remove the first and the last element and return.
"""