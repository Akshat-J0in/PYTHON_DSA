arr = ["interview","internet","internal","interval"]

arr.sort()
first = arr[0]
last = arr[-1]
ans = []

for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
        ''.join(ans)
        break
    ans.append(first[i])
print(''.join(ans))