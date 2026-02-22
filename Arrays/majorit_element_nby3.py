# Problem Statement:
"""Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.
For example:
nums = [1,2,1,1,3,2]
Output:
[1]
"""



# Approach 1:
# arr = [1,2,1,1,3,2,2]
#
# length = len(arr)
# max_count = length // 3
# dictionary = {}
# majority_element = []
#
# for i in range(length):
#     if arr[i] not in dictionary:
#         dictionary[arr[i]] = 1
#     else:
#         dictionary[arr[i]] += 1
#
# for key, value in dictionary.items():
#     if value > max_count:
#         majority_element.append(key)
#
# print(majority_element)
"""Here i have used the concept of dictionary where i have first created an empty dictionary then appended the key and value pair.
Then i have found the length of the array then did the floor division  with 3.
Then i have made the empty list and appended all the values that are greater than n//3 in the empty list.
Its a very simple and easy to understand optimal approach.
"""


# Approach 2:
arr = [1,2,1,1,3,2,2]
count1 = count2 = 0
candidate1 = candidate2 = None

for num in arr:
    if candidate1 == num:
        count1 += 1
    elif candidate2 == num:
        count2 += 1
    elif count1 == 0:
        candidate1 = num
        count1 = 1
    elif count2 == 0:
        candidate2 = num
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1
result = []
for candidate in [candidate1, candidate2]:
    if arr.count(candidate) > len(arr)//3:
        result.append(candidate)

print(result)
"""This approach is called Boyer–Moore Voting Algorithm.
In this approach i have created two candidate and 2 count variable both are set to zero.
Then i run the for loop that iterate over the array.
In this first i have set a condition where if candidate1 == num then we increment the count1.
Else if candidate 2 == num then we increment the count2.
Else if count 1 == 0 that mean we have to set the candidate 1 and make the count value 1.
Else if count 2 == 0 then we have to set the candidate 2 and make the count value 1.
If all this condition does not satisfy, we have to decrement the count1 and 2 by 1.
Once we are out of loop, i have created a empty result list.
Then i run a for loop over the candidate 1 and 2 and check the condition if they are greater than n//3 then we append it in result.
Else we come out of the loop.
"""