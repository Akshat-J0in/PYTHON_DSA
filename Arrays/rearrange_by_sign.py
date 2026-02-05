# Problem Statement:
"""Given an array with equal number of positive and negative elements. Without altering the relative order of positive and negative elements,
you must return an array of alternately positive and negative numbers.
Forx example:
[1,2,-4,-5]
output: [1.-4.2,-5]
"""



# Approach 1:
arr = [1,2,-4,-5]

# pos = []
# neg = []
#
# for x in arr:
#     if x > 0:
#         pos.append(x)
#     else:
#         neg.append(x)
#
# res = []
# i = j = 0
# while i < len(pos):
#     res.append(pos[i])
#     res.append(neg[j])
#     j = j + 1
#     i = i + 1
# print(res)
"""Here i have first created 2 empty list that is for positive element and one for negative element.
Then i have run a loop for the entire array.
Inside the loop, I have first checked a condition where fi the the value of x is greater than 0 that is positive then we append it in the pos list
else we append it in the neg list.
then i have created a empty list res and 2 variable i,j which i have set it to zero.
then i have run a while loop till the length of the pos list because the length of pos is equal to the length of neg value.
inside the while loop, we first append the first pos value then the first neg value and increment the i and j by 1 and we continue till we come out of the loop.
"""



# Approach 2:
# res = [0]*len(arr)
# p = n = 0
# for x in arr:
#     if x >0:
#         res[p] = x
#         p += 2
#     else:
#         res[n+1] = x
#         n += 2
# print(res)
"""This is a interesting approach where i have created a list of zeros till the length of array.
Then i have created a pos and neg variable which is set to zero.
then i have run a loop till the end of array.
Here i have created a condition where if the value is positive then we append it in the res list and increment the value of pos by 2.
We increment it by 2 because positive value will be in even index that is 0,2,4,6,...
If the value is negative then we append the value at the index+1 as the negative value will be on odd index.
"""



# Approach 3:
from collections import deque

pos = deque()
neg = deque()

for x in arr:
    if x > 0:
        pos.append(x)
    else:
        neg.append(x)
res = []
while pos:
    res.append(pos.popleft())
    res.append(neg.popleft())

print(res)
"""Here i am using the same approach as 1 but here the difference is instead of list i have used deque operation.
"""