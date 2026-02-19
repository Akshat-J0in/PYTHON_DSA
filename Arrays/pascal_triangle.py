# Problem Statement:
"""Write a program to generate pascal triangle. In pascal's triangle, each number is the sum of the two number directly above it.
Example:
 N=5
 1
 1 1
 1 2 1
 1 3 3 1
 1 4 6 4 1
 """



# Approach 1:
# num = 5
# for i in range(num):
#     val = 1
#     for j in range(i+1):
#         print(val, end=" ")
#         val = val * (i-j) // (j+1)
#     print()
"""This is the brute force approach where we have run a loop till the num that is 5 in this case.
then we have set a variable val to 1.
Then i have run another loop which will run till i+1 element that is if i =2 then loop will run from 0 to 3(excluding 3)
Inside the loop, I have printed the value first then did a calculation that is val * (i-j) // (j+1)
this will give us the answer.
"""



# Approach 2:
n = 5
triangle = []

for i in range(n):
    row = [1] * (i+1)

    for j in range(1,i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for row in triangle:
    print(row)
"""This is the most optimal solution where first i have created an empty array triangle.
Then i have run a loop till the num that is 5 in this case.
here first we will fill the row array with 1's based on the value of i.
That is i = 0 then we will have row = [1]. When i = 1, row = [1,1] and so on.
then we will run a for loop till 1 to i.
Here in this for loop, we will set a operation.
for the row[j], we have added the triangle[i-1][j-1] + triangle[i-1][j]
then we will append this row in the triangle.
Once we are out of this both loop, we will print each loop.
"""