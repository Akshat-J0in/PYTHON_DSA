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
"""
Here in this code, we are first creating two empty hash maps to store the frequency of each character in both strings.
Then we are iterating through both strings and counting the frequency of each character and storing it in the respective hash maps.
Finally, we are comparing the two hash maps. If they are equal, then we can say that the strings are anagrams of each other.
"""



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
"""
Here in this code, we are first creating an empty hash map to store the frequency of each character in both strings.
Then we are iterating through the first string and counting the frequency of each character and storing it in the hash map.
Then we are iterating through the second string and checking if the character is present in the hash map or not.
If it is not present, then we can say that the strings are not anagrams of each other.
If it is present, then we are decrementing the frequency of that character in the hash map by 1.
If the frequency of any character becomes negative, then we can say that the strings are not anqrams of each other.
Finally, if we have iterated through the second string and we have not found any character that is not present
in the hash map or any character that has negative frequency, then we can say that the strings are anagrams of each other.
"""