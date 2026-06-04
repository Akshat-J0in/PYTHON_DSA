s = "(1+(2*3)+((8)/4))+1"
ans = 0
count = 0
for ch in s:
    if ch == '(':
        count += 1
        ans = max(ans, count)
    elif ch == ')':
        count -= 1
print(ans)
