# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings

def longestCommonPrefix(self, v: List[str]) -> str:
    ans=""
    v = sorted(v)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if(first[i] != last[i]):
            return ans
        ans += first[i]
    return ans

