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

"""
Here we are sorting the array of strings and then we are comparing the first and the last string in the sorted array.
We are using a for loop to iterate through the characters of the first and the last string and we are checking if the characters are the same or not.
If the characters are the same then we are adding the character to the answer list and if the characters are different then we are joining the answer list and returning the string.
Finally we are joining the answer list and returning the string.
"""