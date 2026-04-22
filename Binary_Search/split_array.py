# Problem Statement:
"""
Given an integer array 'A' of size 'N' and a integer 'K'. split the array A into K non-empty subarrays such that the largest sum of any
subarray is minimized. Your task is to return the minimized largest sum of the split. A subarray is a contiguous part of the array.
For example:
arr = [1,2,3,4,5], k = 3
output = 6
"""



def min_sum_split_arr(arr,mid,k):
    val = 0
    count = 1
    for num in arr:
        if num + val <= mid:
            val += num
        else:
            count += 1
            val = num
    return count
def split_arr(arr,k):
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low+high)//2
        partition = min_sum_split_arr(arr,mid,k)
        if partition > k:
            low = mid + 1
        else:
            high = mid - 1
    return low
arr = [1,2,3,4,5]
k = 3
print(split_arr(arr,k))