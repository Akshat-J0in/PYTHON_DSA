def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = list(map(int, input().split()))
print(quick_sort(arr))
"""Here first we take the user input for the array from the user.
then i have made a function for quicksort.
In quick sort, we have to make one pivot element and then divide the array into two parts. Left hand side will contain all the element smaller then the pivot and the right hand side will contain all the element greater then the pivot.
so here in the function first i have made a base condition where if the length of tha array becomes less than or equal to 1 then we return arr.
Then i have made the last element that is arr[-1] as pivot.
now i have made 2 list that is the left and right side elements list.
Here in the left hand side, we take all the element that are smaller than or equal to pivot.
In right hand side, we take all the element that are greater than pivot.
Then we make a recursive call till we have one element present in the array and then we combine them all.
"""