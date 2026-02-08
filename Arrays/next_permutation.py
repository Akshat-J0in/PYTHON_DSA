# Problem Statement:
"""Given an array of integer, rearrange the number of the given array into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must be the lowest possible order.
for example:
Input: arr[] = {1,3,2}
Output: {2,1,3}
"""
arr = [1,3,2]
n= len(arr)
i = n-2

while i>=0 and arr[i]>=arr[i+1]:
    i -= 1

if i >= 0:
    j = n-1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    print(arr)

"""Here i have first found the pivot that is with what element we need to swap.
For that we need to to use the while loop were the index i is greater than or equal to zero and arr[i] is greater than arr of i+1
if the condition is satisfied we will decrement the i. Here the main purpose of this is to find the lowest element in the array.
Now we do the swaping.
For that we first see if i is >= 0
then we set the j value to the last index of the array.
now we run a while loop, where we set a condition where if the value of j <= i then we decrement the j to find something greater than then arr[i].
Now we swap the values.
then we reverse the array from the pivot to the j.
"""