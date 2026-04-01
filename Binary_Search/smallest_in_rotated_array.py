# Problem Statement:
"""Given an integer array arr of size N, sorted in ascending order. Now the array is rotated at any index which is unknown. Find
The minimum element in the array.
For example:
arr = [3,4,5,1,2]
Output: 1
"""



arr = [3,4,5,1,2]
low = 0
high = len(arr)-1
ans = float("inf")
while low <= high:
    mid = (low+high)//2

    if arr[low] < arr[high]:
        ans = min(ans, arr[low])
        break

    if arr[low] <= arr[mid]:
        ans = min(ans, arr[low])
        low = mid+1
    else:
        ans = min(ans, arr[mid])
        high = mid-1
print(ans)
"""
Here this code is very simple to understand.
The core idea is first we check the condition where if the array is completely sorted or not that is if arr[low] < arr[high].
If yes then then the array is not rotated and we can find the min of ans and low and break the while loop.
If the left half is sorted that is if arr[low] <= arr[mid] then we can say that left half is sorted, we will find the min of the ans and arr[low] and do low = mid + 1.
Else we will store the min of ans and high and do high = mid - 1.
"""