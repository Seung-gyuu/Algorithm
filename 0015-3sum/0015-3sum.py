class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3sum == 0
        # for , while - use two pointer
        res =[]
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1  
                    right -= 1 
                elif cur < 0:
                    left += 1
                else:
                    right -= 1
        return res

        