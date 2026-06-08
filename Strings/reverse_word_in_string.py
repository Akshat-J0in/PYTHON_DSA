s = " Welcome to the jungle "



# Approach1: Using built-in functions
# lower_s = s.lower()

# new_string = lower_s.strip(" ")

# list_of_words = new_string.split(" ")

# reversed_string = " ".join(list_of_words[::-1])

# print(reversed_string)



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