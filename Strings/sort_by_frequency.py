w = "tree"

s_dict = {}

for i in w:
    s_dict[i] = s_dict.get(i, 0) + 1

sorted_char = sorted(s_dict.items(),key = lambda x: (-x[1],x[0]))

result = [char for char,freq in sorted_char]
print(result)