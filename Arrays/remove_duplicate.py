# Problem Statement:
"""Given an integer array sorted in non decreasing order, remove the duplicate in place such that each unique element appears only once.
For example, given the array [1,2,2,3,3,4,4,5,5], the output will be [1,2,3,4,5]"""



# Approach 1:
# def remove_duplicates(arr):
#     if not arr:
#         return 0
#
#     i = 0
#     for j in range(len(arr)):
#         if arr[j] != arr[i]:
#             i+=1
#             arr[i] = arr[j]
#
#     return i+1
#
# arr = list(map(int, input().split()))
# new_len = remove_duplicates(arr)
# print("New length is: ", new_len)
# print(arr[:new_len])
"""Here we are using the concept of pointers.
First we take the user input, then we are using a function to remove the duplicates.
Here in the function first we have created a base condition that if there are no number in the array then return 0.
Else we create a variable i that will hold index 0 at start.the we run a loop.
Here in the loop, we check the condition that if arr[i] if it is not equal to arr[j] that means that it is a unique element.
If so then we increment the value of i and place that new value in place of the duplicate.
once we iterate through the loop, we return the index i+1 that is we have unique elements till index i and rest of the index is junk value.
"""
"""------------------------------------- Not in-place approach -----------------------------------------------------------"""



#Approach 2:
# arr = list(map(int, input().split()))
# new_arr = list(set(arr))
# print(new_arr)
"""Here it very simple to understand, we are using the property of the sets that is no duplicate are present in the set.
So we take the user input then convert into the set so that the duplicate are removed then we convert it into the list again then print it."""



# Approach 3:
# arr = list(map(int, input().split()))
# new_arr = list(dict.fromkeys(arr))
# print(new_arr)
"""Here we are using the concept of the dictoneray keys. Here after taking the input, we are using the dict.fromkeys() function.
as keys are always unique, we only get the unique elements."""


# Approach 4:
# arr = list(map(int, input().split()))
# unique_arr = []
# [unique_arr.append(x) for x in arr if x not in unique_arr]
# print(unique_arr)
"""Here its a very simple approach, we are using the in keyword.
Here i have created an empty list then i have run a loop, where inside the loop, we will check if the value is present in the empty list or not.
If the value is not present then we append it else we dont."""



# Approach 5:
from itertools import groupby
arr = list(map(int, input().split()))
unique_arr = [k for k,_ in groupby((arr))]
print(unique_arr)
"""Here we are using the group by function.
In this group by function, we get 2 parameters, the value and the iterable.
That is if we have array[1,1,2,2,3,3] then after using group by function we get:
1[1,1], 2[2,2], ...
so we want only the first part so we ignore the second part by using '_' then we print the array."""