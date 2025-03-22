class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        res = 0

        for i in num:
            if i - 1 not in num:
                curr = 1
                while i + 1 in num:
                    i += 1 
                    curr += 1
                res = max(res, curr) 
        return res

        