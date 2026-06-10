



# Approach 1: Brute Force
# s = "babad"
# result = ""
# # for i in range(len(s)):
# #     for j in range(i, len(s)):
# #         substring = s[i:j + 1]
# #         if substring == substring[::-1]:
# #             if len(substring) > len(result):
# #                 result = substring
# # print(result)



# Approach 2: Expand Around Center
def longest_palindrome(s):
    result = ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(len(s)):
        odd = expand_around_center(i,i)
        even = expand_around_center(i,i+1)
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    return result

print(longest_palindrome("babad"))
