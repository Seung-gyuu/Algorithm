class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        while n != 1: 

            if n in nums:  
                return False
            nums.add(n) 

            n = sum(int(d) ** 2 for d in str(n))
        
        return n == 1 
        
        