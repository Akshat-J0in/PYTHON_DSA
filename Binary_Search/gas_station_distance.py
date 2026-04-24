# Problem Statement:
"""
You are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis.
You are also given an integer ‘k’. You have to place 'k' new gas stations on the X-axis.
You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions.
Let 'dist' be the maximum value of the distance between adjacent gas stations after adding k new gas stations.
Find the minimum value of ‘dist’.
"""



import math


def can_place(arr,d,k):
    required = 0
    for i in range(len(arr)-1):
        gap = arr[i+1] - arr[i]
        required += math.ceil(gap/d)-1
    return required <= k

def minimize_max_distance(arr,k):
    low = 0
    high = max(arr[i+1] - arr[i] for i in range(len(arr)-1))

    eps = 1e-6

    while high - low > eps:

        mid = (low + high) / 2

        if can_place(arr, mid, k):
            high = mid
        else:
            low = mid
    return high


arr = [1,2,3,4,5,6,7,8,9,10]
k = 4
print(minimize_max_distance(arr,k))

"""This is a difficult problem i would suggest watching a video for this."""