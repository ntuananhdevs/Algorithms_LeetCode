# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, 
# T1 = 1,
# T2 = 1,
# Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

# Example 1:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:

# Input: n = 25
# Output: 1389537

# Phương pháp giải quyết vấn đề này:
# 1. dung đệ quy(qua cham)


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        

#2.Dynamic Programming
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                result = helper(n - 1) + helper(n - 2) + helper(n - 3)
                memo[n] = result
                return result
        return helper(n)
# 35 ms

#3. 15ms
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        trib = [-1] * (n + 1)
        trib[0] = 0
        trib[1] = 1
        trib[2] = 1
        def getTrib(idx):
            if trib[idx] == -1:
                if trib[idx-1] == -1: trib[idx-1] = getTrib(idx-1) 
                if trib[idx-2] == -1: trib[idx-2] = getTrib(idx-2) 
                if trib[idx-3] == -1: trib[idx-3] = getTrib(idx-3)            
                return  trib[idx-1] + trib[idx-2] + trib[idx-3]
            else: # base case   
                return trib[idx]
        return getTrib(n)   

#4
class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0,1,1]
        if n <=2:
            return l[n]
        else:
            for i in range(3,n+1):
                l.append(l[-1]+l[-2]+l[-3])
            return l[-1]
