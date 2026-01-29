# Problem Statement:
"""Given an array of integer and target, return yes if there exist two number such that their sum is equal to the target otherwise return no.
For example:
N = 5, arr[] = {2,6,5,8,11}
target = 14
Output: 'Yes'
"""



# Approach 1:
# arr = [2,6,5,8,11]
# ans = 'No'
# target = 14
#
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             ans = 'Yes'
#             break
# print(ans)
"""Here i have used the approach of nested loops.
Here first i have ran a loop from index 0 to the last index of the array.
Then i have run another array where it will run from i+1 to last index of the array.
Inside the second loop, we are checking a condition where if the the value of loop 1 + value of loop 2 is equal to the target then we can say that answer will be yes and we break the loop.
Otherwise this will continue till the end of the loop. Even after that if we dont get the answer, the output will be no
"""



# Approach 2:
# arr = [2,6,5,8,11]
# target = 15
#
# seen = set()
# ans = 'No'
#
# for val in arr:
#     if target - val in seen:
#         ans = 'Yes'
#         break
#     seen.add(val)
# print(ans)
"""Here I have used the concept of sets where i have created a empty set and then run a loop.
Inside the loop, we have set a condition where we check if the target - val is equal to a value that is present in the set or not.
If the value is present in the set then we make our answer yes and we break the loop otherwise we add the num in the set.
The main idea behind this is val + (target - val) = target.
"""



# Approach 3:
arr = [2,6,5,8,11]
target = 14
mp = {}
ans = 'No'

for i,value in enumerate(arr):
    if target - value in mp:
        ans = 'Yes'
        break
    mp[value] = i
print(ans)
print(mp)
"""Here i have used the concept of dictionary where i have first created an empty dictionary and then run a loop.
Here the loop will have 2 parts one is the index and the value hence used the enumerate function.
The if logic will be same as above.
If we dont enter the if condition then we add the value as key and the index as value in the dictionary.
"""