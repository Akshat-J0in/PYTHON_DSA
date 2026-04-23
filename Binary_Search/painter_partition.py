#Problem Statement:
"""
Given an array/list of length ‘N’,
where the array/list represents the boards and each element of the given array/list represents the length of each board.
Some ‘K’ numbers of painters are available to paint these boards.
Consider that each unit of a board takes 1 unit of time to paint.
You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards
under the constraint that any painter will only paint the continuous sections of boards.
"""



def find_total_time(arr,k,mid):
    total_sum = 0
    count = 0
    for val in arr:
        if total_sum + val <= mid:
            total_sum += val
        else:
            count += 1
            total_sum = val
    return count

def find_partition(arr, k):
    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low + high) // 2

        number_of_painters = find_total_time(arr, k, mid)

        if number_of_painters > k:
            low = mid + 1
        else:
            high = mid - 1
    return low


arr = [10,20,30,40,50]
k = 2
print(find_partition(arr, k))