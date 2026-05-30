"""
Problem Statement: 
Write a function to find the longest common prefix string amongst an array of strings. 
If there is no common prefix, return an empty string.
"""



arr = ["interview","internet","internal","interval"]

arr.sort()
first = arr[0]
last = arr[-1]
ans = []

for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
        ''.join(ans)
        break
    ans.append(first[i])
print(''.join(ans))