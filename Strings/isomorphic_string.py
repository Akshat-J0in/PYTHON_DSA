s = "paper"
t = "title"

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_t = {}
    mapping_t_S = {}

    for char_s, char_t in zip(s,t):
        if char_s in mapping_s_t:
            if mapping_s_t[char_s] != char_t:
                return False
        else:
            mapping_s_t[char_s] = char_t
        
        if char_t in mapping_t_S:
            if mapping_t_S[char_t] != char_s:
                return False
        else:
            mapping_t_S[char_t] = char_s
        
    return True

print(isIsomorphic(s,t))