# Problem Statement:
"""A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days
"""



def no_of_days(days, mid, array):
    cal_days = 1  # start with day 1
    threshold_sum = 0

    for values in array:
        if threshold_sum + values <= mid:
            threshold_sum += values
        else:
            cal_days += 1
            threshold_sum = values

    return cal_days <= days


def ans(arr, days):
    low = max(arr)
    high = sum(arr)
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if no_of_days(days, mid, arr):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
print(ans(arr, d))
"""
If you notice the pattern is similar to koko eating banana, minimum days to make n bouquets and find the smallest divisor
I will leave this up to you to understand as a revision.
"""