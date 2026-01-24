# Problem Statement:
"""Given an integer N and an array of size N-1 containing N-1 number between 1 to N.
Find the number that is not present in the array.
For example:
Input: N = 5, array[] = {1,2,4,5}
Output: 3"""



# Approach 1:
n = 5
arr = [1,2,4,5]
# for i in range(1,n+1):
#     if i not in arr:
#         print(i)
#         break
"""Here in this approach, i have used the loops and the in keyword.
Here first we run the loop till the number of values that should be present in the array.
Then we compare if that value is present in the array or not.
If not then we print that value and come out of the loop.
Here the complexity is O(n^2)"""



# Approach 2:
# total_arr = sum(arr)
# total_ans = n*(n+1)//2
# missing_value = total_ans - total_arr
# print(missing_value)
"""Here this is the most optimal approach present.
Here we take the sum of the array and find the sum of first n numbers that should be present in the array.
Then we subtract the sum of number in array with the number that should be present in the array.
"""



# Approach 3:
missing = set(range(1,n-1))-set(arr)
print(missing.pop())
"""Here we have used the concept of the sets where we make one set from the number that should be present in the array.
and we convert the array into the set then subtract it to find the missing value.
Once we get that only value in the set, we pop out that value from the set."""