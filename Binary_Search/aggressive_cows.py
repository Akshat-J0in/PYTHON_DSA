# Problem Statement:
"""You are given an arr of size n which denotes the position of stalls. You are also given an integer k which denotes the number of
aggressive cows. you are given a task if assigning stalls to k cows such that the minimum distance between any 2 of them is the maximum possible
Find the maximum possible minimum distance.
"""



def can_place(arr,k,mid):
    count = 1
    last = arr[0]
    for i in range(1,len(arr)):
        if arr[i] - last >= mid:
            count+=1
            last = arr[i]
        if count == k:
            return True
    return False


def final_position(arr,k):
    arr.sort()
    low = 1
    high = arr[-1] - arr[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place(arr,k,mid):
            ans = mid
            low = mid + 1

        else:
            high = mid - 1
    return ans

arr = [0,3,4,7,10,9]
k = 4
print(final_position(arr,k))