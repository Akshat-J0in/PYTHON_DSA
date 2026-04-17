"""Problem Statement:
You are given a strictly increasing array and a positive integer. Find the 'kth' positive integer missing from array.
Example: arr = [4,7,9,10] k = 4
Output: 5
"""



def find_missing(arr,k):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return low+k

arr = [4,7,9,10]
k = 4
print(find_missing(arr,k))
