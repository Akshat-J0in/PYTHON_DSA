s = "0214638"

# Approach 1: Using a while loop to find the last odd digit
# s = s.lstrip('0')   

# x = len(s) - 1

# while x >= 0:
#     if s[x] in '13579':
#         substring = x
#         break
#     x -= 1

# print(s[:substring + 1])



# Approach 2: Using a for loop to find the last odd digit

s = s.lstrip('0')

for i in range(len(s)-1, -1, -1):
    if s[i] in '13579':
        print(s[:i+1])
        break
else:
    print('')