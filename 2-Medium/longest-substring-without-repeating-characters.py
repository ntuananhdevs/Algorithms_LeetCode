# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = [0] * 128
        left = right = 0
        res = 0
        while right < len(s):
            c = s[right]
            char[ord(c)] += 1
            while char[ord(c)] > 1:
                d = s[left]
                char[ord(d)] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res