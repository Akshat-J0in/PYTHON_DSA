"""
Problem Statement:
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
"""



s = "rotation"
goal = "tionrota"

# approach 1: using a hash map to count the frequency of each character in both strings and comparing the two maps
# s_map = {}
# goal_map = {}

# for i in s:
#     if i in s_map:
#         s_map[i] += 1
#     else:
#         s_map[i] = 1

# for i in goal:
#     if i in goal_map:
#         goal_map[i] += 1
#     else:
#         goal_map[i] = 1

# if s_map == goal_map:
#     print("Yes, the string is a rotation of the other")
# else:
#     print("No, the string is not a rotation of the other")
"""
Here in this code, we are first creating two empty hash maps to store the frequency of each character in both strings.
Then we are iterating through both strings and counting the frequency of each character and storing it in the respective hash maps.
Finally, we are comparing the two hash maps. If they are equal, then we can say that the string is a rotation of the other.
Otherwise, it is not.
"""



# approach 2: adding the string to itself and checking if the goal is a substring of the new string
new_string = s+s
if goal in new_string:
    print("Yes, the string is a rotation of the other")
else:
    print("No, the string is not a rotation of the other")
"""
Here in this code, we are first adding the string to itself.
This is because if the goal is a rotation of the string, then it will be a substring of the new string.
Then we are checking if the goal is a substring of the new string. If it is, then we can say that the string is a rotation of the other.
Otherwise, it is not.
"""