# Problem Statement:
"""Given an array and an element num the task is to find if num is present in the array or not. If present print the index.
Example:
Input: arr[] = 1,2,3,4,5  target = 3
Output: 1"""



# Approach 1:
arr = list(map(int, input().split()))
target = int(input())
# found = False
# for i in range(len(arr)):
#     if arr[i] == target:
#         print("value present at position ",i)
#         found = True
#         break
#
# if not found:
#     print("value not found")
"""Here this is the most simple code where first i have taken the user input.
Then i have asked the user for the array position they want to search.
Then i have set a variable found as false.
Then i have run a for loop where inside it if we find the element the user is looking for, we return the index and make the found = true and then come out of the loop.
Even after iterating through entire loop, we cannot find the element then we print that value not found."""



if target in arr:
    print("Found at index:", arr.index(target))
else:
    print("Not found")
""" Then most simple approach where i have used the in keyword where we see if the element is present in the array or not if not then we
return not found otherwise we return the index."""