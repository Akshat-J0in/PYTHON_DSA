# Problem Statement:
"""Given a number N, print its factorial.
for example:
N = 5
output = 120"""

# Approach 1:
# def fact(n):
#     if n == 0 or n==1:
#         return 1
#     return fact(n - 1) * n
#
# count = int(input("Enter the number whose factorial you want: "))
# print(fact(count))
"""This is the most simple approach and similar to sum of n number approach 1.
Here first we take the user input.
Then i have made a recursive function where i have created a base condition where if n is 0 or 1 then we return 1.
if not then i have made a recursive call where we call the function again and again by decrementing the N and multiplying the value n."""


# Approach 2:
# def fact(n,total=1):
#     if n == 0:
#         return total
#     return fact(n - 1,total*n)
#
# count = int(input("Enter the number whose factorial you want: "))
# print(fact(count))
"""Here i have used the similar approach as sum of n number approach 2.
here we have two parameter n and total which is 1.
if the value of n is 0 then return total.
then we have made a recursive call where we decrement the value of n along with n*total to get the answer."""


# Approach 3:
def fact(start,end):
    if start > end:
        return 1
    if start == end:
        return start
    mid = (start + end) // 2
    return fact(start,mid) * fact(mid+1,end)

count = int(input("Enter the number whose factorial you want: "))
print(fact(1,count))
"""This is also similar approach to sum of n number approach 3.
Here i have used the divide and conquer approach where we have two parameter start and end.
if start is greater than end then we return 1.
if start is equal to end then we return start.
then i have found out the mid value.
after that i have made a recursive call that is one with the parameter start and mid and other recursive call is with the parameter mid+1 and end.
"""