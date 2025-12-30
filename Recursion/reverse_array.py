# Problem statement:
"""You are given an array. The task is to reverse the array.
for example:
Input: N = 5, arr[] = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]"""

# Approach 1:
# def reverse_array(arr,start,end):
#     if start >= end:
#         return
#     arr[start],arr[end] = arr[end],arr[start]
#     reverse_array(arr,start+1,end-1)
#
#
# arr = list(map(int, input("Enter array elements: ").split()))
# reverse_array(arr,0,len(arr)-1)
# print(arr)
"""Here i have used the concept of 2 pointer approach.
Here first i have created a list by first taking the input as string then splitting it with spaces then mapping all the string with int.
then i have called a recursive function where we have 3 parameter, the array, start which is initially 0, end which is len of array-1.
then i have created a base condition which is if start is greater than or equal to end then we return the values.
else we interchange the start with end and visa versa.
then we recursively call the function again where we increment the start and decrement the end."""



# Approach 2:
def reverse_array(arr):
    if len(arr) == 0:
        return []
    return reverse_array(arr[1:]) + [arr[0]]

arr = list(map(int, input("Enter array elements: ").split()))
print(reverse_array(arr))
"""Here i have first taken the user input fot the array.
then created a recursive function where i have only 1 parameter that is the array.
then i have set the base condition where if the length of the array becomes zero then we return the list.
then i have made a recursive call where we return all the values except arr[0] which we add it in the last.
We have done this using the slice operation where we have used arr[1:] means all elements except arr[0]."""