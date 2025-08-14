class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #find intersection without duplicates
        uni =list(set(nums1) & set(nums2))
        return uni
        ## solution 2
        # uni = []
        # for i in range(len(nums1)):
        #     if nums1[i] in nums2:
        #         if nums1[i] not in uni:
        #             uni.append(nums1[i])
        # return uni
            
        