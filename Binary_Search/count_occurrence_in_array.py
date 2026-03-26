# Problem Statement:
"""You are given a sorted array containing N integers and a number x, you have to find the occurrence of x in the given array."""



# Approach 1:
# def first_occ(arr, target):
#     low = 0
#     high = len(arr) - 1
#     ans = -1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             ans = mid
#             high = mid - 1
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans
#
# def second_occ(arr, target):
#     low = 0
#     high = len(arr) - 1
#     ans = -1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             ans = mid
#             low = mid + 1
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return ans
#
# def final_count(arr, target):
#     first = first_occ(arr, target)
#     if first == -1:
#         return 0
#     last = second_occ(arr, target)
#
#     return last - first + 1
#
# arr = [2,2,3,3,3,3,4]
# target = 3
# print(final_count(arr, target))
"""this is a binary search approach.
At first the code looks lengthy but it is simple.
Here we have mainly used the idea of last occurrence - first occurrence + 1
Here first we have found the first occ that is when we get mid == targe, we make our high as mid - 1.
So with this we will get the first occur.
For the final occur, when we get the mid == target, we make the low as low + 1.
And then in the final count function we use the idea of final occur - first occur + 1.
"""



# Approach 2:
arr = [2,2,3,3,3,3,4]
target = 3
count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count += 1
print(count)
"""This is the linear search approach. Its very simple to understand."""