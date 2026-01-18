"""Given an integer array nums, rotate the array to the left by one.
For example:
Input: [1,2,3,4,5]
output: [2,3,4,5,1]"""



# Approach 1:
# arr = list(map(int, input().split()))
# index = 0
# val = arr[0]
# for point in range(1,len(arr)):
#     arr[index] = arr[point]
#     index += 1
#
# arr[len(arr)-1] = val
# print(arr)
"""Here i have first taken the user input.
Then i have made a variable index as 0 so that it holds the first position of the array.
Then we store the first value of the array.
Then we run the loop from 1 to length of the array. That is if the array is [1,2,3,4,5] then the length of the array is 5 and we run the loop from 1 to length so here the number will be 1,2,3,4
Then inside the loop, we left shift the value till arr-1. that is we have last place of the array left and the first element of the array is still left.
So here we insert the first value of the array to the last. hence we left shift the array by 1."""


# Approach 2:
# arr = list(map(int, input().split()))
# temp = arr[0]
# for i in range(len(arr)-1):
#     arr[i] = arr[i+1]
# arr[-1] = temp
# print(arr)
"""Here we have used the same method as that of approach 1 but here i have not used any extra space by creating any extra variable."""



# Approach 3:
# arr = list(map(int, input().split()))
# arr = arr[1:] + arr[:1]
# print(arr)
"""Here I have used the concept of the slicing. Here i have first used the values of the array from index 1 to the last then i have appended the first value in the last."""


# Approach 4:
from collections import deque
arr = deque(map(int, input().split()))
arr.rotate(-1)
print(list(arr))
"""Here i have used the deque library where i have taken the deque input the used the builtin rotate() function of the deque where i have rotated the array to the left using -1.
arr.rotate(k). if k>0 then the array rotates to the right. If k < 0 then the array rotates to the left."""