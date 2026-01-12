# Problem Statement:
"""Given an array, we have to find the largest element in the array.
for example:
input: arr[] = {2,5,1,3,6}
output: 6"""



# Approach 1:
# arr = list(map(int, input().split()))
# maximum = max(arr)
# print(f"Largest value is: {maximum}")
"""Here i have simply used the inbuilt max function where it gives us the largest element from the array."""



# Approach 2
# def recursive_bubble(arr,n):
#     if n == 1:
#         return arr
#     for i in range(n-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#
#     return recursive_bubble(arr,n-1)
#
# arr = list(map(int, input().split()))
# sorted_arr = recursive_bubble(arr,len(arr))
# print(sorted_arr)
# maximum = sorted_arr[-1]
# print(f"Largest value is: {maximum}")
"""Here i have first used the recursive bubble sort method to sort the array. You can use other sorting methods as well as shown in the 'sorting' directory.
Here the array is sorted in the ascending order. then i take the last element from the array which will be the largest element after sorting.
To access the last element of the array, we use [-1] index."""



# Approach 3
# arr = list(map(int, input().split()))
# maximum = arr[0]
# for i in range(1, len(arr)):
#     if maximum < arr[i]:
#         maximum = arr[i]
# print(f"Largest value is: {maximum}")
"""This is the most simple approach to find the largest element in the given array.
Here i have taken the input for the array then i have made the initial largest element as the first element in the array.
Then i have run the loop from the second element to the last element.
Here inside the loop, i have set a condition where if the largest element is smaller than array element then we make the array element as the largest element and we continue till the all element are iterated.
"""



# Approach 4:
# from functools import reduce
# arr = list(map(int, input().split()))
# largest = reduce(lambda a,b: a if a > b else b, arr)
# print(largest)
"""Here i have used a functool library to access the reduce sub library.
Here first i have taken the input for the array then i have made a reduce function call.
Here in the reduce function, there are 2 parameter that is the condition and the other is iterable part.
so here i have made a lambda function where if the first element is greater than the second then we return the first element else the second.
This will continue till we complete the iteration of the entire array."""



# Approach 5:
# def largest_element(arr,l,r):
#     if l == r:
#         return arr[l]
#
#     mid = (l+r)//2
#     return max(largest_element(arr,l,mid),largest_element(arr,mid+1,r))
#
# arr = list(map(int, input().split()))
# print("Largest:", largest_element(arr, 0, len(arr) - 1))
"""Here i have used the divide and conquer approach to find the largest element in the given array.
Here i have set the base condition that if l == r then we return the arr[l] value.
Then i have made a mid variable where we find the mid index for the array.
after finding the mid, we have divided the array into 2. that is the left hand side and the right hand side.
in the left hand side, we have element from start index to the mid index.
in the right hand side, we have element from mid+1 to last index.
and we make a recursive call till the array as 1 element only. After that we find the maximum element."""



# Approach 6:
arr = list(map(int, input().split()))
print(sorted(arr, reverse=True)[0])
"""Here again i have used the inbuilt sorted function.
Here the sorted function sorts the element in the ascending order.
But here i have used the reverse condition = true which helps is converting the element into descending order.
After that the largest element is in the first index.
So here we access the first element using the [0] index and print it."""