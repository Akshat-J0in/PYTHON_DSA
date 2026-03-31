# Problem Statement:
"""Given an array arr of size N, sorted in ascending order and a target value K. Now the array is rotated at same pivot point unknown to you.
Return true if k is present and otherwise return false.
For example:
arr = [7,8,1,2,3,3,3,4,5,6], k = 3
Output = True
"""


def element_rotated_array(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False



arr = [7,8,1,2,3,3,3,4,5,6]
target = 10
print(element_rotated_array(arr, target))
"""This is the same code as that od element_rotated_array one we are just returning over here true or false."""