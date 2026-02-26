# Problem Statement:
"""Given an array with positive and negative integers, find the longest subarray with sum zero.
For example:
N = 6, array[] = {9,-3,3,-1,6,-5}
output: 5
"""



# Approach 1:
arr = [9,-3,3,-1,6,-5]

# n = len(arr)
# max_len = 0
#
# for i in range(n):
#     total = 0
#     for j in range(i,n):
#         total += arr[j]
#         if total == 0:
#             length = j - i + 1
#             max_len = max(max_len, length)
# print(max_len)
"""This approach is a brute force approach to find the longest subarray with sum zero
Here first i have run a for loop that will run till the end of the array.
here first i have made a total variable that will be zero at the start.
Then i have made a nested loop that will run from i to the end of the array.
Here i have added the value of arr[j] in the total and then checked a condition if the total == 0.
If yes then i have made a length variable where it will have the value j - i + 1
Then i have checked the max of max_length and the length.
Once we are out of both the loop, print the max_len.
"""



# Approach 2:
prefix_sum = 0
max_len = 0
first_occurence = {}

for i in range(len(arr)):
    prefix_sum += arr[i]
    if prefix_sum == 0:
        max_len = i+1

    if prefix_sum in first_occurence:
        length = i - first_occurence[prefix_sum]
        max_len = max(max_len, length)
    else:
        first_occurence[prefix_sum] = i

print(max_len)
"""This is the most optimal approach to find the longest subarray with sum zero.
Here first i have initialized prefix_sum, max_len to zero and the first_occurence to the empty dictionary.
then i have run a loop that is till the end of the array.
first i have added the arr[i] in the prefix_sum.
Then first i have checked if the sum == 0.
If yes then we increment the max_len by i + 1
Then we check if the first occurence is in the prefix_sum.
If not then we put it in the dictionary.
If it is there then we create a length variable where we will have i - first_occurence[prefix_sum]
and then we will find the max_length by finding the max of max_len and length.
"""