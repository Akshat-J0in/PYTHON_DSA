# Problem Statement:
"""
Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M.
if the 'nth root is not an integer, return -1
"""


def nth_root(n,m):
    low,high = 1,m
    while low <= high:
        mid = (low + high) // 2

        ans = 1
        for _ in range(n):
            ans = ans * mid
            if ans > m:
                break
        if ans == m:
            return mid
        elif ans < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1
n = 3
m = 27

print(nth_root(n,m))
"""
this is a simple approach somewhat similar to the square root of the number problem.
Here the only thing is we are finding the root of x^n instead of square root using the for loop and store it in the ans variable.
then rest of the condition remain the same that is if ans == m, ans <m and ans > m
So accordingly we return the result that is if we found the ans matches M, return the mid else return -1.
"""