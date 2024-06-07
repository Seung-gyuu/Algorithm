class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #num - ascending order
        # remove the duplicates in-place
        idx = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        # Return the number of unique elements
        return idx + 1

        