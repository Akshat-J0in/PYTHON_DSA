# Problem Statement:
"""
Given a row-wise sorted matrix of size M*N, where M is no. of rows and N is no. of columns,
find the median in the given matrix.
Note: M*N is odd.
"""



import bisect

def find_median(matrix,m,n):
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)

    desired = (m*n)//2

    while low <= high:
        mid = (low + high) // 2

        count = 0
        for row in matrix:
            count += bisect.bisect_right(row, mid)

        if count <= desired:
            low = mid + 1
        else:
            high = mid - 1

    return low

matrix = [
    [1,4,9],
    [2,5,6],
    [3,7,8]
]
m = len(matrix)
n = len(matrix[0])
print(find_median(matrix,m,n))