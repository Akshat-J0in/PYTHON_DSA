# Problem Statement:
"""Given an array of N integers, every number in the array except one appears twice. Find the single number in the array.
For example:
arr = [1,1,2,2,3,3,4,5,5,6,6]
Output: 4
"""



# Approach 1:
# arr = [1,1,2,2,3,3,4,5,5,6,6]
# low = 0
# high = len(arr)-1
#
# while low < high:
#     mid = (low+high)//2
#
#     if arr[mid] == arr[mid ^ 1]:
#         low = mid + 1
#     else:
#         high = mid
# print(arr[low])
"""
Here this is the optimal binary search approach where i have use the concept of index.
Here if the number are repeating, then they are occupying odd and even index so if we do xor, we will find the previous index if its same as that of its preceding index.
If yes then we make the low = mid + 1 as the single value will be at the right of the array.
else we move the high and set it to mid.
"""



# Approach 2:
arr = [1,1,2,2,3,3,4,5,5,6,6]
values = {}

for i in range(len(arr)):
    if arr[i] not in values:
        values[arr[i]] = 1
    else:
        values[arr[i]] += 1

for key,values in values.items():
    if values == 1:
        print(key)
"""
Here i have used the dictionary approach where i have set the empty dictionary then i have filled it with key and value using loops.
Once that is done, we have searched the dictionary to see which key has its corresponding value as 1 and then print the key.
"""