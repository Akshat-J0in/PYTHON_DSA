# Problem Statement:
"""Given an N*N 2D integer matrix, rotate the matrix by 90 degree clockwise.
For example:
input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,2]]
"""



# Approach 1:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# n = len(matrix)
# rotated = [[0]* n for _ in range(n)]
# # print(rotated)
# for i in range(n):
#     for j in range(n):
#         rotated[j][n-1-i] = matrix[i][j]
# print(rotated)
"""Here in this approach, i have mainly used one formula that is matrix[j][n-1-i]
First i have created a new matrix of zeros which we will fill up.
Then i have calculated the length of the matrix then run 2 loop i and j both till the end of the matrix.
inside the matrix, i have used the formula to to fill the position with the value at matrix[i][j]
"""



# Approach 2:
n = len(matrix)
for i in range(n):
    for j in range(i,n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for rows in matrix:
    rows.reverse()

print(matrix)
"""Here this is the most optimal solution.
As no new matrix was created and all changes are done in place
Here to rotate the matrix by 90 degree clockwise, we first need to find the transpose and then reverse it rowwise.
So here first i have taken the transpose of the matrix in the nested for loop.
Then i have done row wise iteration and reversed the row and then print the matrix.
"""