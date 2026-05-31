"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""



s = "paper"
t = "title"

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_t = {}
    mapping_t_S = {}

    for char_s, char_t in zip(s,t):
        if char_s in mapping_s_t:
            if mapping_s_t[char_s] != char_t:
                return False
        else:
            mapping_s_t[char_s] = char_t
        
        if char_t in mapping_t_S:
            if mapping_t_S[char_t] != char_s:
                return False
        else:
            mapping_t_S[char_t] = char_s
        
    return True

print(isIsomorphic(s,t))
"""
This is the code for checking if the two strings are isomorphic or not.
First we are checking if the length of both the strings are same or not.
If not then we can say that they are not isomorphic and return false.
Then we are creating two dictionaries one for mapping the characters of string s to string t
and another for mapping the characters of string t to string s.
Then we are running a loop where we are checking each character of both the strings at the same time using zip function.
Inside the loop we are checking if the character of string s is already present in the mapping_s_t dictionary or not.
If it is present then we are checking if the mapped character is same as the character of string t or not.
If not then we can say that they are not isomorphic and return false.
If the character of string s is not present in the mapping_s_t dictionary then we are adding the mapping of character of string s to character of string t in the dictionary.
Then we are doing the same for the character of string t in the mapping_t_S dictionary.
"""