# Problem Statement:
"""Given an integer array nums, sorted in ascending order, and target value K. the array is rotated at some pivot point that is unknown.
Find the index at which k is present and if k is not present return -1.
For example:
arr = [4,5,6,7,0,1,2], k=0
Output: 4
"""



def rotated_array_search(input_list, target):
    low,high = 0, len(input_list)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1

arr = [4,5,6,7,0,1,2]
target = 0

print(rotated_array_search(arr, target))
"""
Over hare we have a rotated array so the initial steps will be same but now, we will first check in the left sorted half.
That is if arr[low] <= arr[mid] or not. If yes then,
we will create second condition where we will check if arr[low] <= target < arr[mid] if yes then we will do high = mid - 1. Else low = mid + 1
now we will check the second half of the sorted array. Here if the arr[mid] < target <= arr[high] then we do low = mid + 1 else we do high = mid - 1.
Once we are out off loop and still did not get the value, we return -1.
"""