# Problem Statement:
"""
You are given an array of integer arr and an integer that is the threshold value limit. Your task is to find the smallest positive
integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division result is less than or equal to
the given threshold value.
For example:
arr = [1,2,3,4,5], limit = 8
Output: 3
"""



import math

def smaller_value_than_threshold(arr, target,mid):
    sum = 0
    for num in arr:
        sum += math.ceil(num/mid)
    return sum <= target

def smallest_divisor(arr, target):
    left = 1
    right = max(arr)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if smaller_value_than_threshold(arr,target,mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
arr = [8,4,2,3]
limit = 10
print(smallest_divisor(arr,limit))
"""
Here i have set the low and high as 1 and max value of the array. then i found the mid of the value.
Once that is done, i have set a condition where if the sum of the divisor that is ceil of the sum of number divided by mid is
less than or equal to the target then we save it in the ans and make the high as mid -1 as we need to find the minimum value.
If the given sum is greater than the target, we do low as mid + 1
"""