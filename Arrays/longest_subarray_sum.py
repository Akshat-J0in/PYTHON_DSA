# Problem Statement:
"""Given an array nums of size n and integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists return 0.
For example,
given nums = [10,5,2,7,1,9], and k = 15
Output: 3
given nums = [-3,2,1], k = 6
Output: 0
"""



# Approach 1:
# arr = [1, 2, 3, 1, 1, 1]
# k = 3
#
# sub_arr = 0
# for i in range(len(arr)):
#     count = 1
#     total = arr[i]
#     for j in range(i+1,len(arr)):
#         total += arr[j]
#         count +=1
#         if total == k:
#             sub_arr = max(sub_arr,count)
#         elif total > k:
#             break
#
# print(sub_arr)
"""Here i have used the nested loop approach where first i have run the loop through the entire array
Then i have made the count = 1 and the total = the current value where the loop is pointing to the index.
Then i have made another loop where it will run from the current index of i to the last value of the loop.
Inside the second loop, i have added the value with the total and incremented the count.
Then i am checking the condition where if the total is equal to the given value.
If yes then we take the max number between the count and the sub_array.
If the total is greater than the given value, then we do break and come out of the second loop.
"""



# Approach 2:
arr = [10,5,2,7,1,9]
k = 15
left = 0
total = 0
max_length = 0

for right in range(len(arr)):
    total += arr[right]

    while total > k:
        total -= arr[left]
        left += 1

    if total == k:
        max_length = max(max_length, right - left + 1)

print(max_length)
"""This is the most optimal approach and it is called a sliding window approach.
Here i have set the left, total, max_length as 0.
Then i have run a loop through the entire array.
Here first i am taking the total of the value.
Then i have run a while loop where we see if the total is greater than the given value.
If yes then we decrement the total by the arr[left] and we increment the left value.
And if the total is equal to the given value, then we find the max of max_length and right - left +1.
I know the explanation for this code is not that good. What i suggest is first see some video of how sliding window work then you can understand this code properly.
"""