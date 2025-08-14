
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uni = []
        #always length of nums1 is shorter than nums2
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1

        c = Counter(nums2)

        #loop short one
        for i in nums1:
            if c[i] >0:
                uni.append(i)
                c[i] -= 1
        return uni
        
        