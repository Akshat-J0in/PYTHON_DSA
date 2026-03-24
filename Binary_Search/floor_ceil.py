# Problem Statement:
"""Your are given an sorted array of n integers and an integer x. Find the floor and ceil of x in array.
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceil of x is the smallest element in the array which is smaller than or equal to x.
For Example:
arr = [3,4,4,7,8,10], x = 5
Output: 4,7
"""



def floor_ceil(arr, x):
    low = 0
    high = len(arr) - 1
    floor = -1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid],arr[mid]
        elif arr[mid] < x:
            floor = arr[mid]
            low = mid + 1
        else:
            ceil = arr[mid]
            high = mid - 1
    return floor, ceil

arr = [3,4,4,7,8,10]
x = 5
print(floor_ceil(arr,x))
"""Here first i have set 2 variable floor and ceil as -1,-1 then i have run a while loop.
First in the loop, we find out the mid that is by low + high by 2
Then i have made conditional statement that is if arr[mid] is equal to our target variable then we return both floor and ceil as mid.
Else if the arr[mid] is small than x then we return the floor and make the low as mid + 1
else we make the ceil as mid and make high as mid -1.
Once we are out of the loop, we return the floor and the ceil value.
"""