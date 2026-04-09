def mineatingbananaspeed(arr, target):
    left = 1
    right = max(arr)
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        hours = 0
        for values in arr:
            hours += (values + mid - 1) // mid

        if hours <= target:
            ans = mid
            right = mid -1

        else:
            left = mid + 1
    return ans

arr = [7,15,6,3]
target = 8
print(mineatingbananaspeed(arr, target))