def threeSum(self, nums):
    res = set()
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    N, P = set(n), set(p)    

    if z:
        
    

            
