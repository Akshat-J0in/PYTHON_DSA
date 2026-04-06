# Problem Statement:
"""Given array of length N, peak element is defined as the element greater than both of its neighbours. Formally, if arr[i] is the peak
element, arr[i+1]<arr[i] and arr[i-1] < arr[i]. Find the index of a peak element in the array. If there are multiple peak numbers return
the index of any peak number.
"""


arr = [1,2,3,4,5,6,7,8,5,1]
low = 0
high = len(arr)-1

while low < high:

    mid = (low+high)//2

    if arr[mid] <= arr[mid+1]:
        low = mid + 1
    else:
        high = mid

print(low)
"""
Here this is a very simple code where we have made a small change in the logic where we check the neighbour element in the array
to find the peak element. If arr[mid] is less than its neighbour then we increment the low by mid + 1 else we make our high as mid.
"""