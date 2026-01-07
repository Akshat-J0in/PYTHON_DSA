def recursive_bubble_sort(arr,n):
    if n == 1:
        return

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    recursive_bubble_sort(arr,n-1)

arr = list(map(int,input().split()))
n = len(arr)
recursive_bubble_sort(arr,n)
print(arr)
"""This is a simple code where i have taken the user input from the array.
then i have called a recursive function where the parameter that i have taken is arr,n.
inside the function, i have set a base condition where if n == 1 then we come out of the function.
then i have run a for loop till n-1.
Here in the loop, i have set a condition where if the first element is greater than its next element then we swap the numbers.
"""