s = "aabcbaa"
substrings = []

n = len(s)
total = 0
for i in range(n):
    freq = {}
    for j in range(i, n):
        freq[s[j]] = freq.get(s[j], 0) + 1
        substrings.append(s[i:j + 1])

        values = freq.values()
        maxi = max(values)
        mini = min(values)
        total += (maxi - mini)

print(total)
print(substrings)