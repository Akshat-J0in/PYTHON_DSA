# Problem statement:
"""Given an integer N, print the fibonacci sequence. upto the Nth term.
For example:
if n = 5
output: 0 1 1 2 3"""


# Approach 1:
# def feb(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return feb(n-1) + feb(n-2)
#
# n = int(input("Enter the length of the fibonacci sequence: "))
# for i in range(n):
#     print(feb(i), end=" ")
"""This is not a optimal approach, its just for practice.
Here i have first taken input from the user then run a for loop to print the fibonacci sequence.
inside the loop, we will iterate to the length specified by the user. that is if length = 5then we will run the loop from 0 to 4.
inside the loop, we have called the function for every length.
inside the function, we have set the base condition where if length is 0 then we return 0,if n==1 then we return 1.
then i have made a recursive call where if n is lets say 3 then we return the function with length of 2 and 1 then again the length of 2 is divided into 1 and 0.
then we add that numbers and come out of the function.
the time complexitiy for this is O(n^2) so its not at all the optimal solution."""



# Approach 2:
def fib(n,a=0,b=1):
    if n == 0:
        return
    print(a,end=" ")
    fib(n-1,b,a+b)

n=int(input("Enter the length of the fibonacci sequence: "))
fib(n)
"""This is the most optimal approach amongst the 2 approach.
here i have taken the length of the fibonacci series from the user.
Then i have made a recursive function where the parameters are the length, a which is 0 at start, b which is 1 at start.
then i have set a base condition where if the length becomes zero then we come out of the function.
after that we print our fibonacci sequence.
then i have made a recursive call where call the length-1, now we give a the value of b, and b becomes a+b."""