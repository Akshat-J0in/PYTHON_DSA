# Problem Statement:
"""You are given a sorted array of distinct values and a target value x. You need to search for the index of the target value in the array.
Example:
arr[] = {1,2,4,7}, x = 6
output: 3
"""



def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


arr = [1,2,4,7]
x = 2

print(searchInsert(arr,x))
"""This is a very easy to understand code so there is nothing new for me to explain over here."""