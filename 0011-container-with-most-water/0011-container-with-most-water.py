class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Return the maximum amount of water a container can store.
        # two pointers
        left = 0 
        right = len(height) - 1

        max_area = 0 

        while left < right :
            # calc curr area 
            area = min(height[left] , height[right]) * (right - left)
            max_area = max(area, max_area)
            
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1
            
        return max_area
            
            


        