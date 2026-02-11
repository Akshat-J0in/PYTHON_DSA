# Problem Statement:
"""Given an array, find the leaders in the array such that the value in the right side of the array must be smaller than the target index.
For example:
arr = [10,22,12,3,0,6]
Output: [22,12,6]
Here 6 is the leader as there is no element present in the right side.
Then 12 is the leader as 3,0,6 are smaller than 12
same for 22.
"""


arr = [10,22,12,3,0,6]
leader = []

# for i in range(len(arr)):
#     flag = True
#     for j in range(i+1, len(arr)):
#         if arr[i] < arr[j]:
#             flag = False
#             break
#     if flag:
#         leader.append(arr[i])
#
# print(leader)
"""Here first i have run a loop till the end of the array then i have made a flag variable which will be true at start.
Then i have made a second loop that will run from index of i+1 till the end of the array.
Then inside the loop, i have set a condition where if the arr[i] is less than arr[j], we make the flag variable false and break from the inner loop.
then we check if the flag is true, we append that element in the array and then print it.
"""



# Method 2:
max_number = arr[-1]
leader.append(max_number)
for i in range(len(arr)-2,-1,-1):
    if arr[i] >= max_number:
        leader.append(arr[i])
        max_number = arr[i]
leader.reverse()
print(leader)
"""This is the most optimal way to find the leader in the array.
Here we are first creating a empty leader array, and we set the max number to arr[-1] that is the last element.
Then i have run a reverse loop where i have started from the second last element till the first element.
Inside the loop, i have first checked if the i value is greater than the max number if yes then append it else move ahead.
Then we reverse the array and print it.
"""