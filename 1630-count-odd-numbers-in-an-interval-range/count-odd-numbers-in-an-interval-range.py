class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #count the number between low and high
        # //2 for finding odd num  
        count = high - low + 1
        return count //2 + (1 if low % 2 != 0 and high % 2 != 0 else 0)

        