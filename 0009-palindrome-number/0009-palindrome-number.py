class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        str2 = str1[::-1]
        return str1 == str2

        

        