class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #appears three times except for one
        #Find the single element and return it.
        #비트연산으로 해야 빠르게 계산 가능

        ones = 0
        twos = 0
        for i in nums:
            ones = (ones ^ i) & ~twos 
            twos = (twos ^ i) & ~ones
        return ones