# Problem Statement:
"""
Problem Statement: Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the array [i, j]. 
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbours to the left, right, top, and bottom.
Assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
"""
def max_element(arr, col):
    n = len(arr)
    max_val = float('-inf')
    index = -1
    for i in range(n):
        if arr[i][col] > max_val:
            max_val = arr[i][col]
            index = i
    return index

def find_peak_2d(arr):
    n = len(arr)
    m = len(arr[0])

    low = 0
    high = m - 1

    while low <= high:
        mid = (low + high) // 2

        row = max_element(arr, mid)

        left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')
        right = arr[row][mid + 1] if mid + 1 < m else float('-inf')

        if arr[row][mid] > left and arr[row][mid] > right:
            return arr[row][mid]

        elif arr[row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1,-1]

arr = [
    [4,2,5,1,4,5],
    [2,9,3,2,3,2],
    [1,7,6,0,1,3],
    [3,6,2,3,7,2]
]
print(find_peak_2d(arr))
