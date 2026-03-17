# Problem Statement:
"""Given an sorted array of n integers and an integer x, write a code to find the lower bound x.
For example:
arr = [3,5,8,15,19] x = 9
output: 3
"""



# Approach 1:
def lower_bound(arr,x):
    low = 0
    high = len(arr)-1
    ans = len(arr)

    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid + 1
    return ans

arr = [3,5,8,15,19]
x = 9
print(lower_bound(arr,x))
"""Here we have to use the binary search approach where first i have defined the start, end then i have used the while loop.
Here in the while loop, first we set the mid value then we check if the mid is greater then the x or not if yes then we assign the mid to ans and then
make the high to mid-1.
Else we make the low to mid + 1
Once we are done with the loop, we return the ans and print it.
"""