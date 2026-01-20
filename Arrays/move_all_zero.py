# Problem Statement:
"""Given an array of integers, we have to move all the zeros in the array to the end of the array and move non negative integers to the front.
Example:
Input: [1,0,2,3,0,4,0,1]
Output: [1,2,3,4,1,0,0,0]
"""



# Approach 1:
# arr = [1,0,2,3,0,4,0,1]
# count = 0
# i = 0
# while i < len(arr):
#     if arr[i] == 0:
#         count += 1
#         arr.pop(i)
#     i+=1
# for i in range(count):
#     arr.append(0)
# print(arr)
"""Here in this approach, i have first created a variable count then i have run a while loop where the loop run till the value if i is less then the length of the array.
Inside the loop, We check the condition where if the element is zero then we pop the element and increment the count.
After this loop, we have removed all the zero from the array and got the count of the zero.
Then we append the zero in the last."""



# Approach 2:
# arr = [1,0,2,3,0,4,0,1]
# zeros = arr.count(0)
# arr = [x for x in arr if x!=0] + [0] * zeros
# print(arr)
"""Here we have first taken the count of the zeros and used the list comprihension.
Here we have first taken the element that are non zero then appended the zero at the last."""



# Approach 3:
arr = [1,0,2,3,0,4,0,1]
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1
for i in range(pos,len(arr)):
    arr[i] = 0

print(arr)
"""This is the 2 pointer approach and this is the best approach.
Here first i have made a variable position which is zero then run a loop where we move the element if value is non zero and increment the position.
then we append the zero in the last."""