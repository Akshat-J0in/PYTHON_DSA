def max_water_stored(arr):
    max_area = 0
    left = 0
    right = len(arr) - 1
    while left < right:
        width = right - left
        h = min(arr[left], arr[right])
        area = h * width

        max_area = max(max_area, area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area

arr = [1,8,6,2,5,4,8,3,7]
print(max_water_stored(arr))