#Problem Statement:
"""
Problem Statement: You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s.
All the rows are sorted in ascending order. Your task is to find the index of the row with the maximum number of ones.
Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1
"""



def lower_bound(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def num_of_one(arr,m,n):
    cnt_max = 0
    index = -1
    for i in range(n):
        cnt_one = m - lower_bound(arr[i], m, 1)
        if cnt_one > cnt_max:
            cnt_max = cnt_one
            index = i
    return index

arr = [[0,0,0],[0,0,0]]
m = n = 2
print(num_of_one(arr,m,n))