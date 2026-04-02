# Problem Statement:
"""Given an integer array arr of size N, sorted in ascending order. Now the array is rotated between 1 to N times which is unknown. Find
how many times the array has been rotated.
For example:
arr = [4,5,6,7,0,1,2,3]
Output: 4
"""



# Approach 1:
# arr = [4,5,6,7,0,1,2,3]
# n = len(arr)
# for i in range(n-1):
#     if arr[i] > arr[i+1]:
#         print(i+1)
"""Here i have used the loop to find the number of rotation.
If the value of arr[i] greater than arr[i+1] that means that we have found the index of the lowest value thus we return that value.
"""



# Approach 2:
arr = [4,5,6,7,0,1,2,3]
low = 0
high = len(arr)-1
while low < high:
    mid = (low+high)//2

    if arr[mid] > arr[high]:
        low = mid+1
    else:
        high = mid

print(low)
"""Here this is a binary search approach where i have first set a condition where if mid is greater than high that means the lowest value will be present at right side of the array.
so here i have made low = mid + 1
Else if the the above condition is not true that means the lowest value will be at left or mid itself so we made high = mid.
"""