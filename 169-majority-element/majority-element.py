class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check, major = 0, 0
        for i in nums:
            if check == 0:
                major = i
            check += (1 if i == major else -1)
        return major
            

        