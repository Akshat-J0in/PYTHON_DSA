#Problem Statement:
"""Given an array of N integers, write a program to implement the selection sort algorithm
Example:
Input: N=6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,46,52"""


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
arr = list(map(int, input().split()))
print(selection_sort(arr))
"""Here in this code, we are first taking the input from the user, to give us the array.
Then we are passing it to the function selection_sort
Here in this function, we are running the first loop till the length of the array.
Here inside the loop, we are taking the index and storing in the variable min_index
Then we are running the second loop from the index we have stored in the temporary variable and till the length of the array.
Here inside the loop, we are checking if the the value arr[min_index] is greater then arr[j]. If so then we are exchanging the index.
then we come out of the loop and interchange the value of i and min_index. Hence we get the sorted array.
This is how the selection sort works"""