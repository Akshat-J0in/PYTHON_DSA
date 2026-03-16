# Problem Statement:
"""You are given a sorted array of integers and a target, your task is to search for the target in the array. Assume the given array
does not contain any duplicate elements.
For example:
arr = [3,4,6,7,9,12,16,17], target = 6
Output = 3
"""



# Approach 1:
# def binary_search(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = (low+high)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
#
# nums = [3,4,6,7,9,12,16,17]
# target = 6
# print(binary_search(nums,target)+1)
"""This is a traditional binary search approach where i have run a while loop till our start is less than end.
Inside the loop, i have set the mid value that is by adding the start and end and dividing it by 2.
Then we will check if the mid is equal to the target or not if yes then return the index.
If the target is greater than mid then we set the start to index mid +1.
If the target is less than mid then we set the start to index mid -1.
and repeat this process again until we find the index.
"""



# Approach 2:
def binary_search(arr,low,high,value):
    if low > high:
        return -1
    mid = (low+high)//2

    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return binary_search(arr,low,mid-1,value)
    elif arr[mid] < value:
        return binary_search(arr,mid+1,high,value)
    return None


nums = [3,4,6,7,9,12,16,17]
target = 6
result = binary_search(nums,0,len(nums)-1, target)
print(result+1)
"""Here we do the same thing just the thing is that we are using the recursive approach rest the logic will remain the same.
"""