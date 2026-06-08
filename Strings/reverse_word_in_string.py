"""
Problem statement:
Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ).
A word is defined as a sequence of non-space characters.
The words in s are separated by at least one space.
Return a string with the words in reverse order, concatenated by a single space.
"""



s = " Welcome to the jungle "



# Approach1: Using built-in functions
# lower_s = s.lower()

# new_string = lower_s.strip(" ")

# list_of_words = new_string.split(" ")

# reversed_string = " ".join(list_of_words[::-1])

# print(reversed_string)
"""
Here in this code, we are first converting the input string to lower case using the lower() method.
Then we are using the strip() method to remove any leading and trailing spaces from the string.
Then we are using the split() method to split the string into a list of words based on spaces.
Then we are reversing the list of words using slicing and joining them back into a string with a single space in between using the join() method.
Finally, we are printing the reversed string.
"""



# Approach 2: Using two pointers
def reverse_words(s):
    result = ""
    i = len(s) - 1

    while i >= 0:
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        if i < 0:
            break

        end = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        
        word = s[i+1:end+1]

        if result != "":
            result += " "
        
        result += word
    return result

print(reverse_words(s))
""""
Here in this code, we are first initializing an empty string result to store the final output.
Then we are initializing a variable i to the last index of the string s.
Then we are running a loop until i is greater than or equal to 0.
Inside the loop, we are first ignoring any trailing spaces until we find a non-space character.
If we reach the beginning of the string, we break out of the loop.
Then we are setting the end variable to the current index i, which marks the end of a word.
Then we are running another loop to find the start of the word by moving i backwards until we find a space or reach the beginning of the string.
Then we are extracting the word using slicing and adding it to the result string.
If the result string is not empty, we add a space before adding the new word to ensure that the words are separated by a single space.
Finally, we return the result string which contains the words in reverse order.
"""