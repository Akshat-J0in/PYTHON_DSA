# Problem Statement:
"""Given an array of size n, write a program to check if the given array is sorted in ascending order or not. If sorted then return true else return false.
For example:
Input: N = 5, array[] = {1,2,3,4,5}
Output: true

Input: N = 5, array[] = {5,4,6,7,8}
Output: false"""



# Approach 1:
# arr = list(map(int, input().split()))
# is_sorted = True
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] > arr[j]:
#             is_sorted = False
#             break
#
# if is_sorted:
#     print("The array is sorted.")
# else:
#     print("The array is not sorted.")
"""Here in this approach, after taking the user input, i have run a loop from first element to the last element of the array.
Then we run another loop which will run from the element we are on the first loop till the end of the array.
Inside the second loop, we have set a condition where if the element of the first loop is greater than the remaining element of the array that is on the right hand side then we make the variable is_sorted false and come out of the loop.
then if the variable is false after going through the entire loop then the array is not sorted. else its sorted."""



# Approach 2:
# arr = list(map(int, input().split()))
# is_sorted = True
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         is_sorted = False
#         break
# if is_sorted:
#     print("The array is sorted.")
# else:
#     print("The array is not sorted.")
"""Here we are using more optimized approach where we have created a single loop only and we are running it from the first element to second last element.
Here we are checking the adjecent elements. If the element just next to the element is greater than the previous one then is_sorted becomes false and we come out of the loop.
Same as above if is_sorted becomes false then the array is not sorted else it is sorted.
"""



# Approach 3:
# arr = list(map(int, input().split()))
#
# if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
#     print("array is sorted")
# else:
#     print("array is not sorted")
"""Here I have used the inbuilt all function. Where we check that if all the adjecent element are greater than or equal to the previous element by running through the array.
If yes the array is sorted else it is not sorted."""



# Approach 4:
# arr = list(map(int, input().split()))
# if arr == sorted(arr):
#     print("Array is sorted")
# else:
#     print("Array is not sorted")
"""Now this is a interesting and straight forward approach where we have used the inbuilt sorted function to check if the the user array is equal to the sorted array or not.
If yes then the array is sorted else it is not sorted."""



# Approach 5:
arr = list(map(int, input().split()))
if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
    print("Array is not sorted.")
else:
    print("Array is sorted.")
"""Here this is the alternative to the all function. Here we have used the inbuilt any function.
Here we are checking that if any adjecent element is smaller than the previous element then the array is not sorted else it is sorted."""