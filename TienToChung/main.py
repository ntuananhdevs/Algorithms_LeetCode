def longestCommonPrefix(strs):
    if(len(strs)) == 0:
        return ""
    base = strs[0]
    for i in range(len(base)):
        