def atoi(s):
    i = 0

    while i < len(s) and s[i] == ' ':
        i += 1
    
    sign = 1
    if i < len(s):
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
    
    def dfs(idx,num):
        if idx >= len(s) or not s[idx].isdigit():
            return num
        
        num = num * 10 + int(s[idx])
        return dfs(idx+1,num)
    
    num = dfs(i,0)
    num = sign * num

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

S = "   -42"
print(atoi(S))