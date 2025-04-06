class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurrences of val in nums in-place.
        # return the len of nums 
        # k = nums.count(val)
        # for i in range(k):
        #         nums.remove(val)
        # return len(nums)
        # O(n^2)

        #use two pointer
        pointer = 0
        for i in nums:
            if i != val:
                nums[pointer] = i
                pointer += 1
        return pointer

