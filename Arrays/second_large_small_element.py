# Problem Statement:
"""Given an array, find the second smallest and second largest element in the array. Print -1 in the event that either of them does not exist
for example:
input: [1,2,4,7,7,5]
output: second smallest: 2 and second largest element: 5
input: [1]
output: -1"""



# Approach 1:
# def selection_sort(array):
#     for i in range(len(array)):
#         min_index = i
#         for j in range(i+1, len(array)):
#             if array[min_index] > array[j]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i]
#     return array
#
# arr = list(map(int, input().split()))
# new_arr = selection_sort(arr)
# unique_arr = []
# for x in new_arr:
#     if not unique_arr or unique_arr[-1] != x:
#         unique_arr.append(x)
#
# if len(unique_arr) <= 3:
#     print(-1)
# else:
#     print(f"The second smallest element is {unique_arr[1]} and the second largest element is {unique_arr[-2]}")
"""Here in this approach, i have used a sorting technique which is selection sort, you can use any technique for sorting.
After the array is sorted, we have to remove the duplicate value from it.
So for that we have created a empty list and then we run a loop till the end of the array.
Inside the loop, we make a condition where we check if the list has the value already or not if not then we append the element in the new list.
once we get the array without duplicate, we print the second largest and the second smallest element in the array.
"""


# Approach 2:
arr = list(map(int, input().split()))
unique_array = sorted(set(arr))
print(unique_array)
if len(unique_array) <= 3:
    print(-1)
else:
     print(f"The second smallest element is {unique_array[1]} and the second largest element is {unique_array[-2]}")

"""This is the most clean and easy code where i have used the property of sets.
In sets, duplicate elements are automatically removed so we dont have to do extra work for it.
for example: we have arr = set([1,1,2,2]) then or arr will be [1,2]. the duplicate 1 and 2 are removed automatically.
so we simply use the set and sort the array using the inbuilt sorted function.
the we print the second smallest and second largest element in the array.
"""