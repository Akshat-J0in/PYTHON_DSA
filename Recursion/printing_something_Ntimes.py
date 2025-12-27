"""What is recursion:
It is a programming technique where a function calls itself to solve a problem, by breaking it down into smaller subproblems until it reaches a base case that stops further calls.
"""

"""What is Stack overflow in recursion:
Whenever recursion calls are executed, they are simultaniously stored in recursion stack where they wait for the completion of recursive function.
And the function is only completed if a base condition is fulfilled and the control returns to the parent function.
If we dont have a base condition then it gets called indefinitely which results in stack overflow."""

"""Advantage of recursion:
1) simplifies the code
2) natural representation: problems that are recursive in nature are easier to express
3) reduce code complexity
4) useful in divide and conquer algorithms: important for algorithm like quick sort, merge sort, binary search and dynamic programming"""

"""Disadvantage of recursion:
1) High memory usage
2) risk of stack overflow
3) slower execution
4) Harder to debug"""

#problem statement:
"""Printing Hello N times using recursion:"""
def print_n_times(n):
    if n == 0:
        return
    print("Hello ", n)
    print_n_times(n-1)

count = int(input("How many time would you like to print hello? "))
print_n_times(count)

"""Here we have used the recursion method to print the n times hello.
Here first i have taken the input from the user that how many times we have to print the hello.
then i have created the recursion function where i have set a base condition that if n becomes zero then we come out of loop.
then i will print the hello and then run the loop again by decrementing the count."""