#problem statement:
"""Given an integer N, write a program to print number from 1 to N.
For Example:
Input N = 4
Output: 1,2,3,4"""

# Approach 1:
# def asc_number(n):
#     if n == 0:
#         return
#     asc_number(n - 1)
#     print(n,end=" ")
#
# count = int(input("Enter the number you want to print:"))
# asc_number(count)
"""Here in this approach i have first taken a input from the user then i have created the recursion function.
where first i have created a base condition that if n becomes zero then we come out of loop.
then i have used the function name to call the function again with decremented value.
This will continue till the value becomes zero.
once the value becomes zero, there is no value printed, the number will start printing in the reverse order that is 1,2,3,...
if we had printed the number before calling the loop then it would be printed as ...,4,3,2,1"""

#Approach 2:
# def asc_number(n,curr = 1):
#     if curr > n:
#         return
#     print(curr, end=" ")
#     asc_number(n,curr + 1)
#
# count = int(input("Enter the number you want to print:"))
# asc_number(count)
"""Here i have used two function parameter. one is to take the user input and other is a checker parameter where the initial value is 1
then i have created a base condition where if the current value becomes > n then we will come out of the function.
then we print the current value then call the function again with incremented value and n."""

#Approach 3:
def asc_number(n):
    if n == 0:
        return ""
    return asc_number(n - 1) + str(n) + " "
count = int(input("Enter the number you want to print:"))
print(asc_number(count))

