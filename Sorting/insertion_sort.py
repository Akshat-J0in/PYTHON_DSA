arr = list(map(int, input().split()))
n = len(arr)
for i in range(1,n):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j] #right shift
        j = j-1
    arr[j+1] = key

print(arr)
"""Here we are using the insertion sort technique to sort the array.
First we take the input from the user.
Then we run the first for loop from 1 to n. Here the important thing to note is that we dont take the 0 index.
Then we assign the key as arr[i] and j as index i-1.
Then we run other while loop and here we check 2 condition.
First: j should be greater than or equal to 0
second: arr[j] should be greater than the key to perform the right shift.
Both the condition should be true to enter the while loop.
Now inside the while loop, we perform the right shift that is arr[j+1] will have the arr[j] value.
Then we do j-1 so that we can compare the key with the left side of the array.
then we insert the key at the j+1 position."""