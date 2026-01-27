# Problem Statement:
"""Given an non empty array, every element appears twice except for one. Find that single element.
For example:
Input: arr[2,2,1]
Output: 1"""



# Approach 1:
arr = [4,1,2,1,2]
# freq = {}
# for x in arr:
#     freq[x] = freq.get(x, 0) + 1
#
# for keys,value in freq.items():
#     if value == 1:
#         print(keys)
"""Here we have used the Dictionary approach.
Here first we have converted the array into the dictionary then we used the loop to see which key has its corresponding value as 1.
Then print that key value."""



# Approach 2:
# res = 0
# for x in arr:
#     res ^= x
#
# print(res)
"""Here this is the best approach where we have used the logic of xor.
Here we have created the res variable where its initial value will be zero. then we xor it with all the element of the array to find the unique element.
"""



# Approach 3:
for x in set(arr):
    if arr.count(x) == 1:
        print(x)
"""This is not a optimal approach but yes we can do this code in such way as well where we have first removed all the duplicate value from the array by making it as set.
Then we check a condition where if the count of the value is 1 then we print the value else we dont."""