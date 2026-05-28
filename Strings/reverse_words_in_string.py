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
"""
Over here we are using the built-in functions to reverse the words in the string.
First we are splitting the string into a list of words using the split() function.
Then we are reversing the list of words using slicing.
Finally we are joining the reversed list of words using the join() function and returning the string.
"""



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
"""
Over here we are not using any built-in functions to reverse the words in the string.
We are using a while loop to iterate through the string from the end to the beginning.
First we are skipping the spaces at the end of the string.
Then we are finding the end index of the word and then we are finding the start index of the word.
Finally we are appending the word to the list of words and then we are joining the list of words using the join() function and returning the string.
"""