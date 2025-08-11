class Solution:
    def climbStairs(self, n: int) -> int:
        #n /1 or 2 
        if n <= 2:
            return n
        else:
            a, b = 1, 2  # f(1), f(2)
            for _ in range(3, n+1):
                a, b = b, a + b 
            return b
        