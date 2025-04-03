class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use bit calc
        # XOR
        #a ^ a = 0 (같은 숫자를 XOR 하면 0이 됨)
        # a ^ 0 = a (0과 XOR 하면 변하지 않음)
        res = 0
        for i in nums:
            res ^= i
        return res

            
             

        