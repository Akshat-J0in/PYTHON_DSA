# Problem Statement:
"""Given an integer array nums, return the largest element of the array.
For example:
nums = [7,0,0,1,7,7,2,7,7]
Output: 7
"""



# Approach 1:
# arr = [1,1,1,2,1,2]
# dic = {}
# for i in range(len(arr)):
#     if arr[i] not in dic:
#         dic[arr[i]] = 1
#     else:
#         dic[arr[i]] += 1
#
# max_element = max(dic.values())
# for keys in dic:
#     if dic[keys] == max_element:
#         print(keys)
"""Here i have used the concept of dictionary where first i have run a loop and inside the loop, i have checked the condition.
First if the element is not in the array then i have added it in the dictionary and if its there then i have incremented the value by 1.
then i have found the maximum value from the dictionary.
then i have run a loop for the keys in the dictionary then check the condition if the dict[keys].
If yes then we print the value.
"""



# Approach 2:
from collections import Counter
arr = [7,0,0,1,7,7,2,7,7]
print(Counter(arr).most_common(1)[0][0])
"""Here i have used the collection library in which i have used counter sub library.
Then i have used the most_common function from the counter.
Here with the most_common gives the list of tuple
[(7,5)] so the first [0] gives (7,5) then the next [0] gives the frist element of the tuple.
"""