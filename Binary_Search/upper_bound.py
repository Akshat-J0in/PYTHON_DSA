# Problem Statement:
"""given an sorted array of N integer x, write a program to find the upper bound of x.
For example:
arr = [3,5,8,9,15,19], x = 9
Output: 4
"""



# Approach 1:
def upper_bound(val,target):
    low = 0
    high = len(val)-1
    ans = len(val)
    while low <= high:
        mid = (low+high)//2
        if val[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [3,5,8,9,15,19]
x = 9
print(upper_bound(arr,x))
"""Here i have first set the high, low and the ans variable then i have run a while loop.
Here in the while loop, I have first calculated the mid value.
Then i have checked the if condition that is if val[mid] is greater than target
then we set the ans to mid and decrement the high by mid - 1
then in the else condition, i have set the low as mid + 1
Once we are out of loop, we return the ans.
"""