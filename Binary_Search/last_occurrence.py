# Problem Statement:
"""Given an sorted array of n integers, write a program to find the index of the last occurrence of the target key.
If the target is not found then return -1.
For example:
arr = [3,4,13,13,13,20,40], target = 13
Output = 4
"""



# Approach 1:
# arr = [3,4,13,13,13,20,40]
# target = 13
# ans = -1
# low = 0
# high = len(arr) - 1
# while low <= high:
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         ans = mid
#     if arr[mid] <= target:
#         low = mid + 1
#     else:
#         high = mid - 1
# print(ans)
"""This is the optimal approach where i have set the low, high and then run a while loop.
Inside the while loop, first i have found the mid then if the arr[mid] = target, we will store that index mid in the variable.
Otherwise if the arr[mid] is less than or equal to the target, we increment the low by mid +1 else we increment the high by mid -1.
once we are out of the loop, we print the ans.
"""



# Approach 2:
arr = [3,4,13,13,13,20,40]
ans = -1
target = 60
for i in range(len(arr)-1,0,-1):
    if arr[i] == target:
        ans = i
        break
print(ans)
"""This is the brute force approach where i have ran a reversed for loop.
Here if we see the target value then we save that in the variable and break the loop otherwise we iterate the entire loop.
Once we are outside the loop, we print the value.
"""