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



# approach 2: adding the string to itself and checking if the goal is a substring of the new string
new_string = s+s
if goal in new_string:
    print("Yes, the string is a rotation of the other")
else:
    print("No, the string is not a rotation of the other")