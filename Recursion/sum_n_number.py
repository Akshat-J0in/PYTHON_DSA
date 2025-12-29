# problem statement:
"""Given a number N, find out the sum of the first N natural number.
for example:
N = 5
output = 15"""



# Approach 1:
# def sum_number(n):
#     if n == 0:
#         return 0
#     return n + sum_number(n - 1)
# count = int(input("Enter the number you what to find the sum of: "))
# print(sum_number(count))
"""This is a simple approach where we have taken input from the user.
then we have used a recursive function where we have set a base condition where if n becomes 0 then we come out of the function.
then we have made a recursive call where we add the number by calling the function again by decrementing the n."""



# Approach 2
# def sum_number(n,total = 0):
#     if n == 0:
#         return total
#     return sum_number(n-1,total+n)
#
# count = int(input("Enter the number you what to find the sum of: "))
# print(sum_number(count))
"""Here in this approach, it is somewhat similar to the above approach. Where i have taken 2 parameter, one of them is the n and other is total which is zero.
then I have written a base condition where if the n becomes 0 then we come out of the function.
Then i have made a recursive condition where we call the function again by decrementing the n and adding the n in the total."""



# Approach 3
def sum_number(start, end):
    if start > end:
        return 0
    if start == end:
        return start
    mid = (start + end) // 2
    return sum_number(start, mid) + sum_number(mid + 1, end)

count = int(input("Enter the number you what to find the sum of: "))
print(sum_number(1, count))
"""This is a very important approach where i have used a concept of divide and conquer.
Here first i have taken a number till we need to find the sum.
then i have used a recursive function where we have two parameter that is start and end.
here initially start is 1 and end is n.
here the first parameter is if start is greater than end then its wrong so we return 0.
then the second condition that is the base condition that is if start is equal to end then we return start.
here is the important part:
we find the mid that is by dividing start + end by 2
after finding the mid we make a recursive call by calling the function with start and mid and adding it with the the function again by mid+1 and end.
"""