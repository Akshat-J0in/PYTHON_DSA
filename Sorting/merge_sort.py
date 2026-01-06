#Problem Statement:
"""Given an array of size n, sort the array using the merge sort algorithm.
For example:
N = 7, arr[] = {3,2,8,5,1,4,23}"""

"""How does the merge sort work?
Merge sort is a divide and conquer sorting algorithm.
Here we divide the array into two halves until each part has 1 element. Conquer by sorting and merging the halves.
Combine the sorted half into one sorted array.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = list(map(int, input().split()))
sorted_arr = merge_sort(arr)
print(sorted_arr)
"""Here first i have taken the user input for the array.
Then i have called merge_sort function. Here in this function, i have made a base condition that if the length of the arr is less than or equal to 1 then we return array.
Then i have made a mid variable that calculates the mid value of the array so that we can divide the array into two parts.
then i have made a left part and the right part.
here in the both parts, i have made a recursive call where for the left side the array will run till the stat value till the mid where the mid will not be included.
for the right side, the recursive call will be from the mid to last element in the array.
once the array is divided, we call another function that is merge by returning the left and the right value.
Here in the merge function, we have created a empty list result and i,j that will keep track of the index.
then i have run a while loop which check 2 condition that till i < length of left and j < length of right, we run the while loop.
Inside the while loop, we have set a condition where if left[i] < right[j] then we append the left element first and increment the i.
else we append the right element first and increment the j.
after one of them is added, we append the other half.
after all of this, the array becomes sorted and we return the result to the merge sort function and we print the sorted array."""