class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #return the indices of the two numbers, index1 and index2 +1
        res = []

        left = 0
        right = len(numbers) - 1
        
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                res += left +1, right +1
                return res
            elif cur < target:
                left += 1
            else:
                right -= 1
            


         
        