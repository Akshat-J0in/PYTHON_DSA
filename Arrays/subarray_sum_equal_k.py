# Problem Statement:
"""Given an array of integer and an integer k, return the total number of subarray whose sum is equal to k.
For example:
input: N = 4, array[] = {3,1,2,4}, K = 6
Output: 2
"""



# arr = [3,1,2,4]
# k = 6
# count = 0
# for i in range(len(arr)):
#     total = 0
#     for j in range(i,len(arr)):
#         total += arr[j]
#         if total == k:
#             count += 1
# print(count)
"""This is the brute force approach and quit easy to understand.
"""



arr = [3,1,2,4]
count = 0
k = 6
prefix_sum = 0
freq = {0:1}

for num in arr:
    prefix_sum += num

    if prefix_sum-k in freq:
        count += freq[prefix_sum-k]
    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
print(count)
"""This is the most optimal approach where i have used the concept of current_sum - K = previous_sum.
Here first we create a prefix sum and set it to zero.
Then i have made a dictionary where we have set the value 0 appearing 1 time.
Then i have run a loop iterating over all the elements.
inside the loop, first i have set prefix_sum to the value of the array.
Then i have set a condition where if the prefix_sum - k is present in the dictionary then we increment the count by the times when the value prefix-K value appear in the dictionary.
then outside the if condition, increment the prefix_sum by 1. and if the prefix_sum is not in the dictionary then  we append it in the dictionary.
"""