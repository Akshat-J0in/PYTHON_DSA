"""
Problem Statement:
You are given a string s.
Return the array of unique characters, sorted by highest to lowest occurring characters.
If two or more characters have same frequency then arrange them in alphabetic order.
"""



w = "tree"

s_dict = {}

for i in w:
    s_dict[i] = s_dict.get(i, 0) + 1

sorted_char = sorted(s_dict.items(),key = lambda x: (-x[1],x[0]))

result = [char for char,freq in sorted_char]
print(result)
"""
Here first i have taken the string input and then i have created a empty dictionary.
then i have added the values in the dictionary
while sorting i have converted the dictionary into a list of tuples and then i have sorted the list of tuples by using the sorted function.
Here in the sorted function, i have used a lambda function as a key where i have set the condition that first we will sort by frequency in descending order and then if the frequency is same then we will sort by alphabetic order.
after sorting, i have created a list comprehension to get the characters from the sorted list of tuples and then i have printed the result.
"""