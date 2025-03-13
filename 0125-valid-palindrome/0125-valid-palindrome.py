class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1) remove whitespace
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # 2) check if it is empty str
        # 3) divide by 2 
        return s == s[::-1]
