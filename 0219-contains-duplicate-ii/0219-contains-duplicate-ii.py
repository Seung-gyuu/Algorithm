class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #for num val and index
        res = {}
        for i in range(len(nums)):
            # nums[i] == nums[j] && |i - j| <= k -> True
            if nums[i] in res:
                if abs(i- res[nums[i]]) <= k:
                    return True 
            res[nums[i]] = i 
        return False

        