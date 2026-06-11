"""
Problem Statement:
You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.
"""



s = "pqpqs"
k = 2
ans = 0
n = len(s)

for i in range(n):
    freq = {}
    distinct = 0
    for j in range(i, n):
        ch = s[j]

        if ch not in freq:
            freq[ch] = 1
            distinct += 1
        else:
            freq[ch] += 1
        
        if distinct == k:
            ans += 1
        elif distinct > k:
            break

print(ans)