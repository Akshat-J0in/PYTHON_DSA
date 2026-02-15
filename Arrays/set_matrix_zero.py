# Problem Statement:
"""Given a matrix if an element in the matrix is 0, then you will have to set its entire column and row to zero and then return the matrix.
Input: Matrix: [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""



arr = [[1,2,1,2],[1,0,1,2],[1,1,1,2]]
col_len = len(arr[0])
row_len = len(arr)

rows_to_zero = set()
cols_to_zero = set()

for i in range(row_len):
    for j in range(col_len):
        if arr[i][j] == 0:
            rows_to_zero.add(i)
            cols_to_zero.add(j)
for i in rows_to_zero:
    arr[i] = [0] * col_len

for j in cols_to_zero:
    for i in range(row_len):
        arr[i][j] = 0

print(arr)
"""Here first we have set the length of the row and column that is the length of rows is 3 and column is 4.
then we have run nested loop, one till the row length and other till the column length.
Then we have set a condition where if the index arr[i][j] == 0 then we save the index i and j in the set respectively.
Then we first run a loop where we first make the row which had zero to zero.
Then we run a nested loop to make the column zero which had the zero present.
"""