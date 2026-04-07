#Problem Statement:
"""
You are given a positive integer n. Your task is to find and return its square root. If 'n' is not a perfect square then return
the floor value of sqrt(n)
For example:
Input: N = 36
Output: 6
"""



def sqrt_binary(n):
    low = 1
    high = n
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid*mid == n:
            return mid

        elif mid*mid < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

print(sqrt_binary(36))
"""Here this is a classic binary search on the answer problem.
Over here i have found the mid then set a case where if mid square is same as ans then we will return the mid.
else if mid square is less than n then we store that in the ans and then do increment low by mid + 1
else we decrement the high by mid - 1.
Once we are out of the loop, we return the ans and print it.
"""