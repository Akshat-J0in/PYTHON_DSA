# Problem Statement:
"""Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
For example:
Input: [1,1,0,1,1,1]
Output: 3"""



# Approach 1:
arr = [1,1,0,1,1,1]
total = 0
count = 0
# for i in arr:
#     if i == 0:
#         total = max(total, count)
#         count = 0
#     else:
#         count += 1
#     # print(arr[i])
# total = max(total, count)
# print(total)
"""Here in this approach, i have first used a for loop to iterate through the array.
Then inside the loop, i have used the condition where if i == 0 then we find the maximum of the count and the total. If the previous total is greater than the current count then we discard the count else visa vera.
Then we have the else condition where if the value is 1 then we increment the count.
Then after coming out of the loop we again check the condition because if the 1 are at the last, we will not be able to find the max of them in the loop itself.
"""



# Approach 2:
# for i in arr:
#     if i == 1:
#         count += 1
#         total = max(total, count)
#     else:
#         count = 0
# print(total)
"""Here this is more optimized approach then the above.
Here we check the maximum inside the if condition where i == 1 instead of i == 0 so that we are checking the max for all i = 1 unlike the above code.
rest all is same."""



# Approach 3:
# s = ''.join(map(str, arr))
# print(max(len(x) for x in s.split('0')))
"""Here first we are converting the list of array into string using the map.
that is from [1,1,0,1,1,1] to ['1','1','0','1','1','1']
Then we are joining them without any seperator ['110111']
Once that is done, we are then finding the max length of the 1's by sepearating them using the split function.
so we will get max(len(1,1),len(1,1,1))."""


from itertools import groupby
max_ones = 0
for key,group in groupby(arr):
    if key == 1:
        max_ones = max(max_ones,len(list(group)))

print(max_ones)
"""Here we are using the groupby sublibrary. Where we are iterating through the loop. with key and values.
Here key when it is 1, we find the max of the length of 1's by first converting the tuple into the list.
Please use chat gpt for more clear understanding for this approach as i was unable to explain this to you clearly.
"""