# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings

def longestCommonPrefix(self, v: List[str]) -> str:
    res = ""
    for i in range(len(v[0])):
        for s in v:
            if i == len(s) or s[i] != v[0][i]:
                return res
        res += v[0][i]
    return res

