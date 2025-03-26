class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        #find multiples of 5. 5 * 2 = 10 
        while n >= 5 :
            n //= 5
            count += n
        return count
        