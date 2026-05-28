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