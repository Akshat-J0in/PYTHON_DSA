# Problem Statement:
"""Given an array of only 0,1,2. Sort the array in non-decreasing order.
For example:
Input:  given the array [1,0,2,1,0]
Output: [0,0,1,1,2]
"""



# Approach 1:
arr = [1,0,2,1,0]
# sorted_arr = sorted(arr)
# print(sorted_arr)
"""Here we have used the simple built in sorted function of python to sort the array."""



# Approach 2:
# swapped = False
# for i in range(len(arr)):
#     for j in range(0,len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#             swapped = True
#         if not swapped:
#             break
# print(arr)
"""Here we have used the bubble sort approach."""



# Approach 3:
# c0 = arr.count(0)
# c1 = arr.count(1)
# c2 = arr.count(2)
# arr = [0]*c0 + [1]*c1 + [2]*c2
# print(arr)
"""Again this is also a optimal approach where we are using the count function of the python and then multipying it with the values so that we append it accordingly.
"""



# Approach 4:
low = mid = 0
high = len(arr)-1
while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[high], arr[mid] = arr[mid], arr[high]
        high -= 1
print(arr)
"""This is the most optimal approach and this approach is called as dutch flag approach.
Here we have 3 variable low, mid which is set to index 0 and high which is set to the last index of the array.
Now here we run a loop till the condition mid <= high is true.
Inside the while loop, we have 3 condition.
First where If we have 0 in the index where we have mid then we swap the low and the mid and increment both by 1.
If this condition is not satisfied then we check the second condition where of position  mid has the value 1.
If yes then we increment only the mid.
If both the above condition is false then we can say that mid has the value 2 so we swap that with the high and decrement the high index.
"""