class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #check if the last item is 9
        if  digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            for i in range(len(digits) -1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] = digits[i] + 1
                    break

            if digits[0] == 0:
                return [1] + digits

            return digits
                
        