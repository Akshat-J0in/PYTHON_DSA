"""
Problem Statement:
Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ).
A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.
Return a string with the words in reverse order, concatenated by a single space.
"""



word = "Welcome to the jungle"



# Approach 1: Using built-in functions
# words = word.split(" ")
# reversed_words = words[::-1]
# print(' '.join(reversed_words))



# Approach 2: Without using built-in functions
words = []
i = len(word) - 1

while i >= 0:

    while i >= 0 and word[i] == ' ':
        i -= 1

    if i < 0:
        break

    end = i
    while i >= 0 and word[i] != ' ':
        i -= 1

    words.append(word[i + 1:end + 1])

print(' '.join(words))