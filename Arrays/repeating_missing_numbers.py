# Problem Statement:
"""Given an integer array nums of size n containing values from [1,n] and each appears only once in the array except for a which appears twice and b which is missong.
Return the value of a and b
for example:
nums = [3,5,4,1,1]
output: [1,2]
"""



# Approach 1:
# arr = [3,5,4,1,1]
# n = len(arr)
# repeating = -1
# missing = -1
#
# for i in range(1,n+1):
#     count = arr.count(i)
#
#     if count == 2:
#         repeating = i
#
#     elif count == 0:
#         missing = i
# print(f"missing: {missing}, repeating: {repeating}")
"""This is a brute force approach where i have first run a loop from 1 to the length of the array.
Then i have found count of each value in the array, if count is 2 then the value is repeating and if it is zero then it is missing.
Here the time complexity is: O(n^2) because of the for loop and the nested inbuilt count function.
"""



# Approach 2:
# arr = [3,5,4,1,1]
# n = len(arr)
# repeating = -1
# missing = -1
#
# freq = [0]*(n+1)
#
# for num in arr:
#     freq[num] += 1
#
# for i in range(1,n+1):
#     if freq[i] >=2:
#         repeating = i
#     elif freq[i] == 0:
#         missing = i
#
# print(f"missing: {missing}, repeating: {repeating}")
"""In this approach, i have created a array where first i have set all its value to zero.
Then i have created a for loop where i will increment the freq by 1
once our array is ready, we will use another for loop where if the value is greater than 2 then its repeating and if its 0 then its missing.
"""



# Approach 3:
nums = [3,5,4,1,1]
n = len(nums)

s = n*(n+1)//2
s2 = n*(n+1)*(2*n+1)//6

actual_sum = sum(nums)
sqr_sum = sum(x*x for x in nums)

val1 = s - actual_sum
val2 = s2 - sqr_sum

val2 = val2 // val1

missing = (val2 + val1)//2
repeating = missing - val1

print(f"missing = {missing}, repeating = {repeating}")
"""This is the most optimal approach where i have used the concept of maths.
Here the formula for sum of n number is s and the difference between the sum of n number and sum of actual number in array gives us the repeating element.
Then the formula for sum of square of first n number is s2 and then we take the difference of s2 and the actual square sum is val2.
"""