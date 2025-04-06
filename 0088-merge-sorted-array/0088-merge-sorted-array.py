class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        
        #merge nums1 and nums2
        nums1[m:] = nums2
        #sort in ascending order
        nums1.sort()
        