# Problem Statement:
"""Given an array of numbers, you need to return the count of reverse pairs. Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j]
For Example:
arr = [1,3,2,3,1]
Output: 2
"""



# Approach 1:
# arr = [1,3,2,3,1]
# count = 0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] > 2*arr[j]:
#             count+=1
#
# print(count)



# Approach 2:
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def countPairs(arr, low, mid, high):
    count = 0
    right = mid + 1

    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        count += (right - (mid + 1))

    return count


def mergeSort(arr, low, high):
    count = 0

    if low >= high:
        return count

    mid = (low + high) // 2

    count += mergeSort(arr, low, mid)
    count += mergeSort(arr, mid + 1, high)
    count += countPairs(arr, low, mid, high)

    merge(arr, low, mid, high)

    return count


arr = [1, 3, 2, 3, 1]
print(mergeSort(arr, 0, len(arr) - 1))