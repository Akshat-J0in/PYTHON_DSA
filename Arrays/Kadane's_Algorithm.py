# Problem Statement:
"""Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in the subarray.
For example:
Input: arr = [2,3,5,-2,7,4]
Output: 15
"""



# Kadane's Algorithm
arr = [2,3,5,-2,7,-4]
curr_sum = arr[0]
max_sum = arr[0]

for nums in arr[1:]:
    curr_sum = max(nums, curr_sum + nums)
    max_sum = max(curr_sum, max_sum)

print(max_sum)
"""Here i have used the Kadane's Algorithm to find the subarray with the largest sum.
This algorithm is efficient used to find the maximum sum of the contiguous subarray within a 1D array of numbers
Here i have created 2 variables curr_sum and max_sum where the initial value will be index of 0 that is 2 in the case above.
Then i have run a loop from index 1 to n-1 of the array.
Inside the loop, first for the curr_sum, i have found the max of the index at which we are in the loop and the sum of num + the initial value.
Once we get the curr_max, we find the max for max_sum.
Here we compare the max of current_sum and the max sum. and see which one is greater.
Once the loop is completed for all the elements, we come out of it and print the max_sum which will give the sum of the subarray.
"""