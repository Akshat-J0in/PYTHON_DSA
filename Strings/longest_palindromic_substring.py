"""
Problem Statement:
Given a string s, return the longest palindromic substring in s.
"""



# Approach 1: Brute Force
# s = "babad"
# result = ""
# # for i in range(len(s)):
# #     for j in range(i, len(s)):
# #         substring = s[i:j + 1]
# #         if substring == substring[::-1]:
# #             if len(substring) > len(result):
# #                 result = substring
# # print(result)
"""
Here we have taken the input string and then we have made a variable result for storing the longest palindromic substring.
Then we have made two loops for generating all the substrings of the string.
In the inner loop, we have checked if the current substring is a palindrome or not by comparing it with its reverse.
If it is a palindrome, then we have checked if its length is greater than the length of the current longest palindromic substring stored in the result variable.
If it is greater, then we have updated the result variable with the current substring.
Finally, we have printed the result variable which contains the longest palindromic substring.
"""



# Approach 2: Expand Around Center
def longest_palindrome(s):
    result = ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(len(s)):
        odd = expand_around_center(i,i)
        even = expand_around_center(i,i+1)
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    return result

print(longest_palindrome("babad"))
"""Here we have taken the input string and then we have made a variable result for storing the longest palindromic substring.
Then we have defined a helper function expand_around_center which takes two parameters left and right and expands around the center of the string to find the longest palindromic substring.
In the main function, we have made a loop for iterating through each character of the string
and for each character, we have called the expand_around_center function twice, once for odd length palindromes and once for even length palindromes.
Then we have checked if the length of the odd length palindrome is greater than the length of the current longest palindromic substring stored in the result variable.
If it is greater, then we have updated the result variable with the odd length palindrome.
Then we have checked if the length of the even length palindrome is greater than the length of the current longest palindromic substring stored in the result variable.
If it is greater, then we have updated the result variable with the even length palindrome.
Finally, we have printed the result variable which contains the longest palindromic substring.
"""