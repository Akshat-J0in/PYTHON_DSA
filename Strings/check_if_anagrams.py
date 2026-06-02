"""
Problem Statement:
Given two strings, check if two strings are anagrams of each other or not.
"""



w1 = "INTEGER"
w2 = "TEGERNI"


# Approach 1: using two hash maps to count the frequency of each character in both strings and comparing the counts
# w1_map = {}
# w2_map = {}

# for i in w1:
#     if i in w1_map:
#         w1_map[i] += 1
#     else:
#         w1_map[i] = 1

# for i in w2:
#     if i in w2_map:
#         w2_map[i] += 1
#     else:
#         w2_map[i] = 1

# if w1_map == w2_map:
#     print("Yes, the strings are anagrams of each other")
# else:
#     print("No, the strings are not anagrams of each other")


# Approach 2: using a single hash map to count the frequency of each character in both strings and comparing the counts
freq = {}

if len(w1) != len(w2):
    print("No, the strings are not anagrams of each other")

else:
    for i in w1:
        freq[i] = freq.get(i,0) + 1

    for i in w2:
        if i not in freq:
            print("No, the strings are not anagrams of each other")
            break

        freq[i] -= 1

        if freq[i] < 0:
            print("No, the strings are not anagrams of each other")
            break
    else:
        print("Yes, the strings are anagrams of each other")
