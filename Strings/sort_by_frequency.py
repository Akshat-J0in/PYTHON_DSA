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