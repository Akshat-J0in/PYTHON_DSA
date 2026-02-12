# Problem Statement:
"""Given an array of integers, return the length if the longest consecutive integers. The integers in this sequence can appear in any order.
Example:
Input: arr = [100,4,200,1,3,2]
Output: 4
"""



# Approach 1:
nums = [1,2,3,101,102,103,104]
# current = 0
# length = 0
# longest = 0
# set_arr = set(nums)
# for num in set_arr:
#     if num - 1 not in set_arr:
#         current = num
#         length = 1
#     while current+1 in set_arr:
#         length += 1
#         current += 1
#     longest = max(length, longest)
# print(longest)
"""This is the optimal where we first make the array into set.
Then we set some variables like longest = current = length = 0
Then we run a loop till the end of the array.
Here the first condition inside the array is that if the num - 1 value is not in the set then that means that we need to start counting from there that is that value is the starting point.
Here we make the current element = num and make the length = 1
Then we run a while loop where where we set a condtion that if the current+1 element is there in the set then we increment the length by 1 and current by 1
and we continue while loop till we have the curr+1 element in the set.
Once we are out of the loop, we find the max between the longest and the length and store that value in the longest and print it.
"""



# Approach 2:
# longest = 0
# for num in nums:
#     count = 1
#     current = num
#     while current+1 in nums:
#         count += 1
#         current+=1
#     longest = max(count, longest)
# print(longest)
"""This is the brute force solution
Where first i run a loop covering all the element in the array then i make the count = 1 and assign the current to the value that we have in the first loop.
Then we run the while loop till will have the curr+1 element in the loop where we increment the count by 1 and increment the current by 1.
Then find the longest and print it.
"""



# Approach 3:
nums.sort()
longest = 1
current = 1
for i in range(1,len(nums)):
    if nums[i] == nums[i-1]+1:
        current += 1
    else:
        longest = max(longest, current)
        current = 1
longest = max(longest, current)
print(longest)
"""Here i have used the sorting approach.
We first run a loop from index 1 to the last index of the array.
Then i have set 2 condition where if the num[i] == num[i-1]+1 then its a consicutive element and we increment the current by 1.
if not then we will break the sequence by finding the max of the longest and the current variable.
and then print it once the loop is over."""