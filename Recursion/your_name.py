#problem statement:
"""Given an integer N, write a program to print your name N times.
for example:
if N = 3
output: Akshat Akshat Akshat"""

def name(n):
    if n == 0:
        return
    print("Akshat",end=" ")
    name(n-1)

count = int(input("Enter the number of time you want to print your name: "))
name(count)
"""Here this code is similar to the first code that we had done for recursion. Here we are printing the name n times using the recursion method.
Here i have taken input from the user and then run a function.
Here in the function if n becomes 0, we will get out of the loop.
else we will print the name and to print the next name in the same line, we have used a keyword 'end = " "'.
Then we do decrement the count so that we can fulfill the if condition."""