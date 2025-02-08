class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        num = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                count = 1
            else:
                count += 1
            if count <= 2:
                nums[num] = nums[i]
                num += 1
        return num