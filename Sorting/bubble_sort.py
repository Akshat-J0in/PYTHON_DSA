arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
    swapped = False
    for j in range(0,n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break
print(arr)

"""This is the code for bubble sort.
Here first i am taking the user input as list.
then i am running the fist loop till n.
Here first i have introduced a checker that is swapped which is false initially.
then i have run the second loop where it will run from 0 to n-i-1. Why so because -i is done as the greatest element will take the last place so we dont need to check that value again and -1 is done so that index does not go out of bound
inside the second loop, we are checking if the arr[j] is greater than its adjecent value arr[j+1]. If so then we swap the values and make the swapped variable True.
If for the first iteration that is for i=0, we dont swap any value that is if swapped is false then the array is already sorted and we come out of loop.
This condition save us from the multiple iteration again and again.
"""