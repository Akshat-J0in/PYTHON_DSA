# Problem Statement:
"""Given an array of integer A and B. Find the total number of subarray having bitwise XOR of all element equal to k.
For example:
a = [4,2,2,6,4] k = 6
Output = 6
"""



# Approach 1:
arr = [4,2,2,6,4]
# k = 6
# count = 0
# for i in range(len(arr)):
#     xor = 0
#     for j in range(i,len(arr)):
#         xor ^= arr[j]
#         if xor == k:
#             count +=1
#
# print(count)
"""Here i have used the brute force approach where first i run a loop through the entire array.
Here first i make the variable xor as 0.
Then i have used a nested loop from i to the end of the loop.
Here i first do the xor operation then check if xor == target value then increment the count.
"""



# Approach 2:
k = 6
prefix_sum = 0
freq = {0:1}
count = 0

for num in arr:
    prefix_sum ^= num
    if prefix_sum ^ k in freq:
        count += freq[prefix_sum ^ k]
    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
print(count)
"""this is the most optimal approach where i have used the hash map approach.
Here i have set the dictionary with one element that is 0 with value as 1
then i have run a loop where first i do the xor operation then i have set a condition if prefix_sum ^ k is in the dictionary then we increment the count by the value that the key has in the dictionary.
Then we increment the key in the dictionary by 1
"""