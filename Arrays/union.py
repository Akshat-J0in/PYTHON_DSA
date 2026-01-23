# Approach 1:
arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]
# final_arr = {}
# for x in arr1+arr2:
#     if x in final_arr:
#         final_arr[x] += 1
#     else:
#         final_arr[x] = 1
# key_values = list(final_arr.keys())
# print(key_values)
"""Here i have used the dictionary approach where first i have taken 2 arrays. It can be user input as well.
then i have first run a loop where we take the both arrays and inside the loop,
if x is already present in the final_array then we increment the count by 1.
If not then we make the value as 1 corresponding to the key.
Then i have stored all the keys in the list and then print the list."""


# Approach 2:
# final_arr = list(set(arr1 + arr2))
# print(final_arr)
"""The best approach that is present in python is using the sets to remove the duplicate element from the array.
"""


# Approach 3:
union = []
[union.append(x) for x in arr1+arr2 if x not in union]
print(union)
"""Here i have used the concept of the list comprihension and loops where i have run a loop for both the arrays and if  a value is not present in the new list then we append it.
"""