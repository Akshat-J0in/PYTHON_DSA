# Problem Statement:
"""Given a matrix, print the given matrix in the spiral order.
For Example:
input: [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Output: 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""



matrix = [[1,2,3],[4,5,6],[7,8,9]]

if matrix:
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    result = []

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    print(result)
"""Here in this code, first i have created 4 variable that is left which will start from index 0,0 that is the first index.
then we have right which will start from index the first row and last column. Then we have top which will start from 0 that is same as right.
Then we have bottom which will start from the last row and last column.
Then i have run a while loop where i have set a condition where if the left is smaller than right and top is smaller than bottom then we can iterate the loop.
Inside the loop, first we will move from the left to the right. then we will increment the top as our first row is printed.
Now we want to move from top to bottom so here our column will remain constant only our row will change.
So in column we will fix the value as right and for row, we will iterate through a loop and then increment the right by 1.
Similarly, we will do for the right to left that is now we are at bottom.
Now we will fix our row value as bottom and iterate a reverse loop as we want to move from right to left. then we will decrement the bottom by 1.
Now we we will do the same for bottom to up as we did for top to bottom here we will decrement the left by 1.
"""