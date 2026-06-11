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
"""
Here we have a string and a positive integer k and we have to find the number of substrings that contain exactly k distinct characters.
We will keep a frequency dictionary to keep track of the frequency of each character in the current substring
and a variable distinct to keep track of the number of distinct characters in the current substring.
We will use two loops to generate all the substrings of the string.
In the inner loop, we will update the frequency dictionary and the distinct variable for the current character.
Then we will check if the number of distinct characters is equal to k or not.
If it is equal to k, then we will increment the answer variable by 1.
If it is greater than k, then we will break the inner loop as we are only interested in substrings that contain exactly k distinct characters.
Finally, we will return the answer variable which will have the number of substrings that contain exactly k distinct characters.
"""