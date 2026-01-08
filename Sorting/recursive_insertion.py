def recursive_insertion(arr,n):
    if n <= 1:
        return

    recursive_insertion(arr,n-1)
    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = last

arr = list(map(int,input().split()))
n = len(arr)
recursive_insertion(arr,n)
print(arr)
"""Here we have done is recursive insertion sort.
Here first i have taken user input. then called the function which has parameters as array and the size of the array.
then inside the loop, i have first set the base condition where if the length of the array becomes 1 then we return.
After that i have made a recursive call where we decrement the value of n. for example the size of the array will be 5 then by making the recursive call, we make it till 1 then back track the recursion to do the further steps in the code. that is code will now further countinue with size 2 then 3 then ...
then i have created a last variable where it will store the value of index n-1 and another variable which will store the index n-2.
now the value of index n-2 will be just the previous element then the last. for example if last is arr[1] then j = arr[0]
now i have run a while loop where there are 2 condition.
if j is greater than or equal to zero and if value of arr[j] greater than last variable then we enter the loop.
inside the loop, we right shift the values that is the value at index 0 will come to index 1 and we decrement the index j.
Once we are out of the loop, we place the value in the variable last at j+1.
"""