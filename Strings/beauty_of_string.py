""""
Problem Statement:
The beauty of a string is defined as the difference between the frequency of the most frequent character
and the least frequent character (excluding characters that do not appear) in that string.
Given a string s, return the sum of beauty values of all possible substrings of s.
"""



s = "aabcbaa"
substrings = []

n = len(s)
total = 0
for i in range(n):
    freq = {}
    for j in range(i, n):
        freq[s[j]] = freq.get(s[j], 0) + 1
        substrings.append(s[i:j + 1])

        values = freq.values()
        maxi = max(values)
        mini = min(values)
        total += (maxi - mini)

print(total)
print(substrings)
"""
Here first we have taken the input string and then we have made a list for storing all the substrings.
Then we have made a variable total for storing the sum of beauty of all the substrings.
Then we have made two loops for generating all the substrings of the string.
In the inner loop, we have made a frequency dictionary for storing the frequency of each character in the current substring.
Then we have calculated the maximum and minimum frequency of the characters in the current substring and then we have added the difference of maximum and minimum frequency to the total variable.
Finally, we have printed the total variable which contains the sum of beauty of all the substrings and also we have printed all the substrings.
"""