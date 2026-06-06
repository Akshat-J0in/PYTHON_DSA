"""
Problem Statement:
Roman numerals are represented by seven different symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
For example: 2 is written as II, 12 is written as XII, 27 is written as XXVII.
Roman numerals are usually written largest to smallest from left to right. But in six special cases, subtraction is used instead of addition:
I before V or X → 4 and 9,
X before L or C → 40 and 90,
C before D or M → 400 and 900
Given a Roman numeral, convert it to an integer.
"""



s = "MCMXCIV"

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
res = 0
for i in range(len(s)-1):
    if roman[s[i]] < roman[s[i+1]]:
        res -= roman[s[i]]
    else:
        res += roman[s[i]]

res += roman[s[-1]]
print(res)
"""Here in this code, we are first taking the input from the user, to give us the roman numeral.
Then we are creating a dictionary to store the value of each roman numeral.
Then we are running a loop till the length of the string -1.
Here we are checking if the value of the current character is less than the next character.
If so then we are subtracting the value of the current character from the result.
Else we are adding the value of the current character to the result.
Then we are adding the value of the last character to the result and printing it.
This is how we can convert a roman numeral to an integer.
"""